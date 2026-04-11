---
title: Announcing the Agent2Agent Protocol (A2A)
author: Rao Surapaneni, Miku Jha, Michael Vakoc, Todd Segal
url: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
date: 2025-04-09
ingested: 2026-04-10
---

# Announcing the Agent2Agent Protocol (A2A)

**Source:** [Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
**Authors:** Rao Surapaneni, Miku Jha, Michael Vakoc, Todd Segal
**Date:** 2025-04-09

## Core idea
A2A proposes an open interoperability protocol for agents from different vendors or frameworks, centered on capability discovery via Agent Cards, task-oriented communication, artifact exchange, and long-running task status updates.

## Key claims
- Agent collaboration needs an explicit peer protocol, not only tool APIs or shared prompt conventions.
- Capability discovery, task lifecycle tracking, artifact passing, and message parts are distinct protocol concerns.
- Multi-agent ecosystems become more useful when cross-vendor delegation is standardized.

## Harness takeaway
For a multiplayer harness network, A2A is a plausible peer-delegation layer: agents should be discoverable, describable, and able to exchange task objects and artifacts without pretending they all run inside one harness.
