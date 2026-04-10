---
title: "pyvene: A Library for Understanding and Improving PyTorch Models via Interventions"
author: "Zhengxuan Wu, Atticus Geiger, Aryaman Arora, Jing Huang, Zheng Wang, Noah D. Goodman, Christopher D. Manning, Christopher Potts"
url: https://arxiv.org/abs/2403.07809v1
date: 2024-03-12
ingested: 2026-04-10
---

# pyvene: A Library for Understanding and Improving PyTorch Models via Interventions

**Source:** [arXiv](https://arxiv.org/abs/2403.07809v1)
**Authors:** Zhengxuan Wu, Atticus Geiger, Aryaman Arora, Jing Huang, Zheng Wang, Noah D. Goodman, Christopher D. Manning, Christopher Potts
**Date:** 2024-03-12
**Primary category:** cs.LG
**All categories:** cs.LG, cs.CL

## Abstract
Interventions on model-internal states are fundamental operations in many areas of AI, including model editing, steering, robustness, and interpretability. To facilitate such research, we introduce $\textbf{pyvene}$, an open-source Python library that supports customizable interventions on a range of different PyTorch modules. $\textbf{pyvene}$ supports complex intervention schemes with an intuitive configuration format, and its interventions can be static or include trainable parameters. We show how $\textbf{pyvene}$ provides a unified and extensible framework for performing interventions on neural models and sharing the intervened upon models with others. We illustrate the power of the library via interpretability analyses using causal abstraction and knowledge localization. We publish our library through Python Package Index (PyPI) and provide code, documentation, and tutorials at https://github.com/stanfordnlp/pyvene.

## Why it matters here
Primary pyvene paper. It matters less for theory than for experimental discipline: a serious NNPL project needs reproducible intervention infrastructure, not ad hoc forward-hook folklore.
