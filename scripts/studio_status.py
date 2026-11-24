#!/usr/bin/env python3
"""studio_status.py — Live multi-channel inventory & status report for sis studio."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANNELS_DIR = ROOT / "channels"


def extract_field(text: str, label: str) -> str:
    pattern = rf"^\s*-\s*\*\*{re.escape(label)}:\*\*\s*(.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return "-"
    return match.group(1).strip()


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def scan_channels() -> list[dict[str, object]]:
    if not CHANNELS_DIR.is_dir():
        return []
    rows: list[dict[str, object]] = []
    for ch_dir in sorted(p for p in CHANNELS_DIR.iterdir() if p.is_dir()):
        md = ch_dir / "CHANNEL.md"
        text = md.read_text(encoding="utf-8") if md.is_file() else ""
        ep_dir = ch_dir / "episodes"
        episodes = (
            sorted(p.name for p in ep_dir.iterdir() if p.name != ".gitkeep")
            if ep_dir.is_dir()
            else []
        )
        rows.append(
            {
                "slug": ch_dir.name,
                "title": extract_title(text, ch_dir.name),
                "status": extract_field(text, "Durum"),
                "format": extract_field(text, "Format Kilidi"),
                "mode": extract_field(text, "Üretim Modu"),
                "voice": extract_field(text, "Ses Motoru"),
                "episode_count": len(episodes),
                "latest_episode": episodes[-1] if episodes else None,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect all 12 sis channels.")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    rows = scan_channels()
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0

    print("| Kanal | Durum | Format | Bölüm Sayısı |")
    print("| :--- | :--- | :--- | :---: |")
    for r in rows:
        print(f"| {r['title']} | {r['status']} | {r['format']} | {r['episode_count']} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
