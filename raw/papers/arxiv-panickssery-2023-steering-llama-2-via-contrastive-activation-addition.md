---
title: "Steering Llama 2 via Contrastive Activation Addition"
author: "Nina Panickssery, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner"
url: https://arxiv.org/abs/2312.06681v4
date: 2023-12-09
ingested: 2026-04-10
---

# Steering Llama 2 via Contrastive Activation Addition

**Source:** [arXiv](https://arxiv.org/abs/2312.06681v4)
**Authors:** Nina Panickssery, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner
**Date:** 2023-12-09
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.LG

## Abstract
We introduce Contrastive Activation Addition (CAA), an innovative method for steering language models by modifying their activations during forward passes. CAA computes "steering vectors" by averaging the difference in residual stream activations between pairs of positive and negative examples of a particular behavior, such as factual versus hallucinatory responses. During inference, these steering vectors are added at all token positions after the user's prompt with either a positive or negative coefficient, allowing precise control over the degree of the targeted behavior. We evaluate CAA's effectiveness on Llama 2 Chat using multiple-choice behavioral question datasets and open-ended generation tasks. We demonstrate that CAA significantly alters model behavior, is effective over and on top of traditional methods like finetuning and system prompt design, and minimally reduces capabilities. Moreover, we gain deeper insights into CAA's mechanisms by employing various activation space interpretation methods. CAA accurately steers model outputs and sheds light on how high-level concepts are represented in Large Language Models (LLMs).

## Why it matters here
Primary contrastive activation-addition source. It sharpens the steering story by deriving control vectors from differences between contrasted activation sets rather than from prompt text alone.
