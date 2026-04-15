---
title: MathCode: A Frontier Mathematical Coding Agent
author: GitHub
url: https://github.com/math-ai-org/mathcode
ingested: 2026-04-14
---

# MathCode Summary

MathCode is a terminal AI coding assistant aimed at mathematical formalization and proof search. Its central move is to take a natural-language math problem, translate it into a Lean 4 theorem, and then iteratively attempt a formal proof instead of stopping at prose explanation.

## Repository and release shape

- Repository: `math-ai-org/mathcode`
- GitHub description: “MathCode: A Frontier Mathematical Coding Agent”
- Created: 2026-04-02
- Default branch: `main`
- Homepage: `https://math-ai-org.github.io/mathcode`
- Snapshot at ingest: 444 stars, 43 forks, 1 open issue
- The public repository is a bootstrap checkout rather than the full implementation tree: `bash setup.sh` downloads a versioned `mathcode` release binary from GitHub Releases when the local binary is missing.

## Installation model

Quick start from the README:

```bash
git clone https://github.com/math-ai-org/mathcode.git
cd mathcode
bash setup.sh
codex auth login
./run
```

The setup script:
- downloads the matching release asset for macOS arm64 or Linux x86_64
- verifies `SHA256SUMS.txt` when `shasum` or `sha256sum` is available
- creates `.env` from `.env.example`
- bootstraps local Lean tooling when `lean` / `lake` are missing
- fetches Mathlib cache unless explicitly skipped
- creates extension directories for `skills/`, `tools/`, and `plugins/`

The script also exposes `--status` and `--clean` flows. `--clean` removes install artifacts but deliberately preserves user outputs such as `LeanFormalizations/` and vault data.

## Core proving architecture

The README describes MathCode as a coding assistant with a built-in math formalization engine. The public feature surface includes:

- Persistent Lean REPL mode (`MATHCODE_LEAN_REPL=1`) for sub-second compile checks after warmup
- Theorem library mode (`/theorem-store ...`) that stores proved theorems into `TheoremLib/Stored.lean` for later reuse
- Axiom/declaration library mode (`/axiomatize ...`) for persistent, compile-checked assumptions and declarations
- Lean LSP integration (`MATHCODE_USE_LSP=1`) for structured diagnostics plus lemma lookup via leansearch/Loogle
- Obsidian theorem-graph generation (`/obsidian ...`) that visualizes theorem dependencies as a vault
- Agent-mode proving (`MATHCODE_AGENT_PROVE=1`) with iterative compile-repair loops
- Tree-of-subgoals proving (`MATHCODE_TREE_PROVE=1`) that decomposes proofs into parallel subgoals
- Multi-planner execution (`MATHCODE_NUM_PLANNERS`) for diverse proof strategies
- Scheduled agent loops (`/loop ...`) for recurring prompts and monitoring inside interactive sessions

Math outputs are written to `LeanFormalizations/`.

## Model and backend configuration

The default backend is OpenAI / Codex OAuth. The example environment sets `OPENAI_MODEL=gpt-5.4` and `AUTOLEAN_CODEX_MODEL=gpt-5.4`, and the quick start explicitly asks the user to run `codex auth login`.

The `.env.example` also documents alternate Anthropic-compatible backends, including direct Anthropic API, AWS Bedrock, Google Vertex AI, Azure Foundry, and MiniMax. If the operator wants the math tools to stop using `codex exec`, they can set `AUTOLEAN_USE_CODEX=0`.

## Extensibility surface

MathCode exposes three repo-local extension points:

- `skills/` for markdown skills and proving guidance
- `tools/` for Python analysis tools such as `axiom_checker`, `sorry_analyzer`, `proof_stats`, and `lib_search`
- `plugins/` for commands, skills, agents, hooks, MCP servers, and related integrations

The plugin README says `.mathcode-plugin/plugin.json` manifests are the native format, but `.claude-plugin/` is also supported for compatibility with upstream Claude Code plugins.

## Requirements and constraints

- Officially documented platforms: macOS arm64 and Linux x86_64
- Python 3.12+ is only needed for some analysis tools in `tools/`
- Lean toolchain and Mathlib caches are significant enough that the setup script explicitly checks disk space and offers cache-skip controls
- The public repo is not a fully self-hosted source build of the main runtime; it bootstraps a release binary

## Acknowledgment lineage

The README states that MathCode’s math formalization and proving pipeline is based on the AUTOLEAN project.