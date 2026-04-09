---
title: Instruction Layering
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [context-engineering, memory, safety]
sources: [raw/articles/openai-harness-engineering.md, raw/articles/anthropic-claude-code-memory.md, raw/articles/anthropic-claude-code-settings.md, raw/articles/hermes-agent-memory-docs.md, raw/articles/openclaw-agent-runtime-docs.md]
---

# Instruction Layering

## Definition
Instruction layering is the practice of separating durable guidance into explicit scopes instead of shoving every rule into the current prompt. A serious harness usually has repo-level instructions, project or workspace instructions, user-specific preferences, and sometimes managed policy above all of them.

## Representative patterns
[[codex-cli]] favors progressive disclosure through `AGENTS.md` and linked repo docs. [[claude-code]] formalizes scoped `CLAUDE.md` files plus managed settings and auto memory. [[hermes-agent]] uses `MEMORY.md` and `USER.md` as durable context files. [[openclaw]] goes further by injecting workspace bootstrap files such as `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `BOOTSTRAP.md`.

## Why layers matter
When everything lives in one giant prompt, the harness cannot distinguish architecture rules from personal preferences, or policy from project context. Layering makes override rules legible, keeps recurring guidance recoverable across sessions, and reduces the temptation to treat the transcript as the only source of truth.

## Design tension
Instruction layers are adjacent to memory but not identical to it. Some layers are operational policy, some are workspace bootstrap context, and some are long-term user or project memory. Confusing them produces brittle systems that either forget too much or obey stale guidance too confidently. See [[context-engineering]], [[memory-persistence]], and [[safety-and-permissions]].

## Related pages
This page belongs with [[context-engineering]], [[memory-persistence]], [[harness-engineering]], [[claude-code]], and [[openclaw]].
