---
title: Orchestrate teams of Claude Code sessions
author: Anthropic
url: https://code.claude.com/docs/en/agent-teams
ingested: 2026-04-07
---

# Claude Code agent teams

**Source:** [Claude Code Docs](https://code.claude.com/docs/en/agent-teams)
**Topic:** Multi-session Claude Code teams with direct inter-agent communication.

---

## 1. Team lead plus independent teammate sessions
Anthropic describes agent teams as multiple Claude Code instances coordinated by a lead session. Each teammate has its own context window and can communicate directly with other teammates rather than only reporting back upward.

## 2. Explicit contrast with subagents
The docs draw a clean line: subagents operate inside one session and return results to the caller, while agent teams coordinate across separate sessions with a shared task list and peer-to-peer messaging. This is a topology distinction, not a branding variation.

## 3. Best use cases and costs
Anthropic recommends agent teams for parallel research, competing debugging hypotheses, cross-layer changes, and review scenarios where workers benefit from discussing findings. The tradeoff is higher token cost and coordination overhead than a single session or simple subagents.

## 4. Experimental status
Agent teams are documented as experimental, disabled by default, and subject to known limitations around session resumption, task coordination, and shutdown behavior. The page reads like real infrastructure documentation rather than a polished launch slogan.
