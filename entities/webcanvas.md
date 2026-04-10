---
title: WebCanvas
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [benchmark, tool-execution, work-management]
sources: [raw/papers/arxiv-pan-2024-webcanvas.md]
---

# WebCanvas

## Overview
WebCanvas is an online evaluation framework for web agents that explicitly addresses the fact that the web keeps changing. It couples online tasks with intermediate evaluation states and maintenance tooling so the benchmark can remain alive rather than fossilized.

## Why it matters
It matters because interface drift is not a nuisance around the edges of web-agent evaluation; it is the actual medium. WebCanvas treats that as a first-class design problem.

## Distinctive trait
Its distinctive trait is benchmark maintenance under live web change, with lightweight annotation and testing pipelines rather than one frozen dataset.

## Relationships
Read WebCanvas with [[webarena]], [[browsergym]], [[workarena]], and the environment-maintenance discussion in [[rl-gyms-and-executable-environments-for-ai-harnesses]].
