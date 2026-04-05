---
name: evergreen-meeting-prep
description: Generates a pre-meeting briefing from Evergreen CRM — contact profiles, interaction history, shared connections, open actions, and suggested talking points. Use before any meeting, call, or coffee chat to refresh your memory and show up prepared.
---

# Pre-Meeting Briefing

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Before a scheduled meeting or call with a contact
- Preparing for a coffee chat or networking event
- Before a group meeting where you want context on attendees
- When someone messages you and you need a quick refresh

## How It Works

1. Look up the contact(s) with `get_contact` for full profile
2. Pull recent interactions with `interactions.list` (last 5-10)
3. Check pending actions with `actions.list` for open commitments
4. Map their network with `get_contact_network` for shared connections
5. Compile a briefing with talking points and reminders

## Briefing Format

```markdown
## Meeting Brief: [Contact Name]
**[Title] at [Organization]** | [Location]
**Tags:** [relevant tags]

### Relationship Summary
- How you met: [from notes]
- Introduced by: [from relationships]
- Relationship strength: [from interaction frequency]

### Recent Interactions
1. [Date] — [Type]: [Summary]
2. [Date] — [Type]: [Summary]
3. [Date] — [Type]: [Summary]

### Open Items
- [ ] [Pending action 1]
- [ ] [Pending action 2]

### Shared Network
- You both know: [mutual contacts from network]
- They were introduced by: [introducer]

### Suggested Talking Points
1. Follow up on: [topic from last interaction]
2. Ask about: [their current project/role from notes]
3. Mention: [relevant shared connection or interest]
4. Address: [any open action items]

### Notes
[Full contact notes from Evergreen]
```

## Example

**Request:** "I have a call with Sarah Chen in 30 minutes"

**Briefing:**
```markdown
## Meeting Brief: Sarah Chen
**CTO at Meridian Health** | Atlanta, GA
**Tags:** healthcare, ai, atlanta, cto

### Relationship Summary
- Met at Atlanta AI Dinner (Sep 2025)
- Introduced by: David Kim
- Active relationship — 6 interactions in past 3 months

### Recent Interactions
1. Apr 3 — Email: Discussed API integration timeline, agreed on Q3
2. Mar 20 — Meeting: Deep-dive on data pipeline architecture
3. Mar 5 — Email: Shared healthcare AI benchmarks paper

### Open Items
- [ ] Send updated API pricing sheet (due Apr 10)
- [ ] Intro to your ML engineer for technical deep-dive

### Shared Network
- You both know: David Kim (DataTech), Marcus Webb (DataFlow)
- Sarah introduced you to: Lisa Park (Meridian Health, VP Product)

### Suggested Talking Points
1. Follow up on Q3 integration timeline — any blockers?
2. Ask about the patient data pipeline migration she mentioned
3. Discuss the ML engineer intro — ready to make it?
4. Share the updated pricing sheet
```

## Multi-Person Meetings

For meetings with multiple attendees, generate a brief for each person and add a section on group dynamics:

```markdown
### Group Context
- Sarah and Marcus have worked together before (DataFlow was a Meridian vendor)
- Jamie hasn't met Sarah — potential intro opportunity
- All three are interested in healthcare data infrastructure
```

## Checklist

```
Meeting Prep:
- [ ] Contact profile reviewed
- [ ] Last 5+ interactions summarized
- [ ] Open actions identified
- [ ] Shared network mapped
- [ ] 3-4 talking points prepared
- [ ] Any deliverables ready to share
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
