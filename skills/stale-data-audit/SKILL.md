---
name: evergreen-stale-data-audit
description: Audits Evergreen CRM for stale or incomplete contact data — outdated titles, missing fields, potential duplicates, and contacts that may have changed jobs. Use for periodic database hygiene, before a big outreach push, or when data quality feels off.
---

# Stale Data Audit

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Quarterly database cleanup
- Before a bulk outreach or newsletter send
- When you notice contact details are outdated
- After importing contacts from another source

## How It Works

1. Search all contacts with `search_contacts` to get the full database
2. For each contact, check for data quality issues using `get_contact`
3. Flag incomplete records, stale information, and potential problems
4. Prioritize fixes by relationship importance
5. Generate a cleanup task list with suggested fixes

## Data Quality Checks

| Check | What to Look For | Priority |
|-------|-----------------|----------|
| Missing email | Contact has no email address | High |
| Missing organization | No company/org listed | Medium |
| Stale title | Title unchanged for 12+ months on active contact | Medium |
| No interactions | Contact exists but zero interactions logged | Low |
| No tags | Contact has no tags for filtering | Low |
| Empty notes | No context about the relationship | Medium |
| No location | Missing city/region | Low |
| Orphaned contacts | No relationships, no interactions, no tags | High |

## Example Output

```markdown
## Data Audit Report — April 2026

### Summary
- **Total contacts:** 187
- **Complete records:** 112 (60%)
- **Needs attention:** 75 (40%)

### Critical Issues (12)
1. **Sarah Chen** — Email missing (have everything else)
2. **Marcus Webb** — Title still says "Stealth Mode" (company launched 6 months ago)
3. **[5 contacts]** — No interactions ever logged (orphaned?)
4. **[5 contacts]** — Duplicate suspected (same org + similar name)

### Missing Fields Summary
| Field | Missing Count | % of Contacts |
|-------|--------------|---------------|
| Email | 23 | 12% |
| Organization | 18 | 10% |
| Title | 31 | 17% |
| Location | 45 | 24% |
| Tags | 38 | 20% |

### Likely Job Changes
Contacts where title was set 12+ months ago and they're at a startup
(high likelihood of role change):
1. **Jamie Rodriguez** — "Senior Engineer at Acme Labs" (set 14 months ago)
2. **Priya Sharma** — "ML Engineer at NewCo" (set 13 months ago)

### Suggested Actions
1. Enrich the 12 critical contacts (use contact-enrichment skill)
2. Review 5 suspected duplicates for merging
3. Archive or delete 5 orphaned contacts with no activity
4. Batch-update missing tags for 38 untagged contacts
```

## Checklist

```
Data Audit:
- [ ] All contacts scanned for completeness
- [ ] Critical issues (missing email, duplicates) flagged first
- [ ] Missing fields summarized by type
- [ ] Potentially stale titles identified
- [ ] Orphaned contacts flagged for review
- [ ] Cleanup actions prioritized by impact
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
