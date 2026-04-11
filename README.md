# Agent Harness Wiki

An interlinked markdown wiki on agent harnesses: coding-agent runtimes, orchestration patterns, durable memory, formal methods, non-linear interfaces, and adjacent research threads.

This repository is organized as a plain markdown knowledge base first, with a Quartz 4 publishing layer on top for GitHub Pages.

Published site:
- https://ericfode.github.io/agent-harness-wiki/

Structure:
- `SCHEMA.md` — wiki conventions and tag taxonomy
- `index.md` — top-level content catalog
- `log.md` — chronological ingest and maintenance history
- `entities/` — concrete systems and projects
- `concepts/` — reusable ideas and architectural patterns
- `comparisons/` — side-by-side evaluations
- `queries/` — synthesized answers, research passes, and design notes
- `raw/` — immutable source notes and assets

The current domain centers on agent harness engineering, including Codex CLI, Claude Code, Hermes Agent, Gas Town / Gas City, formal semantics for harnesses, and newer topics such as neural-native programming.

Open the repo in any markdown editor, or in Obsidian, to browse the graph directly.

Local preview:
```bash
python3 scripts/prepare_quartz_content.py
cd .quartz-site
npm ci
npx quartz build --serve --port 8787
```

The GitHub Pages workflow rebuilds the site automatically on pushes to `main`.
