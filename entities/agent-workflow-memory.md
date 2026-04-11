---
title: Agent Workflow Memory
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, work-management, context-engineering]
sources: [raw/papers/arxiv-wang-2024-agent-workflow-memory.md]
---

# Agent Workflow Memory

## Overview
Agent Workflow Memory induces reusable workflows from past trajectories and recalls them later as external procedural memory. The result is a system where routines can accumulate outside the transient prompt.

## Why it matters
It matters because it shifts memory from “more retrieved facts” toward “reusable procedures.” That is a cleaner fit for long-lived harnesses that want to remember how to work, not only what they once saw.

## Distinctive trait
Its distinctive trait is routine induction from trajectories: successful runs are compressed into workflow artifacts that can guide later task execution.

## Relationships
Read Agent Workflow Memory with [[memory-persistence]], [[self-evolving-workflows]], and [[compiled-memory|Compiled Memory]]. It also sits near [[graph-of-skills|Graph of Skills]] once the reusable library grows large.
