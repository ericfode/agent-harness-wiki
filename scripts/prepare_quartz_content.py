#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".quartz-site" / "content"

ROOT_FILES = ["index.md", "projects.md", "news.md", "SCHEMA.md", "log.md", "README.md"]
TREE_DIRS = [
    "entities",
    "concepts",
    "comparisons",
    "queries",
    "raw",
    "east-bay-catholic-property-monitor",
]
DATE_KEYS = {"date", "created", "updated", "modified", "published", "ingested"}
FRONTMATTER_LINE_RE = re.compile(r"^(\s*)([^:#\n][^:]*):(\s*)(.+?)\s*$")
FIRST_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def infer_title(path: Path, text: str) -> str:
    match = FIRST_H1_RE.search(text)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def sanitize_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text

    lines = text.splitlines()
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return text

    kept: list[str] = [lines[0]]
    for i in range(1, end):
        line = lines[i]
        match = FRONTMATTER_LINE_RE.match(line)
        if not match:
            kept.append(line)
            continue

        indent, key, spacing, value = match.groups()
        normalized_key = key.strip().lower()
        stripped = value.strip()

        if normalized_key in DATE_KEYS and stripped.lower() == "unknown":
            continue

        if indent:
            kept.append(line)
            continue

        if not stripped or stripped.startswith(("[", "{", '"', "'")) or stripped in {"|", ">"}:
            kept.append(line)
            continue

        if normalized_key in {"type"}:
            kept.append(line)
            continue

        if stripped in {"true", "false", "null"}:
            kept.append(line)
            continue

        kept.append(f"{indent}{key}:{spacing}{json.dumps(stripped)}")

    kept.extend(lines[end:])
    return "\n".join(kept) + ("\n" if text.endswith("\n") else "")


def ensure_frontmatter_title(path: Path, text: str) -> str:
    if text.startswith("---\n"):
        return sanitize_frontmatter(text)

    title = infer_title(path, text)
    return f"---\ntitle: {json.dumps(title)}\n---\n\n{text.lstrip()}"


def escape_currency_dollars_for_quartz(src: Path, text: str) -> str:
    """Prevent Quartz/KaTeX from treating East Bay currency as inline math.

    The Oakland church pages contain many ordinary currency ranges such as
    ``$438,838–$997,359``. Quartz's Latex transformer sees the first ``$`` as a
    math delimiter and merrily eats the price text. This keeps source Markdown
    readable while escaping dollars only in the prepared Quartz content tree.
    Code fences and inline code are left alone.
    """
    try:
        rel = src.relative_to(ROOT).as_posix()
    except ValueError:
        rel = src.as_posix()
    if not rel.startswith("east-bay-catholic-property-monitor/"):
        return text

    out: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        pieces = re.split(r"(`+[^`]*`+)", line)
        for i, piece in enumerate(pieces):
            if i % 2 == 1:
                out.append(piece)
                continue
            escaped: list[str] = []
            for j, ch in enumerate(piece):
                if ch == "$" and (j == 0 or piece[j - 1] != "\\"):
                    escaped.append("\\$")
                else:
                    escaped.append(ch)
            out.append("".join(escaped))
    return "".join(out)


def transform_markdown(src: Path) -> str:
    text = read_text(src)
    text = ensure_frontmatter_title(src, text)
    return escape_currency_dollars_for_quartz(src, text)


def reset_output_dir() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)


def copy_markdown(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(transform_markdown(src), encoding="utf-8")


def copy_root_files() -> None:
    for name in ROOT_FILES:
        src = ROOT / name
        if src.exists():
            copy_markdown(src, OUT / name)


def copy_tree_dirs() -> None:
    for dirname in TREE_DIRS:
        src_dir = ROOT / dirname
        if not src_dir.exists():
            continue
        for src in sorted(src_dir.rglob("*")):
            if src.is_dir():
                continue
            rel = src.relative_to(ROOT)
            dest = OUT / rel
            if src.suffix.lower() == ".md":
                copy_markdown(src, dest)
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)


def count_markdown_files() -> int:
    return sum(1 for _ in OUT.rglob("*.md"))


def main() -> None:
    quartz_root = ROOT / ".quartz-site"
    if not quartz_root.exists():
        raise SystemExit(f"Quartz site directory not found at {quartz_root}")

    reset_output_dir()
    copy_root_files()
    copy_tree_dirs()
    print(f"Prepared {count_markdown_files()} markdown files in {OUT}")


if __name__ == "__main__":
    main()
