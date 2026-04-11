---
title: Reflexion
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, error-recovery, context-engineering]
sources: [raw/papers/arxiv-shinn-2023-reflexion.md]
---

# Reflexion

## Overview
Reflexion lets language agents learn from trial and error through verbal feedback stored in episodic memory. It is one of the clearest early systems where improvement happens by writing language back into external state rather than by updating model weights.

## Why it matters
It matters because much later work on skills, compiled instructions, and external memory loops quietly starts here. Reflexion made linguistic self-critique into a reusable learning primitive.

## Distinctive trait
Its distinctive trait is verbal reinforcement learning: the agent writes reflective feedback after a run and conditions future attempts on that memory.

## Relationships
Read Reflexion with [[expel|ExpeL]], [[compiled-memory|Compiled Memory]], and [[memory-persistence]]. It is an early ancestor of the broader artifact-centric story in [[self-evolving-workflows]].
