---
title: Safety and Permissions
created: 2026-04-07
updated: 2026-04-09
type: concept
tags: [safety, tool-execution, error-recovery]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-introducing-codex-app.md, raw/articles/openai-codex-app-server-readme.md, raw/articles/codex-cli-github.md, raw/articles/anthropic-claude-code-settings.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md]
---

# Safety and Permissions

## Definition
Safety and permissions are the controls that determine what an agent may execute, when a human must approve a step, and how the runtime limits damage when the agent is wrong or the ecosystem is hostile. A capable model without execution boundaries is not autonomy; it is simply uncontained power.

## Main control surfaces
- Sandboxes and execution boundaries around shell, file, and network tools, as emphasized by [[codex-cli]] and the [[codex-app-server]].
- Approval checkpoints that pause the turn until a human authorizes risky work.
- Hierarchical allow/deny policy rules and managed settings, which Anthropic now treats as deployable harness policy rather than optional prompt advice.
- Hardened runtimes and pre-execution scanning, which the [[hermes-agent]] material treats as first-class operating concerns.
- Skill-registry and integration hygiene, where [[openclaw]] demonstrates how ecosystem breadth can expand the blast radius.

## Typical failure modes
- Malicious or low-quality third-party skills entering the execution path.
- Credential leakage through unsafe transports or over-privileged tooling.
- Destructive commands becoming too easy because the runtime exposes more power than the task requires.
- Defensive paralysis, where the harness is so opaque or restrictive that the agent stops validating reality and merely narrates intent.

## Design lesson
Safety is not only a policy layer glued on top of tools. It is part of [[agent-harness-anatomy]] and [[harness-engineering]] because permission boundaries, warning surfaces, managed settings, and remediation hints shape how every later turn behaves. Good harnesses make denial legible: the agent should learn what was blocked, why, and what safer path remains.

## Related pages
Read this page with [[agent-harness-anatomy]], [[harness-engineering]], [[instruction-layering]], [[automation-and-background-work]], [[codex-cli]], [[hermes-agent]], and [[openclaw]]. The trade-offs here also inform [[harness-architecture-comparison]] and [[context-engineering]].
