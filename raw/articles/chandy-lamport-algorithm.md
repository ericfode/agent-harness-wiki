---
title: Chandy–Lamport algorithm
author: Wikipedia
url: https://en.wikipedia.org/wiki/Chandy%E2%80%93Lamport_algorithm
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Chandy–Lamport algorithm

**Source:** [Wikipedia](https://en.wikipedia.org/wiki/Chandy%E2%80%93Lamport_algorithm)
**Topic:** Recording a consistent global state in an asynchronous distributed system.

## Core idea
The Chandy–Lamport algorithm captures a consistent global state of an asynchronous system without stopping the world.

## Key claims
- A useful snapshot is a consistent cut, not just a pile of local states captured at arbitrary times.
- Replay, audit, and debugging get much cleaner when the system can name such cuts explicitly.
- Snapshotting is a semantic operation over a distributed run, not merely a storage backup trick.

## Harness takeaway
The studio should have first-class consistent cuts for replay, review bundles, incident reports, and approval checkpoints.
