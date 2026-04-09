---
title: Codex App Server README
author: GitHub
url: https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
ingested: 2026-04-07
---

# Codex App Server README

**Source:** [openai/codex GitHub repository](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md)
**Topic:** Canonical implementation documentation for the Codex App Server protocol.

---

## 1. Durable session protocol
The README defines the App Server as the persistent boundary between Codex core and clients. It exposes a structured protocol with `thread/start`, `thread/resume`, and `thread/fork`, plus durable thread identifiers rather than a flat transcript model.

## 2. Rich turn and item lifecycle
The protocol distinguishes threads, turns, and items, with evented notifications for progress and streaming updates. This gives clients a principled way to observe tool calls, diffs, and review work.

## 3. Reviews and approvals
The README documents explicit review flows such as `review/start` and approval requests that pause work until the client responds. This confirms that review and permission handling are first-class protocol concerns rather than UI hacks.

## 4. Tool and file operations
The surface covers command execution, filesystem operations, and configuration negotiation during initialization. In other words, the App Server is not merely a chat transport; it is the operational control plane for Codex sessions.
