#!/usr/bin/env python3
"""Validate skill structure and README/marketplace.json integrity.

Checks that:
  * every skill path referenced by .claude-plugin/marketplace.json points to a
    real directory containing a SKILL.md;
  * every skills/*/SKILL.md has parseable YAML frontmatter with non-empty
    `name` and `description` fields;
  * no two skills share the same frontmatter `name`;
  * README plugin install commands reference the manifest's marketplace name
    and defined plugin bundles;
  * the README marketplace-add repository slug matches the marketplace name;
  * no SKILL.md reintroduces a retired tool-name or query-token pattern that was
    verified against the Evergreen MCP server to match nothing (denylist only —
    there is no allowlist of valid tool names here);
  * (warning only) every skills/* directory is referenced by at least one bundle.

Exits non-zero if any error is found. Run locally with:

    python3 scripts/validate_skills.py

No third-party dependencies are required. PyYAML is used if installed,
otherwise a minimal parser handles the flat `key: value` frontmatter.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = REPO_ROOT / "skills"
README = REPO_ROOT / "README.md"

INSTALL_COMMAND = re.compile(r"^\s*/plugin install ([^@\s]+)@([^\s]+)\s*$")
MARKETPLACE_ADD_COMMAND = re.compile(r"^\s*/plugin marketplace add ([^/\s]+)/([^/\s]+)\s*$")

# Dot-notation tool calls that were removed from the skills because they match no
# tool the Evergreen MCP server registers. Listed as exact retired method names
# rather than a generic `word.word` pattern so ordinary prose is never flagged.
RETIRED_TOOL_CALLS = (
    "contacts.create",
    "contacts.update",
    "interactions.log",
    "interactions.list",
    "actions.create",
    "actions.list",
    "actions.complete",
    "relationships.create",
    "notes.append",
    "tags.add_to_contact",
)

RETIRED_PATTERNS = (
    (
        re.compile(r"\b(?:%s)\b" % "|".join(re.escape(call) for call in RETIRED_TOOL_CALLS)),
        "retired dot-notation tool name; use the snake_case evergreen-mcp tool "
        "(notes and tags are contact fields set via create_contact/update_contact)",
    ),
    (
        re.compile(r"\btouched:"),
        "retired search_contacts query token; search_contacts has no time-threshold "
        "filter, so recency must be computed from returned last-interaction dates",
    ),
)

try:
    import yaml  # type: ignore

    def parse_frontmatter(text: str) -> dict:
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            raise ValueError("frontmatter is not a YAML mapping")
        return data

except ImportError:

    def parse_frontmatter(text: str) -> dict:
        """Minimal parser for flat `key: value` frontmatter (no PyYAML)."""
        data: dict = {}
        for raw in text.splitlines():
            line = raw.rstrip()
            if not line or line.lstrip().startswith("#"):
                continue
            if ":" not in line:
                raise ValueError(f"cannot parse frontmatter line: {raw!r}")
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip("'\"")
        return data


def read_frontmatter(skill_md: Path) -> dict:
    """Extract and parse the YAML frontmatter block from a SKILL.md file."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("file does not start with a '---' frontmatter delimiter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter block is not closed with '---'")
    return parse_frontmatter(parts[1])


def scan_retired_patterns(text: str, label: str) -> list[str]:
    """Return an error per line of `text` that reintroduces a retired pattern."""
    found: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern, reason in RETIRED_PATTERNS:
            for match in pattern.finditer(line):
                found.append(f"{label}:{line_number}: '{match.group(0)}' is a {reason}")
    return found


# Spelled out literally rather than derived from RETIRED_TOOL_CALLS, so that
# dropping an entry from the denylist fails the self-test instead of silently
# shrinking it too.
SELF_TEST_BANNED = """---
name: fixture
---
1. contacts.create({ first_name: "Sarah" })
2. contacts.update(contact_id, {})
3. interactions.log(contact_id, {})
4. interactions.list(contact_id)
5. actions.create(contact_id, {})
6. actions.list({ status: "open" })
7. actions.complete(action_id)
8. relationships.create(a, b)
9. notes.append(contact_id, "note")
10. tags.add_to_contact(contact_id, "ai")
11. search_contacts("touched:>90d")
"""

SELF_TEST_EXPECTED = (
    "contacts.create",
    "contacts.update",
    "interactions.log",
    "interactions.list",
    "actions.create",
    "actions.list",
    "actions.complete",
    "relationships.create",
    "notes.append",
    "tags.add_to_contact",
    "touched:",
)

SELF_TEST_CLEAN = """---
name: fixture
---
1. create_contact({ first_name: "Sarah", email: "sarah@meridianhealth.com" })
2. log_interaction(contact_id, {})
3. update_contact(contact_id, { tags: ["ai"], notes: "Met at the AI dinner." })
4. Review open actions. Complete anything overdue.
5. search_contacts({ query: "Meridian", hasEmail: true })
"""


