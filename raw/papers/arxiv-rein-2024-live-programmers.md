---
title: Broadening the View of Live Programmers: Integrating a Cross-Cutting Perspective on Run-Time Behavior into a Live Programming Environment
author: Patrick Rein, Christian Flach, Stefan Ramson, Eva Krebs, Robert Hirschfeld
url: https://arxiv.org/abs/2403.02428v1
date: 2024-03-04
ingested: 2026-04-08
---

# Broadening the View of Live Programmers: Integrating a Cross-Cutting Perspective on Run-Time Behavior into a Live Programming Environment

**Source:** [arXiv](https://arxiv.org/abs/2403.02428v1)
**Authors:** Patrick Rein, Christian Flach, Stefan Ramson, Eva Krebs, Robert Hirschfeld
**Date:** 2024-03-04
**Primary category:** cs.PL
**All categories:** cs.PL

## Abstract
Live programming provides feedback on run-time behavior by visualizing concrete values of expressions close to the source code. When using such a local perspective on run-time behavior, programmers have to mentally reconstruct the control flow if they want to understand the relation between observed values. As this requires complete and correct knowledge of all relevant code, this reconstruction is impractical for larger programs as well as in the case of unexpected program behavior. In turn, cross-cutting perspectives on run-time behavior can visualize the actual control flow directly. At the same time, cross-cutting perspectives are often difficult to navigate due to the large number of run-time events. We propose to integrate cross-cutting perspectives into live programming environments based on local perspectives so that the two complement each other: the cross-cutting perspective provides an overview of the run-time behavior; the local perspective provides detailed feedback as well as points of interest to navigate the cross-cutting perspective. We present a cross-cutting perspective prototype in the form of a call tree browser integrated into the Babylonian/S live programming environment. In an exploratory user study, we observed that programmers found the tool useful for debugging, code comprehension, and navigation. Finally, we discuss how our prototype illustrates how the features of live programming environments may serve as the basis for other powerful dynamic development tools.
