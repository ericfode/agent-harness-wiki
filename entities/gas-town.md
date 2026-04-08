---
title: Gas Town
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [gas-town, orchestration, work-management]
sources: [raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-future-of-coding-agents.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/yegge-birthday-blog.md]
---

# Gas Town

## Overview
Gas Town is Steve Yegge's orchestrator for running swarms of coding agents. The essential move is to stop treating the coding agent as a heroic individual and instead treat it as labor inside a factory: mayors, polecats, witness roles, merge queues, and a ledger of work items. If this sounds industrial, that is because it is trying to be.

## Operating model
Gas Town distinguishes human oversight from worker roles. The Mayor is the chief-of-staff interface, polecats do project work, the Refinery manages merge flow, and the Witness or Deacon family watches for stuck or unhealthy states. This makes Gas Town more structurally explicit than most chat-first harnesses. See [[work-management-primitives]] and [[harness-architecture-comparison]].

## MEOW stack
The central abstraction is the MEOW stack: beads, epics, molecules, protomolecules, formulas, and wisps. These are not merely task names; they are the durable substrate that lets work survive crashes, handoffs, and sheer agent volatility. The system is tightly coupled to [[memory-persistence]] because the work graph doubles as a design-intent record.

## Strengths
- Explicit work primitives rather than vague task prose.
- Strong orchestration vocabulary for large parallel swarms.
- A clear theory that throughput comes from factories, not super-workers.
- Direct line of development toward [[gas-city]].

## Weaknesses and limits
The Yegge material is candid about cost, instability, and velocity-induced chaos. Gas Town optimizes for throughput and experimentation more than for gentle operator ergonomics. It is closer to a machine shop than a valet.

## Relationships
Gas Town is the precursor to [[gas-city]], the main source for [[work-management-primitives]], and a counterpoint to [[codex-cli]] and [[claude-code]] in [[harness-quality-comparison]].
