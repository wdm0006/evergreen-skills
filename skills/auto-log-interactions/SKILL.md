---
name: auto-logging-email-interactions
description: Parses recent Gmail activity and logs interaction summaries to Evergreen CRM contacts — without storing full email bodies. Use when you want to sync email activity to your CRM, update interaction history, or keep Evergreen current with your communications. Requires Gmail connected in Claude.
---

# Auto-Log Email Interactions

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- End-of-week sync: "Log all my email interactions from this week to Evergreen"
- After a flurry of email activity: "Make sure Evergreen is up to date"
- Before reviewing your follow-up list: ensure interaction dates are current
- Periodic maintenance to keep "Last Interaction" field accurate

## Prerequisites

- Gmail connected in Claude (via Google Workspace MCP or Gmail integration)
- Evergreen MCP server running

## How It Works

1. Fetch recent sent and received emails from Gmail for the target period
2. Group emails by contact/thread
3. Match email addresses to Evergreen contacts using `search_contacts` with `email:` token
4. For each matched contact, summarize the email thread (topic, outcome, next steps)
5. Log the interaction with `interactions.log` (type: "email")
6. Skip contacts that already have a more recent interaction logged

## Privacy-First Approach

| Do | Don't |
|----|-------|
| Log a brief summary of the topic | Store full email bodies in notes |
| Note key decisions or commitments | Copy sensitive content |
| Record the date and direction (sent/received) | Log every single email in a thread |
| Capture next steps | Store attachments or links |

## Example

**Gmail activity (past week):**
```
- 3 emails with sarah@meridianhealth.com (re: API integration timeline)
- 1 email to marcus@dataflow.io (sent partnership proposal)
- 5 emails with jamie@acmelabs.io (re: conference panel planning)
- 2 emails with unknown@newstartup.com (cold outreach, not in CRM)
```

**Logged to Evergreen:**
```
1. search_contacts("email:sarah@meridianhealth.com") → Sarah Chen
   interactions.log(sarah_id, {
     type: "email",
     summary: "Discussed API integration timeline — agreed on Q3 target, Sarah reviewing docs",
     date: "2026-04-03"
   })

2. search_contacts("email:marcus@dataflow.io") → Marcus Webb
   interactions.log(marcus_id, {
     type: "email",
     summary: "Sent partnership proposal for data pipeline collaboration",
     date: "2026-04-01"
   })

3. search_contacts("email:jamie@acmelabs.io") → Jamie Rodriguez
   interactions.log(jamie_id, {
     type: "email",
     summary: "Planning conference panel on AI in healthcare — confirmed topic and date",
     date: "2026-04-04"
   })

4. unknown@newstartup.com → Not in Evergreen (flagged for review)
```

## Checklist

```
Auto-Log:
- [ ] Time period specified for email scan
- [ ] Emails grouped by contact and thread
- [ ] Addresses matched to Evergreen contacts
- [ ] Summaries are concise (not full email bodies)
- [ ] Duplicate interactions not created (check existing)
- [ ] Unknown contacts flagged for potential addition
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
