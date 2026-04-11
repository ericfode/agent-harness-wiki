---
title: DyFlow
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [orchestration, error-recovery, work-management]
sources: [raw/papers/arxiv-wang-2025-dyflow.md]
---

# DyFlow

## Overview
DyFlow dynamically constructs and revises workflows from intermediate feedback during execution instead of fixing one plan upfront. It treats workflow repair as part of runtime behavior rather than a separate offline ceremony.

## Why it matters
It matters because many tasks do not reveal the right procedure in advance. Dynamic revision is often more realistic than pretending the first graph will be perfect.

## Distinctive trait
Its distinctive trait is in-flight workflow revision: intermediate evidence can trigger restructuring before the run is over.

## Relationships
Read DyFlow with [[self-evolving-workflows]], [[error-recovery]], and [[judgeflow|JudgeFlow]]. It is a useful contrast to the more static search style of [[aflow|AFlow]] and [[mermaidflow|MermaidFlow]].
