---
title: TextGrad: Automatic "Differentiation" via Text
author: Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou
url: https://arxiv.org/abs/2406.07496
date: 2024-06-11
ingested: 2026-04-11
---

# TextGrad: Automatic "Differentiation" via Text

**Source:** [arXiv](https://arxiv.org/abs/2406.07496)
**Authors:** Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou
**Date:** 2024-06-11
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.LG

## Abstract / key passage
TextGrad proposes a PyTorch-like optimization framework for compound AI systems in which language models emit textual feedback that plays the role of gradients. Instead of optimizing only one prompt string, it treats prompts, code, and other text-defined variables inside a computation graph as editable objects and propagates natural-language blame or improvement suggestions backward through that graph.

## Harness takeaway
TextGrad matters because serious agent harnesses are compound systems rather than single prompts. It is one of the clearest attempts to give those systems a unified optimization substrate with something like module-level credit assignment, which makes it unusually relevant to prompt programs, workflow graphs, and other durable control-plane artifacts.