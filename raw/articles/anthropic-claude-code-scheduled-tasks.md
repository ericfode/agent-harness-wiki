---
title: Run prompts on a schedule
author: Anthropic
url: https://code.claude.com/docs/en/scheduled-tasks
ingested: 2026-04-07
---

# Claude Code scheduled tasks

**Source:** [Claude Code Docs](https://code.claude.com/docs/en/scheduled-tasks)
**Topic:** Claude Code scheduling modes, `/loop`, and session-scoped recurring prompts.

---

## 1. Three scheduling modes
Anthropic compares cloud tasks, desktop tasks, and session-scoped `/loop` tasks. The table is useful because it spells out where work runs, whether the machine must stay on, whether the session must remain open, and whether the schedule survives restarts.

## 2. `/loop` is lightweight but ephemeral
The `/loop` skill schedules recurring prompts inside the current session. It is explicitly session-scoped and disappears when the process exits, which makes it good for polling and reminders but not for durable automation.

## 3. Scheduled tasks are first-class tooling
Claude uses dedicated cron tools such as `CronCreate`, `CronList`, and `CronDelete`. Scheduled prompts can also invoke other commands or skills, which means the scheduler is operating on harness primitives rather than only on plain text reminders.

## 4. Runtime semantics matter
The docs specify local-timezone interpretation, low-priority enqueueing between turns, deterministic jitter, and one-shot reminders. Anthropic is therefore documenting scheduling as runtime behavior, not only as UX sugar.
