---
name: drafting-evergreen-follow-ups
description: Drafts personalized follow-up emails and messages based on Evergreen CRM contact history, past interactions, and pending actions. Use when you need to write a follow-up email, thank-you note, check-in message, or any outreach to an existing contact.
---

# Draft Follow-Up Message

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- After a meeting and you need to send a recap or thank-you
- Following up on a promised deliverable or introduction
- Checking in with someone you haven't talked to recently
- Responding to a trigger (job change, funding news, birthday)

## How It Works

1. Retrieve the contact with `get_contact` for full profile
2. Pull recent interactions with `interactions.list` for conversation history
3. Check pending actions with `actions.list` for any commitments
4. Review the contact's network with `get_contact_network` for shared connections context
5. Draft a message that references specific shared history and feels personal
6. After sending, log the interaction with `interactions.log`
7. Mark any related actions complete with `actions.complete`

## Message Types

| Type | Tone | Key Elements |
|------|------|-------------|
| Post-meeting recap | Professional, warm | Key takeaways, action items, next steps |
| Thank-you note | Grateful, specific | What you're thankful for, why it mattered |
| Check-in | Casual, genuine | Reference last conversation, ask about their work |
| Introduction follow-up | Enthusiastic, brief | Reference who introduced you, what excited you |
| Congratulations | Warm, sincere | Specific achievement, genuine reaction |
| Re-engagement | Low-pressure, curious | Shared memory, open-ended question |

## Example

**Context from Evergreen:**
```
Contact: Sarah Chen (CTO, Meridian Health)
Last interaction: Meeting on Mar 20 — "Discussed API integration possibilities"
Pending action: "Send API documentation" (due Apr 2)
Notes: "Interested in our healthcare data pipeline"
```

**Drafted message:**
```
Subject: API docs + a few thoughts from our chat

Hi Sarah,

Great catching up at the dinner last month. I've been thinking more
about the integration approach we discussed for Meridian's patient
data pipeline.

As promised, here are our API docs: [link]

I flagged the batch processing section specifically — based on what
you described about your throughput needs, that's probably the most
relevant starting point.

Happy to jump on a quick call if any questions come up as your team
reviews. What does your week look like?

Best,
[Name]
```

**Post-send:**
```
1. interactions.log(contact_id, type: "email", summary: "Sent API docs follow-up, offered call to discuss")
2. actions.complete(action_id)  // "Send API documentation"
```

## Writing Principles

| Principle | Meaning |
|-----------|---------|
| Specific | Reference real details from your history, not generic pleasantries |
| Brief | Respect their time — get to the point in 3-5 sentences |
| Action-oriented | Include a clear next step or question |
| Authentic | Match the user's natural voice and relationship level |
| Contextual | Show you remember what matters to them |

## Checklist

```
Follow-Up Draft:
- [ ] Contact history reviewed for relevant context
- [ ] Message references specific shared details
- [ ] Clear call-to-action or next step included
- [ ] Tone matches the relationship level
- [ ] Interaction logged after sending
- [ ] Related actions marked complete
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
