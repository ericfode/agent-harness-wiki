---
title: Claude Code
created: 2026-04-07
updated: 2026-04-09
type: entity
tags: [claude-code, subagents, context-engineering]
sources: [raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-three-agent-harness-infoq.md, raw/articles/anthropic-claude-code-overview.md, raw/articles/anthropic-claude-code-memory.md, raw/articles/anthropic-claude-code-settings.md, raw/articles/anthropic-claude-code-subagents.md, raw/articles/anthropic-claude-code-agent-teams.md, raw/articles/anthropic-claude-code-scheduled-tasks.md]
formal:
  harness_id: claude_code
  session_model: fresh_session_handoff
  memory_model: repo_artifacts
  work_model: sprint_contracts
  evaluation_model: separate_evaluator
  surface_model: coding_surface
  topology: session_team
  work_primitives: [sprint_contract, feature_list, progress_log, automation]
  surfaces: [terminal, ide, desktop, browser]
  durable_stores: [repo_artifacts, transcript]
  evaluation_primitives: [separate_evaluator, tool_observation, ci_review, browser_evaluation]
  coordination_roles: [planner, generator, evaluator, reviewer]
  explicit_protocol_boundary: false
  fresh_session_resets: true
  skill_learning: false
  observability_hooks: true
---

# Claude Code

## Overview
Claude Code is Anthropic's broader agentic coding system, available across terminal, IDE, desktop app, and browser surfaces. The more interesting contribution remains the harness research around it: structured handoff artifacts, evaluator agents, scoped memory, hooks, and explicit policy controls for long-running work.

## Long-running workflow
Anthropic's effective-harnesses work proposes a pragmatic two-stage recovery strategy: an initializer session prepares the environment and durable state files; later coding sessions read those artifacts, verify the project still runs, and then advance one feature at a time. The newer product docs make the same philosophy concrete through `CLAUDE.md`, auto memory, session transfer across surfaces, and scheduled work. This is a direct answer to the failure modes cataloged in [[context-engineering]], [[memory-persistence]], and [[instruction-layering]].

## Orchestration modes
Anthropic now documents at least three distinct coordination modes. Subagents are specialized workers inside one session, each with its own context window, tool profile, and optional persistent memory. Agent teams are heavier: multiple Claude Code sessions with a lead, direct teammate messaging, and shared task coordination. Scheduled tasks are yet another mode, with `/loop` for session-scoped polling and separate cloud or desktop scheduling for work that must survive restarts. This makes [[claude-code]] one of the clearest exemplars of explicit [[orchestration-topologies]] in the current corpus.

## Three-agent harness pattern
Anthropic's later harness-design work separates planner, generator, and evaluator. The evaluator uses browser automation and explicit criteria, which is the important part. The current docs extend that logic with first-class subagents, hooks, and CI/review integrations. Agents are not naturally stern critics of their own work; one must introduce a second mind, or at least a second boundary, whose job is to be unimpressed. See [[evaluation-and-review-loops]], [[agent-harness-anatomy]], [[harness-architecture-comparison]], and [[harness-quality-comparison]].

## Strengths
- Strong treatment of context resets and resumable work.
- Serious emphasis on structured state artifacts, persistent instruction files, and auto memory.
- Better explicit QA loop than a naive single-agent prompt.
- First-class support for hooks, MCP, subagents, agent teams, and cross-surface continuation.
- Good fit for UI-heavy or long-running app development where evaluation must happen against a live system.

## Weaknesses and limits
The harness is heavier and more expensive than a solo-agent loop. It also relies on externalized artifacts, policy configuration, and tool-equipped evaluators; without those, it degrades toward the usual premature-victory behavior. Anthropic's own docs also mark agent teams as experimental and acknowledge coordination and shutdown rough edges.

## Relationships
Claude Code connects most directly to [[context-engineering]], [[instruction-layering]], [[memory-persistence]], [[automation-and-background-work]], [[orchestration-topologies]], [[work-management-primitives]], and [[harness-engineering]]. It is also one of the main comparands in [[harness-architecture-comparison]].
