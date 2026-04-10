---
title: τ-bench
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, work-management]
sources: [raw/papers/arxiv-yao-2024-tau-bench.md]
---

# τ-bench

## Overview
τ-bench evaluates tool-agent-user interaction in dynamic real-world domains with policy rules, domain-specific APIs, and simulated user conversation. It is one of the cleanest tool-centric environments for studying whether agents behave consistently and follow rules.

## Why it matters
It matters because many harness failures are not navigation failures but policy and interaction failures. τ-bench puts that problem in the foreground.

## Distinctive trait
Its distinctive trait is end-state grading over multi-turn tool use plus domain rules, rather than just checking whether the agent touched the right API in the right order once.

## Relationships
Read τ-bench with [[appworld]], [[proxy-state-based-evaluation]], [[sopbench]] if mentioned through related queries, and [[rl-gyms-and-executable-environments-for-ai-harnesses]].
