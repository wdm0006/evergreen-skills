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

1. Call `get_relationship_strength_statistics` for the network summary, including the average score and contact count by grade
2. Call `get_relationship_strengths` with the Weak grade filter and `limit: 100`, then repeat with the Dormant grade filter, to build the ranked needs-attention list without scanning every contact
3. For the handful of contacts included in the report, use `get_contact` and `get_contact_interactions` to explain why the relationship needs attention and suggest a specific action
4. Analyze the global network with `get_global_network` for cluster and relationship patterns
5. For a single-contact health check, call `get_relationship_strength` and supplement it with contact details and interactions as needed

## Health Scoring

Evergreen calculates relationship strength scores from 0–100 based on recency,
frequency, depth, and variety of interactions. Use the score returned by the
relationship-strength tools rather than calculating or weighting these factors
in the skill.

## Health Grades

| Grade | Score | Action |
|-------|-------|--------|
| Strong | 80–100 | Maintain current pace |
| Good | 60–79 | No action needed |
| Moderate | 40–59 | Consider a check-in |
| Weak | 20–39 | Prioritize outreach this week |
| Dormant | 0–19 | Re-engagement needed |

## Example Output

```markdown
## Network Health Report — April 2026

### Summary
- **Total active contacts:** 127
- **Strong:** 12 (9%)
- **Good:** 34 (27%)
- **Moderate:** 28 (22%)
- **Weak:** 18 (14%)
- **Dormant:** 35 (28%)

### Needs Attention (Top 5 Weak or Dormant)
1. **Marcus Webb** (Founder, DataFlow) — Weak, score 38.
   Was very active (4 interactions in Q1). Partnership proposal pending.
2. **Lisa Park** (VP Product, Meridian) — Weak, score 35. Procurement
   discussion stalled. You owe security questionnaire.
3. **David Kim** (DataTech) — Weak, score 32. Key introducer in your network
   (introduced 4 contacts). Worth maintaining.
4. **Rachel Torres** (Angel investor) — Dormant, score 18. Offered to help with
   hiring, never followed up.
5. **Tom Bradley** (Advisor) — Dormant, score 15. Quarterly coffee overdue.

### Network Insights
- Your most active cluster: Atlanta AI community (23 contacts, avg 18 days between interactions)
- Weakest cluster: College network (15 contacts, avg 140 days between interactions)
- Top introducer going dormant: David Kim — maintain this relationship
- You have 8 contacts with pending actions older than 2 weeks
```

## Checklist

```
Relationship Health:
- [ ] Relationship strength statistics summarized
- [ ] Strong, Good, Moderate, Weak, and Dormant grades reported
- [ ] Weak and Dormant relationships prioritized by value
- [ ] Specific action suggested for each Weak or Dormant contact
- [ ] Network-level insights provided (clusters, trends)
- [ ] Pending stale actions flagged
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Vibe Coding a Personal CRM](https://mcginniscommawill.com/posts/2025-09-05-vibe-coding-personal-crm/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
