---
title: GEPA
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-agrawal-2025-gepa.md]
---

# GEPA

## Overview
GEPA is a prompt and program optimizer that learns from full language-rich traces rather than mostly from scalar rewards. It reflects on trajectories in natural language, proposes prompt updates, and keeps complementary candidates on a Pareto frontier.

## Why it matters
It matters because real harnesses already emit the traces GEPA wants to learn from: reasoning steps, tool calls, tool outputs, and evaluator feedback. That makes it a much better fit for compound systems than a story built purely around reward signals.

## Distinctive trait
Its distinctive trait is reflective evolution with Pareto retention: it preserves different candidates that succeed on different cases instead of immediately collapsing search to one global best prompt.

## Relationships
Read GEPA with [[rlprompt]], [[dspy]], [[reflexion]], and [[prompt-optimization-eval-transfer-robustness-open-questions]]. It also sits naturally beside [[self-evolving-workflows]], where improvement happens through durable external artifacts rather than weight updates.