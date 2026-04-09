---
title: Codex CLI
created: 2026-04-07
updated: 2026-04-09
type: entity
tags: [codex-cli, tool-execution, context-engineering]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/openai-introducing-codex-app.md, raw/articles/openai-codex-app-server-readme.md, raw/articles/codex-cli-github.md]
formal:
  harness_id: codex_cli
  session_model: thread_turn_item
  memory_model: repo_artifacts
  work_model: plans
  evaluation_model: repo_checks
  surface_model: cli_ide_web_protocol
  topology: single_session
  work_primitives: [plan, automation]
  surfaces: [cli, terminal, ide, web, app, cloud, sdk, slack]
  durable_stores: [repo_artifacts, shared_client_state, transcript]
  evaluation_primitives: [self_review, repo_check, tool_observation]
  coordination_roles: [generator, reviewer]
  explicit_protocol_boundary: true
  fresh_session_resets: false
  skill_learning: false
  observability_hooks: true
---

# Codex CLI

## Overview
Codex CLI is OpenAI's terminal-native entrypoint into a broader Codex agent system. In this wiki, it matters less as an isolated shell tool than as one surface over a reusable harness that now spans CLI, IDE, web, app, and cloud workflows via the [[codex-app-server]] and shared configuration model.

## Architecture highlights
The most distinctive architectural move is the [[codex-app-server]]: a long-lived process that hosts durable threads and exposes UI-friendly notifications. The protocol distinguishes items, turns, and threads, which is a cleaner decomposition than treating a session as a flat transcript. OpenAI's newer product material extends that architecture into multi-agent app workflows with worktrees, diff review, skills, and automations. See [[harness-engineering]], [[context-engineering]], and [[safety-and-permissions]].

## Engineering discipline
OpenAI's broader harness-engineering writeup frames Codex as part of a larger practice: build the scaffolding, encode repo knowledge into markdown, and make violations mechanically legible to the agent. The CLI inherits that discipline, but the newer Codex app material makes clear that the same worldview now governs parallel-agent supervision and recurring background work as well. In other words, Codex treats [[instruction-layering]] and [[automation-and-background-work]] as product features, not only as operator folklore.

## Strengths
- Strong separation between harness core and client surfaces.
- Clear protocol surface for tools, approvals, reviews, and session state.
- A repo discipline that treats `AGENTS.md`, plans, and linters as first-class harness machinery.
- Good fit for local or remote execution where the agent should live near compute, but still move across surfaces.

## Weaknesses and limits
Codex's public materials still emphasize harness shape and implementation rigor more than persistent personal memory. It is excellent at being an agentic coding runtime and command center; it is less obviously designed as a lifelong assistant in the [[hermes-agent]] sense.

## Relationships
Codex CLI is best read alongside [[codex-app-server]], [[instruction-layering]], [[automation-and-background-work]], [[harness-engineering]], [[context-engineering]], [[safety-and-permissions]], and [[harness-quality-comparison]]. Its App Server model is one of the central comparison points in [[harness-architecture-comparison]].
