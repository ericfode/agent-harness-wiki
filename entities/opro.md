---
title: OPRO
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-yang-2023-opro.md]
---

# OPRO

## Overview
OPRO is the optimization-by-prompting method introduced in Large Language Models as Optimizers (2023). It treats a language model as a black-box optimizer that proposes new candidate solutions from a history of previously tried candidates and their scores.

## Why it matters
It matters because it is the cleanest reference for the “LLM as optimizer” branch. For harnesses, it is useful whenever there is a scoreable artifact but little structured critique, making candidate history itself a reusable optimization substrate.

## Distinctive trait
Its distinctive trait is in-context black-box optimization over candidate/value histories rather than tree search, population evolution, or explicit prompt-program structure.

## Relationships
Read OPRO with [[promptbreeder]], [[promptagent]], [[rlprompt]], and [[prompt-optimizer-regimes-for-harnesses]]. It is a natural contrast class for [[textgrad]], where the update signal is richer than scalar score history.