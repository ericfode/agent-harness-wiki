---
title: "Steering Language Models With Activation Engineering"
author: "Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J. Vazquez, Ulisse Mini, Monte MacDiarmid"
url: https://arxiv.org/abs/2308.10248v5
date: 2023-08-20
ingested: 2026-04-10
---

# Steering Language Models With Activation Engineering

**Source:** [arXiv](https://arxiv.org/abs/2308.10248v5)
**Authors:** Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J. Vazquez, Ulisse Mini, Monte MacDiarmid
**Date:** 2023-08-20
**Primary category:** cs.CL
**All categories:** cs.CL, cs.LG

## Abstract
Prompt engineering and finetuning aim to maximize language model performance on a given metric (like toxicity reduction). However, these methods do not fully elicit a model's capabilities. To reduce this gap, we introduce activation engineering: the inference-time modification of activations in order to control (or steer) model outputs. Specifically, we introduce the Activation Addition (ActAdd) technique, which contrasts the intermediate activations on prompt pairs (such as "Love" versus "Hate") to compute a steering vector (Subramani et al. 2022). By tactically adding in e.g. the "Love" - "Hate" steering vector during the forward pass, we achieve SOTA on negative-to-positive sentiment shift and detoxification using models including LLaMA-3 and OPT. ActAdd yields inference-time control over high-level output properties (like topic and sentiment) while preserving performance on off-target tasks. ActAdd is lightweight: it does not require any machine optimization and works with a single pair of data points, which enables rapid iteration over steering. ActAdd demonstrates the power of activation engineering.

## Why it matters here
Primary activation-engineering paper. It provides a concrete read/write primitive for intervening on hidden activations without retraining the whole model.
