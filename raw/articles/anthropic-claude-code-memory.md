---
title: How Claude remembers your project
author: Anthropic
url: https://code.claude.com/docs/en/memory
ingested: 2026-04-07
---

# How Claude remembers your project

**Source:** [Claude Code Docs](https://code.claude.com/docs/en/memory)
**Topic:** Persistent instructions and auto memory in Claude Code.

---

## 1. Two memory layers
Claude Code distinguishes between user-authored `CLAUDE.md` files and automatically collected memory. `CLAUDE.md` carries explicit project, user, or organization instructions; auto memory stores learnings and patterns Claude discovers while working.

## 2. Scoped instruction files
The docs define multiple `CLAUDE.md` scopes, including managed policy, project instructions, and user instructions. More specific files override broader ones, which gives Claude Code a structured hierarchy for persistent guidance.

## 3. Cross-session carryover without pretending the transcript is infinite
Anthropic’s framing is pragmatic: Claude reads these files at session start, and the docs link this memory model to session management, context exploration, and resume flows. The persistence model is therefore artifact-based rather than raw transcript accumulation.

## 4. Subagent memory
The page also notes that subagents can maintain their own auto memory. That makes memory isolation part of orchestration, not just a global shared store.
