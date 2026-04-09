---
title: Hermes Agent
created: 2026-04-07
updated: 2026-04-09
type: entity
tags: [hermes-agent, memory, safety]
sources: [raw/articles/hermes-agent-github.md, raw/articles/hermes-agent-memory-docs.md, raw/articles/hermes-agent-api-server-docs.md, raw/articles/newstack-openclaw-vs-hermes.md]
formal:
  harness_id: hermes_agent
  session_model: persistent_conversation
  memory_model: searchable_personal_memory
  work_model: tasks_skills_cron
  evaluation_model: tool_verification
  surface_model: cli_gateway_mcp
  topology: service_hub
  work_primitives: [task, skill, cron_job]
  surfaces: [cli, messaging, mcp, http_api]
  durable_stores: [searchable_memory, service_workspace, session_database]
  evaluation_primitives: [tool_observation]
  coordination_roles: [generator, reviewer, memory_manager, scheduler]
  explicit_protocol_boundary: false
  fresh_session_resets: false
  skill_learning: true
  observability_hooks: true
---

# Hermes Agent

## Overview
Hermes Agent is a persistent, self-improving agent runtime from Nous Research. Its signature idea is a closed learning loop: preserve useful facts, turn repeated procedures into skills, and make future runs slightly less foolish than the last. The current docs make that story broader than the old repository snapshot: Hermes is memory system, tool runtime, automation engine, and API surface all at once.

## Memory and learning model
Hermes combines durable session memory with summarization and searchable recall. The current docs sharpen that into explicit `MEMORY.md` and `USER.md` files plus searchable session history in SQLite. Add skill creation, profiles, and scheduled automation, and Hermes sits near the center of [[memory-persistence]] rather than only in the coding-agent lane.

## Runtime surface
Hermes spans CLI, messaging platforms, cron tasks, MCP serving, an OpenAI-compatible API server, and multiple terminal backends. That breadth makes it architecturally different from [[codex-cli]] or [[claude-code]], which are primarily coding-agent surfaces. Hermes is closer to a personal operating environment with coding as one mode among several, which makes it one of the clearer exemplars of [[automation-and-background-work]] in this corpus.

## Strengths
- Durable cross-session memory and recall.
- Autonomous skill creation from successful procedures.
- Multi-platform gateway and profile isolation.
- OpenAI-compatible API surface for reusing the full agent runtime behind other frontends.
- Safety-oriented execution features such as pre-execution scanning and hardened deployment paths.

## Weaknesses and limits
Relative to [[openclaw]], Hermes is less ecosystem-maximal. Relative to [[codex-cli]], its public materials emphasize learning loops and tooling breadth more than a clean protocol architecture. The charm is depth, not tidiness.

## Relationships
Hermes Agent should be read with [[instruction-layering]], [[memory-persistence]], [[automation-and-background-work]], [[work-management-primitives]], [[safety-and-permissions]], and [[harness-architecture-comparison]]. It is one of the poles in [[harness-quality-comparison]] when the evaluation criterion is durable usefulness rather than only code-generation throughput.
