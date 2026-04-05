---
name: enriching-evergreen-contacts
description: Researches and enriches Evergreen CRM contacts with publicly available information — LinkedIn details, company info, recent news, and shared context. Use when a contact has sparse details, before an important meeting, or when batch-updating stale records.
---

# Contact Enrichment

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- A contact record has only a name and email
- You want to fill in title, organization, location, or social links
- Before an important meeting where you need full context
- Periodic batch enrichment to keep your database current

## How It Works

1. Retrieve the contact with `get_contact` to see what's already known
2. Use web search to find publicly available information (LinkedIn profile, company website, recent news)
3. Update the contact with `contacts.update` to fill in missing fields
4. Append research findings to notes with `notes.append`
5. Add or update tags with `tags.add_to_contact` based on what you learn

## Fields to Enrich

| Field | Sources |
|-------|---------|
| Title / Role | LinkedIn headline, company about page |
| Organization | LinkedIn, company website, news articles |
| Location | LinkedIn profile, company HQ |
| Background | LinkedIn summary, personal blog, conference talks |
| Recent activity | News mentions, blog posts, social media |
| Mutual connections | LinkedIn shared connections, event co-attendance |

## Example

**Starting contact:**
```
Name: Jamie Rodriguez
Email: jamie@acmelabs.io
(everything else blank)
```

**After enrichment:**
```
1. get_contact(id) → sparse record
2. Web search "Jamie Rodriguez acmelabs.io"
3. contacts.update(id, {
     title: "VP of Engineering",
     organization: "Acme Labs",
     location: "San Francisco, CA"
   })
4. notes.append(id, "## Research (2026-04-05)\n- VP Eng at Acme Labs (Series B, 50 employees)\n- Previously at Stripe (2019-2024)\n- Speaks at PyCon regularly\n- Interested in developer tools and open source")
5. tags.add_to_contact(id, ["engineering", "startup", "developer-tools"])
```

## Checklist

```
Enrichment:
- [ ] Existing data reviewed before overwriting
- [ ] Only publicly available information used
- [ ] Research date noted in appended notes
- [ ] Sources are credible (not outdated profiles)
- [ ] Tags updated to reflect new information
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious: Building Tools That Think With You](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
