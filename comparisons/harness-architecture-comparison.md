---
title: Harness Architecture Comparison
created: 2026-04-07
updated: 2026-04-09
type: comparison
tags: [comparison, orchestration, tool-execution, subagents]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-introducing-codex-app.md, raw/articles/openai-codex-app-server-readme.md, raw/articles/openai-codex-chatgpt-plan.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-claude-code-overview.md, raw/articles/anthropic-claude-code-subagents.md, raw/articles/anthropic-claude-code-agent-teams.md, raw/articles/anthropic-claude-code-scheduled-tasks.md, raw/articles/hermes-agent-github.md, raw/articles/hermes-agent-api-server-docs.md, raw/articles/openclaw-agent-runtime-docs.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-welcome-to-the-wasteland.md, raw/papers/arxiv-zhou-2026-memento-skills.md, raw/articles/memento-skills-github.md]
---

# Harness Architecture Comparison

## Key dimensions
The pages in this wiki differ most clearly along five architectural axes: session container, memory substrate, work representation, evaluation loop, and deployment surface.

## Comparison table
| System | Session container | Memory substrate | Work representation | Evaluation style | Surface model |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [[codex-cli]] | Threads / turns / items via [[codex-app-server]] plus cloud-delegated tasks | Session history plus repo docs and shared client state | Plans, docs, tool state, worktrees, automations, plugins | Self-review, GitHub auto-review, and enforced repo checks | CLI, IDE, web, app, cloud, and SDK/Slack control paths |
| [[claude-code]] | Fresh sessions with resumable artifacts, custom subagents, and experimental agent teams across separate sessions | `CLAUDE.md`, auto memory, feature lists, progress logs | Sprint contracts, subagents, agent teams, scheduled tasks, and explicit pass/fail features | Separate evaluator plus CI/review integrations and hooks | Terminal, IDE, desktop, browser, and remote-control surfaces |
| [[hermes-agent]] | Persistent multi-platform conversations and gateway-backed sessions | Searchable memory, skills, user modeling, API-backed reuse | Tasks, skills, cron jobs, profiles | Tool-driven verification and memory reuse | CLI, messaging, MCP, and OpenAI-compatible HTTP frontends |
| [[memento-skills]] | Persistent local sessions plus per-user IM sessions and stateful prompts | Structured markdown skills, local/vector/db skill stores, and layered runtime configuration | Retrieved skills, generated skills, reflection-driven rewrites, skill market downloads | Reflection loop plus static and execution-oriented skill verification | CLI, desktop GUI, local sandbox, and IM gateway surfaces |
| [[gas-town]] | Swarm sessions across named roles | Beads in Git / Dolt | Beads, epics, molecules, formulas, wisps | Human plus role-based oversight | tmux-style orchestrator/factory |
| [[gas-city]] | Modular orchestration nodes | Beads plus Wasteland federation | Builder primitives and wanted-board exchange | Federated trust and validator roles | Custom topologies over shared protocols |
| [[openclaw]] | Persistent service runtime | Workspace files, long-lived agent state, and layered skills | Embedded runtime plus ecosystem skills and integrations | Less explicit in current corpus | Cross-channel background service with a single main workspace |

## Main architectural lesson
The important divergence is not "which model is best" but where state lives and how work is represented. Codex externalizes protocol boundaries, Claude externalizes handoff artifacts, Hermes externalizes personal memory and skills, Memento-Skills externalizes learning itself into a writable skill library, and Gas Town externalizes the work graph.

## Related pages
Read this page after [[agent-harness-anatomy]] and alongside [[orchestration-topologies]], [[memory-persistence]], and [[work-management-primitives]]. It is also the factual substrate for [[new-harness-design-notes]].
