---
title: Viewstamped Replication Revisited
author: Barbara Liskov, James Cowling
url: https://ying-zhang.cn/dist/2012-vr.html
date: 2012
accessed: 2026-04-09
ingested: 2026-04-09
---

# Viewstamped Replication Revisited

**Source:** [Viewstamped Replication Revisited](https://ying-zhang.cn/dist/2012-vr.html)
**Authors:** Barbara Liskov, James Cowling
**Topic:** Replicated-state-machine control planes with explicit views and reconfiguration.

## Core idea
Viewstamped Replication provides a crash-tolerant replicated service through deterministic log replication, view changes, and reconfiguration.

## Key claims
- A replicated service should make reorganization under failures explicit.
- Control operations are best represented as deterministic log entries.
- View changes are a semantic part of the service, not merely an implementation nuisance.

## Harness takeaway
The studio's control plane should treat approvals, cancellations, grants, and routing changes as durable replicated commands rather than mutable dashboard state.
