---
title: Suspend & Approval / Prompts
author: Windmill
url: https://www.windmill.dev/docs/flows/flow_approval
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# Suspend & Approval / Prompts

**Source:** [Windmill docs](https://www.windmill.dev/docs/flows/flow_approval)
**Topic:** First-class approval and suspension steps in workflows.

## Core idea
Windmill treats approval and suspension as explicit workflow steps, with forms, permissions, and integrations such as Slack and Microsoft Teams.

## Key claims
- Human approval is a durable workflow primitive, not an afterthought.
- Approval steps can carry structure through forms and permissions.
- Ambient review channels can participate without losing workflow state.

## Harness takeaway
This is a useful model for code-review and permission gates in a harness: human checkpoints should be schema-backed nodes in the work graph, not improvised chat interruptions.
