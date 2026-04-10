---
title: "Locating and Editing Factual Associations in GPT"
author: "Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov"
url: https://arxiv.org/abs/2202.05262v5
date: 2022-02-10
ingested: 2026-04-10
---

# Locating and Editing Factual Associations in GPT

**Source:** [arXiv](https://arxiv.org/abs/2202.05262v5)
**Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov
**Date:** 2022-02-10
**Primary category:** cs.CL
**All categories:** cs.CL, cs.LG

## Abstract
We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/

## Why it matters here
Primary ROME / causal-tracing source. It matters here because NNPL site selection and write protocols need causal evidence about where semantically meaningful computation actually lives.
