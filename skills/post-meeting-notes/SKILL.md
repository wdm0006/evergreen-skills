---
name: processing-meeting-notes-for-evergreen
description: Processes raw meeting notes into structured Evergreen CRM records — logs interactions, creates action items, adds new contacts, and updates notes. Use after any meeting, call, or conversation to capture everything in your CRM without manual data entry.
---

# Post-Meeting Notes Processor

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- After a meeting, call, or coffee chat
- When you have voice-transcribed notes to process
- After a group meeting with multiple contacts
- When you jotted down quick notes and want to formalize them

## How It Works

1. Parse the raw notes to identify: attendees, topics discussed, decisions made, action items, and new contacts mentioned
2. Match attendees to existing contacts with `search_contacts`
3. Log the interaction for each attendee with `interactions.log`
4. Create action items with `actions.create` for any commitments
5. For new people mentioned, create contacts with `contacts.create`
6. Append detailed notes with `notes.append` for relevant contacts
7. Create relationships with `relationships.create` if new connections were established

## Extraction Targets

| Element | What to Look For | Evergreen Action |
|---------|-----------------|-----------------|
| Attendees | Names, titles, companies | Match or create contacts |
| Topics | Key subjects discussed | Include in interaction summary |
| Decisions | Agreed-upon outcomes | Note in interaction + notes |
| Action items | "I'll...", "You should...", "Let's..." | `actions.create` with due dates |
| New contacts | "You should talk to..." | `contacts.create` + flag for follow-up |
| Relationships | "Sarah works with Marcus on..." | `relationships.create` |
| Follow-ups | Next meeting, deadlines | `actions.create` with dates |

## Example

**Raw meeting notes:**
```
Call with Sarah Chen and Lisa Park from Meridian Health on Apr 5.

Discussed the API integration timeline. Sarah wants to start the
pilot in Q3. Lisa is handling the procurement side — she needs our
security questionnaire filled out by end of April.

They mentioned their new data engineer Raj Patel would be our main
technical contact. Sarah will send his details.

We agreed to:
- Send the security questionnaire by Apr 15
- Schedule a technical deep-dive with Raj once connected
- Sarah will share their data schema doc by next week
```

**Processed into Evergreen:**
```
1. interactions.log(sarah_id, {
     type: "call",
     summary: "Discussed API integration — Q3 pilot start. Lisa handling procurement. New tech contact Raj Patel joining."
   })

2. interactions.log(lisa_id, {
     type: "call",
     summary: "Procurement discussion for API integration. Needs security questionnaire by end of April."
   })

3. actions.create({
     contact_id: lisa_id,
     title: "Send security questionnaire to Lisa Park",
     due_date: "2026-04-15",
     priority: "high"
   })

4. actions.create({
     contact_id: sarah_id,
     title: "Schedule technical deep-dive with Raj Patel (after intro)",
     priority: "medium"
   })

5. actions.create({
     contact_id: sarah_id,
     title: "Follow up if Sarah hasn't sent data schema doc by Apr 12",
     due_date: "2026-04-12",
     priority: "medium"
   })

6. notes.append(sarah_id, "Apr 5 call: Q3 pilot confirmed. New tech contact: Raj Patel (data engineer). Lisa handling procurement.")
```

## Checklist

```
Post-Meeting Processing:
- [ ] All attendees identified and matched to contacts
- [ ] Interaction logged for each attendee
- [ ] All action items captured with owners and due dates
- [ ] New contacts created (or flagged for creation)
- [ ] Relevant notes appended to contact records
- [ ] Relationships updated if new connections established
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
