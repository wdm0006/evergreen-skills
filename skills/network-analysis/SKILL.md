---
name: evergreen-network-analysis
description: Analyzes your Evergreen CRM contact network to surface clusters, bridge contacts, top introducers, and introduction chains. Use when you want to understand your network structure, find connection opportunities, or identify key people in your network.
---

# Network Map & Cluster Analysis

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- "Who are the most connected people in my network?"
- "How did I end up knowing [person]?" — trace the introduction chain
- "What clusters exist in my network?"
- "Who bridges different parts of my network?"
- Planning who to bring to an event or dinner

## How It Works

1. Pull the full network graph with `get_global_network`
2. Identify top introducers with `get_top_introducers`
3. Trace specific introduction chains with `get_introduction_chain`
4. For key contacts, get detailed networks with `get_contact_network`
5. Analyze for clusters, bridges, and structural insights

## Analysis Outputs

### Top Introducers

People who've connected you to the most contacts. These are high-value relationships to maintain.

```markdown
## Your Top Introducers
1. **David Kim** — Introduced you to 8 contacts (Sarah Chen, Marcus Webb, ...)
2. **Alex Torres** — Introduced you to 5 contacts
3. **Jamie Rodriguez** — Introduced you to 3 contacts
```

### Network Clusters

Groups of contacts that are densely connected to each other.

```markdown
## Network Clusters
### Atlanta AI Community (23 contacts)
- Hub: David Kim (connected to 15 others in this cluster)
- Active: 18 contacts interacted with in last 60 days
- Key members: Sarah Chen, Marcus Webb, Lisa Park, Priya Sharma

### Startup Founders (14 contacts)
- Hub: Alex Torres (connected to 9 others)
- Active: 8 contacts interacted with in last 60 days
- Key members: Marcus Webb, Jamie Rodriguez, Tom Bradley

### College Network (15 contacts)
- Hub: Rachel Torres (connected to 6 others)
- Mostly dormant: only 3 contacted in last 90 days
```

### Bridge Contacts

People who connect otherwise separate parts of your network.

```markdown
## Bridge Contacts
- **Marcus Webb** bridges Atlanta AI ↔ Startup Founders
  (only person in both clusters)
- **Rachel Torres** bridges College Network ↔ Angel Investors
```

### Introduction Chains

How you got connected to someone through a series of introductions.

```markdown
## How you know Sarah Chen
You → David Kim (met at PyCon 2024) → Sarah Chen (introduced Sep 2025)

## How you know Raj Patel
You → Sarah Chen → Raj Patel (technical contact at Meridian, Apr 2026)
```

## Use Cases

| Goal | Analysis |
|------|----------|
| Event planning | Find contacts from different clusters for diverse guest list |
| Relationship investment | Prioritize top introducers and bridge contacts |
| Warm path finding | Trace introduction chains to reach a target person |
| Network gaps | Identify clusters with no bridges between them |
| Gratitude | Know who's responsible for your best connections |

## Checklist

```
Network Analysis:
- [ ] Global network data retrieved
- [ ] Top introducers identified and ranked
- [ ] Clusters detected with hub contacts
- [ ] Bridge contacts surfaced
- [ ] Introduction chains traced for key relationships
- [ ] Actionable insights provided
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
