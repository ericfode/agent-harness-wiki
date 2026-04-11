---
title: AFlow
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [orchestration, work-management, error-recovery]
sources: [raw/papers/arxiv-zhang-2024-aflow.md]
---

# AFlow

## Overview
AFlow is a workflow-search system that represents agent procedures as code and then improves them with Monte Carlo Tree Search plus execution feedback. It treats workflow topology as an explicit search object rather than a fixed scaffold.

## Why it matters
It matters because it turns workflow improvement into a concrete optimization problem over executable artifacts. That is unusually close to what a Codex-native control plane actually needs.

## Distinctive trait
Its distinctive trait is code-level workflow search: candidate graphs are not merely described, but executed, scored, and revised through a tree-search loop.

## Relationships
Read AFlow with [[self-evolving-workflows]], [[harness-engineering]], and [[judgeflow|JudgeFlow]]. It is a natural contrast class for [[autoflow|AutoFlow]] and [[dyflow|DyFlow]].
