#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: bash scripts/install.sh --agent claude|codex|cursor --scope user|project [--force]

Run from any directory. For --scope project, installs into the current directory.
No downloads, no telemetry, and no overwrite unless --force.
EOF
}

agent='' scope='' force='false'
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent) [[ $# -ge 2 ]] || { usage; exit 2; }; agent="$2"; shift 2 ;;
    --scope) [[ $# -ge 2 ]] || { usage; exit 2; }; scope="$2"; shift 2 ;;
    --force) force='true'; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done
[[ "$agent" == 'claude' || "$agent" == 'codex' || "$agent" == 'cursor' ]] || { usage >&2; exit 2; }
[[ "$scope" == 'user' || "$scope" == 'project' ]] || { usage >&2; exit 2; }
[[ "$agent" != 'cursor' || "$scope" == 'project' ]] || { echo 'Cursor adapter supports only project scope. Use Cursor Settings for global rules.' >&2; exit 2; }

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "$scope" == 'user' ]]; then root="$HOME"; else root="$PWD"; fi

case "$agent" in
  claude)
    dest="$root/.claude/skills/asdify"
    source="$repo/skills/asdify"
    kind='directory'
    ;;
  codex)
    dest="$root/.agents/skills/asdify"
    source="$repo/skills/asdify"
    kind='directory'
    ;;
  cursor)
    dest="$root/.cursor/rules/asdify.mdc"
    source="$repo/integrations/cursor-rule.mdc"
    kind='file'
    ;;
esac

if [[ -e "$dest" || -L "$dest" ]]; then
  if [[ "$force" != 'true' ]]; then
    echo "Refusing to overwrite $dest. Check contents, then add --force if appropriate." >&2
    exit 1
  fi
fi

parent="$(dirname "$dest")"
mkdir -p "$parent"
if [[ "$kind" == 'directory' ]]; then
  tmp="$(mktemp -d "$parent/.asdify.XXXXXXXX")"
  trap 'rm -rf "$tmp"' EXIT
  cp -R "$source" "$tmp/asdify"
  if [[ -e "$dest" || -L "$dest" ]]; then rm -rf "$dest"; fi
  mv "$tmp/asdify" "$dest"
else
  tmp="$(mktemp "$parent/.asdify.XXXXXXXX")"
  trap 'rm -f "$tmp"' EXIT
  cp "$source" "$tmp"
  if [[ -e "$dest" || -L "$dest" ]]; then rm -f "$dest"; fi
  mv "$tmp" "$dest"
fi

echo "Installed $agent ($scope): $dest"
