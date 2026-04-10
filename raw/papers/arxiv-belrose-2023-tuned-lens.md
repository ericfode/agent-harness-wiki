---
title: "Eliciting Latent Predictions from Transformers with the Tuned Lens"
author: "Nora Belrose, Igor Ostrovsky, Lev McKinney, Zach Furman, Logan Smith, Danny Halawi, Stella Biderman, Jacob Steinhardt"
url: https://arxiv.org/abs/2303.08112v6
date: 2023-03-14
ingested: 2026-04-10
---

# Eliciting Latent Predictions from Transformers with the Tuned Lens

**Source:** [arXiv](https://arxiv.org/abs/2303.08112v6)
**Authors:** Nora Belrose, Igor Ostrovsky, Lev McKinney, Zach Furman, Logan Smith, Danny Halawi, Stella Biderman, Jacob Steinhardt
**Date:** 2023-03-14
**Primary category:** cs.LG
**All categories:** cs.LG

## Abstract
We analyze transformers from the perspective of iterative inference, seeking to understand how model predictions are refined layer by layer. To do so, we train an affine probe for each block in a frozen pretrained model, making it possible to decode every hidden state into a distribution over the vocabulary. Our method, the tuned lens, is a refinement of the earlier "logit lens" technique, which yielded useful insights but is often brittle. We test our method on various autoregressive language models with up to 20B parameters, showing it to be more predictive, reliable and unbiased than the logit lens. With causal experiments, we show the tuned lens uses similar features to the model itself. We also find the trajectory of latent predictions can be used to detect malicious inputs with high accuracy. All code needed to reproduce our results can be found at https://github.com/AlignmentResearch/tuned-lens.

## Why it matters here
Primary tuned-lens paper. It is the cleanest source for layerwise translators that compensate for basis drift and make intermediate-state decoding substantially less naive than the original logit lens.
