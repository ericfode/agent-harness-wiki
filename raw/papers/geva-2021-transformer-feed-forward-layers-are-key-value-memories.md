---
title: "Transformer Feed-Forward Layers Are Key-Value Memories"
author: "Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy"
url: https://aclanthology.org/2021.emnlp-main.446/
date: 2021-11-01
ingested: 2026-04-10
---

# Transformer Feed-Forward Layers Are Key-Value Memories

**Source:** [ACL Anthology](https://aclanthology.org/2021.emnlp-main.446/)
**Authors:** Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy
**Date:** 2021-11-01

## Abstract
Feed-forward layers constitute two-thirds of a transformer model’s parameters, yet their role in the network remains under-explored. We show that feed-forward layers in transformer-based language models operate as key-value memories, where each key correlates with textual patterns in the training examples, and each value induces a distribution over the output vocabulary. Our experiments show that the learned patterns are human-interpretable, and that lower layers tend to capture shallow patterns, while upper layers learn more semantic ones. The values complement the keys’ input patterns by inducing output distributions that concentrate probability mass on tokens likely to appear immediately after each pattern, particularly in the upper layers. Finally, we demonstrate that the output of a feed-forward layer is a composition of its memories, which is subsequently refined throughout the model’s layers via residual connections to produce the final output distribution.

## Why it matters here
This paper makes the residual-stream “read key / write value” story concrete for transformer MLP blocks. It is one of the clearest sources for treating internal activations as a manipulable workspace rather than as mere pre-logit mush.
