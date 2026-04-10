---
title: Optimistic replication
author: Wikipedia
url: https://en.wikipedia.org/wiki/Optimistic_replication
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Optimistic replication

**Source:** [Wikipedia](https://en.wikipedia.org/wiki/Optimistic_replication)
**Topic:** Tentative updates with later reconciliation instead of universal lockstep agreement.

## Core idea
Optimistic replication accepts local updates first and reconciles conflicts later, rather than forcing all replicas into immediate synchronization.

## Key claims
- Disconnected or partitioned work can still make progress.
- Tentative state and merge rules are first-class operational concerns.
- The useful question is often not whether conflict can happen, but how it should be resolved when it does.

## Harness takeaway
Speculative branches, offline work, and delayed merges should be explicit tentative states in a harness rather than embarrassing exceptions to the main model.
