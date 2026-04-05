---
name: evergreen-news-alerts
description: Monitors news and web mentions for Evergreen CRM contacts and their companies — funding rounds, product launches, press coverage, job changes. Use to surface timely conversation starters and stay informed about your network's activities.
---

# News & Social Signal Monitor

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Weekly review: "Any news about my key contacts or their companies?"
- Before reaching out to someone: "What's been happening at their company?"
- When looking for natural conversation hooks for re-engagement
- Monitoring a specific company or industry segment

## How It Works

1. Pull target contacts with `search_contacts` (filter by tags like "investor", "founder", or specific orgs)
2. Get full details with `get_contact` for name, organization, and context
3. Web search for recent news about the contact and their company
4. For notable findings, append to notes with `notes.append`
5. Create outreach actions with `actions.create` for timely conversation starters
6. Log any outreach as interactions with `interactions.log`

## What to Monitor

| Signal | Search Strategy | Value |
|--------|----------------|-------|
| Funding rounds | "[Company] funding" or "[Company] raises" | High — great congratulations hook |
| Product launches | "[Company] launches" or "[Company] announces" | Medium — shows you follow their work |
| Press coverage | "[Person name] [Company]" | Medium — reference in conversation |
| Job changes | "[Person name] joins" or LinkedIn activity | High — update record + congratulate |
| Speaking / Writing | "[Person name] talk" or "[Person name] blog" | Medium — shows genuine interest |
| Awards / Recognition | "[Person name] award" or "[Company] recognized" | High — easy congratulations |
| Company milestones | "[Company] customers" or "[Company] growth" | Medium — conversation starter |

## Example

**Monitoring your top 10 contacts:**

```markdown
## News Digest — Week of April 7, 2026

### Notable Finds

1. **DataFlow** (Marcus Webb's company)
   "DataFlow raises $12M Series A led by Sequoia"
   → notes.append(marcus_id, "Apr 2026: DataFlow raised $12M Series A (Sequoia)")
   → actions.create({ title: "Congratulate Marcus on Series A", priority: "high" })

2. **Sarah Chen** (Meridian Health)
   Published a blog post: "How We Rebuilt Our Data Pipeline in 6 Months"
   → notes.append(sarah_id, "Apr 2026: Published blog on data pipeline rebuild")
   → Good reference for your next conversation

3. **Jamie Rodriguez** (Acme Labs)
   LinkedIn shows new title: "VP of Engineering" (was Senior Engineer)
   → contacts.update(jamie_id, { title: "VP of Engineering" })
   → actions.create({ title: "Congratulate Jamie on VP promotion", priority: "medium" })

### No News Found
- Tom Bradley, Lisa Park, David Kim, Priya Sharma (4 contacts)
  Last checked: Apr 7, 2026

### Suggested Outreach This Week
1. Marcus Webb — Congratulate on funding (time-sensitive)
2. Jamie Rodriguez — Congratulate on promotion
3. Sarah Chen — Reference her blog post in your next email
```

## Monitoring Frequency

| Contact Tier | Frequency | Rationale |
|-------------|-----------|-----------|
| Close collaborators (top 10) | Weekly | Stay current on people who matter most |
| Active network (top 50) | Bi-weekly | Catch major news |
| Extended network | Monthly | Spot big events only |
| Pre-meeting | On demand | Always check before a meeting |

## Checklist

```
News Monitoring:
- [ ] Target contacts selected (by tag, tier, or specific list)
- [ ] Web search performed for each contact/company
- [ ] Notable findings recorded in contact notes with date
- [ ] Contact records updated if profile changed (new title, company)
- [ ] Outreach actions created for timely hooks
- [ ] "Last checked" date noted to avoid duplicate searches
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
