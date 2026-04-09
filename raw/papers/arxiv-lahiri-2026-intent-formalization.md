---
title: Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents
author: Shuvendu K. Lahiri
url: https://arxiv.org/abs/2603.17150v1
date: 2026-03-17
ingested: 2026-04-08
---

# Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents

**Source:** [arXiv](https://arxiv.org/abs/2603.17150v1)
**Authors:** Shuvendu K. Lahiri
**Date:** 2026-03-17
**Primary category:** cs.SE
**All categories:** cs.SE, cs.AI, cs.PL

## Abstract
Agentic AI systems can now generate code with remarkable fluency, but a fundamental question remains: \emph{does the generated code actually do what the user intended?} The gap between informal natural language requirements and precise program behavior -- the \emph{intent gap} -- has always plagued software engineering, but AI-generated code amplifies it to an unprecedented scale. This article argues that \textbf{intent formalization} -- the translation of informal user intent into a set of checkable formal specifications -- is the key challenge that will determine whether AI makes software more reliable or merely more abundant. Intent formalization offers a tradeoff spectrum suitable to the reliability needs of different contexts: from lightweight tests that disambiguate likely misinterpretations, through full functional specifications for formal verification, to domain-specific languages from which correct code is synthesized automatically. The central bottleneck is \emph{validating specifications}: since there is no oracle for specification correctness other than the user, we need semi-automated metrics that can assess specification quality with or without code, through lightweight user interaction and proxy artifacts such as tests. We survey early research that demonstrates the \emph{potential} of this approach: interactive test-driven formalization that improves program correctness, AI-generated postconditions that catch real-world bugs missed by prior methods, and end-to-end verified pipelines that produce provably correct code from informal specifications. We outline the open research challenges -- scaling beyond benchmarks, achieving compositionality over changes, metrics for validating specifications, handling rich logics, designing human-AI specification interactions -- that define a research agenda spanning AI, programming languages, formal methods, and human-computer interaction.
