---
title: "Tracr: Compiled Transformers as a Laboratory for Interpretability"
author: "David Lindner, János Kramár, Sebastian Farquhar, Matthew Rahtz, Thomas McGrath, Vladimir Mikulik"
url: https://arxiv.org/abs/2301.05062v5
date: 2023-01-12
ingested: 2026-04-10
---

# Tracr: Compiled Transformers as a Laboratory for Interpretability

**Source:** [arXiv](https://arxiv.org/abs/2301.05062v5)
**Authors:** David Lindner, János Kramár, Sebastian Farquhar, Matthew Rahtz, Thomas McGrath, Vladimir Mikulik
**Date:** 2023-01-12
**Primary category:** cs.LG
**All categories:** cs.LG, cs.AI, stat.ML

## Abstract
We show how to "compile" human-readable programs into standard decoder-only transformer models. Our compiler, Tracr, generates models with known structure. This structure can be used to design experiments. For example, we use it to study "superposition" in transformers that execute multi-step algorithms. Additionally, the known structure of Tracr-compiled models can serve as ground-truth for evaluating interpretability methods. Commonly, because the "programs" learned by transformers are unknown it is unclear whether an interpretation succeeded. We demonstrate our approach by implementing and examining programs including computing token frequencies, sorting, and parenthesis checking. We provide an open-source implementation of Tracr at https://github.com/google-deepmind/tracr.

## Why it matters here
Primary Tracr paper. It shows how symbolic programs such as RASP can be compiled into transformers, which is useful when thinking about invertible interfaces between language-like objects and network internals.
