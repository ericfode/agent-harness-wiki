---
title: "A Mathematical Framework for Transformer Circuits"
author: "Anthropic / Transformer Circuits"
url: https://transformer-circuits.pub/2021/framework/index.html
date: 2021-01-01
ingested: 2026-04-10
---

# A Mathematical Framework for Transformer Circuits

**Source:** [Anthropic / Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
**Date:** 2021-01-01

## Summary
This essay reframes transformers as collections of small computational motifs that read from and write to a shared residual stream. It is still the clearest public articulation of the residual stream as the model’s central communication bus.

## Why it matters here
For NNPL, this is the conceptual bridge from “token model” to “editable workspace.” If the residual stream really is the shared substrate through which heads and MLPs communicate, it becomes plausible to attach read/write interfaces there.
