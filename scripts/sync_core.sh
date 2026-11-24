#!/usr/bin/env bash
# sync_core.sh — Pull latest CONTENTY core changes into sis/core submodule.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git submodule sync -- core
git submodule update --init --remote --merge core
echo "core/ alt modulu guncellendi:"
git submodule status core
