---
title: Sybilproof reputation mechanisms
author: Alice Cheng, Eric Friedman
url: https://doi.org/10.1145/1080192.1080202
date: 2005
ingested: 2026-04-11
---

# Sybilproof reputation mechanisms

**Source:** [ACM DOI](https://doi.org/10.1145/1080192.1080202)
**Authors:** Alice Cheng, Eric Friedman
**Date:** 2005

## Abstract / key passage
Cheng and Friedman formalize sybilproofness for reputation systems on static graphs and show that there is no symmetric sybilproof reputation function. For nonsymmetric reputations, they describe a general path- and flow-based formulation and give conditions for sybilproofness.

## Harness takeaway
This is a clean formal argument against global reputation for multiplayer harnesses. If identities are cheap, a symmetric score can be inflated by spawning linked sybils. Any trust signal that survives should therefore stay directional, observer-relative, and subordinate to provenance, commitments, credentials, and local policy evaluation rather than pretending to be a universal measure of goodness.
