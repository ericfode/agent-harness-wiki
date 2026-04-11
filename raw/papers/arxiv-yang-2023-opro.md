---
title: Large Language Models as Optimizers
author: Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, Xinyun Chen
url: https://arxiv.org/abs/2309.03409
date: 2023-09-07
ingested: 2026-04-11
---

# Large Language Models as Optimizers

**Source:** [arXiv](https://arxiv.org/abs/2309.03409)
**Authors:** Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, Xinyun Chen
**Date:** 2023-09-07
**Primary category:** cs.LG
**All categories:** cs.LG, cs.AI, cs.CL

## Abstract / key passage
This paper introduces Optimization by PROmpting (OPRO), where a language model acts as a black-box optimizer that proposes new candidate solutions from a prompt containing previously tried solutions and their scores. In the prompt-optimization setting, the candidates are task instructions whose downstream task performance is evaluated and fed back into the next optimization step.

## Harness takeaway
OPRO is the clean canonical reference for the “LLM as optimizer” branch. For harnesses it is useful whenever there is a scoreable artifact and little structured critique, but it also highlights how much optimization can proceed with almost nothing except candidate history and scalar value feedback.