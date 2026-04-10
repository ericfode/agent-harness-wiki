---
title: "Neural Discrete Representation Learning"
author: "Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu"
url: https://arxiv.org/abs/1711.00937v2
date: 2017-11-02
ingested: 2026-04-10
---

# Neural Discrete Representation Learning

**Source:** [arXiv](https://arxiv.org/abs/1711.00937v2)
**Authors:** Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu
**Date:** 2017-11-02
**Primary category:** cs.LG
**All categories:** cs.LG

## Abstract
Learning useful representations without supervision remains a key challenge in machine learning. In this paper, we propose a simple yet powerful generative model that learns such discrete representations. Our model, the Vector Quantised-Variational AutoEncoder (VQ-VAE), differs from VAEs in two key ways: the encoder network outputs discrete, rather than continuous, codes; and the prior is learnt rather than static. In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ). Using the VQ method allows the model to circumvent issues of "posterior collapse" -- where the latents are ignored when they are paired with a powerful autoregressive decoder -- typically observed in the VAE framework. Pairing these representations with an autoregressive prior, the model can generate high quality images, videos, and speech as well as doing high quality speaker conversion and unsupervised learning of phonemes, providing further evidence of the utility of the learnt representations.

## Why it matters here
Primary VQ-VAE source. It is the standard citation for learned discrete latent codebooks and therefore a natural precedent for discrete NNPL spines.
