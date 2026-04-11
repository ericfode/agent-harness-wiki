---
title: AutoDSPy
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [dspy, context-engineering, program-synthesis]
sources: [raw/papers/azim-2025-autodspy.md]
---

# AutoDSPy

## Overview
AutoDSPy is a 2025 system that frames DSPy pipeline construction as a reinforcement-learning problem. Its policy selects reasoning modules, signatures, and execution strategies, so the optimized object is a modular LM program rather than only a prompt string.

## Why it matters
It matters because it shifts the RL target from prompt text toward workflow structure. For long-lived harnesses, that is much closer to the real object of control: reusable, inspectable program artifacts that can be evaluated, promoted, and rolled back.

## Distinctive trait
Its distinctive trait is RL over DSPy program structure and configuration rather than RL over discrete prompt tokens.

## Relationships
Read AutoDSPy with [[dspy]], [[dspy-assertions]], [[rlprompt]], and [[prompt-optimizer-regimes-for-harnesses]]. It is a useful bridge between flat prompt optimization and the more general problem of optimizing modular language workflows.