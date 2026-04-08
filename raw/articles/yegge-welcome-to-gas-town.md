---
title: Welcome to Gas Town
author: Steve Yegge
url: https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
date: 2026-01-01
ingested: 2026-04-07
---

# Welcome to Gas Town

Gas Town is an opinionated AI agent orchestrator designed to solve the yak shaving involved in managing multiple AI coding sessions. Built on top of Beads (a Git-backed data plane) and uses tmux as its primary UI.

## The 8 Stages of AI Dev Evolution
Gas Town is only for those at Stage 7 or 8:
- Stage 6: CLI, multi-agent, YOLO (3-5 parallel instances)
- Stage 7: 10+ agents, hand-managed
- Stage 8: Building/using an orchestrator to automate the workflow

## The Worker Roles (The Crew)
- The Mayor: Chief-of-staff/concierge; primary agent human interacts with
- Polecats: Ephemeral, per-project workers producing Merge Requests
- Refinery: Manages the Merge Queue; resolves conflicts and rebases
- The Witness: Monitors polecats and refinery for stuck states
- The Deacon: Daemon beacon running town-level patrols
- Dogs: Deacon's helpers; maintenance and cleanup
- The Crew: Long-lived, named agents for direct human collaboration
- The Overseer: The human

## MEOW Stack (Molecular Expression of Work)
- Beads: Atomic unit; lightweight issues stored as JSONL in Git
- Epics: Beads with children (hierarchical plans)
- Molecules: Workflows chained with Beads; durable across agent crashes
- Protomolecules: Templates for molecules
- Formulas: TOML-based source forms cooked into molecules
- Wisps: Ephemeral, non-persisted Beads for high-velocity orchestration noise

## Technical Principles
- GUPP (Gastown Universal Propulsion Principle): "If there is work on your hook, YOU MUST RUN IT."
- NDI (Nondeterministic Idempotence): AI is good at following TODO lists; outcome guaranteed even if path is nondeterministic
- gt seance: New agent session talks to dead ancestors via Claude Code's /resume

## Critical Warnings
- Cost: Cash guzzler requiring multiple Claude Code accounts
- Stability: Young codebase, "vibe coded"
- Throughput over 100% efficiency
