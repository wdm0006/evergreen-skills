---
name: re-engaging-evergreen-contacts
description: Identifies dormant contacts in Evergreen CRM and drafts natural re-engagement messages. Use when you want to reconnect with people you haven't spoken to in months, revive stale relationships, or systematically re-engage your extended network.
---

# Re-Engagement Outreach

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- You notice important contacts going stale (3-6+ months since last interaction)
- You want to systematically re-engage your extended network
- A contact's company is in the news and it's a good excuse to reach out
- You're expanding into a new area and want to reconnect with relevant people

## How It Works

1. Search for dormant contacts with `search_contacts` using `touched:>90d` or `touched:>180d`
2. For each candidate, pull full context with `get_contact` and `interactions.list`
3. Check their network connections with `get_contact_network` for warm re-entry points
4. Research recent activity (job changes, company news) for a natural conversation hook
5. Draft a low-pressure re-engagement message
6. Create a follow-up action with `actions.create` to track the outreach

## Re-Engagement Hooks

| Hook Type | Example | When to Use |
|-----------|---------|-------------|
| News-based | "Saw Acme just raised their Series B — congrats!" | Company milestone or funding |
| Shared memory | "Been thinking about that project we discussed at..." | Genuine shared experience |
| Value-first | "Found this article that reminded me of your work on..." | Offering something relevant |
| Life event | "Happy work anniversary! 3 years at Meridian already?" | LinkedIn milestones |
| Mutual connection | "Just had coffee with Alex — your name came up" | Recent interaction with shared contact |
| Seasonal | "Hope Q1 went well — how's the new product coming?" | Natural transition points |

## Example

**Dormant contact:**
```
Contact: Marcus Webb (Founder, DataFlow)
Last interaction: Oct 15 (meeting) — "Discussed potential data partnership"
Tags: founder, data, atlanta
Notes: "Building real-time analytics platform. Previously at Google."
Dormant: 173 days
```

**Drafted message:**
```
Hey Marcus,

It's been a while — hope things are going well at DataFlow. I remember
you were heads-down on the real-time analytics engine when we last
caught up.

I've been working on some CRM integrations that touch on similar data
pipeline challenges and it made me think of your approach. Would love
to hear how things have evolved.

Coffee sometime in the next couple weeks?
```

**Post-draft:**
```
actions.create(contact_id, {
  title: "Follow up if Marcus doesn't reply by Apr 19",
  due_date: "2026-04-19",
  priority: "low"
})
```

## Principles

| Principle | Why |
|-----------|-----|
| Low pressure | Don't make them feel guilty for not being in touch |
| Genuine hook | Reference something real, not "just checking in" |
| Short | 3-5 sentences max for a re-engagement |
| Easy reply | Ask one simple question, not a laundry list |
| No ask on first touch | Reconnect first, then work up to asks over time |

## Checklist

```
Re-Engagement:
- [ ] Dormant contacts identified by interaction recency
- [ ] Prioritized by relationship value and re-engagement potential
- [ ] Natural hook found for each message (not generic)
- [ ] Message is brief and low-pressure
- [ ] Follow-up action created to track response
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
