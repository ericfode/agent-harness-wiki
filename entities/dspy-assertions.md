---
title: DSPy Assertions
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [dspy, context-engineering, program-synthesis]
sources: [raw/papers/arxiv-singhvi-2023-dspy-assertions.md]
---

# DSPy Assertions

## Overview
DSPy Assertions extends the DSPy programming model with explicit computational constraints that language-model outputs should satisfy. It turns contracts, validation, and self-repair into part of the LM program rather than leaving them implicit in prompt prose.

## Why it matters
It matters because once prompt programs become operational components, they need invariants. DSPy Assertions is one of the clearest early systems that treats schemas, rule compliance, and repair loops as first-class program objects.

## Distinctive trait
Its distinctive trait is that failed assertions can trigger automatic self-refinement, so reliability logic is attached directly to the LM pipeline instead of bolted on as an afterthought.

## Relationships
Read DSPy Assertions with [[dspy]], [[sammo]], [[prompt-program-deployment-open-questions]], and [[sopbench]]. It is also a useful bridge between prompt-program optimization and the harder problem of keeping constraints hard under self-modification.