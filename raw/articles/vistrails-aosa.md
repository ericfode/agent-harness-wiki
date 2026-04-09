---
title: VisTrails
author: Juliana Freire, David Koop, Emanuele Santos, Carlos Scheidegger, Claudio Silva, Huy T. Vo
url: https://aosabook.org/en/v1/vistrails.html
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# VisTrails

**Source:** [The Architecture of Open Source Applications](https://aosabook.org/en/v1/vistrails.html)
**Topic:** Workflow systems for exploration, visualization, and provenance.

## Core idea
VisTrails supports data exploration and visualization through explicit workflows. The broader project is also known for treating the evolution of workflows as something worth recording, not just the current snapshot.

## Key claims
- Computational processes should be represented as explicit workflow structures.
- Exploration benefits from preserving how a result was produced, not merely what the latest result is.
- Versioning and comparison are part of the exploratory interface, not post-hoc bookkeeping.

## Harness takeaway
A programming harness should preserve derivation paths: prompts, edits, commands, traces, approvals, and outputs should be inspectable as lineage, not only as a final transcript.
