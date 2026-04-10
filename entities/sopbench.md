---
title: SOPBench
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, work-management]
sources: [raw/papers/arxiv-li-2025-sopbench.md]
---

# SOPBench

## Overview
SOPBench is an executable evaluation framework for language agents that must follow standard operating procedures, policies, and constraints while taking actions and making tool calls. It provides executable environments, SOP graphs, and rule-based verifiers rather than relying on post-hoc prose judgments.

## Why it matters
It matters because many serious harness failures are failures of procedure following, not merely failures of raw competence. SOPBench makes that procedural layer measurable.

## Distinctive trait
Its distinctive trait is oracle-style rule-based verification over procedure graphs. That gives it a cleaner promotion signal than vague “did the agent seem responsible?” grading.

## Relationships
Read SOPBench with [[tau-bench]], [[appworld]], [[evaluation-and-review-loops]], and the broader map in [[rl-gyms-and-executable-environments-for-ai-harnesses]].
