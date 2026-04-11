---
title: Probabilistic Plan Recognition Using Off-the-Shelf Classical Planners
author: Miguel Ramírez, Hector Geffner
url: https://doi.org/10.1609/aaai.v24i1.7745
date: 2010
ingested: 2026-04-10
---

# Probabilistic Plan Recognition Using Off-the-Shelf Classical Planners

**Source:** [DOI](https://doi.org/10.1609/aaai.v24i1.7745)
**Authors:** Miguel Ramírez, Hector Geffner
**Date:** 2010

## Core idea
Observed actions should update a probability distribution over candidate goals rather than collapse immediately into one asserted intention.

## Key claims
- Goal inference is model-relative and evidence-relative.
- Multiple candidate goals should remain live when evidence is ambiguous.
- Confidence should come from a clear inference method rather than from impressionistic certainty.

## Harness takeaway
A multiplayer harness should store inferred goals as competing, revisionable hypotheses with evidence links and explicit confidence semantics, not as durable facts about a person.
