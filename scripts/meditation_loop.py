#!/usr/bin/env python3
"""meditation_loop.py — Build 1-8h seamless ambient meditation videos with low CPU cost.

Creates a sample-continuous audio loop unit via crossfading the stem's tail into its head,
then streams it to the target duration alongside a static image or short seamless video loop.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


class LoopBuildError(RuntimeError):
    """Structured domain error for meditation loop rendering."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"[{code}] {message}")
        self.code = code


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build 1-8h seamless silent Stoic/meditation video loops."
    )
    parser.add_argument("--audio", required=True, type=Path, help="Input 3-5 min ambient audio stem")
    media = parser.add_mutually_exclusive_group(required=True)
    media.add_argument("--image", type=Path, help="Static 16:9 background image")
    media.add_argument("--video", type=Path, help="Short seamless background video loop")
    dur = parser.add_mutually_exclusive_group(required=True)
    dur.add_argument("--hours", type=float, help="Target duration in hours (e.g. 1, 3, 8)")
    dur.add_argument("--seconds", type=float, help="Target duration in seconds")
    parser.add_argument("--output", required=True, type=Path, help="Output MP4 path")
    parser.add_argument("--crossfade", type=float, default=4.0, help="Seam crossfade seconds (default: 4.0)")
    parser.add_argument("--lufs", type=float, default=-18.0, help="Target integrated LUFS (default: -18.0)")
    parser.add_argument("--width", type=int, default=1920, help="Output width (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Output height (default: 1080)")
    parser.add_argument("--fps", type=int, default=24, help="Video fps (default: 24; image mode uses 2 fps)")
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs and print commands without rendering")
    return parser.parse_args(argv)


def require_binary(name: str) -> str:
    found = shutil.which(name)
    if not found:
        raise LoopBuildError("MISSING_BIN", f"Required binary not found on PATH: {name}")
    return found


def probe_duration(path: Path) -> float:
    ffprobe = require_binary("ffprobe")
    cmd = [
        ffprobe,
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise LoopBuildError("FFPROBE_FAILED", proc.stderr.strip() or f"Could not probe {path}")
    try:
        duration = float(proc.stdout.strip())
    except ValueError as exc:
        raise LoopBuildError("INVALID_DURATION", f"Unexpected ffprobe duration output: {proc.stdout!r}") from exc
    if duration <= 0:
        raise LoopBuildError("INVALID_DURATION", f"Non-positive audio duration: {duration}")
    return duration


def build_seam_unit_cmd(
    ffmpeg: str,
    audio_path: Path,
    unit_path: Path,
    stem_duration: float,
    crossfade: float,
) -> list[str]:
    if crossfade <= 0:
        return [
            ffmpeg, "-y", "-i", str(audio_path),
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(unit_path),
        ]
    if stem_duration <= 2.5 * crossfade:
        raise LoopBuildError(
            "STEM_TOO_SHORT",
            f"Audio stem ({stem_duration:.2f}s) must exceed 2.5x crossfade ({crossfade:.2f}s).",
        )
    tail_start = stem_duration - crossfade
    # Blend the tail into the head so wrapping end->start is sample-continuous.
    filter_complex = (
        f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=3[a_tail][a_head][a_body];"
        f"[a_tail]atrim=start={tail_start:.4f}:end={stem_duration:.4f},asetpts=PTS-STARTPTS,"
        f"afade=t=out:st=0:d={crossfade:.4f}:curve=tri[tail_f];"
        f"[a_head]atrim=start=0:end={crossfade:.4f},asetpts=PTS-STARTPTS,"
        f"afade=t=in:st=0:d={crossfade:.4f}:curve=tri[head_f];"
        f"[tail_f][head_f]amix=inputs=2:duration=shortest:normalize=0[seam];"
        f"[a_body]atrim=start={crossfade:.4f}:end={tail_start:.4f},asetpts=PTS-STARTPTS[body];"
        f"[seam][body]concat=n=2:v=0:a=1[outa]"
    )
    return [
        ffmpeg, "-y", "-i", str(audio_path),
        "-filter_complex", filter_complex,
        "-map", "[outa]",
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        str(unit_path),
    ]


def build_render_cmd(
    ffmpeg: str,
    unit_path: Path,
    args: argparse.Namespace,
    target_seconds: float,
) -> list[str]:
    scale_pad = (
        f"scale={args.width}:{args.height}:force_original_aspect_ratio=decrease,"
        f"pad={args.width}:{args.height}:(ow-iw)/2:(oh-ih)/2,format=yuv420p"
    )
    audio_filter = f"loudnorm=I={args.lufs:.1f}:TP=-1.0:LRA=11"

    if args.image is not None:
        img_fps = min(args.fps, 2)
        return [
            ffmpeg, "-y",
            "-loop", "1", "-framerate", str(img_fps), "-i", str(args.image),
            "-stream_loop", "-1", "-i", str(unit_path),
            "-t", f"{target_seconds:.3f}",
            "-vf", scale_pad,
            "-af", audio_filter,
            "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", "-shortest",
            str(args.output),
        ]

    return [
        ffmpeg, "-y",
        "-stream_loop", "-1", "-i", str(args.video),
        "-stream_loop", "-1", "-i", str(unit_path),
        "-t", f"{target_seconds:.3f}",
        "-vf", f"{scale_pad},fps={args.fps}",
        "-af", audio_filter,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", "-shortest",
        str(args.output),
    ]


def run_step(cmd: list[str], step_name: str) -> None:
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        tail = "\n".join(proc.stderr.splitlines()[-15:])
        raise LoopBuildError("FFMPEG_FAILED", f"{step_name} failed (exit {proc.returncode}):\n{tail}")


def main(argv: list[str] | None = None) -> int:
    try:
        args = parse_args(argv)
        target_seconds = args.seconds if args.seconds is not None else args.hours * 3600.0
        if target_seconds <= 0:
            raise LoopBuildError("INVALID_ARGS", "Target duration must be positive.")
        if args.crossfade < 0:
            raise LoopBuildError("INVALID_ARGS", "Crossfade cannot be negative.")
        if not args.audio.is_file():
            raise LoopBuildError("MISSING_INPUT", f"Audio file not found: {args.audio}")
        visual_path = args.image if args.image is not None else args.video
        if visual_path is None or not visual_path.is_file():
            raise LoopBuildError("MISSING_INPUT", f"Visual file not found: {visual_path}")

        ffmpeg = require_binary("ffmpeg")
        stem_duration = probe_duration(args.audio)

        with tempfile.TemporaryDirectory(prefix="sis_medloop_") as tmp_dir:
            unit_path = Path(tmp_dir) / "loop_unit.wav"
            seam_cmd = build_seam_unit_cmd(ffmpeg, args.audio, unit_path, stem_duration, args.crossfade)
            render_cmd = build_render_cmd(ffmpeg, unit_path, args, target_seconds)

            if args.dry_run:
                print(f"STEM_DURATION={stem_duration:.3f}s TARGET={target_seconds:.3f}s")
                print("SEAM_CMD:", " ".join(seam_cmd))
                print("RENDER_CMD:", " ".join(render_cmd))
                return 0

            args.output.parent.mkdir(parents=True, exist_ok=True)
            run_step(seam_cmd, "seam_unit")
            run_step(render_cmd, "render_loop")
            print(f"OK: {args.output} ({target_seconds:.1f}s)")
            return 0
    except LoopBuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
