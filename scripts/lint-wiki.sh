#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT"

errors=0

error() {
  printf 'ERROR: %s\n' "$*" >&2
  errors=$((errors + 1))
}

expected_type() {
  case "$1" in
    entities/*) printf 'entity' ;;
    concepts/*) printf 'concept' ;;
    comparisons/*) printf 'comparison' ;;
    queries/*) printf 'query' ;;
    *) return 1 ;;
  esac
}

content_files=(entities/*.md concepts/*.md comparisons/*.md queries/*.md)
actual_count=${#content_files[@]}
today=$(date +%F)

allowed_tags_file=$(mktemp)
all_pages_file=$(mktemp)
index_pages_file=$(mktemp)
modified_pages_file=$(mktemp)
trap 'rm -f "$allowed_tags_file" "$all_pages_file" "$index_pages_file" "$modified_pages_file"' EXIT

sed -n '/^### /,/^## /p' SCHEMA.md | rg -o '^- `([^`]+)`' -r '$1' | sort -u > "$allowed_tags_file"
for f in "${content_files[@]}"; do
  basename "$f" .md
done | sort -u > "$all_pages_file"
rg -o '\[\[[^]]+\]\]' index.md | sed 's/\[\[//;s/\]\]//' | sort -u > "$index_pages_file"

declared_count=$(sed -n 's/^> Last updated: .* | Total pages: \([0-9][0-9]*\)$/\1/p' index.md | head -n 1)
if [ -z "$declared_count" ]; then
  error "index.md is missing the Total pages header line"
elif [ "$declared_count" != "$actual_count" ]; then
  error "index.md declares $declared_count pages but the corpus contains $actual_count"
fi

missing_from_index=$(comm -23 "$all_pages_file" "$index_pages_file" || true)
if [ -n "$missing_from_index" ]; then
  while IFS= read -r page; do
    [ -n "$page" ] && error "$page is not listed in index.md"
  done <<< "$missing_from_index"
fi

stale_index_entries=$(comm -13 "$all_pages_file" "$index_pages_file" || true)
if [ -n "$stale_index_entries" ]; then
  while IFS= read -r page; do
    [ -n "$page" ] && error "index.md references missing page $page"
  done <<< "$stale_index_entries"
fi

for f in "${content_files[@]}"; do
  if [ "$(sed -n '1p' "$f")" != '---' ]; then
    error "$f is missing YAML frontmatter"
    continue
  fi

  frontmatter_end=$(awk 'NR > 1 && /^---$/ { print NR; exit }' "$f")
  if [ -z "${frontmatter_end:-}" ]; then
    error "$f has unterminated YAML frontmatter"
    continue
  fi

  if ! ruby - "$f" "$frontmatter_end" <<'RUBY'
require 'yaml'
require 'date'
require 'time'

path = ARGV[0]
frontmatter_end = Integer(ARGV[1])
lines = File.readlines(path, chomp: true)
frontmatter = lines[1...frontmatter_end - 1].join("\n") + "\n"
parsed = YAML.safe_load(frontmatter, permitted_classes: [Date, Time], aliases: false)
exit(parsed.is_a?(Hash) ? 0 : 1)
RUBY
  then
    error "$f has invalid YAML frontmatter"
    continue
  fi

  title=$(sed -n 's/^title: //p' "$f" | head -n 1)
  created=$(sed -n 's/^created: //p' "$f" | head -n 1)
  updated=$(sed -n 's/^updated: //p' "$f" | head -n 1)
  page_type=$(sed -n 's/^type: //p' "$f" | head -n 1)
  tags_line=$(sed -n 's/^tags: \[\(.*\)\]/\1/p' "$f" | head -n 1)
  sources_line=$(sed -n 's/^sources: \[\(.*\)\]/\1/p' "$f" | head -n 1)

  [ -n "$title" ] || error "$f is missing title frontmatter"
  [ -n "$created" ] || error "$f is missing created frontmatter"
  [ -n "$updated" ] || error "$f is missing updated frontmatter"

  expected=$(expected_type "$f")
  if [ "$page_type" != "$expected" ]; then
    error "$f has type '$page_type' but expected '$expected'"
  fi

  if [ -z "$tags_line" ]; then
    error "$f is missing tags frontmatter"
  else
    while IFS= read -r tag; do
      [ -z "$tag" ] && continue
      if ! rg -Fxq "$tag" "$allowed_tags_file"; then
        error "$f uses tag '$tag' which is not declared in SCHEMA.md"
      fi
    done < <(printf '%s\n' "$tags_line" | tr ',' '\n' | sed 's/^ *//;s/ *$//')
  fi

  if [ -z "$sources_line" ]; then
    error "$f is missing sources frontmatter"
  else
    while IFS= read -r source; do
      [ -z "$source" ] && continue
      if [ ! -f "$source" ]; then
        error "$f references missing source $source"
      fi
    done < <(printf '%s\n' "$sources_line" | tr ',' '\n' | sed 's/^ *//;s/ *$//')
  fi

  link_count=$({ rg -o '\[\[[^]]+\]\]' "$f" || true; } | wc -l | tr -d ' ')
  if [ "$link_count" -lt 2 ]; then
    error "$f has only $link_count outbound wikilinks"
  fi
done

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if ! git diff --cached --quiet -- entities/*.md concepts/*.md comparisons/*.md queries/*.md; then
    git diff --cached --name-only --diff-filter=M -- entities/*.md concepts/*.md comparisons/*.md queries/*.md > "$modified_pages_file" || true
  else
    git diff --name-only --diff-filter=M -- entities/*.md concepts/*.md comparisons/*.md queries/*.md > "$modified_pages_file" || true
  fi
fi

while IFS= read -r f; do
  [ -z "$f" ] && continue
  updated=$(sed -n 's/^updated: //p' "$f" | head -n 1)
  if [ "$updated" != "$today" ]; then
    error "$f is modified in git but updated=$updated (expected $today)"
  fi
done < "$modified_pages_file"

while IFS= read -r bare_log_path; do
  [ -z "$bare_log_path" ] && continue
  error "log.md contains bare internal path $bare_log_path (use [[wikilinks]] with an alias if you want the repo path shown)"
done < <(
  python3 - <<'PY'
from pathlib import Path
import re

root = Path('.')
text = (root / 'log.md').read_text(encoding='utf-8')
text = re.sub(r'\[\[[^\]]+\]\]', '', text)

internal_paths = set()
for name in ['index.md', 'SCHEMA.md', 'log.md', 'README.md']:
    if (root / name).exists():
        internal_paths.add(name)
for dirname in ['entities', 'concepts', 'comparisons', 'queries', 'raw']:
    base = root / dirname
    if not base.exists():
        continue
    for path in base.rglob('*.md'):
        internal_paths.add(path.relative_to(root).as_posix())

pattern = re.compile(r'(?<![\w/])(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.md\b')
found = sorted({m.group(0) for m in pattern.finditer(text) if m.group(0) in internal_paths})
for item in found:
    print(item)
PY
)

if [ "$errors" -gt 0 ]; then
  printf 'wiki lint failed with %s error(s)\n' "$errors" >&2
  exit 1
fi

printf 'wiki lint passed: %s content pages checked\n' "$actual_count"
