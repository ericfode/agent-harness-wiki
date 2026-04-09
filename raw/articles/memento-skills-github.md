---
title: Memento-Skills GitHub Repository
author: Memento-Teams
url: https://github.com/Memento-Teams/Memento-Skills
ingested: 2026-04-09
---

# Memento-Skills Repository Summary

**Memento-Skills** is a Python 3.12+ agent runtime and research codebase that implements the paper's self-evolving skill-memory design. The repository is not only a benchmark release: it includes the runtime, configuration system, local sandboxing, verification commands, built-in skills, and multiple operator surfaces.

## Core repository shape

- `core/skill/` separates skill building, downloading, loading, retrieval, storage, and execution into explicit subsystems.
- `core/memento_s/phases/` and `core/protocol/` expose a staged agent pipeline rather than a single monolithic loop.
- `middleware/sandbox/` plus execution-policy modules (`tool_gate`, `path_validator`, `pre_execute`, `recovery`) make tool use an explicit control layer.
- `builtin/skills/*/SKILL.md` packages skills as markdown artifacts with metadata, scripts, and optional supporting assets.
- `tests/` covers skill retrieval, execution, downloading, storage, schema handling, and tool-security paths.

## Surfaces and operations

- CLI entrypoint: `memento`
- Desktop GUI entrypoint: `memento-gui`
- Verification command: `memento verify`
- Messaging and gateway integrations under `im/` and `middleware/im/gateway/`

## Architectural signal

The repository makes the paper's thesis concrete: skills are not static prompts pasted into context but durable packages that can be retrieved, executed, verified, downloaded, and rewritten over time. The codebase therefore belongs in this wiki as a harness artifact, not only as a benchmark attachment.
