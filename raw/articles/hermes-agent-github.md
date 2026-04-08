---
title: Hermes Agent
author: GitHub
url: https://github.com/nousresearch/hermes-agent
ingested: 2026-04-07
---

# Hermes Agent Summary

**Hermes Agent** is a self-improving AI agent developed by **Nous Research**. It is designed with a built-in learning loop that allows it to create and improve skills from experience, maintain persistent knowledge across sessions, and operate across multiple platforms (CLI, Telegram, Discord, etc.) from a single gateway.

## Quick Start & Installation

The installer supports **Linux, macOS, and WSL2**. It automatically handles Python, Node.js, and all necessary dependencies.

### One-Line Install
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### Post-Installation
```bash
source ~/.bashrc
hermes
```

---

## Key Features & Capabilities

- **Closed Learning Loop:** Curates its own memory, creates autonomous skills after complex tasks, and uses Honcho for dialectic user modeling.
- **Multi-Platform Gateway:** A single process supports Telegram, Discord, Slack, WhatsApp, Signal, and Email with cross-platform conversation continuity.
- **Flexible Model Support:** Compatible with Nous Portal, OpenRouter (200+ models), OpenAI, Anthropic, Gemini, and custom endpoints.
- **Advanced Terminal Backends:** Runs in Local, Docker, SSH, Daytona, Singularity, or Modal. Modal/Daytona allow the environment to hibernate when idle to save costs.
- **Scheduled Automations:** Built-in cron scheduler for natural language reports, backups, and audits delivered to your preferred platform.
- **Research-Ready:** Includes batch trajectory generation and RL environments (Atropos) for training future tool-calling models.

---

## CLI & Messaging Commands

| Action | Command / Slash Command |
| :--- | :--- |
| **Start Fresh** | `/new` or `/reset` |
| **Change Model** | `hermes model` (CLI) or `/model [provider:model]` |
| **Configure Tools** | `hermes tools` |
| **Check Usage** | `/usage` or `/insights [--days N]` |
| **Stop Work** | `Ctrl+C` (CLI) or `/stop` (Messaging) |
| **Update Agent** | `hermes update` |
| **Diagnostics** | `hermes doctor` |

---

## Repository Structure & Technical Details

- **`agent/`**: Core logic, memory management, and provider adapters.
- **`gateway/`**: Platform-specific adapters and message routing.
- **`tools/`**: Built-in tools including browser, file operations, and code execution.
- **`skills/`**: Procedural memory and skill management.
- **`cron/`**: Logic for scheduled natural language tasks.
- **`nix/`**: Nix flake and NixOS module for hardened, reproducible deployments.

### Recent Technical Updates (v0.7.0)
- **Pluggable Memory:** Support for various memory providers (Honcho, Supermemory, etc.).
- **Camofox Browser:** Added a local anti-detection browser backend to bypass bot detection without API costs.
- **Structured Reasoning:** Improved handling for models that produce reasoning-only responses.
- **Profiles:** Support for multiple isolated instances with independent configs and memories.

---

## Migration from OpenClaw
Hermes provides a migration path for users moving from OpenClaw. It imports personas (`SOUL.md`), memories, user-created skills, and API keys.

```bash
hermes claw migrate
hermes claw migrate --dry-run
```

---

## Contributing & Community
- **Language:** Primarily Python.
- **Development Setup:** Uses `uv` for dependency management and virtual environments.
- **RL Training:** Optional integration with `tinker-atropos` submodule.
- **Links:** Documentation, Discord, and MIT License are provided in the repository.
