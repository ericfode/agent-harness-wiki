---
title: Promptbreeder
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-fernando-2023-promptbreeder.md]
---

# Promptbreeder

## Overview
Promptbreeder is a 2023 evolutionary prompt-optimization method that co-evolves task prompts and the mutation prompts used to edit them. The search procedure itself becomes part of the writable artifact set.

## Why it matters
It matters because it pushes prompt optimization beyond “find a good prompt” toward “improve the optimizer that improves the prompt.” For long-lived harnesses, that suggests mutation heuristics, repair prompts, and evaluator-facing instructions may all deserve versioned treatment.

## Distinctive trait
Its distinctive trait is self-referential prompt evolution: mutation prompts are themselves optimized rather than treated as a fixed hidden mechanism.

## Relationships
Read Promptbreeder with [[opro]], [[promptagent]], [[gepa]], and [[prompt-optimizer-regimes-for-harnesses]]. It is also a useful contrast class for [[rlprompt]], where the optimizer is RL over one prompt artifact rather than evolution over prompts and mutators.