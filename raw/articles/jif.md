---
title: Jif
author: Cornell University
url: https://www.cs.cornell.edu/jif/
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Jif

**Source:** [Cornell Jif](https://www.cs.cornell.edu/jif/)
**Topic:** Security-typed programming with information-flow and access-control labels.

## Core idea
Jif extends Java with labels that describe how information may flow and who may affect it, with enforcement at compile time and run time.

## Key claims
- Confidentiality and integrity can travel with the data as labels.
- Information-flow control is more precise than coarse role-based access checks.
- End-to-end policy enforcement becomes part of the program semantics rather than an afterthought.

## Harness takeaway
A harness control plane could label artifacts, traces, prompts, and approvals by secrecy and integrity, then use those labels to constrain who may inspect, reuse, or act on them.
