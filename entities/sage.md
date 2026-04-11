---
title: SAGE
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, work-management, orchestration]
sources: [raw/papers/arxiv-wang-2025-self-improving-agent-skill-library.md]
---

# SAGE

## Overview
SAGE is a reinforcement-learning framework in which agents accumulate and reuse skills across sequential rollouts. It makes skill acquisition part of an ongoing training loop rather than an occasional manual packaging step.

## Why it matters
It matters because it pushes skill-library self-improvement past prompt tinkering and into a persistent learning regime. The promotion of new skills becomes part of the loop itself.

## Distinctive trait
Its distinctive trait is cross-rollout skill accumulation: learned capabilities persist and shape future episodes instead of being relearned from scratch each time.

## Relationships
Read SAGE with [[skillx|SkillX]], [[memento-skills]], and [[self-evolving-workflows]]. It also provides a useful RL-flavored contrast to the more artifact-driven library systems such as [[skillfoundry|SkillFoundry]].
