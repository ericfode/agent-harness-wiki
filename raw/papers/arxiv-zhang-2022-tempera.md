---
title: TEMPERA: Test-Time Prompting via Reinforcement Learning
author: Tianjun Zhang, Xuezhi Wang, Denny Zhou, Dale Schuurmans, Joseph E. Gonzalez
url: https://arxiv.org/abs/2211.11890
date: 2022-11-21
ingested: 2026-04-11
---

# TEMPERA: Test-Time Prompting via Reinforcement Learning

**Source:** [arXiv](https://arxiv.org/abs/2211.11890)
**Authors:** Tianjun Zhang, Xuezhi Wang, Denny Zhou, Dale Schuurmans, Joseph E. Gonzalez
**Date:** 2022-11-21
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI

## Abstract / key passage
TEMPERA trains a reinforcement-learning policy to edit an initial prompt at inference time for each query. Its action space spans commonly used prompt components such as instruction phrases, few-shot exemplars, and verbalizers, so the method is runtime prompt adaptation rather than one-shot offline prompt search.

## Harness takeaway
TEMPERA is a useful anchor for the runtime-adaptation branch of the literature. It shows that prompt surfaces can be treated as live control surfaces per query without updating model weights, though the learned policy is still trained offline and the setting is much narrower than long-horizon agent workflows.