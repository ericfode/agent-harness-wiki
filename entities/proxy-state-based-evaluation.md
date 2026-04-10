---
title: Proxy State-Based Evaluation
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, work-management]
sources: [raw/papers/arxiv-chuang-2026-proxy-state-based-evaluation.md]
---

# Proxy State-Based Evaluation

## Overview
Proxy State-Based Evaluation is a scalable reward and grading approach for multi-turn tool-calling agents that replaces fully deterministic backends with structured scenarios, proxy-state tracking, and LLM judges. It aims to preserve state-based evaluation without paying the full cost of hand-built deterministic worlds.

## Why it matters
It matters because deterministic backends are expensive, and many harnesses will need something less brittle if they want wide coverage without a small civil-service devoted to simulator upkeep.

## Distinctive trait
Its distinctive trait is verifiable-enough proxy state: structured scenario constraints plus state tracking and judging rather than freeform grader sentiment.

## Relationships
Read Proxy State-Based Evaluation with [[tau-bench]], [[evaluation-and-review-loops]], [[appworld]], and the gym-design discussion in [[rl-gyms-and-executable-environments-for-ai-harnesses]].
