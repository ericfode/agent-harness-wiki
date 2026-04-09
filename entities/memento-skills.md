---
title: Memento-Skills
created: 2026-04-09
updated: 2026-04-09
type: entity
tags: [memento-skills, memory, work-management]
sources: [raw/papers/arxiv-zhou-2026-memento-skills.md, raw/articles/memento-skills-github.md]
---

# Memento-Skills

## Overview
Memento-Skills is a 2026 paper and agent runtime from Memento-Teams built around a blunt claim: if an agent is going to improve after deployment, the improvement surface should be writable skill artifacts rather than repeated manual prompt edits or weight updates. The system treats skill memory as the place where learning accumulates, so a generalist agent can retrieve, repair, and generate task-specific agents through use.

## Learning model
The paper centers a read-execute-reflect-write loop over stateful prompts and structured markdown skills. A router selects relevant skills, execution runs them in a local tool environment, reflection attributes failures to concrete capabilities when possible, and write-back revises utility, prompts, or skill code. This places the system directly inside [[memory-persistence]] while also making the skill library a set of [[work-management-primitives]] rather than mere reference text.

## Runtime shape
The attached repository is a real Python runtime rather than a paper-only dump. `core/skill/` separates skill lifecycle concerns, `builtin/skills/*/SKILL.md` makes skills durable markdown packages with scripts, `middleware/sandbox/` and execution policies bound tool use, and the project ships CLI, GUI, verification, and IM gateway surfaces. Architecturally it sits between [[hermes-agent]] and [[openclaw]]: like Hermes it cares about continual self-improvement, and like OpenClaw it treats skills as first-class executable artifacts with distribution machinery.

## Strengths
- Deployment-time learning without fine-tuning the underlying model.
- Inspectable external skill artifacts instead of hidden internal adaptation.
- Clear emphasis on retrieval, verification, and skill quality as the library grows.
- Concrete operator surfaces beyond the paper: CLI, desktop GUI, local sandbox, and messaging gateways.

## Risks and limits
The same architecture inherits the usual hazards of skill-centric systems: routing mistakes, stale low-quality skills, and additional supply-chain surface once skills can be downloaded or shared. The public material is also more research-forward than protocol-clean, so it currently says less about crisp operator boundaries than [[codex-cli]] or [[codex-app-server]].

## Relationships
Read Memento-Skills with [[memory-persistence]], [[work-management-primitives]], [[harness-engineering]], and [[safety-and-permissions]]. It is especially useful as a contrast class beside [[hermes-agent]], [[openclaw]], and the system table in [[harness-architecture-comparison]].
