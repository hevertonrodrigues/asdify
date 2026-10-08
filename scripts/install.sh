#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: bash scripts/install.sh --agent ID --scope user|project [--force]
       bash scripts/install.sh --list

Run from any directory. Project scope installs into the current directory.
--list shows the supported destination snapshot; it does not detect installed apps.
No downloads, no telemetry, and no overwrite unless --force.

Compatibility: claude = claude-code; cursor = cursor-rule (project rule).
Use cursor-skill to install the complete native skill for Cursor.
USAGE
}

fail() { printf '%s\n' "$1" >&2; exit "${2:-2}"; }
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
registry="$repo/integrations/agents.tsv"
agent='' scope='' force='false' list='false'
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent) [[ $# -ge 2 ]] || { usage >&2; exit 2; }; agent="$2"; shift 2 ;;
    --scope) [[ $# -ge 2 ]] || { usage >&2; exit 2; }; scope="$2"; shift 2 ;;
    --force) force='true'; shift ;;
    --list) list='true'; shift ;;
    -h|--help) usage; exit 0 ;;
    *) fail "Unknown argument: $1. Run --help for usage." ;;
  esac
done
[[ -r "$registry" ]] || fail "Missing agent registry: $registry" 1

if [[ "$list" == 'true' ]]; then
  [[ -z "$agent" && -z "$scope" && "$force" == 'false' ]] || fail '--list must be used on its own.'
  printf 'ASDify destination snapshot (2026-10-08); host behavior is not certified.\n\n'
  printf '%-22s %-13s %-6s %s\n' 'ID' 'SCOPES' 'KIND' 'NAME'
  while IFS=$'\t' read -r row_id row_name row_project row_user row_kind row_source; do
    [[ -n "$row_id" && "$row_id" != \#* ]] || continue
    scopes='project'
    [[ "$row_user" == '-' ]] || scopes='project,user'
    printf '%-22s %-13s %-6s %s\n' "$row_id" "$scopes" "$row_kind" "$row_name"
  done < "$registry"
  exit 0
fi
[[ -n "$agent" && ( "$scope" == 'user' || "$scope" == 'project' ) ]] || { usage >&2; exit 2; }

found='false'
while IFS=$'\t' read -r row_id row_name row_project row_user row_kind row_source row_extra; do
  [[ "$row_id" == "$agent" ]] || continue
  [[ -n "$row_name" && -n "$row_project" && -n "$row_user" && -n "$row_source" && -z "$row_extra" ]] || fail "Invalid registry entry: $agent" 1
  display_name="$row_name" project_path="$row_project" user_path="$row_user" kind="$row_kind"
  found='true'
  break
done < "$registry"
[[ "$found" == 'true' ]] || fail "Unknown agent: $agent. Run --list for supported IDs."
[[ "$kind" == 'skill' || "$kind" == 'rule' ]] || fail "Invalid registry kind for $agent" 1
[[ "$scope" != 'user' || "$user_path" != '-' ]] || fail "$display_name supports only project scope."

# Registry paths are data, never evaluated as shell expressions.
validate_relative_path() {
  local relative="$1" component
  local -a components
  [[ -n "$relative" && "$relative" != /* && "$relative" != */ && "$relative" != *'//'* ]] || fail "Invalid destination path: $relative" 1
  IFS='/' read -r -a components <<< "$relative"
  for component in "${components[@]}"; do
    [[ "$component" != '.' && "$component" != '..' && "$component" =~ ^[a-zA-Z0-9._-]+$ ]] || fail "Invalid destination component: $component" 1
  done
}

# Resolve an explicitly selected root without creating it. Missing components
# remain beneath the nearest existing directory; system /tmp aliases are fine.
physical_root() {
  local candidate="$1" missing='' component
  [[ "$candidate" == /* ]] || fail 'User configuration roots must be absolute paths.'
  while [[ "$candidate" != '/' && "$candidate" == */ ]]; do candidate="${candidate%/}"; done
  case "/${candidate#/}/" in
    */../*|*/./*) fail 'User configuration roots must not contain . or .. components.' ;;
  esac
  while [[ ! -d "$candidate" ]]; do
    [[ ! -e "$candidate" && ! -L "$candidate" ]] || fail "Configuration root is not a directory: $candidate"
    component="${candidate##*/}"
    missing="/$component$missing"
    candidate="${candidate%/*}"
    [[ -n "$candidate" ]] || candidate='/'
  done
  candidate="$(cd "$candidate" && pwd -P)"
  if [[ "$candidate" == '/' ]]; then
    printf '/%s\n' "${missing#/}"
  else
    printf '%s%s\n' "$candidate" "$missing"
  fi
}

# Specific host variables use the upstream trimmed value. Empty values use the
# documented default. Relative explicit values fail instead of writing to cwd.
host_root() {
  local value="$1" fallback="$2"
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  if [[ -n "$value" ]]; then
    install_root="$(physical_root "$value")"
  else
    install_root="$install_home"
    relative="$fallback/$relative"
  fi
}

if [[ "$scope" == 'project' ]]; then
  install_root="$(pwd -P)"
  relative="$project_path"
else
  [[ -n "${HOME:-}" && "$HOME" == /* && -d "$HOME" ]] || fail 'HOME must identify an existing absolute directory for user scope.'
  install_home="$(cd "$HOME" && pwd -P)"
  [[ "$user_path" =~ ^\{([A-Z_]+)\}/(.+)$ ]] || fail "Invalid user destination for $agent" 1
  root_token="${BASH_REMATCH[1]}"
  relative="${BASH_REMATCH[2]}"
  case "$root_token" in
    HOME) install_root="$install_home" ;;
    XDG_CONFIG_HOME)
      if [[ "${XDG_CONFIG_HOME:-}" == /* ]]; then
        install_root="$(physical_root "$XDG_CONFIG_HOME")"
      else
        install_root="$install_home"
        relative=".config/$relative"
      fi
      ;;
    CLAUDE_CONFIG_DIR) host_root "${CLAUDE_CONFIG_DIR:-}" '.claude' ;;
    AUTOHAND_HOME) host_root "${AUTOHAND_HOME:-}" '.autohand' ;;
    GROK_HOME) host_root "${GROK_HOME:-}" '.grok' ;;
    HERMES_HOME) host_root "${HERMES_HOME:-}" '.hermes' ;;
    VIBE_HOME) host_root "${VIBE_HOME:-}" '.vibe' ;;
    OPENCLAW_HOME)
      install_root="$install_home"
      openclaw_dir='.openclaw'
      if [[ -e "$install_home/.openclaw" ]]; then :
      elif [[ -e "$install_home/.clawdbot" ]]; then openclaw_dir='.clawdbot'
      elif [[ -e "$install_home/.moltbot" ]]; then openclaw_dir='.moltbot'
      fi
      relative="$openclaw_dir/$relative"
      ;;
    *) fail "Unsupported registry root: $root_token" 1 ;;
  esac
fi
validate_relative_path "$relative"
if [[ "$kind" == 'skill' ]]; then
  relative="$relative/asdify"
  source="$repo/skills/asdify"
else
  source="$repo/integrations/cursor-rule.mdc"
fi
dest="${install_root%/}/$relative"
parent="${dest%/*}"

# A symlink at the final destination is replaceable with --force. Ancestors
# beneath the chosen root must be real directories, so copying stays in scope.
check_ancestors() {
  local current="$install_root" component parent_relative="${relative%/*}"
  local -a components
  IFS='/' read -r -a components <<< "$parent_relative"
  for component in "${components[@]}"; do
    current="${current%/}/$component"
    [[ ! -L "$current" ]] || fail "Refusing symlink ancestor: $current" 1
    [[ ! -e "$current" || -d "$current" ]] || fail "Destination parent is not a directory: $current" 1
  done
}
check_destination() {
  if [[ -e "$dest" || -L "$dest" ]]; then
    [[ "$force" == 'true' ]] || fail "Refusing to overwrite $dest. Review it before adding --force." 1
    [[ "$kind" != 'rule' || ! -d "$dest" || -L "$dest" ]] || fail "Refusing to replace a directory with a rule file: $dest" 1
  fi
}
check_ancestors
check_destination
mkdir -p "$parent"
check_ancestors
stage="$(mktemp -d "$parent/.asdify.XXXXXXXX")"
installed='false'
cleanup() {
  local status="$?" keep='false'
  if [[ "$installed" != 'true' && ( -e "$stage/previous" || -L "$stage/previous" ) ]]; then
    if [[ ! -e "$dest" && ! -L "$dest" ]] && mv "$stage/previous" "$dest"; then
      :
    else
      printf 'Previous install preserved at %s\n' "$stage/previous" >&2
      keep='true'
    fi
  fi
  [[ "$keep" == 'true' ]] || rm -rf "$stage"
  return "$status"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
if [[ "$kind" == 'skill' ]]; then cp -R "$source" "$stage/new"; else cp "$source" "$stage/new"; fi
check_ancestors
check_destination
if [[ -e "$dest" || -L "$dest" ]]; then mv "$dest" "$stage/previous"; fi
mv "$stage/new" "$dest"
installed='true'
printf 'Installed %s (%s): %s\n' "$agent" "$scope" "$dest"
