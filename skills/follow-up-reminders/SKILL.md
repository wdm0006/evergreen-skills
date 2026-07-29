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
2. Identify contacts with stale interactions by listing them with `search_contacts` — always passing an explicit `limit: 100`, its maximum, since the default of 20 would sweep only a fraction of the database — and comparing each contact's last-interaction date against your cadence thresholds
3. If there are more than 100 contacts, sweep in batches using the filters `search_contacts` already exposes (`tags`, `organization`, `location`, `hasEmail`, `hasPhone`, `overdue`, `hasNextAction`), prioritizing the slices that hold your important relationships, and say which slices the list came from
4. Cross-reference with relationship context using `get_contact` for high-priority contacts
5. Prioritize by: overdue actions first, then high-value relationships, then cadence-based follow-ups
6. Present a ranked list with context for each follow-up

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
4. **David Kim** — Last interaction: 45 days ago (meeting). Was discussing partnership.
5. **Rachel Torres** — Last interaction: 38 days ago (email). Offered to help with hiring.

### Cadence Check-Ins (4)
6. **Tom Bradley** — Quarterly check-in due. Last: Jan 15 coffee.
7. **Nina Patel** — Monthly sync overdue. Last: Mar 1 call.
```

## Suggested Cadences

| Relationship Type | Cadence | Flag When Last Interaction Exceeds |
|-------------------|---------|------------------------------------|
| Close collaborators | Every 2 weeks | 14 days |
| Active network | Monthly | 30 days |
| Extended network | Quarterly | 90 days |
| Dormant (re-engage?) | 6+ months | 180 days |

`search_contacts` has no time-based filter, so compare each contact's last-interaction date against these thresholds yourself — over the batch you actually retrieved, which is at most 100 contacts per call.

## Checklist

```
Follow-Up Review:
- [ ] Overdue actions surfaced and prioritized
- [ ] `search_contacts` called with an explicit `limit: 100` (never the default 20)
- [ ] Stale high-value contacts identified
- [ ] Context provided for each follow-up
- [ ] Actionable next step suggested for each
- [ ] List is manageable (5-10 items for the week)
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
