---
title: ComputerRL
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, orchestration]
sources: [raw/papers/arxiv-lai-2025-computerrl.md]
---

# ComputerRL

## Overview
ComputerRL is a framework for scaling online reinforcement learning for computer-use agents across distributed virtual desktops. It combines API and GUI interaction and focuses on training stability at scale rather than only evaluation.

## Why it matters
It matters because a harness does not really have a gym until it can run many environments in parallel without turning infrastructure into tragic performance art.

## Distinctive trait
Its distinctive trait is infrastructure seriousness: thousands of parallel desktops, mixed API/GUI interaction, and training strategies to survive long online runs.

## Relationships
Read ComputerRL with [[osworld]], [[windows-agent-arena]], [[appworld]], and the training-focused section of [[rl-gyms-and-executable-environments-for-ai-harnesses]].
