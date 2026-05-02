---
title: COBALT-TLA
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [formal-methods]
sources: [raw/papers/arxiv-2604.12172-cobalt-tla.md]
---

# COBALT-TLA

## Overview
COBALT-TLA is a neuro-symbolic verification architecture that integrates an LLM with the TLA+ TLC model checker in a tight loop.

## Architecture Highlights
It uses the verifier as a hallucination-free oracle. The LLM generates TLA+ specifications and properties, the TLC model checker evaluates them, and the trace feedback is fed back to the LLM to refine the design or find exploits.

## Significance
It provides a strong architectural precedent for the verifier as a first-class oracle rather than a post-hoc linter, and has discovered real exploits in practice.

## Relationships
- Foundational for [[agent-facing-verifier-environment-architecture]]
- Exemplifies the [[formal-cognition-loop]]
- Contributes to [[evaluation-and-review-loops]]
- Conceptually related to [[formal-methods-for-agent-harnesses]]
