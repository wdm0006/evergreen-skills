---
name: evergreen-relationship-health
description: Scores and surfaces relationship health across your Evergreen CRM contacts — identifies thriving relationships, ones at risk, and dormant connections needing attention. Use when you want a high-level view of your network health or need to prioritize relationship investment.
---

# Relationship Health Check

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- Monthly network review: "How healthy is my network?"
- When deciding where to invest relationship energy
- Before planning outreach for the week
- When feeling like you're losing touch with your network

## How It Works

1. Pull all contacts and recent interactions with `search_contacts`
2. For high-value contacts, get full details with `get_contact` and `interactions.list`
3. Analyze the global network with `get_global_network` for relationship patterns
4. Score each relationship on recency, frequency, and depth
5. Categorize into health tiers and surface actionable insights

## Health Scoring

| Factor | Signal | Weight |
|--------|--------|--------|
| Recency | Days since last interaction | High |
| Frequency | Interactions per month over last 6 months | Medium |
| Depth | Mix of interaction types (not just email) | Medium |
| Reciprocity | Balance of inbound vs outbound | Low |
| Momentum | Increasing or decreasing frequency | Medium |

## Health Tiers

| Tier | Criteria | Action |
|------|----------|--------|
| Thriving | Interacted in last 14 days, regular cadence | Maintain current pace |
| Healthy | Interacted in last 30 days, steady cadence | No action needed |
| Cooling | 30-60 days since last interaction | Consider a check-in |
| At Risk | 60-90 days, declining frequency | Prioritize outreach this week |
| Dormant | 90+ days since last interaction | Re-engagement needed |

## Example Output

```markdown
## Network Health Report — April 2026

### Summary
- **Total active contacts:** 127
- **Thriving:** 12 (9%)
- **Healthy:** 34 (27%)
- **Cooling:** 28 (22%)
- **At Risk:** 18 (14%)
- **Dormant:** 35 (28%)

### Needs Attention (Top 5 At-Risk)
1. **Marcus Webb** (Founder, DataFlow) — 62 days since last contact.
   Was very active (4 interactions in Q1). Partnership proposal pending.
2. **Lisa Park** (VP Product, Meridian) — 58 days. Procurement
   discussion stalled. You owe security questionnaire.
3. **David Kim** (DataTech) — 55 days. Key introducer in your network
   (introduced 4 contacts). Worth maintaining.
4. **Rachel Torres** (Angel investor) — 71 days. Offered to help with
   hiring, never followed up.
5. **Tom Bradley** (Advisor) — 68 days. Quarterly coffee overdue.

### Network Insights
- Your most active cluster: Atlanta AI community (23 contacts, avg 18 days between interactions)
- Weakest cluster: College network (15 contacts, avg 140 days between interactions)
- Top introducer going dormant: David Kim — maintain this relationship
- You have 8 contacts with pending actions older than 2 weeks
```

## Checklist

```
Relationship Health:
- [ ] All contacts scored on recency, frequency, depth
- [ ] Health tiers assigned
- [ ] At-risk relationships prioritized by value
- [ ] Specific action suggested for each at-risk contact
- [ ] Network-level insights provided (clusters, trends)
- [ ] Pending stale actions flagged
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
