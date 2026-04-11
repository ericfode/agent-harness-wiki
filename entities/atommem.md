---
title: AtomMem
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, context-engineering, work-management]
sources: [raw/papers/arxiv-huo-2026-atommem.md]
---

# AtomMem

## Overview
AtomMem decomposes memory management into atomic CRUD-like operations and learns a policy over those operations. It turns memory maintenance from invisible plumbing into an explicit control routine.

## Why it matters
It matters because long-lived agents eventually live or die by memory hygiene. AtomMem treats that problem as learnable procedure rather than fixed infrastructure.

## Distinctive trait
Its distinctive trait is atomic memory control: read, write, update, and delete become first-class decisions that can themselves be optimized.

## Relationships
Read AtomMem with [[memory-persistence]], [[self-evolving-workflows]], and [[memskill|MemSkill]]. It also complements [[context-engineering]] by making context maintenance an explicit policy surface.
