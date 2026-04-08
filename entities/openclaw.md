---
title: OpenClaw
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [openclaw, memory, safety]
sources: [raw/articles/newstack-openclaw-vs-hermes.md]
---

# OpenClaw

## Overview
OpenClaw is a persistent agent runtime optimized for breadth: many integrations, many models, many surfaces, and a large public skill ecosystem. In the source set here, it functions as the archetype of ecosystem-first persistence, in contrast to [[hermes-agent]], which prioritizes learning depth.

## Integration model
The New Stack comparison presents OpenClaw as a cross-channel background service spanning messaging platforms, model providers, and ClawHub skills. This makes OpenClaw architecturally interesting even apart from coding: it treats presence and reach as first-class harness capabilities. See [[agent-harness-anatomy]].

## Strengths
- Exceptional surface-area breadth.
- Large public skill marketplace and community energy.
- Strong fit for users who want one runtime to be reachable from everywhere.

## Risks
The same source also emphasizes serious security concerns: malicious skill entries, supply-chain risk, and unsafe websocket behavior. OpenClaw is therefore a useful object lesson in [[safety-and-permissions]].

## Relationships
OpenClaw is best read against [[hermes-agent]], [[memory-persistence]], and [[safety-and-permissions]]. It appears in both [[harness-quality-comparison]] and [[harness-architecture-comparison]] as the ecosystem-maximal pole.
