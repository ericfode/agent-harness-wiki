---
title: Harness Quality Comparison
created: 2026-04-07
updated: 2026-04-07
type: comparison
tags: [comparison, benchmark, code-quality]
sources: [raw/articles/openai-harness-engineering.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/hermes-agent-github.md, raw/articles/yegge-future-of-coding-agents.md]
---

# Harness Quality Comparison

## Scope
This page compares the harnesses in the source set on the engineering qualities their public materials emphasize: implementation rigor, resumability, evaluation discipline, persistence, and orchestration power. It is qualitative rather than benchmark-numerical; the source corpus here is better at architecture than leaderboard theater.

## Comparison table
| System | Primary quality bet | Where it looks strongest | Typical weakness |
| :--- | :--- | :--- | :--- |
| [[codex-cli]] | Clean protocol architecture and repo legibility | Reusable harness core, App Server, enforcement of taste and invariants | Less emphasis on lifelong personal memory |
| [[claude-code]] | Long-running task coherence through explicit handoffs and evaluators | Recovery from context loss, UI validation, structured progress | Higher operator and compute overhead |
| [[hermes-agent]] | Persistent usefulness through memory and skill accumulation | Long-term recall, profiles, self-improvement loop | Public architecture looks less protocol-clean than Codex |
| [[gas-town]] | Throughput through factory orchestration | Large-swarm coordination and explicit work graphs | Cost, rough edges, operator complexity |
| [[gas-city]] | Modular orchestration primitives | Custom topologies and federated work exchange | Early-stage instability and migration risk |
| [[openclaw]] | Ecosystem breadth | Integrations, public skill marketplace, cross-channel presence | Security and supply-chain exposure |

## Synthesis
No single system dominates all dimensions because they are not optimizing the same objective. Codex prioritizes architectural cleanliness, Claude prioritizes coherent long-running execution, Hermes prioritizes durable learning, Gas Town/Gas City prioritize factory-scale coordination, and OpenClaw prioritizes reach.

## Practical verdict
- If you want a reference architecture for a coding harness, start with [[codex-cli]].
- If you need reliable long-running implementation with explicit QA, study [[claude-code]].
- If you want a persistent assistant that compounds value over time, look at [[hermes-agent]].
- If your taste runs to swarms and ledgers, the Yegge line of [[gas-town]] and [[gas-city]] is the interesting frontier.

## Related pages
This page pairs with [[harness-architecture-comparison]] and draws heavily on [[harness-engineering]], [[context-engineering]], and [[evaluation-and-review-loops]].
