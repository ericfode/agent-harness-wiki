---
title: PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization
author: Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric P. Xing, Zhiting Hu
url: https://arxiv.org/abs/2310.16427
date: 2023-10-25
ingested: 2026-04-11
---

# PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization

**Source:** [arXiv](https://arxiv.org/abs/2310.16427)
**Authors:** Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric P. Xing, Zhiting Hu
**Date:** 2023-10-25
**Primary category:** cs.CL

## Abstract / key passage
PromptAgent treats prompt optimization as a strategic planning problem. It reflects on model errors, explores prompt states with a Monte-Carlo-tree-search-style procedure, and searches for high-reward edit paths rather than only proposing independent prompt candidates.

## Harness takeaway
PromptAgent is the clearest planning-based prompt optimizer in this cluster. It matters for harnesses because it assumes richer failure traces than scalar-only search and therefore sits closer to systems that already log structured error evidence, tool traces, or evaluator feedback.