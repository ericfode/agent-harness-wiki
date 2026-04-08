---
title: Hermes Agent
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [hermes-agent, memory, safety]
sources: [raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md]
---

# Hermes Agent

## Overview
Hermes Agent is a persistent, self-improving agent runtime from Nous Research. Its signature idea is a closed learning loop: preserve useful facts, turn repeated procedures into skills, and make future runs slightly less foolish than the last. A modest ambition, but civilized.

## Memory and learning model
Hermes combines durable session memory with summarization and searchable recall. The New Stack comparison emphasizes FTS5-backed persistence; the repository overview adds skill creation, profiles, and scheduled automation. This places Hermes near the center of [[memory-persistence]] rather than only in the coding-agent lane.

## Runtime surface
Hermes spans CLI, messaging platforms, cron tasks, MCP serving, and multiple terminal backends. That breadth makes it architecturally different from [[codex-cli]] or [[claude-code]], which are primarily coding-agent surfaces. Hermes is closer to a personal operating environment with coding as one mode among several.

## Strengths
- Durable cross-session memory and recall.
- Autonomous skill creation from successful procedures.
- Multi-platform gateway and profile isolation.
- Safety-oriented execution features such as pre-execution scanning and hardened deployment paths.

## Weaknesses and limits
Relative to [[openclaw]], Hermes is less ecosystem-maximal. Relative to [[codex-cli]], its public materials emphasize learning loops and tooling breadth more than a clean protocol architecture. The charm is depth, not tidiness.

## Relationships
Hermes Agent should be read with [[memory-persistence]], [[work-management-primitives]], [[safety-and-permissions]], and [[harness-architecture-comparison]]. It is one of the poles in [[harness-quality-comparison]] when the evaluation criterion is durable usefulness rather than only code-generation throughput.
