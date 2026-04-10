---
title: AppWorld
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, work-management]
sources: [raw/papers/arxiv-trivedi-2024-appworld.md]
---

# AppWorld

## Overview
AppWorld is a controllable multi-app world for interactive coding agents, with hundreds of APIs, realistic users, and state-based unit-test evaluation. It is designed for tasks that require rich code generation and multi-step interaction rather than a trivial sequence of tool calls.

## Why it matters
It matters because it is one of the best current bridges between harness evaluation and genuine RL-style training. The world is rich enough to matter and structured enough to grade.

## Distinctive trait
Its distinctive trait is state-based evaluation with collateral-damage checks: different valid solutions can pass, but careless world mutations still fail.

## Relationships
Read AppWorld with [[rl-gyms-and-executable-environments-for-ai-harnesses]], [[evaluation-and-review-loops]], [[swe-gym]], and compare it with [[tau-bench]] plus [[computer-rl]].
