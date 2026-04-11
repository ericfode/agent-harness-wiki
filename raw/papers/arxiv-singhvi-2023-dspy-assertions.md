---
title: DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines
author: Arnav Singhvi, Manish Shetty, Shangyin Tan, Christopher Potts, Koushik Sen, Matei Zaharia, Omar Khattab
url: https://arxiv.org/abs/2312.13382
date: 2023-12-20
ingested: 2026-04-11
---

# DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

**Source:** [arXiv](https://arxiv.org/abs/2312.13382)
**Authors:** Arnav Singhvi, Manish Shetty, Shangyin Tan, Christopher Potts, Koushik Sen, Matei Zaharia, Omar Khattab
**Date:** 2023-12-20
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.PL

## Abstract / key passage
DSPy Assertions extends the DSPy programming model with explicit computational constraints that language-model outputs should satisfy. Instead of relying only on prompt wording to coax compliance, it lets the program express assertions directly and adds strategies for compilation-time reliability improvements plus inference-time self-refinement when assertions fail.

## Harness takeaway
This paper matters because it turns constraints into first-class program objects. For a long-lived harness, that means schemas, citation requirements, tool-use limits, and other invariants can live as durable artifacts rather than as polite hints hidden in prose prompts.