---
name: evergreen-context-recall
description: Generates a narrative summary of everything known about a contact in Evergreen CRM — how you met, what you've discussed, mutual connections, and pending threads. Use when you need to quickly refresh your memory before reaching out, replying, or meeting someone.
---

# Context Recall — "Refresh My Memory"

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- "What do I know about [name]?" before reaching out
- Someone emails you and you can't place them
- Before replying to a message from a contact you haven't talked to in a while
- When you need to brief someone else about a contact

## How It Works

1. Look up the contact with `get_contact` for full profile
2. Pull all interactions with `interactions.list` for complete history
3. Check pending actions with `actions.list`
4. Map their network with `get_contact_network` for relationships and introductions
5. Check introduction chains with `get_introduction_chain`
6. Compile into a narrative summary

## Output Format

```markdown
## [Name] — What You Know

**[Title] at [Organization]** | [Location]
**In your CRM since:** [date] | **Last interaction:** [date] ([days] ago)
**Tags:** [tags]

### How You Connected
[Narrative: who introduced you, where you met, initial context]

### Relationship Timeline
- **[Date]** — [Interaction type]: [Summary]
- **[Date]** — [Interaction type]: [Summary]
- **[Date]** — [Interaction type]: [Summary]
[... complete history]

### What They're Working On
[Synthesized from notes and recent interactions — their current focus,
projects, interests]

### Your Shared Network
- **Introduced by:** [name and context]
- **You both know:** [mutual connections]
- **You introduced them to:** [names]

### Open Threads
- [Pending action 1]
- [Pending action 2]
- [Unanswered question or unresolved topic from last interaction]

### Key Details
[Anything notable from their notes — preferences, interests, important
context for future conversations]
```

## Example

**Request:** "Refresh my memory on Marcus Webb"

**Output:**
```markdown
## Marcus Webb — What You Know

**Founder & CEO at DataFlow** | Atlanta, GA
**In your CRM since:** Sep 2025 | **Last interaction:** Apr 1, 2026 (4 days ago)
**Tags:** founder, data, atlanta, startup

### How You Connected
David Kim introduced you at the Atlanta AI Dinner in September 2025.
Marcus was building DataFlow out of stealth at the time.

### Relationship Timeline
- **Apr 1** — Email: You sent the partnership proposal for data pipeline collaboration
- **Mar 20** — Meeting: Deep-dive on data architecture at his office
- **Feb 10** — Coffee: Caught up on DataFlow's progress, discussed hiring challenges
- **Dec 5** — Meeting: Holiday dinner, met his co-founder Alex Torres
- **Sep 15** — Meeting: First met at Atlanta AI Dinner

### What They're Working On
Building a real-time analytics platform for enterprise data pipelines.
Previously spent 5 years at Google on BigQuery. Recently closed a
$4M seed round. Hiring engineers aggressively.

### Your Shared Network
- **Introduced by:** David Kim
- **You both know:** Sarah Chen (Meridian Health), David Kim (DataTech)
- **His co-founder:** Alex Torres (met at Dec holiday dinner)

### Open Threads
- Partnership proposal sent Apr 1 — awaiting response
- Promised to intro him to your contact at Stripe

### Key Details
- Prefers morning meetings (noted from scheduling patterns)
- Big fan of Rust and real-time systems
- Has a dog named Byte (mentioned multiple times)
```

## Checklist

```
Context Recall:
- [ ] Full contact profile retrieved
- [ ] Complete interaction history reviewed
- [ ] Network and relationships mapped
- [ ] Introduction chain traced
- [ ] Open actions and threads identified
- [ ] Narrative is readable and useful (not just raw data)
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
