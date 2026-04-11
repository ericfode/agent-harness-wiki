---
title: Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization
author: Tobias Schnabel, Jennifer Neville
url: https://doi.org/10.18653/v1/2024.findings-emnlp.37
date: 2024
ingested: 2026-04-11
---

# Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization

**Source:** [DOI](https://doi.org/10.18653/v1/2024.findings-emnlp.37)
**Authors:** Tobias Schnabel, Jennifer Neville
**Date:** 2024

## Abstract / key passage
This paper introduces SAMMO, a framework for symbolic prompt-program search aimed at compile-time optimization of reusable prompt programs. Instead of assuming a flat prompt string or a fixed prompt structure, SAMMO represents prompt programs symbolically and searches over structure-aware transformations. The reported gains cover instruction tuning, RAG pipeline tuning, and prompt compression across several language models.

## Harness takeaway
SAMMO is unusually relevant to harness design because it treats prompt programs as versioned artifacts that can be optimized before deployment. That is much closer to real control-plane engineering than endlessly editing one monolithic prompt string.