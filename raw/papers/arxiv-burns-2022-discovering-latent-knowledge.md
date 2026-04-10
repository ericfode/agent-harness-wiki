---
title: "Discovering Latent Knowledge in Language Models Without Supervision"
author: "Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt"
url: https://arxiv.org/abs/2212.03827v2
date: 2022-12-07
ingested: 2026-04-10
---

# Discovering Latent Knowledge in Language Models Without Supervision

**Source:** [arXiv](https://arxiv.org/abs/2212.03827v2)
**Authors:** Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt
**Date:** 2022-12-07
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.LG

## Abstract
Existing techniques for training language models can be misaligned with the truth: if we train models with imitation learning, they may reproduce errors that humans make; if we train them to generate text that humans rate highly, they may output errors that human evaluators can't detect. We propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way. Specifically, we introduce a method for accurately answering yes-no questions given only unlabeled model activations. It works by finding a direction in activation space that satisfies logical consistency properties, such as that a statement and its negation have opposite truth values. We show that despite using no supervision and no model outputs, our method can recover diverse knowledge represented in large language models: across 6 models and 10 question-answering datasets, it outperforms zero-shot accuracy by 4\% on average. We also find that it cuts prompt sensitivity in half and continues to maintain high accuracy even when models are prompted to generate incorrect answers. Our results provide an initial step toward discovering what language models know, distinct from what they say, even when we don't have access to explicit ground truth labels.

## Why it matters here
Primary latent-knowledge paper. It is useful as a warning that what is present in internal representations and what is surfaced in ordinary outputs can diverge in safety-relevant ways.
