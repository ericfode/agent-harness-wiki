---
title: Harness Architecture Comparison
created: 2026-04-07
updated: 2026-04-07
type: comparison
tags: [comparison, orchestration, tool-execution, subagents]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-welcome-to-the-wasteland.md]
---

# Harness Architecture Comparison

## Key dimensions
The pages in this wiki differ most clearly along five architectural axes: session container, memory substrate, work representation, evaluation loop, and deployment surface.

## Comparison table
| System | Session container | Memory substrate | Work representation | Evaluation style | Surface model |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [[codex-cli]] | Threads / turns / items via App Server | Session history plus repo docs | Plans, docs, tool state | Self-review plus enforced repo checks | CLI, IDE, web, app through a shared protocol |
| [[claude-code]] | Fresh sessions with structured handoffs | Feature lists, progress logs, init scripts | Sprint contracts and explicit pass/fail features | Separate evaluator with browser automation | Coding surface plus external tool integrations |
| [[hermes-agent]] | Persistent multi-platform conversations | Searchable memory, skills, user modeling | Tasks, skills, cron jobs, profiles | Tool-driven verification and memory reuse | CLI plus messaging gateway and MCP |
| [[gas-town]] | Swarm sessions across named roles | Beads in Git / Dolt | Beads, epics, molecules, formulas, wisps | Human plus role-based oversight | tmux-style orchestrator/factory |
| [[gas-city]] | Modular orchestration nodes | Beads plus Wasteland federation | Builder primitives and wanted-board exchange | Federated trust and validator roles | Custom topologies over shared protocols |
| [[openclaw]] | Persistent service runtime | Long-lived agent state plus marketplace skills | Ecosystem skills and integrations | Less explicit in current corpus | Cross-channel background service |

## Main architectural lesson
The important divergence is not "which model is best" but where state lives and how work is represented. Codex externalizes protocol boundaries, Claude externalizes handoff artifacts, Hermes externalizes memory and skills, and Gas Town externalizes the work graph itself.

## Related pages
Read this page after [[agent-harness-anatomy]] and alongside [[memory-persistence]] and [[work-management-primitives]]. It is also the factual substrate for [[new-harness-design-notes]].
