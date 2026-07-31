---
name: evergreen-follow-up-reminders
description: Generates a prioritized follow-up list from Evergreen CRM based on overdue actions, stale contacts, and interaction cadences. Use when planning your week, checking who needs attention, or building a daily outreach list.
---

# Follow-Up Reminder Generator

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Start of the week: "Who do I need to follow up with?"
- Daily outreach planning: "What's my follow-up list today?"
- After returning from travel or a busy period
- When you feel like you're losing touch with important contacts

## How It Works

1. Pull overdue actions with `get_overdue_actions` and actions approaching their due dates with `get_actions_due_soon`
2. Shortlist cold relationships with `get_relationship_strengths` — call it with `grade: "Weak"` and again with `grade: "Dormant"` (or set a `maxScore` ceiling), each with an explicit `limit: 100`, its maximum. The server scores every contact 0–100 and returns them sorted strongest-first, so one or two calls give you a ranked candidate set without scanning the whole database
3. Resolve each shortlisted candidate to a contact ID with `search_contacts({ query: "<name>" })` — `get_relationship_strengths` returns name, organization, score and grade, but no contact ID
4. Read each candidate's actual `Last Interaction` date from `get_contact` (and `get_contact_interactions` where the timeline matters) before stating any day count. The score blends recency with frequency, depth and variety, so a low grade means "probably cold, go check" — it is a candidate filter, not the verdict
5. To scope the list to part of your network rather than all of it, use the filters `search_contacts` already exposes (`tags`, `organization`, `location`, `hasEmail`, `hasPhone`, `overdue`, `hasNextAction`, `recent`) with an explicit `limit: 100`, its maximum, since the default of 20 would sweep only a fraction of the database — then say which slices the list came from. Its results carry `Last Updated`, the record's modification time, not an interaction date
6. Prioritize by: overdue actions first, then high-value relationships, then cadence-based follow-ups
7. Present a ranked list with context for each follow-up

## Priority Framework

| Priority | Criteria | Example |
|----------|----------|---------|
| Urgent | Overdue action with a due date | "Send proposal to Kim — due 3 days ago" |
| High | Important contact not touched in 30+ days | "Haven't talked to your co-founder in 6 weeks" |
| Medium | Regular contact approaching stale threshold | "Coffee with Alex was 3 weeks ago" |
| Low | Weak tie worth maintaining quarterly | "Last saw Jordan at the conference 2 months ago" |

## Example Output

```markdown
## Follow-Up List — Week of April 7

### Overdue Actions (3)
1. **Sarah Chen** — Send API documentation (due Apr 2) [High priority]
2. **Marcus Webb** — Intro to Jamie at Acme Labs (due Apr 4) [Medium priority]
3. **Lisa Park** — Review proposal draft (due Apr 5) [Medium priority]

### Stale Relationships (5)
4. **David Kim** — Weak (score 32). Last interaction: 45 days ago (meeting). Was discussing partnership.
5. **Rachel Torres** — Dormant (score 18). Last interaction: 38 days ago (email). Offered to help with hiring.

### Cadence Check-Ins (4)
6. **Tom Bradley** — Quarterly check-in due. Last: Jan 15 coffee.
7. **Nina Patel** — Monthly sync overdue. Last: Mar 1 call.
```

Note that Rachel grades lower than David despite the shorter gap — the score
weighs frequency, depth and variety alongside recency. That is why the day counts
above come from each contact's `Last Interaction` field rather than from the
ranking, and why the shortlist covers both the Weak and Dormant bands.

## Suggested Cadences

| Relationship Type | Cadence | Flag When Last Interaction Exceeds |
|-------------------|---------|------------------------------------|
| Close collaborators | Every 2 weeks | 14 days |
| Active network | Monthly | 30 days |
| Extended network | Quarterly | 90 days |
| Dormant (re-engage?) | 6+ months | 180 days |

No read filters contacts by elapsed time, and neither of the list-style reads
returns an interaction date: `search_contacts` reports `Last Updated` (the record's
modification time, which an enrichment edit refreshes) and `get_relationship_strengths`
reports a score. So shortlist with the grade filters, then compare the `Last Interaction`
date from `get_contact` against these thresholds yourself, one candidate at a time.

## Checklist

```
Follow-Up Review:
- [ ] Overdue actions surfaced and prioritized
- [ ] Cold candidates shortlisted with `get_relationship_strengths` (Weak and Dormant grades, explicit `limit: 100`)
- [ ] Each candidate resolved to an ID with `search_contacts({ query })`
- [ ] Every day count read from `get_contact`'s `Last Interaction` — never from a score or from `Last Updated`
- [ ] Stale high-value contacts prioritized by relationship value
- [ ] Context and an actionable next step provided for each follow-up
- [ ] List is manageable (5-10 items for the week)
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
