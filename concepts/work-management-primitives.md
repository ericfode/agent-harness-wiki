---
title: Work Management Primitives
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [work-management, orchestration, error-recovery]
sources: [raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/yegge-vibe-maintainer.md, raw/articles/anthropic-effective-harnesses.md]
---

# Work Management Primitives

## Definition
Work-management primitives are the concrete objects through which an agent harness represents pending, active, reviewed, and completed work. Good primitives make retries and handoffs routine. Bad ones turn every resumption into archaeology.

## Gas Town family
The richest vocabulary in the source set comes from [[gas-town]]: beads, epics, molecules, protomolecules, formulas, and wisps. These objects encode hierarchy, workflow composition, and persistence. Gas City then generalizes them into a more modular coordination kit.

## Anthropic family
Anthropic's feature lists, init scripts, and progress logs are much simpler primitives, but simplicity is the point. A large JSON checklist with explicit pass/fail state avoids the soft deceit of freeform notes and gives later agents a recoverable truth source.

## Operational lesson
The right primitive is the one that survives interruption and guides the next action. In that respect, a dull `feature_list.json` can beat a flamboyant swarm if the former actually causes the next session to test the right thing.

## Related pages
Work primitives are where [[memory-persistence]] meets orchestration. See [[gas-town]], [[gas-city]], and [[claude-code]], then compare approaches in [[harness-architecture-comparison]].
