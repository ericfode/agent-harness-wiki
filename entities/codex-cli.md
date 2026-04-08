---
title: Codex CLI
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [codex-cli, tool-execution, context-engineering]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/codex-cli-github.md]
---

# Codex CLI

## Overview
Codex CLI is OpenAI's terminal-native coding agent. In this wiki, it matters less as a chat surface than as a reference design for a deliberately separable harness: the agent loop can be reused across CLI, IDE, web, and app clients via the [[harness-architecture-comparison|App Server pattern]].

## Architecture highlights
The most distinctive architectural move is the App Server: a long-lived JSON-RPC process that hosts durable threads and exposes UI-friendly notifications. The protocol distinguishes items, turns, and threads, which is a cleaner decomposition than treating a session as a flat transcript. It also gives Codex a principled story for approvals, tool invocation, and reconnectable clients. See [[harness-engineering]], [[context-engineering]], and [[safety-and-permissions]].

## Engineering discipline
OpenAI's broader harness-engineering writeup frames Codex as part of a larger practice: build the scaffolding, encode repo knowledge into markdown, and make violations mechanically legible to the agent. The code is mostly Rust, which is not morally superior, merely refreshingly unwilling to tolerate vague boundaries. That helps.

## Strengths
- Strong separation between harness core and client surfaces.
- Clear protocol surface for tools, approvals, and session state.
- A repo discipline that treats `AGENTS.md`, plans, and linters as first-class harness machinery.
- Good fit for local or remote execution where the agent should live near compute.

## Weaknesses and limits
Codex's public materials emphasize harness shape and implementation rigor more than persistent personal memory. It is excellent at being an agentic coding runtime; it is less obviously designed as a lifelong assistant in the [[hermes-agent]] sense.

## Relationships
Codex CLI is best read alongside [[harness-engineering]], [[context-engineering]], [[safety-and-permissions]], and [[harness-quality-comparison]]. Its App Server model is one of the central comparison points in [[harness-architecture-comparison]].
