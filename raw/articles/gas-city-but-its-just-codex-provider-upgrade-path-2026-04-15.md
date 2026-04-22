---
title: Gas City But It's Just Codex Provider Upgrade Path (2026-04-15)
author: local runtime verification
url: file:///Users/ericfode/.hermes/profiles/codex-kernel/CODEX_PROVIDER_UPGRADE.md
ingested: 2026-04-15
---

# Gas City But It's Just Codex Provider Upgrade Path (2026-04-15)

This note captures the practical conclusion after implementing and smoke-testing a `codex-kernel` Hermes profile plugin against a live local Codex app-server.

## Verdict

The right near-term primitive is not a new Hermes core provider transport.

It is a plugin-first bridge that treats Codex app-server as a stateful runtime primitive with explicit:
- server lifecycle
- thread lifecycle
- turn lifecycle
- sandbox policy
- approval policy

Hermes remains the orchestrator. Codex app-server becomes a bounded execution kernel.

## Why the provider path is the wrong shape today

Hermes core provider logic is built around inference APIs. The current runtime/provider system expects variants of:
- `chat_completions`
- `codex_responses`
- `anthropic_messages`

Codex app-server is not mainly an inference endpoint. It is a stateful remote runtime with its own thread and turn graph, approval flows, server-initiated requests, and websocket session semantics.

So if it were promoted directly into the current provider core, Hermes would need to absorb another large special case of the sort already visible in the `copilot-acp` path. That would increase cleverness while decreasing legibility, which is not a bargain worth admiring.

## What the plugin now proves

The `codex-kernel` profile/plugin can now do the useful narrow thing.

Implemented bridge surface:
- `codex_app_server_start/status/stop`
- `codex_thread_start/resume/read`
- `codex_turn_start/steer/interrupt`
- `codex_command_exec`

Most important implementation correction in this pass:
- replace per-request websocket reconnect behavior with a persistent `websockets.sync` connection and one initialize handshake per live server connection

That matters because the first credible Codex-native behavior is continuity: the same server, the same thread, the same turn stream, the same sandbox semantics.

## Smoke-tested facts

Verified locally against a live app-server:
- `thread/start` succeeds
- `turn/start` on the same persistent connection succeeds
- the smoke reply returns correctly (`PONG`)
- after the first turn, `thread/read` and `thread/resume` succeed

An important semantic nuance also showed up clearly:
- a fresh thread exists immediately after `thread/start`
- but its turns are not materialized yet
- therefore `thread/read(includeTurns=true)` before the first user turn must degrade to `includeTurns=false`

The plugin was hardened accordingly. It now returns the thread plus an explicit note rather than failing dramatically over a perfectly normal pre-materialization state. One hates to waste drama on bookkeeping.

## What remains missing

The bridge is useful, but still partial.

Main gaps:
- no background event loop / pending-request map like the upstream app-server clients
- no serious handling yet for server-initiated approval/auth/elicitation requests
- only a subset of protocol methods exposed
- auth-refresh and remote-plugin-sync noise still exist operationally

So this bridge is credible for bounded non-interactive flows today, especially with `approval_policy=never`, but it is not yet full app-server parity.

## Practical upgrade sequence

1. Keep the plugin-first path.
2. Harden the bridge toward upstream client architecture:
   - background reader
   - pending request table
   - explicit server-request handling
   - more method coverage
3. Only after that, consider a deeper Hermes abstraction split between:
   - inference API backends
   - stateful agent-runtime backends

If that higher-order abstraction exists, Codex app-server can be reconsidered there. Until then, calling it a “provider upgrade” is directionally understandable and architecturally misleading.

## Operational footnote

App-server startup noise was traced to malformed YAML in the `control-plane-ops` skill front matter inside the `another-harness` Codex control-plane plugin source. The source copy has been corrected. Cached plugin copies may continue to grumble until refreshed.

## Bottom line

The practical upgrade is:
- not core transport surgery
- not another provider shim
- yes to a plugin-native Codex kernel bridge
- yes to using app-server thread/turn state as a runtime primitive
- yes to delaying core abstraction changes until the boundary is clean enough to deserve them

This is, admittedly, less theatrical than declaring a new universal provider. It is also much more likely to keep working.