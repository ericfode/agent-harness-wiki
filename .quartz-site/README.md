# Quartz publishing layer

This directory vendors the Quartz 4 site generator used to publish the wiki to GitHub Pages.

Design intent:
- The canonical wiki source remains the repository-root markdown corpus (`index.md`, `SCHEMA.md`, `log.md`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `raw/`).
- `scripts/prepare_quartz_content.py` materializes that corpus into `.quartz-site/content/` for Quartz.
- GitHub Pages builds from this directory without requiring the wiki source layout itself to conform to Quartz's preferred project shape.

Upstream:
- Project: https://github.com/jackyzha0/quartz
- Vendored from Quartz v4 branch commit `59b5807`

Useful commands:
```bash
python3 scripts/prepare_quartz_content.py
cd .quartz-site
npm ci
npx quartz build --serve --port 8787
```
