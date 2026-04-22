---
title: Codex App-Server Provider vs Runtime Bridge
created: 2026-04-15
updated: 2026-04-15
type: query
tags: [codex-cli, hermes-agent, orchestration, tool-execution, error-recovery]
sources: [raw/articles/gas-city-but-its-just-codex-provider-upgrade-path-2026-04-15.md, entities/codex-app-server.md, entities/codex-cli.md, entities/hermes-agent.md, queries/gas-city-but-its-just-codex.md]
---

# Codex App-Server Provider vs Runtime Bridge

## Verdict
Treat [[codex-app-server]] as a runtime bridge inside [[hermes-agent]], not as a primary provider transport in the current core.

Hermes's provider layer is inference-shaped. Codex app-server is runtime-shaped.

That distinction matters.

## Why this is the right split

Hermes providers currently resolve into LLM-facing transport families such as `chat_completions`, `codex_responses`, and `anthropic_messages`.

[[codex-app-server]] instead exposes durable execution machinery:
- websocket server lifecycle
- thread creation and resumption
- turn execution and interruption
- sandbox policy
- approval policy
- server-initiated requests and notifications

So the natural place for it is not the same layer that swaps OpenAI for Anthropic. It is the layer where Hermes grows bounded foreign runtimes and names their control surfaces explicitly.

## What the current plugin demonstrates

A `codex-kernel` profile/plugin now proves the narrow path works:
- start a local app-server
- bind a Hermes session to a Codex thread
- run a turn on the same persistent websocket connection
- read or resume the thread after the first turn

This is enough to show that Codex-native thread continuity is real and useful without pretending the current Hermes provider abstraction has already become something larger.

## Important semantic nuance

Fresh threads exist before they have a materialized turn history.

So a newly created thread may be readable as thread metadata while still lacking materialized turns. In practice this means `thread/read(includeTurns=true)` must degrade cleanly before the first user turn rather than being treated as catastrophic failure. The runtime is being exact, not malicious.

## Why not elevate it to core transport yet

Because that would force [[hermes-agent]] to absorb a second kind of backend abstraction without admitting it has done so.

A real provider upgrade would require a cleaner split between:
- inference backends
- stateful agent-runtime backends

Until that abstraction exists, promoting app-server into the provider core would mostly create another special-case shim and another seam where the code lies politely about what it is.

## Practical path

1. Keep the plugin-first `codex-kernel` bridge.
2. Harden it toward upstream app-server client architecture.
3. Add server-request handling and broader protocol coverage.
4. Only then consider a core abstraction upgrade if the runtime/backend boundary becomes explicit enough to deserve one.

## Bottom line

The practical upgrade is not “make Codex app-server the new provider.”

It is: keep Hermes as orchestrator, let Codex app-server serve as a bounded execution kernel, and only widen the core abstraction after the bridge has earned it.