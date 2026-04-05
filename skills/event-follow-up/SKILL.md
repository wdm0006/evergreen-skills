---
name: evergreen-event-follow-up
description: Batch-processes contacts from a conference, dinner, or networking event into Evergreen CRM — creates records, tags them by event, and drafts personalized follow-up messages. Use after any event where you met multiple new people.
---

# Event Follow-Up Workflow

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- After a conference, meetup, dinner, or networking event
- You have a stack of business cards or a list of people you met
- You want to batch-create contacts and send personalized follow-ups
- After hosting or attending a group event

## How It Works

1. Parse the attendee list or notes to extract contact details
2. For each person, check for duplicates with `search_contacts`
3. Create new contacts with `contacts.create`
4. Tag all contacts with the event name using `tags.add_to_contact`
5. Log the initial meeting as an interaction with `interactions.log`
6. Append conversation context to notes with `notes.append`
7. Draft personalized follow-up messages for each contact
8. Create follow-up actions with `actions.create`

## Event Tag Convention

Use consistent event tags for easy filtering later:

```
Format: event-[name]-[year]
Examples:
  event-ai-dinner-2026
  event-pycon-2026
  event-founders-retreat-q1
  event-team-offsite-apr26
```

## Example

**Input: Notes from Atlanta AI Dinner**
```
Met at Atlanta AI Dinner, April 3, 2026:

1. Sarah Chen — CTO at Meridian Health. Talked about healthcare data
   pipelines. Very interested in our API. sarah@meridianhealth.com

2. Marcus Webb — Founder of DataFlow. Building real-time analytics.
   Previously at Google. marcus@dataflow.io

3. Priya Sharma — ML Engineer at NewCo. Working on NLP for
   customer support. priya@newco.ai. Introduced by David Kim.
```

**Batch processing:**
```
For each contact:
1. search_contacts("[name]") → check for duplicates
2. contacts.create({ ... })
3. tags.add_to_contact(id, ["event-ai-dinner-2026", "atlanta", "ai"])
4. interactions.log(id, {
     type: "meeting",
     summary: "Met at Atlanta AI Dinner — [conversation topic]"
   })
5. notes.append(id, "[conversation details]")
6. actions.create({
     contact_id: id,
     title: "Send follow-up email to [name]",
     due_date: "2026-04-05",
     priority: "medium"
   })
```

**Sample follow-up for Sarah:**
```
Subject: Great meeting you at the AI Dinner

Hi Sarah,

Really enjoyed our conversation about healthcare data pipelines last
night. The challenges you described with real-time patient data are
exactly the kind of problems I find fascinating.

I'd love to continue the conversation — especially around how our
API might fit into Meridian's architecture. Free for a quick call
next week?

Best,
[Name]
```

## Follow-Up Timing

| Priority | When to Send | Who |
|----------|-------------|-----|
| Same night / next morning | People you had deep conversations with |
| Within 48 hours | Everyone else you want to stay in touch with |
| Within a week | Lower priority but still worth connecting |
| Skip | Brief hellos with no real connection point |

## Checklist

```
Event Follow-Up:
- [ ] All contacts created with complete details
- [ ] Event tag applied consistently
- [ ] Initial interaction logged with conversation context
- [ ] Notes capture what you discussed (not just who they are)
- [ ] Follow-up messages personalized per conversation
- [ ] Follow-up actions created with appropriate deadlines
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
