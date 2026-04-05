---
name: capturing-contacts-in-evergreen
description: Parses unstructured text (email signatures, business cards, LinkedIn profiles, meeting notes) into structured Evergreen CRM contacts. Use when adding new contacts from raw text, importing contacts from emails or messages, or batch-creating contacts from event notes.
---

# Smart Contact Capture

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Someone shares a business card or email signature
- You have raw text with contact details (from a conference, email thread, or LinkedIn)
- You need to batch-create contacts from meeting notes or an event attendee list
- You received an introduction email and want to add the new person

## How It Works

1. Parse the unstructured text to extract: name, title, organization, email, phone, location, and any contextual notes
2. Search existing contacts with `search_contacts` to check for duplicates
3. If the contact doesn't exist, create it with `contacts.create`
4. Add relevant tags with `tags.add_to_contact` (e.g., "met-at-conference", "investor", "lead")
5. Append context notes with `notes.append` (how you met, who introduced you, conversation topics)
6. If an introduction, log the interaction with `interactions.log`

## Extraction Patterns

| Source | What to Extract |
|--------|----------------|
| Email signature | Name, title, org, email, phone, address |
| LinkedIn URL | Name, headline as title, company as org |
| Business card text | All fields, watch for multiple phone/email |
| Meeting notes | Names, affiliations, discussion context |
| Introduction email | Both parties, relationship context, reason for intro |

## Example

**Input:**
```
Hey, great meeting Sarah Chen at the AI dinner last night. She's the
CTO at Meridian Health, based in Atlanta. Her email is sarah@meridianhealth.com
and she's really interested in our API work.
```

**Actions:**
```
1. search_contacts("Sarah Chen") → no match
2. contacts.create({
     first_name: "Sarah",
     last_name: "Chen",
     title: "CTO",
     organization: "Meridian Health",
     email: "sarah@meridianhealth.com",
     location: "Atlanta"
   })
3. tags.add_to_contact(contact_id, ["ai", "healthcare", "atlanta"])
4. notes.append(contact_id, "Met at Atlanta AI Dinner. Interested in our API work.")
5. interactions.log(contact_id, type: "meeting", summary: "Met at Atlanta AI Dinner — discussed API work")
```

## Checklist

```
Contact Capture:
- [ ] Name parsed correctly (first/last split)
- [ ] Duplicate check performed before creating
- [ ] All available fields populated
- [ ] Tags applied for context/source
- [ ] Meeting context saved in notes
- [ ] Initial interaction logged
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
