#!/usr/bin/env python3
"""Validate skill structure and marketplace.json integrity.

Checks that:
  * every skill path referenced by .claude-plugin/marketplace.json points to a
    real directory containing a SKILL.md;
  * every skills/*/SKILL.md has parseable YAML frontmatter with non-empty
    `name` and `description` fields;
  * no two skills share the same frontmatter `name`;
  * (warning only) every skills/* directory is referenced by at least one bundle.

Exits non-zero if any error is found. Run locally with:

    python3 scripts/validate_skills.py

No third-party dependencies are required. PyYAML is used if installed,
otherwise a minimal parser handles the flat `key: value` frontmatter.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = REPO_ROOT / "skills"

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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

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
