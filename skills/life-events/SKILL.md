---
name: evergreen-life-event-tracker
description: Tracks and acts on life events and milestones for Evergreen CRM contacts — birthdays, work anniversaries, job changes, promotions, and personal milestones. Use when you want to stay on top of important dates and send timely, thoughtful messages.
---

# Life Event & Milestone Tracker

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Setting up recurring reminders for important dates
- When you learn about a contact's milestone (job change, promotion, funding round)
- Planning proactive outreach around life events
- Weekly check: "Any milestones coming up for my contacts?"

## How It Works

1. Search contacts for known milestones with `search_contacts` and `get_contact`
2. Review notes for date-related context (birthdays, anniversaries mentioned)
3. Create reminder actions with `actions.create` for upcoming events
4. Draft congratulatory or celebratory messages
5. Log the outreach as an interaction with `interactions.log`
6. Update notes with `notes.append` when you learn new milestones

## Milestone Types

| Milestone | How to Learn | Action |
|-----------|-------------|--------|
| Birthday | Contact mentions it, LinkedIn | Annual reminder action |
| Work anniversary | LinkedIn notifications, notes | Congratulatory message |
| Job change | LinkedIn, news, email signature | Update record + congratulate |
| Promotion | LinkedIn, direct conversation | Congratulatory message |
| Company milestone | News, funding announcements | Acknowledge + discuss |
| Personal milestone | Direct conversation, social media | Thoughtful note |
| Speaking engagement | Conference listings, social media | Attend or congratulate |

## Recording Milestones

When you learn about a milestone, record it in notes with a consistent format:

```
notes.append(contact_id, "## Milestones\n- Birthday: March 15\n- Started at Meridian: Jan 2024\n- DataFlow Series A: Oct 2025")
```

Create recurring actions for annual events:

```
actions.create({
  contact_id: id,
  title: "Birthday — send a note to Sarah Chen",
  due_date: "2027-03-15",
  priority: "medium"
})
```

## Message Templates by Milestone

**Job change:**
```
Saw you made the move to [Company] — congrats! [Role] sounds like
a great fit given your background in [area]. How are the first
few weeks going?
```

**Promotion:**
```
Just saw the news about your promotion to [Title] — well deserved!
I remember when you were telling me about [project]. Clearly
making an impact. Coffee to celebrate?
```

**Funding round:**
```
Congrats on the [round] — huge milestone for [Company]! I remember
when you were [earlier stage context]. Exciting to see the momentum.
```

**Work anniversary:**
```
[X] years at [Company] already! Time flies. Hope you're still
enjoying the [thing they mentioned liking about the role].
```

## Checklist

```
Life Events:
- [ ] Known milestones recorded in contact notes
- [ ] Reminder actions created for recurring dates
- [ ] Messages personalized with real context (not generic)
- [ ] Interaction logged after sending
- [ ] Contact record updated if milestone changes their profile (new title, new company)
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
