---
title: OpenClaw
created: 2026-04-07
updated: 2026-04-09
type: entity
tags: [openclaw, memory, safety]
sources: [raw/articles/openclaw-agent-runtime-docs.md, raw/articles/newstack-openclaw-vs-hermes.md]
formal:
  harness_id: openclaw
  session_model: service_runtime
  memory_model: service_state
  work_model: ecosystem_skills
  evaluation_model: tool_verification
  surface_model: multi_channel_service
  topology: service_hub
  work_primitives: [task, ecosystem_skill]
  surfaces: [cli, messaging, web, app]
  durable_stores: [service_workspace, workspace_files, transcript]
  evaluation_primitives: [tool_observation]
  coordination_roles: [generator, reviewer, scheduler]
  explicit_protocol_boundary: false
  fresh_session_resets: false
  skill_learning: true
  observability_hooks: true
---

# OpenClaw

## Overview
OpenClaw is a persistent agent runtime optimized for breadth: many integrations, many models, many surfaces, and a large public skill ecosystem. The current docs clarify that this breadth sits on top of a concrete runtime discipline: one main workspace, injected bootstrap files, layered skills, and JSONL session storage. In this wiki, it remains the ecosystem-first counterpoint to [[hermes-agent]].

## Integration model
The current docs present OpenClaw as a single embedded agent runtime wrapped by OpenClaw-owned session, delivery, and discovery layers. The required workspace files (`AGENTS.md`, `SOUL.md`, `TOOLS.md`, `BOOTSTRAP.md`, and friends) make it architecturally interesting even apart from coding: it treats presence, persona, and workspace bootstrapping as first-class harness capabilities. See [[agent-harness-anatomy]], [[memory-persistence]], and [[instruction-layering]].

## Strengths
- Exceptional surface-area breadth.
- Large public skill marketplace and community energy.
- Explicit workspace and session model under the ecosystem story.
- Strong fit for users who want one runtime to be reachable from everywhere.

## Risks
The same source also emphasizes serious security concerns: malicious skill entries, supply-chain risk, and unsafe websocket behavior. OpenClaw is therefore a useful object lesson in [[safety-and-permissions]].

## Relationships
OpenClaw is best read against [[hermes-agent]], [[instruction-layering]], [[memory-persistence]], and [[safety-and-permissions]]. It appears in both [[harness-quality-comparison]] and [[harness-architecture-comparison]] as the ecosystem-maximal pole.
