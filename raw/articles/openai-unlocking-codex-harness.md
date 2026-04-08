---
title: Unlocking the Codex Harness
author: OpenAI
url: https://openai.com/index/unlocking-the-codex-harness/
date: 2026-02-04
ingested: 2026-04-07
---

# Unlocking the Codex Harness: Building the App Server

**Source:** [OpenAI](https://openai.com/index/unlocking-the-codex-harness/)
**Date:** February 4, 2026
**Topic:** Engineering the infrastructure behind OpenAI’s coding agent, Codex.

---

## 1. Overview: The Codex App Server
The **Codex App Server** is the critical link between the core Codex "harness" (the agent loop and logic) and various user interfaces (Web, CLI, IDEs, macOS app). It is a client-friendly, bidirectional **JSON-RPC API** designed to allow different products to reuse the same agent logic without re-implementation.

### Key Responsibilities of the Harness
- **Thread Lifecycle:** Managing conversation persistence, forking, and archiving.
- **Config & Auth:** Handling "Sign in with ChatGPT" and credential states.
- **Tool Execution:** Running shell/file tools in sandboxes and integrating MCP (Model Context Protocol) servers.

---

## 2. Architecture & Protocol
The App Server acts as a long-lived process hosting **Codex core threads**. It translates low-level internal events into stable, UI-ready JSON-RPC notifications.

### The Three Conversation Primitives
To handle complex agent interactions (beyond simple request/response), the protocol uses:
1. **Item:** The atomic unit of I/O (e.g., user message, tool execution, diff).
   - *Lifecycle:* `item/started` → `item/*/delta` (streaming) → `item/completed`.
2. **Turn:** A single unit of work initiated by user input. It contains a sequence of items.
3. **Thread:** The durable container for the session, persisting history across reconnections.

### The Initialization Handshake
Clients must send an `initialize` request to agree on versioning and capabilities.
**Example Request:**
```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}
```

---

## 3. Integration Patterns
The App Server uses **JSON-RPC over stdio (JSONL)**. Developers can generate bindings for various languages:

- **TypeScript:** `codex app-server generate-ts`
- **Other Languages:** `codex app-server generate-json-schema` (for use with code generators).

### Implementation by Surface
| Surface | Implementation Detail |
| :--- | :--- |
| **Local Apps/IDEs** | Bundles a platform-specific binary; launches it as a child process with a bidirectional stdio channel. |
| **Codex Web** | Runs in a container; the web app communicates via HTTP/SSE to a worker that maintains the App Server session. |
| **TUI / CLI** | Moving toward the App Server model to allow remote connections (keeping the agent close to compute). |

---

## 4. Choosing the Right Integration Method
OpenAI recommends the **App Server** for most use cases, but provides alternatives:

- **Codex App Server:** Best for full harness functionality, UI-friendly streaming, and stable session management.
- **Codex as MCP Server:** Best if you already use an MCP-based workflow and want to call Codex as a tool.
- **Codex Exec:** A lightweight CLI mode for one-off tasks and CI/CD pipelines.
- **Codex SDK:** A TypeScript library for programmatic control (currently has a smaller surface area than the App Server).

---

## 5. Actionable Insights for Developers
- **Bidirectional Communication:** The server can initiate requests (e.g., asking for user approval to run a command), pausing the agent turn until the client responds.
- **Backward Compatibility:** The JSON-RPC surface is designed so older clients can safely interact with newer server binaries, allowing for server-side improvements without breaking integrations.
- **Debugging:** Developers can test the protocol using the debug command:
  ```bash
  codex debug app-server send-message-v2 "run tests and summarize failures"
  ```
- **Open Source:** The source code and documentation are available in the [Codex CLI repository](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md).
