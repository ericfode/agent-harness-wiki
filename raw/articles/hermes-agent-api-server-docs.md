---
title: API Server
author: Nous Research
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/
ingested: 2026-04-07
---

# Hermes Agent API Server

**Source:** [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/)
**Topic:** Hermes as an OpenAI-compatible backend service.

---

## 1. OpenAI-compatible endpoint
Hermes exposes itself as an OpenAI-compatible HTTP API so third-party frontends can use it as a backend.

## 2. Full tool-backed runtime behind the API
The docs say API requests are handled by the full Hermes toolset, including terminal access, file operations, web search, memory, and skills. This is not only a chat wrapper; it is the agent runtime surfaced over HTTP.

## 3. Gateway-centered architecture
The API server is enabled through the Hermes gateway and advertises standard endpoints such as `/v1/chat/completions`, `/v1/responses`, `/v1/models`, and `/health`.
