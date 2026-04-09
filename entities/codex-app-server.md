---
title: Codex App Server
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [codex-cli, tool-execution, context-engineering]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-introducing-codex-app.md, raw/articles/openai-codex-app-server-readme.md]
---

# Codex App Server

## Overview
The Codex App Server is the long-lived protocol boundary between Codex core and its client surfaces. It matters because OpenAI is no longer describing Codex as merely a terminal tool; the App Server is what lets the same runtime power the CLI, IDE, web, and app experiences without each client inventing its own harness.

## Core protocol model
The central decomposition is threads, turns, and items. That sounds dry, but it is the real architectural move: sessions become durable containers with explicit work units, resumable history, and UI-visible lifecycle events rather than one giant transcript blob. See [[codex-cli]], [[agent-harness-anatomy]], and [[context-engineering]].

## Reviews and approvals
The App Server surface includes approval requests and review flows, which means permission handling and code review are first-class protocol concerns. This places Codex closer to a controllable operating substrate than to a thin text-generation shell. Read with [[evaluation-and-review-loops]] and [[safety-and-permissions]].

## Why it matters
The App Server is the cleanest statement of OpenAI's harness philosophy in this corpus: separate the agent core from the client surfaces, make session state durable, and express operational control through a stable interface. It is one of the main reasons [[codex-cli]] is useful as a reference architecture rather than only as a product.

## Relationships
This page belongs with [[codex-cli]], [[harness-engineering]], [[harness-architecture-comparison]], and [[new-harness-design-notes]].
