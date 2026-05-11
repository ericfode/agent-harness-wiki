#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / ".quartz-site" / "public"
SKIP_NAMES = {"index.html", "404.html"}
BASE_TAG = '<base href="../">'


def alias_html(page: Path) -> str:
    text = page.read_text(encoding="utf-8")
    if BASE_TAG in text:
        return text
    if "<head>" in text:
        return text.replace("<head>", f"<head>\n{BASE_TAG}", 1)
    return f"<!DOCTYPE html>\n<html><head>{BASE_TAG}</head><body>{text}</body></html>"


def main() -> None:
    if not PUBLIC.is_dir():
        raise SystemExit(f"Quartz public directory not found: {PUBLIC}")

    made = 0
    skipped = 0
    for page in sorted(PUBLIC.rglob("*.html")):
        rel = page.relative_to(PUBLIC)
        if rel.name in SKIP_NAMES:
            continue

        alias = page.with_suffix("") / "index.html"
        if alias.exists():
            skipped += 1
            continue

        alias.parent.mkdir(parents=True, exist_ok=True)
        alias.write_text(alias_html(page), encoding="utf-8")
        made += 1

    print(f"Added {made} trailing-slash aliases; skipped {skipped} existing aliases.")


if __name__ == "__main__":
    main()
