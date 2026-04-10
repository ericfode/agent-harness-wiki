#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".site-docs"

ROOT_FILES = ["index.md", "SCHEMA.md", "log.md", "README.md"]
TREE_DIRS = ["entities", "concepts", "comparisons", "queries", "raw"]

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FENCED_BLOCK_RE = re.compile(r"(```.*?```)", re.S)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_title(path: Path) -> str:
    text = read_text(path)
    if text.startswith("---\n"):
        lines = text.splitlines()
        for line in lines[1:80]:
            if line.strip() == "---":
                break
            if line.startswith("title:"):
                value = line.split(":", 1)[1].strip().strip('"')
                return value
    return path.stem.replace("-", " ").title()


def collect_markdown_sources() -> list[Path]:
    paths: list[Path] = []
    for name in ROOT_FILES:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    for dirname in TREE_DIRS:
        for p in sorted((ROOT / dirname).rglob("*.md")):
            if ".site-docs" not in p.parts and "site" not in p.parts:
                paths.append(p)
    return paths


def output_rel_path(src: Path) -> Path:
    rel = src.relative_to(ROOT)
    if rel.as_posix() == "README.md":
        return Path("repository.md")
    return rel


def copy_non_markdown_assets() -> None:
    for dirname in TREE_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for src in sorted(base.rglob("*")):
            if src.is_dir():
                continue
            if src.suffix.lower() == ".md":
                continue
            rel = src.relative_to(ROOT)
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)


def site_rel_url(rel_md: Path) -> str:
    rel_posix = rel_md.as_posix()
    if rel_posix == "index.md":
        return "/"
    if rel_posix.endswith("/index.md"):
        return "/" + rel_posix[: -len("index.md")]
    return "/" + rel_posix[:-3] + "/"


def relative_md_link(from_rel: Path, to_rel: Path) -> str:
    from_dir = from_rel.parent
    link = os.path.relpath(to_rel, start=from_dir if str(from_dir) != "." else Path("."))
    return link.replace(os.sep, "/")


def rewrite_wikilinks(text: str, source_rel: Path, stem_to_rel: dict[str, Path], stem_to_title: dict[str, str]) -> str:
    def replace_in_plain(plain: str) -> str:
        def repl(match: re.Match[str]) -> str:
            inner = match.group(1).strip()
            alias = None
            anchor = None
            if "|" in inner:
                inner, alias = inner.split("|", 1)
                inner = inner.strip()
                alias = alias.strip()
            if "#" in inner:
                inner, anchor = inner.split("#", 1)
                inner = inner.strip()
                anchor = anchor.strip()

            stem = Path(inner).name
            target_rel = stem_to_rel.get(stem)
            if not target_rel:
                return match.group(0)

            label = alias or stem_to_title.get(stem, stem.replace("-", " "))
            link = relative_md_link(source_rel, target_rel)
            if anchor:
                slug = re.sub(r"[^a-z0-9\- ]", "", anchor.lower()).strip().replace(" ", "-")
                if slug:
                    link += f"#{slug}"
            return f"[{label}]({link})"

        return WIKILINK_RE.sub(repl, plain)

    parts = FENCED_BLOCK_RE.split(text)
    for i, part in enumerate(parts):
        if i % 2 == 0:
            parts[i] = replace_in_plain(part)
    return "".join(parts)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    sources = collect_markdown_sources()
    stem_to_rel: dict[str, Path] = {}
    stem_to_title: dict[str, str] = {}
    for src in sources:
        rel = output_rel_path(src)
        stem_to_rel[src.stem] = rel
        stem_to_title[src.stem] = parse_title(src)

    copy_non_markdown_assets()

    for src in sources:
        rel = output_rel_path(src)
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = read_text(src)
        rewritten = rewrite_wikilinks(text, rel, stem_to_rel, stem_to_title)
        dest.write_text(rewritten, encoding="utf-8")

    print(f"Prepared {len(sources)} markdown files in {OUT}")


if __name__ == "__main__":
    main()
