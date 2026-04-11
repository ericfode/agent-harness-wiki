---
title: TEMPERA
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-zhang-2022-tempera.md]
---

# TEMPERA

## Overview
TEMPERA is a runtime prompt-adaptation method that trains a reinforcement-learning policy to edit an existing prompt per query at test time. Instead of searching once for a single global prompt, it operates over a structured action space spanning instruction phrases, exemplar selection, and verbalizer choice.

## Why it matters
It matters because it is a clean anchor for the runtime-adaptation branch of prompt optimization. For harness engineering, the important distinction is that it adapts the live prompt instance without updating model weights or necessarily promoting a durable artifact.

## Distinctive trait
Its distinctive trait is interpretable test-time prompt editing over human-seeded prompt components rather than opaque prompt synthesis from scratch.

## Relationships
Read TEMPERA with [[rlprompt]], [[autodspy]], [[prompt-program-deployment-open-questions]], and [[prompt-optimizer-regimes-for-harnesses]]. It is a useful contrast class for [[sammo]] and [[dspy]], where optimization is more compile-time and artifact-oriented.