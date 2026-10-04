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

1. Read network statistics, the relationship-type tally, and the top-20 degree ranking with `get_global_network`. Its contact list shows only the top 20 contacts and its edge list only 30 relationships; it takes no arguments, offset, or cursor, so neither list can be paged
2. Read the edges for cluster and bridge analysis with `list_relationships({ limit: 100 })` — 100 is its maximum. Compare the number of distinct relationship IDs returned with the total relationships reported by `get_global_network` before claiming complete coverage
3. Past 100 relationships, sweep in batches using `list_relationships` filters (`relationshipType`, `contactId`), keeping each slice under the cap and deduplicating overlapping results by relationship ID. There is no offset or cursor; a slice returning 100 may be incomplete. State which slices were covered and which remain unresolved, and qualify cluster, hub, bridge, and absence-of-connection claims to the edges actually read
4. Identify top introducers with `get_top_introducers({ limit: 50 })` — its maximum (allowed range 1–50; default 10). If 50 return, label the ranking capped; if it returns "No introductions recorded yet.", report that instead of inventing a ranking
5. Trace specific introduction chains with `get_introduction_chain` and get detailed networks for key contacts with `get_contact_network`
6. Analyze the retrieved edges for clusters, bridges, and structural insights. Count distinct neighboring contacts for hub degrees, and state coverage up front. Network reads do not supply interaction recency, so omit activity-by-date figures from this analysis

## Analysis Outputs

Open the report with a coverage line: distinct edges read versus the global relationship total, filters used, any slices at the 100-edge ceiling, and whether the introducer ranking hit 50. The illustrative sections below share this coverage:

```markdown
_Coverage: 81 of 81 relationships read with list_relationships(limit: 100),
covering all 50 connected contacts; no filtered slices needed. Four introducers
returned with limit: 50, below the cap. Cluster sizes overlap: Marcus belongs to
Atlanta AI and Startup Founders; Jamie belongs to Startup Founders and College Network._
```

### Top Introducers

People who've connected you to the most contacts. These are high-value relationships to maintain.

If no introductions are recorded, output "No introductions recorded yet." This does not mean the relationship graph is empty; skip the ranking and any unsupported introduction chains.

```markdown
## Your Top Introducers
1. **David Kim** — Introduced you to 8 contacts (Sarah Chen, Marcus Webb, ...)
2. **Alex Torres** — Introduced you to 5 contacts
3. **Jamie Rodriguez** — Introduced you to 3 contacts
4. **Sarah Chen** — Introduced you to 1 contact (Raj Patel)
```

### Network Clusters

Groups of contacts that are densely connected to each other.

```markdown
## Network Clusters
### Atlanta AI Community (23 contacts)
- Hub: David Kim (connected to 15 others in this cluster)
- Key members: Sarah Chen, Marcus Webb, Lisa Park, Priya Sharma

### Startup Founders (14 contacts)
- Hub: Alex Torres (connected to 9 others)
- Key members: Marcus Webb, Jamie Rodriguez, Tom Bradley

### College Network (15 contacts)
- Hub: Rachel Torres (connected to 6 others)
- Key members: Jamie Rodriguez, Rachel Torres
```

### Bridge Contacts

People who connect otherwise separate parts of your network.

```markdown
## Bridge Contacts
- **Marcus Webb** bridges Atlanta AI ↔ Startup Founders
  (only person in both clusters)
- **Jamie Rodriguez** bridges Startup Founders ↔ College Network
```

### Introduction Chains

How you got connected to someone through a series of introductions.

```markdown
## How you know Sarah Chen
You → David Kim (met at PyCon 2024) → Sarah Chen (introduced Sep 2025)

## How you know Raj Patel
You → David Kim → Sarah Chen → Raj Patel (technical contact at Meridian, Apr 2026)
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
- [ ] Global network summary retrieved with its top-20 / 30-edge caps understood
- [ ] Edges read with `list_relationships({ limit: 100 })`, filtered batches deduplicated by relationship ID where needed
- [ ] Coverage stated against the global total, with unresolved slices and capped reads named
- [ ] Top introducers read with `limit: 50`, or no recorded introductions reported
- [ ] Clusters detected with hub contacts
- [ ] Bridge contacts surfaced
- [ ] Introduction chains traced for key relationships
- [ ] Actionable insights provided
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
