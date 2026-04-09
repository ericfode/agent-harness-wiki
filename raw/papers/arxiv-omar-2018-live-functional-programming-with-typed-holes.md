---
title: Live Functional Programming with Typed Holes
author: Cyrus Omar, Ian Voysey, Ravi Chugh, Matthew A. Hammer
url: https://arxiv.org/abs/1805.00155v4
date: 2018-05-01
ingested: 2026-04-09
---

# Live Functional Programming with Typed Holes

**Source:** [arXiv](https://arxiv.org/abs/1805.00155v4)
**Authors:** Cyrus Omar, Ian Voysey, Ravi Chugh, Matthew A. Hammer
**Date:** 2018-05-01
**Primary category:** cs.PL

## Abstract
This paper develops a dynamic semantics for incomplete functional programs. Instead of aborting when evaluation reaches holes or inconsistencies, evaluation continues around holes while tracking closures that help the programmer understand partial behavior. These hole closures enable fill-and-resume editing so evaluation does not need to restart after every hole-filling change. The approach is mechanized in Agda and implemented in the Hazel environment, aiming for a live programming setting where useful feedback exists for every reachable editor state.

## Harness takeaway
A serious harness should remain inspectable and live even when work is incomplete. Draft plans, partial code, provisional traces, and unresolved branches should not collapse feedback entirely.
