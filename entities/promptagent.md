---
title: PromptAgent
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/arxiv-wang-2023-promptagent.md]
---

# PromptAgent

## Overview
PromptAgent is a prompt optimizer that casts prompt improvement as a strategic planning problem. It reflects on errors, explores prompt states with a Monte-Carlo-tree-search-style procedure, and searches for high-reward edit paths instead of only proposing flat prompt candidates.

## Why it matters
It matters because it is the clearest planning-based member of the prompt-optimizer cluster. For harnesses that already produce structured failure evidence, it points toward optimizer loops that use richer traces than scalar scores alone.

## Distinctive trait
Its distinctive trait is planning over prompt states and edit trajectories rather than independent candidate generation or population evolution.

## Relationships
Read PromptAgent with [[opro]], [[promptbreeder]], [[gepa]], and [[prompt-optimizer-regimes-for-harnesses]]. It also sits naturally beside [[textgrad]], where the system similarly benefits from richer error information than plain reward.