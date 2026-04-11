---
title: RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning
author: Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yihan Wang, Han Guo, Tianmin Shu, Meng Song, Eric P. Xing, Zhiting Hu
url: https://arxiv.org/abs/2205.12548
date: 2022-05-25
ingested: 2026-04-11
---

# RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning

**Source:** [arXiv](https://arxiv.org/abs/2205.12548)
**Authors:** Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yihan Wang, Han Guo, Tianmin Shu, Meng Song, Eric P. Xing, Zhiting Hu
**Date:** 2022-05-25
**Primary category:** cs.CL
**All categories:** cs.CL, cs.LG

## Abstract / key passage
RLPrompt frames discrete prompt search as a reinforcement-learning problem over a frozen language model. Instead of tuning soft embeddings, it trains a lightweight policy network to generate prompt tokens and stabilizes learning against noisy downstream rewards. The paper is notable not only because it makes RL-on-prompts explicit, but because the learned prompts are often ungrammatical “gibberish” that still transfer surprisingly well across language models.

## Harness takeaway
RLPrompt is the clean canonical anchor for the branch of the literature that treats a prompt as an optimizable external artifact rather than something sacred or purely handcrafted. For harness design, it is useful partly as a success case and partly as a warning: evaluator quality, provenance, and rollback matter because reward-optimized prompt artifacts need not remain human-legible.