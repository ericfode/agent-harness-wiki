---
title: Claude Code settings
author: Anthropic
url: https://code.claude.com/docs/en/settings
ingested: 2026-04-07
---

# Claude Code settings

**Source:** [Claude Code Docs](https://code.claude.com/docs/en/settings)
**Topic:** Configuration scopes, permissions, hooks, and policy controls in Claude Code.

---

## 1. Hierarchical configuration scopes
Claude Code supports managed, user, project, and local scopes, with managed settings taking precedence. Anthropic presents this as a real policy system for teams and enterprises, not merely user preferences.

## 2. Permission rules as configuration
Project and managed settings can define allow and deny rules for tools and paths. The docs show concrete examples like allowing selected bash commands while denying reads of secret files.

## 3. Managed policy and lockdown controls
Anthropic includes settings that let administrators restrict hooks, MCP servers, permission rules, channels, and plugin marketplaces. This makes safety a deployable governance layer inside the harness.

## 4. Worktree and subagent awareness
The settings system explicitly includes worktree settings, subagent configuration, hook configuration, and transcript cleanup behavior. That ties configuration directly to long-running and multi-agent workflows.