def self_test() -> list[str]:
    """Check the denylist scanner itself against known-bad and known-good bodies."""
    failures: list[str] = []

    flagged = scan_retired_patterns(SELF_TEST_BANNED, "<self-test>")
    for expected in SELF_TEST_EXPECTED:
        if not any(f"'{expected}'" in message for message in flagged):
            failures.append(f"denylist self-test: '{expected}' was not flagged")

    for message in scan_retired_patterns(SELF_TEST_CLEAN, "<self-test>"):
        failures.append(f"denylist self-test: false positive on valid usage: {message}")

    return failures


def validate_readme_commands(manifest: dict, errors: list[str], warnings: list[str]) -> None:
    """Check documented plugin commands against the marketplace manifest."""
    try:
        lines = README.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        warnings.append(f"cannot read README.md; plugin commands were not checked: {exc}")
        return

    marketplace_name = manifest.get("name")
    bundle_names = {plugin.get("name") for plugin in manifest.get("plugins", [])}
    install_commands = 0
    marketplace_add_commands = 0

    for line_number, line in enumerate(lines, start=1):
        install_match = INSTALL_COMMAND.match(line)
        if install_match:
            install_commands += 1
            bundle, documented_marketplace = install_match.groups()
            if documented_marketplace != marketplace_name:
                errors.append(
                    f"README.md:{line_number}: install command uses marketplace "
                    f"'{documented_marketplace}', expected '{marketplace_name}'"
                )
            if bundle not in bundle_names:
                errors.append(
                    f"README.md:{line_number}: install command references unknown "
                    f"bundle '{bundle}'"
                )

        marketplace_add_match = MARKETPLACE_ADD_COMMAND.match(line)
        if marketplace_add_match:
            marketplace_add_commands += 1
            documented_slug = "-".join(marketplace_add_match.groups())
            if documented_slug != marketplace_name:
                errors.append(
                    f"README.md:{line_number}: marketplace add command resolves to "
                    f"slug '{documented_slug}', expected '{marketplace_name}'"
                )

    if not install_commands:
        warnings.append("README.md contains no /plugin install commands")
    if not marketplace_add_commands:
        warnings.append("README.md contains no /plugin marketplace add commands")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    errors.extend(self_test())

    # --- Load the manifest ------------------------------------------------
    try:
        manifest = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {MARKETPLACE.relative_to(REPO_ROOT)}: {exc}")
        return 1

    referenced: set[str] = set()
    for plugin in manifest.get("plugins", []):
        bundle = plugin.get("name", "<unnamed>")
        for skill_path in plugin.get("skills", []):
            referenced.add(skill_path)
            rel = skill_path.lstrip("./")
            skill_dir = REPO_ROOT / rel
            if not skill_dir.is_dir():
                errors.append(
                    f"bundle '{bundle}' references missing skill directory: {skill_path}"
                )
            elif not (skill_dir / "SKILL.md").is_file():
                errors.append(
                    f"bundle '{bundle}' references '{skill_path}' but it has no SKILL.md"
                )

    # --- Validate README plugin commands ---------------------------------
    validate_readme_commands(manifest, errors, warnings)

    # --- Validate every skill's frontmatter -------------------------------
    names: dict[str, str] = {}
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.is_dir() else []
    for skill_dir in skill_dirs:
        rel = skill_dir.relative_to(REPO_ROOT)
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel}: missing SKILL.md")
            continue
        try:
            fm = read_frontmatter(skill_md)
        except (ValueError, OSError) as exc:
            errors.append(f"{rel}/SKILL.md: {exc}")
            continue

        errors.extend(
            scan_retired_patterns(skill_md.read_text(encoding="utf-8"), f"{rel}/SKILL.md")
        )

        name = fm.get("name")
        if not name or not str(name).strip():
            errors.append(f"{rel}/SKILL.md: frontmatter missing 'name'")
        else:
            if name in names:
                errors.append(
                    f"{rel}/SKILL.md: duplicate frontmatter name '{name}' "
                    f"(also in {names[name]})"
                )
            else:
                names[name] = str(rel)

        description = fm.get("description")
        if not description or not str(description).strip():
            errors.append(f"{rel}/SKILL.md: frontmatter missing 'description'")

        # Warn if a skill directory is not referenced by any bundle.
        ref_forms = {f"./{rel.as_posix()}", rel.as_posix()}
        if not (ref_forms & referenced):
            warnings.append(f"{rel}: directory is not referenced by any bundle")

    # --- Report -----------------------------------------------------------
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\n{len(errors)} error(s) found.")
        return 1

    print(f"OK: {len(skill_dirs)} skills validated, {len(referenced)} bundle references resolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
