---
title: Agent Runtime
author: OpenClaw
url: https://docs.openclaw.ai/concepts/agent
ingested: 2026-04-07
---

# OpenClaw Agent Runtime

**Source:** [OpenClaw docs](https://docs.openclaw.ai/concepts/agent)
**Topic:** OpenClaw’s runtime, workspace, injected files, and session storage.

---

## 1. Single embedded runtime
OpenClaw documents itself as running a single embedded agent runtime with OpenClaw-owned session, discovery, tool, and delivery layers around the core.

## 2. Workspace as operating substrate
The runtime expects one main workspace directory as the agent’s working directory. Within it, OpenClaw injects bootstrap and profile files such as `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, and `USER.md`.

## 3. Skills and layered precedence
The docs define several skill-loading locations, including workspace skills, project `.agents/skills`, personal `~/.agents/skills`, managed skills, bundled skills, and extra directories.

## 4. JSONL session storage
Session transcripts are stored as JSONL files under the agent’s state directory. This confirms that OpenClaw’s persistence model is a concrete runtime and workspace discipline, not only a marketplace story.
