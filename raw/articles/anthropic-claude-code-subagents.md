---
title: Create custom subagents
author: Anthropic
url: https://code.claude.com/docs/en/subagents
ingested: 2026-04-07
---

# Claude Code subagents

**Source:** [Claude Code Docs](https://code.claude.com/docs/en/subagents)
**Topic:** Specialized Claude Code subagents with separate context windows, scoped tools, memory, and permissions.

---

## 1. Subagents are isolated workers inside one session
Anthropic defines subagents as specialized assistants that each run in their own context window with their own system prompt, tool access, and permissions. They return results back to the calling session rather than becoming peer participants in the conversation.

## 2. Built-in and custom delegation types
Claude Code ships built-in subagents such as Explore, Plan, and general-purpose. The docs emphasize that this is not only a user customization feature; the harness itself relies on specialized delegated workers with different tool and model profiles.

## 3. Scoped distribution and precedence
Subagents can come from managed settings, session-only CLI JSON, project `.claude/agents/`, user `~/.claude/agents/`, or plugins. Higher-priority scopes override lower ones. This makes subagents part of Claude Code’s broader instruction and policy layering model.

## 4. Fine-grained controls
The subagent frontmatter supports tool allowlists, denied tools, model choice, permission mode, hooks, MCP server scope, skills, background execution, isolation, and optional persistent memory. Plugin-delivered subagents are intentionally more restricted and cannot define certain high-risk fields like hooks or permission mode.
