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

1. Shortlist candidates with `get_relationship_strengths({ grade: "Dormant", limit: 100 })`, then repeat with `grade: "Weak"` (or set a `maxScore` ceiling) to widen the net. The server scores every contact 0–100 on recency, frequency, depth and variety and returns them sorted strongest-first
2. Resolve each candidate to a contact ID with `search_contacts({ query: "<name>" })` — `get_relationship_strengths` returns name, organization, score and grade, but no contact ID
3. Confirm each one is genuinely dormant by reading the `Last Interaction` date from `get_contact`, and pull the history with `get_contact_interactions`. The score is a candidate filter, not the verdict — a low grade means "probably cold, go check", so the "older than 90 or 180 days" judgment and any day count you state come from that date. `search_contacts` results report `Last Updated`, the record's modification time, which an enrichment edit refreshes
4. Check their network connections with `get_contact_network` for warm re-entry points
5. Research recent activity (job changes, company news) for a natural conversation hook
6. Draft a low-pressure re-engagement message
7. Create a follow-up action with `create_action` to track the outreach

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
Relationship strength: 38/100 (Weak) — from get_relationship_strengths
Last interaction: Oct 15 (meeting) — "Discussed potential data partnership",
  from get_contact
Tags: founder, data, atlanta
Notes: "Building real-time analytics platform. Previously at Google."
Dormant: 173 days since last interaction
```

Marcus grades Weak rather than Dormant — an earlier run of frequent, substantive
meetings still props up his score — which is why the shortlist covers both bands
and why the 173 days is read from `get_contact`, not inferred from the grade.

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
create_action({
  contactId: marcus_id,
  title: "Follow up if Marcus doesn't reply by Apr 19",
  dueDate: "2026-04-19",
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
- [ ] Candidates shortlisted with `get_relationship_strengths` (Dormant, plus Weak to widen the net)
- [ ] Each candidate resolved to an ID with `search_contacts({ query })`
- [ ] Dormancy confirmed against `get_contact`'s `Last Interaction` date, not a score
- [ ] Prioritized by relationship value and re-engagement potential
- [ ] Natural hook found for each message (not generic)
- [ ] Message is brief and low-pressure
- [ ] Follow-up action created to track response
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
