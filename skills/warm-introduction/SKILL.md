---
name: drafting-warm-introductions
description: Drafts double-opt-in introduction emails connecting two Evergreen CRM contacts. Use when someone asks for an introduction, when you spot a mutually beneficial connection, or when facilitating networking between contacts.
---

# Warm Introduction Drafting

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Someone asks "Do you know anyone who...?"
- You spot a mutually beneficial connection between two contacts
- You promised to make an introduction
- After a meeting where two contacts should meet

## How It Works

1. Retrieve both contacts with `get_contact` for full profiles
2. Pull interaction history for both with `interactions.list`
3. Check if they're already connected with `get_contact_network`
4. Draft a double-opt-in permission email (ask each party first)
5. Draft the actual introduction email
6. Log the interaction for both contacts with `interactions.log`
7. Create relationships with `relationships.create` (type: "introduced_by")

## Double-Opt-In Process

**Step 1: Permission ask (to each party separately)**

```
Subject: Quick intro — [Name] at [Company]?

Hey Sarah,

I've been talking with Marcus Webb, who's building a real-time analytics
platform at DataFlow. Based on what you've told me about Meridian's
data infrastructure challenges, I think you two would have a lot to
discuss.

Would you be open to an intro? Happy to connect you over email.
```

**Step 2: Introduction email (after both agree)**

```
Subject: Intro — Sarah Chen <> Marcus Webb

Sarah, Marcus — excited to connect you two.

Sarah is the CTO at Meridian Health, building out their healthcare
data pipeline. Marcus is the founder of DataFlow, focused on
real-time analytics infrastructure.

I think there's a natural overlap in the data pipeline space that
would make for a great conversation.

I'll let you two take it from here!
```

**Step 3: Log in Evergreen**

```
1. interactions.log(sarah_id, type: "email", summary: "Introduced to Marcus Webb (DataFlow) — data pipeline overlap")
2. interactions.log(marcus_id, type: "email", summary: "Introduced to Sarah Chen (Meridian Health) — data pipeline overlap")
3. relationships.create({
     contact_id: sarah_id,
     related_contact_id: marcus_id,
     type: "introduced_by",
     notes: "Connected re: data infrastructure — Apr 2026"
   })
```

## Introduction Quality Checklist

| Element | Why |
|---------|-----|
| Both parties opted in | Respect and trust — never blind-intro |
| Clear reason for connecting | Not just "you should know each other" |
| Brief context on each person | Save them the Googling |
| Specific overlap highlighted | Give them a starting point |
| Graceful exit | "I'll let you two take it from here" |

## Checklist

```
Warm Introduction:
- [ ] Both contacts' profiles and history reviewed
- [ ] Mutual benefit clearly identified
- [ ] Double-opt-in obtained before sending intro
- [ ] Introduction email includes context on both parties
- [ ] Interaction logged for both contacts
- [ ] Relationship created in Evergreen
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
