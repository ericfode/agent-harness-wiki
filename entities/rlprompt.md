---
title: RLPrompt
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-deng-2022-rlprompt.md]
---

# RLPrompt

## Overview
RLPrompt is a discrete prompt-optimization method that trains a lightweight policy network to produce prompt tokens for a frozen language model. It is the clean canonical paper for reinforcement learning over prompt text rather than over model weights.

## Why it matters
It matters because it makes the basic move explicit: the prompt is a learnable external artifact. For harness design, that is a decisive conceptual shift even when the optimized object is still only one prompt.

## Distinctive trait
Its distinctive trait is that the learned prompts are often ungrammatical but still effective and somewhat transferable across models. The optimizer is clearly doing something, but not necessarily something a human would enjoy reading.

## Relationships
Read RLPrompt with [[tempera]], [[autodspy]], [[dspy]], [[gepa]], [[prompt-optimization-and-dspy-follow-ups]], and [[prompt-optimization-timeline-and-harness-lessons]]. It is also a useful contrast class for [[reflexion]], where the learned artifact is memory rather than a single prompt.