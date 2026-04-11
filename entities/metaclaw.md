---
title: MetaClaw
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [orchestration, memory, tool-execution]
sources: [raw/papers/arxiv-xia-2026-metaclaw.md]
---

# MetaClaw

## Overview
MetaClaw studies continual evolution for a deployed multi-channel agent platform that must improve without downtime. It combines rapid skill synthesis from failures with slower policy optimization during quiet windows.

## Why it matters
It matters because it is unusually explicit about the operational problem of continual learning. Real platforms need fast local repairs and slower global improvement without theatrical redeploy rituals.

## Distinctive trait
Its distinctive trait is a two-speed evolution loop: immediate skill synthesis for live failures and opportunistic policy optimization when the platform can afford deeper change.

## Relationships
Read MetaClaw with [[hermes-agent]], [[self-evolving-workflows]], and [[metaagent|MetaAgent]]. It is also a useful contrast to the more specification-driven stance of [[severa|SEVerA]].
