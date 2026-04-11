---
title: JudgeFlow
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [benchmark, error-recovery, work-management]
sources: [raw/papers/arxiv-ma-2026-judgeflow.md]
---

# JudgeFlow

## Overview
JudgeFlow adds a judge module that assigns responsibility scores to workflow blocks so repair can target the part that actually failed. It tries to close the gap between “the workflow went badly” and “here is the piece worth mutating.”

## Why it matters
It matters because serious control planes need diagnosis, not only generation. Promotion requires knowing which block deserves blame and which does not.

## Distinctive trait
Its distinctive trait is block-level responsibility assignment over workflow traces, which turns vague failure into actionable repair signals.

## Relationships
Read JudgeFlow with [[self-evolving-workflows]], [[evaluation-and-review-loops]], and [[robustflow|RobustFlow]]. It also pairs naturally with [[aflow|AFlow]] when search needs a sharper evaluator lane.
