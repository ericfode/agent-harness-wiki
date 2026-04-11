---
title: SAMMO
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [context-engineering, program-synthesis]
sources: [raw/papers/schnabel-2024-sammo.md]
---

# SAMMO

## Overview
SAMMO is a framework for symbolic prompt-program search aimed at compile-time optimization of reusable prompt programs. It represents prompt programs symbolically and searches over structure-aware transformations rather than assuming a flat prompt string or a fixed prompt layout.

## Why it matters
It matters because it is one of the clearest papers in the literature that treats prompt programs as versioned artifacts to be optimized before deployment. That is unusually close to the actual needs of harness engineering.

## Distinctive trait
Its distinctive trait is symbolic compile-time search over a prompt-program intermediate representation, which makes optimizer actions more structural than ordinary prompt rewriting.

## Relationships
Read SAMMO with [[dspy]], [[textgrad]], [[dspy-assertions]], and [[prompt-program-representation-and-optimizer-open-questions]]. It is a natural contrast class for [[rlprompt]], where the optimization target is still a single prompt rather than a symbolic program.