---
title: "Neural Programmer-Interpreters"
author: "Scott Reed, Nando de Freitas"
url: https://arxiv.org/abs/1511.06279v4
date: 2015-11-19
ingested: 2026-04-10
---

# Neural Programmer-Interpreters

**Source:** [arXiv](https://arxiv.org/abs/1511.06279v4)
**Authors:** Scott Reed, Nando de Freitas
**Date:** 2015-11-19
**Primary category:** cs.LG
**All categories:** cs.LG, cs.NE

## Abstract
We propose the neural programmer-interpreter (NPI): a recurrent and compositional neural network that learns to represent and execute programs. NPI has three learnable components: a task-agnostic recurrent core, a persistent key-value program memory, and domain-specific encoders that enable a single NPI to operate in multiple perceptually diverse environments with distinct affordances. By learning to compose lower-level programs to express higher-level programs, NPI reduces sample complexity and increases generalization ability compared to sequence-to-sequence LSTMs. The program memory allows efficient learning of additional tasks by building on existing programs. NPI can also harness the environment (e.g. a scratch pad with read-write pointers) to cache intermediate results of computation, lessening the long-term memory burden on recurrent hidden units. In this work we train the NPI with fully-supervised execution traces; each program has example sequences of calls to the immediate subprograms conditioned on the input. Rather than training on a huge number of relatively weak labels, NPI learns from a small number of rich examples. We demonstrate the capability of our model to learn several types of compositional programs: addition, sorting, and canonicalizing 3D models. Furthermore, a single NPI learns to execute these programs and all 21 associated subprograms.

## Why it matters here
Early continuous program-representation paper. It is a useful ancestor for the idea that program structure can be stored and manipulated in non-text neural state.
