---
title: Reliable multicast / Virtual synchrony
author: Wikipedia
url: https://en.wikipedia.org/wiki/Virtual_synchrony
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Reliable multicast / Virtual synchrony

**Source:** [Wikipedia](https://en.wikipedia.org/wiki/Virtual_synchrony)
**Topic:** Group communication with explicit membership views and reliable message delivery semantics.

## Core idea
Virtual synchrony is the idea that a group should observe message delivery and membership changes through a consistent sequence of views rather than through ad hoc partial reconfiguration.

## Key claims
- Group communication becomes more intelligible when delivery and reconfiguration are tied together.
- Membership epochs matter: who was in the group when an event was delivered is part of the semantics.
- Failure and rejoin should appear as structured view changes rather than as mysterious transport noise.

## Harness takeaway
A moldable operations studio should treat operator groups, agent coalitions, watchers, and approval audiences as view-scoped memberships. Failover and takeover become explicit view transitions, not folklore.
