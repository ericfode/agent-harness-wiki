---
title: Persistent Memory
author: Nous Research
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
ingested: 2026-04-07
---

# Hermes Agent Persistent Memory

**Source:** [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/)
**Topic:** Hermes memory architecture and cross-session recall.

---

## 1. File-based durable memory
Hermes uses `MEMORY.md` and `USER.md` as explicit durable memory files for project and user context.

## 2. Searchable session recall
The docs say Hermes stores CLI and messaging sessions in SQLite with FTS5 full-text search, then summarizes relevant results when searching old conversations. This is memory as searchable history, not only hand-written notes.

## 3. Layered external memory providers
Hermes also ships external memory-provider integrations that add semantic search, fact extraction, and user modeling. The built-in memory is therefore extensible rather than monolithic.
