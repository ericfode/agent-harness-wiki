---
title: MetaAgent
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [memory, tool-execution, orchestration]
sources: [raw/papers/arxiv-qian-2025-metaagent.md]
---

# MetaAgent

## Overview
MetaAgent is a self-evolving framework that starts with a minimal workflow, organizes tool-use history, distills lessons, and grows in-house tools plus a persistent knowledge base. Its learning surface is capability growth as much as workflow revision.

## Why it matters
It matters because it treats tool strategy and internal capability construction as the real place where an agent matures. That is wider, and probably truer, than workflow mutation alone.

## Distinctive trait
Its distinctive trait is capability bootstrapping from tool traces: successful and failed interactions become lessons, then durable tools and knowledge artifacts.

## Relationships
Read MetaAgent with [[self-evolving-workflows]], [[memory-persistence]], and [[memento-skills]]. Compared with [[metaclaw|MetaClaw]] and [[agentevolver|AgentEvolver]], it is the clearest example here of tool meta-learning as the growth substrate.
