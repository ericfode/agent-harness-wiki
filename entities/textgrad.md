---
title: TextGrad
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-yuksekgonul-2024-textgrad.md]
---

# TextGrad

## Overview
TextGrad is an optimization framework for compound AI systems that propagates textual feedback backward through a computation graph. It treats prompts, code, and other text-defined components as variables that can be improved through natural-language “gradients.”

## Why it matters
It matters because long-lived harnesses are compound systems rather than single prompts. TextGrad is one of the clearest attempts to give those systems a unified optimizer substrate instead of treating every prompt edit as an isolated craft exercise.

## Distinctive trait
Its distinctive trait is PyTorch-like textual autograd: optimization happens through language-model-generated feedback that plays the role of gradients over graph nodes.

## Relationships
Read TextGrad with [[dspy]], [[sammo]], [[prompt-program-representation-and-optimizer-open-questions]], and [[prompt-optimization-and-dspy-follow-ups]]. It is also a useful counterpoint to [[rlprompt]], where the search object is a single discrete prompt rather than a compound system.