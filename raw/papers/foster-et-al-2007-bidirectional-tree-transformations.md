---
title: Combinators for bidirectional tree transformations
author: J. Nathan Foster, Michael B. Greenwald, Jonathan T. Moore, Benjamin C. Pierce, Alan Schmitt
url: https://doi.org/10.1145/1232420.1232424
date: 2007
ingested: 2026-04-09
---

# Combinators for bidirectional tree transformations

**Source:** [DOI](https://doi.org/10.1145/1232420.1232424)
**Authors:** J. Nathan Foster, Michael B. Greenwald, Jonathan T. Moore, Benjamin C. Pierce, Alan Schmitt
**Date:** 2007

## Core idea
Bidirectional transformations, or lenses, provide well-behaved mappings between source structures and editable views, including rules for propagating view edits back to the source.

## Harness takeaway
Each major studio projection should be thought of as a typed lens over the canonical control-plane state, not as a disconnected UI replica.
