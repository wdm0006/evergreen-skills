---
name: auto-logging-email-interactions
description: Parses recent Gmail activity and logs interaction summaries to Evergreen CRM contacts — without storing full email bodies. Use when you want to sync email activity to your CRM, update interaction history, or keep Evergreen current with your communications. Requires Gmail connected in Claude.
---

# Auto-Log Email Interactions

> Works with [Evergreen](https://heltonlabs.com/evergreen), a local-first personal CRM for macOS. [Get it on the Mac App Store](https://apps.apple.com/us/app/evergreencrm/id6753191506?mt=12).

## When to Use

- End-of-week sync: "Log all my email interactions from this week to Evergreen"
- After a flurry of email activity: "Make sure Evergreen is up to date"
- Before reviewing your follow-up list: ensure interaction dates are current
- Periodic maintenance to keep "Last Interaction" field accurate

## Prerequisites

- Gmail connected in Claude (via Google Workspace MCP or Gmail integration)
- Evergreen MCP server running

## How It Works

The unit of import is one **substantive thread exchange** within the requested period: a thread, or a later run of messages in it, that produced a topic, decision, commitment, or next step. Skip pleasantries ("thanks", "got it"), automated mail, and newsletters. Log one interaction per exchange, not one per message.

1. Fetch sent and received emails from Gmail for the stated period and group them into thread exchanges per correspondent
2. Resolve each address with `search_contacts` (pass the address as the `query`). Exactly one contact must match; zero or several matches make the exchange an **unresolved contact** and nothing is written for it
3. For each resolved contact, read history before any write: `get_contact_interactions({ contactId, limit: 50 })`. 50 is the maximum, and the read has no offset or cursor
4. Draft a concise summary of each exchange (topic, outcome, next steps) and compare it with the contact's existing `email` interactions on date, topic, participants/direction, and substantive outcome. A newer meeting, call, or unrelated email is not a duplicate of an older exchange; only a matching email interaction is
5. Also compare against interactions already logged earlier in this run, so two threads on one topic are not both written
6. Decide each exchange:
   - **Already recorded**: a clear match on topic and outcome. Skip it
   - **New**: no match, and history covers the exchange date. Call `log_interaction` with `type: "email"`, the exchange date, and the summary
   - **Review needed**: several plausible matches, a partial match you cannot call the same exchange, or an exchange older than the oldest record returned when the read came back at 50 (older records may be inaccessible). Do not write it; list it for the user
7. A later reply in an already-recorded thread is a new exchange only if it adds a new decision, commitment, or outcome. Log it dated at that reply and describe only what is new. If it adds nothing, treat the thread as already recorded
8. Report the outcome (see Report)

Logging is best-effort: `log_interaction` has no source-thread ID or idempotency key, so nothing prevents a duplicate if the comparison errs. Do not claim exactly-once import, and do not keep local checkpoint files.

## Report

State the period scanned and history coverage (contacts whose read returned 50 entries, so older records may be inaccessible). Give counts for **logged**, **already recorded**, **unresolved contacts**, and **review needed**. These four must sum to the number of candidate exchanges, and each exchange is listed once under its outcome.

## Privacy-First Approach

| Do | Don't |
|----|-------|
| Log a brief summary of the topic | Store full email bodies in notes |
| Note key decisions or commitments | Copy sensitive content |
| Record the date and direction (sent/received) | Log every single email in a thread |
| Capture next steps | Store attachments or links |

## Example

Synthetic data. Contacts: Sarah Chen, Marcus Webb, Jamie Rodriguez.

**Scan 1, period 2026-03-01 to 2026-04-07 (first scan):**
```
Candidates: 4 exchanges
- sarah@meridianhealth.com: API integration timeline, agreed Q3 target (2026-04-03)
- marcus@dataflow.io: sent partnership proposal (2026-04-01)
- jamie@acmelabs.io: conference panel planning (2026-03-02)
- unknown@newstartup.com: cold outreach, no contact
```
```
1. search_contacts({ query: "sarah@meridianhealth.com" }) → Sarah Chen (one match)
   get_contact_interactions({ contactId: sarah_id, limit: 50 }) → 4 entries, none about the API timeline
   log_interaction({
     contactId: sarah_id,
     type: "email",
     description: "Discussed API integration timeline: agreed on Q3 target, Sarah reviewing docs",
     date: "2026-04-03"
   })

2. search_contacts({ query: "marcus@dataflow.io" }) → Marcus Webb (one match)
   get_contact_interactions({ contactId: marcus_id, limit: 50 }) → newest is a meeting on 2026-04-05;
   no email about a proposal. The newer meeting does not cover the older email.
   log_interaction({
     contactId: marcus_id,
     type: "email",
     description: "Sent partnership proposal for data pipeline collaboration",
     date: "2026-04-01"
   })

3. search_contacts({ query: "jamie@acmelabs.io" }) → Jamie Rodriguez (one match)
   get_contact_interactions({ contactId: jamie_id, limit: 50 }) → 50 entries, oldest 2026-03-20.
   The exchange (2026-03-02) predates the oldest visible record, so a prior log cannot be ruled out.
   Not written. Review needed.

4. unknown@newstartup.com → no match, unresolved contact (flagged for review)
```
Report: logged 2, already recorded 0, unresolved contacts 1, review needed 1 (= 4 candidates). Period 2026-03-01 to 2026-04-07. Jamie's history read hit the 50 limit, so older records may be inaccessible.

**Scan 2, period 2026-03-01 to 2026-04-10 (repeat scan).** Sarah has since replied on 2026-04-08 moving the target to Q4:
```
Candidates: 5 exchanges
- Sarah, 2026-04-03 API timeline: history now has an email "API integration timeline, Q3 target" on 2026-04-03
  → already recorded, skipped
- Sarah, 2026-04-08 reply moving the target to Q4: new outcome not in history
  log_interaction({
    contactId: sarah_id,
    type: "email",
    description: "Replied on API timeline thread: target moved from Q3 to Q4, awaiting revised scope",
    date: "2026-04-08"
  })
- Marcus, 2026-04-01 proposal: email on 2026-04-01 already in history → already recorded, skipped
- Jamie, 2026-03-02: still at the 50 ceiling, older than the oldest visible record → review needed
- unknown@newstartup.com: unresolved contact
```
Report: logged 1, already recorded 2, unresolved contacts 1, review needed 1 (= 5 candidates). Period 2026-03-01 to 2026-04-10. Jamie's history read hit the 50 limit, so older records may be inaccessible.

## Checklist

```
Auto-Log:
- [ ] Time period specified for email scan
- [ ] Emails grouped into substantive thread exchanges per contact
- [ ] Each address resolved to exactly one contact; others reported as unresolved
- [ ] get_contact_interactions({ contactId, limit: 50 }) read before every log_interaction
- [ ] Compared on date, topic, participants/direction, outcome, and against this run's own writes
- [ ] Unrelated newer interactions not treated as duplicates
- [ ] Clear duplicates skipped; ambiguous or ceiling-limited cases listed for review, not written
- [ ] Later replies logged only when they add a new outcome
- [ ] Summaries are concise (no full bodies, attachments, or links)
- [ ] Report gives period, history coverage, and the four counts summing to candidates
```

## Learn More

- [Evergreen — Local-First Personal CRM](https://heltonlabs.com/evergreen)
- [Evergreen Gets Serious](https://mcginniscommawill.com/posts/2025-10-08-evergreen-gets-serious/)
- [Evergreen Gets Even Evergreener](https://mcginniscommawill.com/posts/2026-01-26-evergreen-gets-even-evergreener/)
