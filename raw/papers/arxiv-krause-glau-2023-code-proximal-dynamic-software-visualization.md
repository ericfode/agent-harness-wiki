---
title: Collaborative, Code-Proximal Dynamic Software Visualization within Code Editors
author: Alexander Krause-Glau, Wilhelm Hasselbring
url: https://arxiv.org/abs/2308.15785v1
date: 2023-08-30
ingested: 2026-04-08
---

# Collaborative, Code-Proximal Dynamic Software Visualization within Code Editors

**Source:** [arXiv](https://arxiv.org/abs/2308.15785v1)
**Authors:** Alexander Krause-Glau, Wilhelm Hasselbring
**Date:** 2023-08-30
**Primary category:** cs.SE
**All categories:** cs.SE

## Abstract
Software visualizations are usually realized as standalone and isolated tools that use embedded code viewers within the visualization. In the context of program comprehension, only few approaches integrate visualizations into code editors, such as integrated development environments. This is surprising since professional developers consider reading source code as one of the most important ways to understand software, therefore spend a lot of time with code editors. In this paper, we introduce the design and proof-of-concept implementation for a software visualization approach that can be embedded into code editors. Our contribution differs from related work in that we use dynamic analysis of a software system's runtime behavior. Additionally, we incorporate distributed tracing. This enables developers to understand how, for example, the currently handled source code behaves as a fully deployed, distributed software system. Our visualization approach enhances common remote pair programming tools and is collaboratively usable by employing shared code cities. As a result, user interactions are synchronized between code editor and visualization, as well as broadcasted to collaborators. To the best of our knowledge, this is the first approach that combines code editors with collaboratively usable code cities. Therefore, we conducted a user study to collect first-time feedback regarding the perceived usefulness and perceived usability of our approach. We additionally collected logging information to provide more data regarding time spent in code cities that are embedded in code editors. Seven teams with two students each participated in that study. The results show that the majority of participants find our approach useful and would employ it for their own use. We provide each participant's video recording, raw results, and all steps to reproduce our experiment as supplementary package.
