---
title: Stoppable Paxos
author: Dahlia Malkhi, Leslie Lamport, Lidong Zhou
url: https://www.microsoft.com/en-us/research/wp-content/uploads/2008/04/stoppableV9.pdf
date: 2008-04-28
ingested: 2026-04-09
---

# Stoppable Paxos

**Source:** [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2008/04/stoppableV9.pdf)
**Authors:** Dahlia Malkhi, Leslie Lamport, Lidong Zhou
**Date:** 2008-04-28

## Core idea
Stoppable Paxos introduces a stopping command that creates a hard barrier, allowing replicated state machines to reconfigure as a sequence of epochs rather than as blurred partial transitions.

## Harness takeaway
Policy, protocol, or membership epochs in the studio should change via explicit stop-and-reconfigure barriers, not silent drift.
