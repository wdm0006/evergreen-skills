# Evergreen CRM Skills for Claude Code

A comprehensive set of Claude Code skills for personal CRM workflows with [Evergreen](https://heltonlabs.com/evergreen), the local-first personal CRM for macOS.

[Get Evergreen on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12) | [Learn more at Helton Labs](https://heltonlabs.com/evergreen)

## What is Evergreen?

[Evergreen](https://heltonlabs.com/evergreen) is a privacy-first personal CRM for macOS. All your data stays on your Mac in a single SQLite file — no cloud, no subscriptions, no telemetry. It includes a built-in MCP server that lets AI agents like Claude read and write your contacts, interactions, actions, and relationships directly.

Read about how Evergreen was built and what it can do:

- [Vibe Coding a Personal CRM in Swift](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/) — the origin story
- [Evergreen Gets Serious: Building Tools That Think With You](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/) — MCP integration, data model expansion
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/) — network visualization, analytics, and more

## Installation

### Step 1: Add the Marketplace

First, add this repository as a plugin marketplace in Claude Code:

```
/plugin marketplace add wdm0006/evergreen-skills
```

### Step 2: Install a Plugin Bundle

Install the complete skill set (recommended):

```
/plugin install evergreen-complete@wdm0006-evergreen-skills
```

Or install specific bundles based on your needs:

```
# Core daily-driver skills
/plugin install evergreen-essentials@wdm0006-evergreen-skills

# Gmail integration skills
/plugin install evergreen-email@wdm0006-evergreen-skills

# Relationship nurturing skills
/plugin install evergreen-networking@wdm0006-evergreen-skills

# Monitoring and maintenance skills
/plugin install evergreen-reporting@wdm0006-evergreen-skills
```

### Alternative: Local Installation

For project-specific installation, clone this repository and copy the skills you need:

```bash
# Clone the repository
git clone https://github.com/wdm0006/evergreen-skills.git

# Copy skills to your project's .claude/skills/ directory
mkdir -p .claude/skills
cp -r evergreen-skills/skills/* .claude/skills/
```

Or for global installation (available in all projects):

```bash
# Copy to your personal Claude skills directory
mkdir -p ~/.claude/skills
cp -r evergreen-skills/skills/* ~/.claude/skills/
```

### Verifying Installation

After installation, you can verify the skills are loaded by running:

```
/plugin list
```

> **Note:** Skills require Claude Code Pro, Max, Team, or Enterprise. Free tier users do not have access to Skills.

## Prerequisites

### Evergreen CRM

[Download Evergreen from the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12) and make sure the MCP server is configured in your Claude settings:

```json
{
  "mcpServers": {
    "evergreen-crm": {
      "command": "/Applications/Evergreen.app/Contents/MacOS/evergreen-mcp"
    }
  }
}
```

### Gmail Integration (Optional)

Some skills (inbox-scan, auto-log-interactions) work best with Gmail connected in Claude. If you have Gmail set up via Google Workspace MCP or Claude's built-in Gmail integration, those skills can scan your email and sync activity to Evergreen automatically.

## Available Skills

| Skill | Description | Gmail? |
|-------|-------------|--------|
| **[capturing-contacts-in-evergreen](skills/contact-capture/)** | Parse unstructured text into CRM contacts | |
| **[enriching-evergreen-contacts](skills/contact-enrichment/)** | Web-research contacts and fill in missing details | |
| **[evergreen-follow-up-reminders](skills/follow-up-reminders/)** | Generate prioritized follow-up lists | |
| **[drafting-evergreen-follow-ups](skills/draft-follow-up/)** | Draft personalized follow-up messages | |
| **[re-engaging-evergreen-contacts](skills/re-engagement/)** | Find and re-engage dormant contacts | |
| **[drafting-warm-introductions](skills/warm-introduction/)** | Draft double-opt-in introduction emails | |
| **[scanning-inbox-for-evergreen](skills/inbox-scan/)** | Scan Gmail for action items mapped to contacts | Yes |
| **[auto-logging-email-interactions](skills/auto-log-interactions/)** | Sync Gmail activity to Evergreen interaction history | Yes |
| **[evergreen-meeting-prep](skills/meeting-prep/)** | Pre-meeting briefings with full contact context | |
| **[processing-meeting-notes-for-evergreen](skills/post-meeting-notes/)** | Process raw notes into CRM records and actions | |
| **[evergreen-event-follow-up](skills/event-follow-up/)** | Batch-process contacts from events and conferences | |
| **[evergreen-context-recall](skills/context-recall/)** | "Refresh my memory" narrative summaries | |
| **[evergreen-relationship-health](skills/relationship-health/)** | Score and surface relationship health across your network | |
| **[evergreen-network-analysis](skills/network-analysis/)** | Analyze clusters, bridges, and introduction chains | |
| **[evergreen-weekly-report](skills/weekly-report/)** | Weekly relationship management digest | |
| **[evergreen-stale-data-audit](skills/stale-data-audit/)** | Find and fix stale or incomplete contact data | |
| **[evergreen-life-event-tracker](skills/life-events/)** | Track and act on birthdays, job changes, milestones | |
| **[evergreen-news-alerts](skills/news-alerts/)** | Monitor news about contacts and their companies | |

## Plugin Bundles

### evergreen-complete
All 18 skills for comprehensive CRM workflow automation with Evergreen.

### evergreen-essentials
Core daily-driver skills:
- Contact capture
- Follow-up reminders
- Draft follow-up messages
- Context recall
- Meeting prep

### evergreen-email
Gmail integration skills:
- Inbox scan for action items
- Auto-log email interactions
- Draft follow-up messages
- Re-engagement outreach

### evergreen-networking
Relationship nurturing skills:
- Event follow-up
- Warm introductions
- Network analysis
- Relationship health
- Life event tracking

### evergreen-reporting
Monitoring and maintenance skills:
- Weekly relationship report
- Stale data audit
- Relationship health
- News alerts

## Usage

Once installed, Claude will automatically use these skills when you ask about:

- Adding contacts to your CRM
- Following up with someone
- Preparing for a meeting
- Processing meeting notes
- Checking on your network health
- Scanning your inbox for missed items
- Analyzing your contact network
- And more...

### Example Prompts

```
"I just met these people at the conference — add them to Evergreen"
"Who do I need to follow up with this week?"
"Prep me for my call with Sarah Chen"
"Process my meeting notes from today"
"How healthy is my network right now?"
"Draft a re-engagement email to Marcus"
"Any news about my top contacts?"
```

## About Evergreen

[Evergreen](https://heltonlabs.com/evergreen) is built by [Helton Labs](https://heltonlabs.com/evergreen). It's a local-first, privacy-respecting personal CRM designed for people who value their relationships and their data.

- No cloud sync — your data stays on your Mac
- No subscriptions — buy once, own forever
- No telemetry — zero tracking, zero analytics
- AI-native — built-in MCP server for Claude and other AI agents
- Fast — handles thousands of contacts with a keyboard-first interface

[Download Evergreen on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12)

## Contributing

Contributions are welcome! Please open an issue or PR on [GitHub](https://github.com/wdm0006/evergreen-skills).

## License

MIT License - see [LICENSE](LICENSE) for details.
