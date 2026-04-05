---
name: scanning-inbox-for-evergreen
description: Scans Gmail for actionable items and maps them to Evergreen CRM contacts — unanswered questions, promised deliverables, introduction requests, and follow-ups needed. Use when triaging your inbox, catching missed commitments, or syncing email activity to your CRM. Requires Gmail connected in Claude.
---

# Inbox Scan for Action Items

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Weekly inbox triage: "What did I miss this week?"
- After a busy period: "What commitments did I make in email that I haven't followed through on?"
- CRM sync: "Update Evergreen with everything that happened in email this week"
- Before a meeting: "Any recent emails from this person I should review?"

## Prerequisites

- Gmail connected in Claude (via Google Workspace MCP or Gmail integration)
- Evergreen MCP server running

## How It Works

1. Search Gmail for recent emails (sent and received) from the target time period
2. For each email thread, identify: unanswered questions, promised deliverables, meeting requests, and introduction requests
3. Match email addresses to Evergreen contacts using `search_contacts` with `email:` token
4. For known contacts: create actions with `actions.create` for anything that needs follow-through
5. For unknown senders worth tracking: flag for potential contact creation
6. Summarize findings in a structured report

## What to Surface

| Category | Signal | Action |
|----------|--------|--------|
| Unanswered questions | Someone asked you something, no reply sent | Create action: "Reply to [name] re: [topic]" |
| Promised deliverables | You said "I'll send..." or "Let me check on..." | Create action: "Send [deliverable] to [name]" |
| Introduction requests | "Can you connect me with...?" | Create action: "Intro [name] to [name]" |
| Meeting requests | Scheduling discussion without resolution | Create action: "Schedule meeting with [name]" |
| Stale threads | Important thread with no response for 3+ days | Create action: "Follow up on [topic]" |
| New contacts | Interesting person not yet in Evergreen | Flag for contact capture |

## Example Output

```markdown
## Inbox Scan — Apr 1-5, 2026

### Needs Action (4)
1. **Sarah Chen** (sarah@meridianhealth.com) — Asked about API pricing on Apr 3.
   No reply sent. → Created action: "Reply to Sarah re: API pricing"

2. **You → Marcus Webb** — Wrote "I'll send the deck by EOW" on Apr 1.
   Not sent yet. → Created action: "Send partnership deck to Marcus"

3. **Jamie Rodriguez** — Requested intro to your contact at Stripe on Apr 2.
   → Created action: "Intro Jamie to [Stripe contact]"

4. **Tom Bradley** — Proposed coffee next week on Apr 4.
   No reply. → Created action: "Reply to Tom re: coffee scheduling"

### New Contacts Detected (2)
- **Priya Sharma** (priya@newco.ai) — 3 email exchanges, not in Evergreen
- **Alex Chen** (alex@investorgroup.com) — Intro from Sarah, not in Evergreen

### Already Handled (12 threads reviewed, no action needed)
```

## Checklist

```
Inbox Scan:
- [ ] Time period specified (default: last 7 days)
- [ ] Both sent and received emails reviewed
- [ ] Email addresses matched to Evergreen contacts
- [ ] Actions created for items needing follow-through
- [ ] Unknown important contacts flagged
- [ ] Summary report generated
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
