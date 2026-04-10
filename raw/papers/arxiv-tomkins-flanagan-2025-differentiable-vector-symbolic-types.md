---
title: "Hey Pentti, We Did It Again!: Differentiable vector-symbolic types that prove polynomial termination"
author: "Eilene Tomkins-Flanagan, Connor Hanley, Mary A. Kelly"
url: https://arxiv.org/abs/2510.16533v1
date: 2025-10-18
ingested: 2026-04-10
---

# Hey Pentti, We Did It Again!: Differentiable vector-symbolic types that prove polynomial termination

**Source:** [arXiv](https://arxiv.org/abs/2510.16533v1)
**Authors:** Eilene Tomkins-Flanagan, Connor Hanley, Mary A. Kelly
**Date:** 2025-10-18
**Primary category:** cs.AI
**All categories:** cs.AI, cs.LG

## Abstract
We present a typed computer language, Doug, in which all typed programs may be proved to halt in polynomial time, encoded in a vector-symbolic architecture (VSA). Doug is just an encoding of the light linear functional programming language (LLFPL) described by (Schimanski2009, ch. 7). The types of Doug are encoded using a slot-value encoding scheme based on holographic declarative memory (HDM; Kelly, 2020). The terms of Doug are encoded using a variant of the Lisp VSA defined by (Flanagan, 2024). Doug allows for some points on the embedding space of a neural network to be interpreted as types, where the types of nearby points are similar both in structure and content. Types in Doug are therefore learnable by a neural network. Following (Chollet, 2019), (Card, 1983), and (Newell, 1981), we view skill as the application of a procedure, or program of action, that causes a goal to be satisfied. Skill acquisition may therefore be expressed as program synthesis. Using Doug, we hope to describe a form of learning of skilled behaviour that follows a human-like pace of skill acquisition (i.e., substantially faster than brute force; Heathcote, 2000), exceeding the efficiency of all currently existing approaches (Kaplan, 2020; Jones, 2021; Chollet, 2024). Our approach brings us one step closer to modeling human mental representations, as they must actually exist in the brain, and those representations' acquisition, as they are actually learned.

## Why it matters here
Current typed-VSA citation closest to the draft’s “Doug” motivation. It matters because it treats types themselves as geometric objects with learnable structure rather than as entirely external symbolic annotations.
