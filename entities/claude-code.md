---
title: Claude Code
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [claude-code, subagents, context-engineering]
sources: [raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-three-agent-harness-infoq.md]
---

# Claude Code

## Overview
Claude Code is Anthropic's coding agent surface, but the more interesting contribution here is the harness research around it: initializer phases, structured handoff artifacts, evaluator agents, and context resets. In other words, Claude Code is not only a worker; it is also a small literature review on why long-running workers go strange.

## Long-running workflow
Anthropic's effective-harnesses work proposes a pragmatic two-stage recovery strategy: an initializer session prepares the environment and durable state files; later coding sessions read those artifacts, verify the project still runs, and then advance one feature at a time. This is a direct answer to the failure modes cataloged in [[context-engineering]] and [[memory-persistence]].

## Three-agent harness pattern
Anthropic's later harness-design work separates planner, generator, and evaluator. The evaluator uses browser automation and explicit criteria, which is the important part. Agents are not naturally stern critics of their own work; one must introduce a second mind whose job is to be unimpressed. See [[evaluation-and-review-loops]], [[harness-architecture-comparison]], and [[harness-quality-comparison]].

## Strengths
- Strong treatment of context resets and resumable work.
- Serious emphasis on structured state artifacts such as feature lists and progress logs.
- Better explicit QA loop than a naive single-agent prompt.
- Good fit for UI-heavy or long-running app development where evaluation must happen against a live system.

## Weaknesses and limits
The harness is heavier and more expensive than a solo-agent loop. It also relies on externalized artifacts and tool-equipped evaluators; without those, it degrades toward the usual premature-victory behavior.

## Relationships
Claude Code connects most directly to [[context-engineering]], [[work-management-primitives]], and [[harness-engineering]]. It is also one of the main comparands in [[harness-architecture-comparison]].
