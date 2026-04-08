---
title: OpenAI Codex CLI: Lightweight Terminal Coding Agent
author: GitHub
url: https://github.com/openai/codex
ingested: 2026-04-07
---

# OpenAI Codex CLI: Lightweight Terminal Coding Agent

**Codex CLI** is an official OpenAI coding agent designed to run locally in your terminal. It provides a lightweight, command-line-driven alternative to IDE-based agents like Cursor or Windsurf.

## Quickstart & Installation

You can install Codex CLI via package managers or by downloading standalone binaries.

### Installation Commands
```bash
# Install using npm
npm install -g @openai/codex

# Install using Homebrew
brew install --cask codex
```

### Manual Binary Selection
For manual installation, download the appropriate executable from the [latest GitHub Release](https://github.com/openai/codex/releases/latest):
- **macOS:** `codex-aarch64-apple-darwin.tar.gz` (Apple Silicon) or `codex-x86_64-apple-darwin.tar.gz` (Intel).
- **Linux:** `codex-x86_64-unknown-linux-musl.tar.gz` or `codex-aarch64-unknown-linux-musl.tar.gz`.
- *Note: Rename the extracted file to `codex` for easier use.*

## Authentication & Plans
Codex is designed to work with existing ChatGPT subscriptions.
- **ChatGPT Plans:** Supports Plus, Pro, Business, Edu, and Enterprise.
- **Sign-in:** Run `codex` and select **Sign in with ChatGPT**.
- **API Key:** Can be used with an API key, though this requires additional setup.

## Key Features & Technical Insights

### Core Capabilities
- **Terminal-Native:** Runs directly in the shell for fast, low-friction coding assistance.
- **Experimental JS REPL:** Includes a feature-gated `js_repl` tool allowing models to execute JavaScript in a persistent context across tool calls.
  - *Enable via config:* `[features] js_repl = true`
- **Hooks Engine:** Supports `SessionStart` and `Stop` hooks that run synchronously to provide context (appended to the user's prompt).

### Technical Architecture
- **Languages:** Primarily **Rust (94.8%)**, with supporting code in Python, TypeScript, and Starlark.
- **Build System:** Uses **Bazel 9** and **pnpm** for monorepo management.
- **Cross-Platform Support:** Extensive recent work has been done to ensure CI parity for Windows (using `windows-gnullvm` and MSVC host toolchains).

## Repository Structure
| Path | Description |
| :--- | :--- |
| `codex-cli/` | The main CLI implementation. |
| `codex-rs/` | Core Rust logic, including tools and schema tests. |
| `sdk/` | SDK for interacting with OpenAI services. |
| `agents.md` | Guidelines for agent development and module visibility. |
| `patches/` | Local patches for dependencies like `rules_rust`, `v8`, and `aws-lc-sys`. |

## Documentation & Resources
- [**Official Documentation**](https://developers.openai.com/codex)
- [**Contributing Guide**](https://github.com/openai/codex/blob/main/docs/contributing.md)
- [**Security Policy**](https://github.com/openai/codex/blob/main/SECURITY.md): Reports should be directed via Bugcrowd.
- **License:** [Apache-2.0](https://github.com/openai/codex/blob/main/LICENSE).

For the web-based experience, visit [chatgpt.com/codex](https://chatgpt.com/codex). For IDE integration, see the OpenAI Codex IDE setup docs.
