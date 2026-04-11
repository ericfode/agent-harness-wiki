---
title: Atropos
created: 2026-04-10
updated: 2026-04-11
type: entity
tags: [tool-execution, orchestration, benchmark]
sources: [raw/articles/hermes-atropos-integration-2026-04-09.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/another-harness-work-item-closure-environment-2026-04-10.md, raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md]
---

# Atropos

## Overview
Atropos is the RL environment and rollout substrate used by Hermes for multi-turn tool-calling tasks. In the Hermes stack it supplies the BaseEnv contract, server management, scheduling, logging, and `serve/process/evaluate` modes, while Hermes layers on agent-loop orchestration and reward verification in the same sandbox.

## Why it matters
It matters because it shows what a harness-native environment API looks like when the agent is not just completing one prompt but acting through tools across multiple turns.

## Distinctive trait
Its distinctive trait is scope: in Hermes it is neither a bare trainer nor a mere leaderboard wrapper, but an environment/runtime contract with training hookup through the broader Tinker-Atropos stack.

## Relationships
Read Atropos with [[hermes-agent]], [[agentgym]], [[rl-gyms-and-executable-environments-for-ai-harnesses]], the fit analysis in [[another-harness-and-atropos]], and the local stepping-stone prototypes in [[another-harness-work-item-closure-environment]] and [[another-harness-evaluator-discipline-environment]].
