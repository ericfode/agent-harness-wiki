---
title: Temporal Web UI
author: Temporal
url: https://docs.temporal.io/web-ui
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Temporal Web UI

**Source:** [Temporal docs](https://docs.temporal.io/web-ui)
**Topic:** Inspecting and debugging durable workflow executions.

## Core idea
The Temporal Web UI gives users workflow execution state and metadata for debugging purposes. The documentation highlights history, namespaces, workflows, task failures, and schedules.

## Key claims
- Long-running workflows deserve a dedicated visibility and control surface.
- Event history is central to debugging durable execution.
- Workflow state should be inspectable independently of the worker implementation.

## Harness takeaway
A next-generation harness should expose agent runs as durable addressable executions with their own history, metadata, and control actions rather than hiding everything inside a monolithic conversation log.
