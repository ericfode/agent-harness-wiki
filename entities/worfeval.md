---
title: WorfEval
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [benchmark, work-management, orchestration]
sources: [raw/papers/arxiv-qiao-2024-benchmarking-agentic-workflow-generation.md]
---

# WorfEval

## Overview
WorfEval is the evaluation layer paired with WorfBench, focusing on graph structure, subsequence alignment, and downstream usefulness for generated workflows. It is the scoring apparatus that makes the benchmark more than polite scenery.

## Why it matters
It matters because two workflows can differ superficially yet preserve the same useful substructure. WorfEval tries to score that middle ground instead of reducing everything to exact-match puritanism.

## Distinctive trait
Its distinctive trait is multi-view workflow scoring: structure, partial alignment, and practical downstream usefulness all count.

## Relationships
Read WorfEval with [[worfbench|WorfBench]], [[robustflow|RobustFlow]], and [[evaluation-and-review-loops]]. It also complements procedure-oriented evaluation in [[sopbench|SOPBench]].
