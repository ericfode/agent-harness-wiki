---
title: Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution
author: Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, Tim Rocktäschel
url: https://arxiv.org/abs/2309.16797
date: 2023-09-28
ingested: 2026-04-11
---

# Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

**Source:** [arXiv](https://arxiv.org/abs/2309.16797)
**Authors:** Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, Tim Rocktäschel
**Date:** 2023-09-28
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.LG, cs.NE

## Abstract / key passage
Promptbreeder evolves a population of task prompts and, crucially, also evolves the mutation prompts used to edit them. Its central move is self-referential improvement: the mutator itself becomes part of the search object rather than a fixed hidden heuristic.

## Harness takeaway
Promptbreeder matters because it treats optimization procedures as writable artifacts, not only the task prompt. For long-lived harnesses that is a suggestive model: mutation heuristics, repair prompts, and evaluator-facing instructions may all be worth versioning rather than treating as ambient magic.