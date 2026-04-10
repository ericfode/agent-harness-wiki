---
title: "Searching Latent Program Spaces"
author: "Matthew V Macfarlane, Clement Bonnet"
url: https://arxiv.org/abs/2411.08706v3
date: 2024-11-13
ingested: 2026-04-10
---

# Searching Latent Program Spaces

**Source:** [arXiv](https://arxiv.org/abs/2411.08706v3)
**Authors:** Matthew V Macfarlane, Clement Bonnet
**Date:** 2024-11-13
**Primary category:** cs.LG
**All categories:** cs.LG, cs.AI

## Abstract
General intelligence requires systems that acquire new skills efficiently and generalize beyond their training distributions. Although program synthesis approaches have strong generalization power, they face scaling issues due to the large combinatorial spaces that quickly render them impractical, requiring human-generated DSLs or pre-trained priors to narrow this search space. On the other hand, deep learning methods have had high successes, but they lack structured test-time adaptation and rely on heavy stochastic sampling or expensive gradient updates for fine-tuning. In this work, we propose the Latent Program Network (LPN), a novel architecture that builds in test-time search directly into neural models. LPN learns a latent space of implicit programs -- neurally mapping inputs to outputs -- through which it can search using gradients at test time. LPN combines the adaptability of symbolic approaches and the scalability of neural methods. It searches through a compact latent space at test time and bypasses the need for pre-defined domain-specific languages. On a range of programming-by-examples tasks, LPN either outperforms or matches performance compared to in-context learning and test-time training methods. Tested on the ARC-AGI benchmark, we demonstrate that LPN can both learn a compact program space and search through it at test time to adapt to novel tasks. LPN doubles its performance on out-of-distribution tasks when test-time search is switched on.

## Why it matters here
Primary latent-program-search paper. It directly supports the framing of program induction as search and optimization in a latent space rather than only in token space.
