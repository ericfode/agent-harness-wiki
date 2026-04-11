---
title: EvoSkills
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, work-management, benchmark]
sources: [raw/papers/arxiv-zhang-2026-evoskills.md]
---

# EvoSkills

## Overview
EvoSkills studies how agents can generate skills as structured multi-file artifacts while a co-evolving surrogate verifier critiques them. It makes the verifier lane part of the learning surface rather than an afterthought.

## Why it matters
It matters because self-improvement without a verifier quickly becomes eloquent self-deception. EvoSkills is one of the cleanest papers insisting that mutation and evaluation must evolve together.

## Distinctive trait
Its distinctive trait is co-evolutionary verification: the skill generator is paired with a surrogate verifier that supplies actionable feedback even when hidden tests are unavailable.

## Relationships
Read EvoSkills with [[memento-skills]], [[skillfoundry|SkillFoundry]], and [[judgeflow|JudgeFlow]]. It also belongs inside [[self-evolving-workflows]] as a strong model of verifier-guided promotion.
