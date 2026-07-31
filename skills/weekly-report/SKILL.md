---
name: evergreen-weekly-report
description: Generates a weekly relationship management digest from Evergreen CRM — interactions logged, follow-ups completed vs missed, network growth, and a spotlight contact. Use for weekly reviews, accountability, or planning the week ahead.
---

# Weekly Relationship Report

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Sunday/Monday planning: "How did last week go and what's ahead?"
- Weekly accountability check on relationship management habits
- Before a 1:1 where you want to share networking activity
- Monthly roll-ups for tracking relationship investment over time

## How It Works

1. Pull recent activity with `get_activity_log`, passing `limit: 100` (its maximum; the default is 20). The tool has no date-range parameter — it returns the most recent entries and you select the week from them client-side, so the week is only fully covered if the response comes back under 100. At exactly 100 the log is truncated at the ceiling and the week may start before the oldest entry you got; there is no offset or cursor to reach further back, so say so instead of publishing counts you know are floors
2. List interactions logged with `get_contact_interactions` for the period, passing `limit: 50` (its maximum; the default is 10 per contact). This read has no pagination either — a contact returning 50 has more history than one call can reach
3. Check completed actions with `list_actions`, passing `limit: 100` (its maximum; the default is 50)
4. Check overdue actions with `get_overdue_actions` and upcoming actions with `get_actions_due_soon`
5. Search for new contacts added with `search_contacts`, passing `limit: 100` (its maximum; the default is 20)
6. Compile into a structured weekly digest. A read that comes back at its maximum is truncated, and none of these reads paginate — so narrow it with the filters the tool already exposes (`get_activity_log` takes `entityType` and `agentId`; `list_actions` takes `status` and `dueDateAfter`/`dueDateBefore`) and state in the coverage line which reads hit their ceiling

## Report Format

```markdown
## Weekly Relationship Report — [Date Range]

_Coverage: 87 activity entries, 41 actions and 63 contacts read — no read came back
at its maximum, so the counts below are complete for the period. The activity log
has no date filter, so the week was selected client-side from those 87 entries._

### Activity Summary
| Metric | This Week | Trend |
|--------|-----------|-------|
| Interactions logged | 12 | +3 from last week |
| New contacts added | 4 | +2 from last week |
| Actions completed | 7 | Same as last week |
| Actions overdue | 2 | -1 from last week |

### Interactions by Type
- Meetings: 4
- Emails: 5
- Calls: 2
- DMs: 1

### Follow-Up Scorecard
- **Completed on time:** 7/9 (78%)
- **Overdue:** 2 (Send proposal to Kim, Intro Jamie to Stripe contact)
- **Created this week:** 5

### New Contacts
1. Raj Patel — Data Engineer, Meridian Health (via Sarah Chen)
2. Amy Liu — Product Manager, TechCorp (met at meetup)
3. [...]

### Notable Interactions
- Deep-dive meeting with Sarah Chen on API integration (progressing toward Q3 deal)
- Reconnected with Tom Bradley after 2 months (coffee scheduled)
- Introduced Marcus Webb to Jamie Rodriguez

### Spotlight: Contact Worth Investing In
**David Kim** — Your top introducer (8 intros), but you haven't
reached out in 45 days. He recently posted about launching a new
product. Consider a congratulatory message this week.

### Next Week Preview
- 3 pending actions due
- 5 contacts approaching stale threshold
- 1 overdue action from this week to carry forward
```

## Checklist

```
Weekly Report:
- [ ] Every read passed an explicit `limit` at the tool's maximum — `get_activity_log` 100, `get_contact_interactions` 50, `list_actions` 100, `search_contacts` 100 (never the defaults: 20, 10, 50, 20)
- [ ] Coverage line states what was read and whether any read came back at its maximum, which means truncation — none of these reads take an offset or cursor
- [ ] Activity entries filtered to the correct date range client-side (`get_activity_log` has no date parameter)
- [ ] Interaction counts broken down by type
- [ ] Follow-up completion rate calculated
- [ ] New contacts listed with source/context
- [ ] Notable interactions highlighted
- [ ] Spotlight contact selected with actionable suggestion
- [ ] Next week preview included
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
