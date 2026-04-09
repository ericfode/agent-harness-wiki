---
title: Automation and Background Work
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [work-management, orchestration, tool-execution]
sources: [raw/articles/openai-introducing-codex-app.md, raw/articles/openai-codex-chatgpt-plan.md, raw/articles/anthropic-claude-code-overview.md, raw/articles/anthropic-claude-code-scheduled-tasks.md, raw/articles/hermes-agent-github.md]
---

# Automation and Background Work

## Definition
Automation and background work are the harness capabilities that let agents execute tasks outside the narrow rhythm of a live chat turn. The common pattern is simple: define a job, let it run later or elsewhere, and return the result to a review surface instead of pretending the user must supervise every keystroke in real time.

## Representative models
[[codex-cli]] now participates in this through Codex app automations, cloud-delegated background tasks, and automatic GitHub review. [[claude-code]] documents recurring tasks, CI usage, and remote-control flows as part of the main product story rather than as side experiments; its scheduling docs also distinguish durable cloud or desktop tasks from session-scoped `/loop` jobs. [[hermes-agent]] treats cron-style natural-language automations as a core feature of the runtime.

## What background work requires
- Durable state so the job can start without relying on a warm transcript.
- Clear work objects and destinations, which is why this topic overlaps with [[work-management-primitives]].
- Explicit execution locality: some jobs run in a fresh cloud clone, some on a local machine, and some only inside a live session.
- A review or inbox surface where results can be inspected before the system quietly compounds its own mistakes.
- Permission boundaries suitable for unattended execution, because an agent running later is still an agent with tools now.

## Design lesson
Background execution turns a harness from an interactive helper into an operating system for delegated work. That is powerful, but it also means automation quality depends on [[context-engineering]], [[evaluation-and-review-loops]], [[safety-and-permissions]], and the chosen [[orchestration-topologies]] rather than on model cleverness alone.

## Related pages
Read this with [[work-management-primitives]], [[evaluation-and-review-loops]], [[orchestration-topologies]], [[codex-cli]], [[claude-code]], and [[hermes-agent]].
