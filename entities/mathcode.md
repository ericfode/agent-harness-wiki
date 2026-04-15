---
title: MathCode
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [mathcode, formal-methods, tool-execution]
sources: [raw/articles/math-ai-org-mathcode-github.md]
---

# MathCode

## Overview
MathCode is a terminal-native mathematical coding agent that routes natural-language math problems into Lean 4 theorems and then tries to close them with an explicit proof workflow. In harness terms, it is interesting because it does not treat formalization as a post-hoc ceremonial flourish; the formal proof environment is the main work surface. That makes it a concrete implementation of ideas developed more abstractly in [[theorem-proving-as-cognitive-kernel]] and [[formal-cognition-loop]].

## Architecture highlights
The public repository is a lightweight bootstrap layer: `bash setup.sh` downloads a versioned MathCode binary from GitHub Releases, bootstraps Lean locally, fetches Mathlib cache, and creates extension directories for skills, tools, and plugins. The runtime surface then layers several formal-workflow features on top of a terminal agent shell: persistent Lean REPL checks, Lean LSP integration, theorem and axiom libraries, agent-mode compile-repair proving, tree-of-subgoals decomposition, and optional Obsidian theorem-graph generation. The resulting shape is not merely “an LLM with Lean attached,” but a harness that tries to make the proof state, theorem store, and declaration store durable working memory.

## Why it matters
MathCode is a useful data point for the harness wiki because it shows what happens when a coding agent specializes around a narrow but serious formal space. It operationalizes the claim that some tasks should be pushed into a sterner substrate than chat prose. Relative to more general systems such as [[codex-cli]], MathCode is narrower in domain but clearer about the value of proof-state-grounded iteration, lemma retrieval, and stored formal artifacts.

## Extensibility and workflow surface
MathCode exposes repo-local `skills/`, `tools/`, and `plugins/` directories, plus a plugin manifest format that can also read `.claude-plugin/` layouts for compatibility. It also ships scheduled `/loop` commands, so the proving environment is not just a one-shot theorem transcriber. There is a small but notable work-management layer here: recurring prompts, stored theorems, stored declarations, and generated Obsidian vaults all behave like durable artifacts rather than ephemeral chat residue. Read that alongside [[memory-persistence]] and [[work-management-primitives]].

## Strengths
- Treats Lean formalization and proof search as the primary reasoning loop, not just a verification afterthought.
- Makes reusable formal artifacts explicit through theorem and axiom libraries.
- Combines persistent Lean REPL and Lean LSP so compile-repair loops can become operationally fast enough to matter.
- Keeps extension seams visible through skills, Python tools, plugins, and MCP-facing plugin support.
- Offers a concrete bridge between terminal agent UX and graph-oriented theorem navigation via Obsidian vault generation.

## Weaknesses and limits
MathCode's public repo is mostly a bootstrap shell around a release binary, so the implementation is less inspectable than source-first harnesses in this wiki. Its documented platform support is also narrower, and the default flow leans on Codex authentication and substantial Lean/Mathlib setup. Architecturally, that means the public material is better at revealing workflow shape than at exposing a fully legible protocol boundary.

## Relationships
MathCode should be read with [[theorem-proving-as-cognitive-kernel]], [[formal-cognition-loop]], [[codex-cli]], [[memory-persistence]], and [[work-management-primitives]]. It is especially useful as a concrete specialized descendant of the broader harness pattern: take a general coding agent substrate, add durable formal artifacts, and let proof obligations rather than prose plausibility decide whether the work has actually closed.