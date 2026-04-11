---
title: in-toto: Providing farm-to-table guarantees for bits and bytes
author: Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curtmola, Justin Cappos
url: https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias
date: 2019
ingested: 2026-04-10
---

# in-toto: Providing farm-to-table guarantees for bits and bytes

**Source:** [USENIX Security](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias)
**Authors:** Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curtmola, Justin Cappos
**Date:** 2019

## Core idea
Software supply chains become auditable when each step emits signed provenance metadata that can be verified against a declared layout of steps, actors, and thresholds.

## Key claims
- Artifact lineage should be verified step by step rather than trusted in bulk.
- Thresholded attestations are useful for high-trust workflows.
- Provenance should attach to the produced artifact, not disappear into operations folklore.

## Harness takeaway
Artifacts, approvals, and promotions in a multiplayer harness should carry signed provenance bundles. That turns trust into inspectable evidence of who did what under which workflow constraints.
