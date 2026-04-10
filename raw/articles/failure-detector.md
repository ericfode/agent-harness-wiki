---
title: Failure detector
author: Wikipedia
url: https://en.wikipedia.org/wiki/Failure_detector
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Failure detector

**Source:** [Wikipedia](https://en.wikipedia.org/wiki/Failure_detector)
**Topic:** Suspicion and crash detection as graded signals rather than perfect truth.

## Core idea
A failure detector is a subsystem that reports suspected failures, with different formal strengths of completeness and accuracy rather than magical certainty.

## Key claims
- Distributed systems rarely know failure perfectly.
- Suspicion quality matters because different guarantees require different detector strengths.
- Timeout is not the same thing as fact.

## Harness takeaway
The studio should represent agent and service status as suspected, unreachable, timed out, or confirmed failed, instead of collapsing all delay into death.
