---
title: "Latent Programmer: Discrete Latent Codes for Program Synthesis"
author: "Joey Hong, David Dohan, Rishabh Singh, Charles Sutton, Manzil Zaheer"
url: https://arxiv.org/abs/2012.00377v2
date: 2020-12-01
ingested: 2026-04-10
---

# Latent Programmer: Discrete Latent Codes for Program Synthesis

**Source:** [arXiv](https://arxiv.org/abs/2012.00377v2)
**Authors:** Joey Hong, David Dohan, Rishabh Singh, Charles Sutton, Manzil Zaheer
**Date:** 2020-12-01
**Primary category:** cs.LG
**All categories:** cs.LG, cs.AI

## Abstract
In many sequence learning tasks, such as program synthesis and document summarization, a key problem is searching over a large space of possible output sequences. We propose to learn representations of the outputs that are specifically meant for search: rich enough to specify the desired output but compact enough to make search more efficient. Discrete latent codes are appealing for this purpose, as they naturally allow sophisticated combinatorial search strategies. The latent codes are learned using a self-supervised learning principle, in which first a discrete autoencoder is trained on the output sequences, and then the resulting latent codes are used as intermediate targets for the end-to-end sequence prediction task. Based on these insights, we introduce the \emph{Latent Programmer}, a program synthesis method that first predicts a discrete latent code from input/output examples, and then generates the program in the target language. We evaluate the Latent Programmer on two domains: synthesis of string transformation programs, and generation of programs from natural language descriptions. We demonstrate that the discrete latent representation significantly improves synthesis accuracy.

## Why it matters here
Primary discrete-latent program-synthesis paper. It is one of the strongest precedents for mediating program generation through a latent code rather than direct token emission.
