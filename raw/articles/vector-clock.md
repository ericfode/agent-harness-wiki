---
title: Vector clock
author: Wikipedia
url: https://en.wikipedia.org/wiki/Vector_clock
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Vector clock

**Source:** [Wikipedia](https://en.wikipedia.org/wiki/Vector_clock)
**Topic:** Capturing causality and concurrency in distributed systems.

## Core idea
Vector clocks refine simple logical clocks by distinguishing causal order from genuine concurrency.

## Key claims
- Not all "later" events are causally later.
- A useful system should distinguish happened-before from concurrent updates.
- Merge and replay logic improve when concurrency is represented explicitly rather than flattened into timestamp order.

## Harness takeaway
A harness should carry causal frontiers on work objects and projections so it can tell independent branches from true conflicts.
