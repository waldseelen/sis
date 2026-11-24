#!/usr/bin/env bash
# setup.sh — Link sis + core (CONTENTY) skills/plugins for Antigravity, Claude Code, or OpenCode.
# Idempotent; does NOT download AI models or pip packages automatically.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-all}"

if [[ ! -d "$ROOT/core/skills" ]]; then
  echo "HATA: core/ alt modulu bos gorunuyor. Once su komutu calistir:" >&2
  echo "  git submodule update --init --recursive" >&2
  exit 1
fi

link_antigravity() {
  local dest="$HOME/.gemini/config/plugins/contenty-studio"
  mkdir -p "$dest"
  cp -f "$ROOT/core/plugins/contenty-studio/plugin.json" "$dest/"
  cp -f "$ROOT/core/plugins/contenty-studio/README.md" "$dest/"
  cp -Rf "$ROOT/core/plugins/contenty-studio/rules" "$dest/"
  ln -sfn "$ROOT/core/skills" "$dest/skills"
  echo "[Antigravity] Eklenti ve core skill'ler baglandi -> $dest"
}

link_claude() {
  local dest="$HOME/.claude/skills"
  mkdir -p "$dest"
  for dir in "$ROOT"/core/skills/*/; do
    local name
    name="$(basename "$dir")"
    ln -sfn "$dir" "$dest/$name"
  done
  echo "[Claude Code] Core skill'ler baglandi -> $dest"
}

link_opencode() {
  echo "[OpenCode] Kök AGENTS.md -> CLAUDE.md dogrudan otomatik okunur (ek baglanti gerekmez)."
}

case "$TARGET" in
  antigravity) link_antigravity ;;
  claude) link_claude ;;
  opencode) link_opencode ;;
  all)
    link_antigravity
    link_claude
    link_opencode
    ;;
  *)
    echo "Kullanim: $0 [antigravity|claude|opencode|all]" >&2
    exit 1
    ;;
esac

echo "Not: Hicbir AI modeli veya pip paketi otomatik indirilmedi (playbooks/tts-and-music-stack.md)."
