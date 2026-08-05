"""Turn an EDL into a finished 9:16 reel with burned-in subtitles."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .edl import Edl, Segment

# Slate colours for segments that have no footage yet — cycled so the animatic
# still has visible cut points.
SLATE_PALETTE = [
    "0x11151C", "0x1B2430", "0x142033", "0x1F1B2E",
    "0x101C1A", "0x241A1A", "0x1A1F2B", "0x0E1A22",
]


class RenderError(RuntimeError):
    pass


def require_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if not exe:
        raise RenderError(
            "ffmpeg not found. macOS: `brew install ffmpeg`. "
            "Debian/Ubuntu: `sudo apt-get install ffmpeg`."
        )
    return exe


def _escape_filter_path(path: Path) -> str:
    """Escape a path for use inside an ffmpeg filter argument."""
    return str(path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


def _video_input(edl: Edl, seg: Segment, index: int) -> tuple[list[str], bool]:
    """ffmpeg input args for one segment. Returns (args, is_real_footage)."""
    src = edl.source_for(seg)
    if src is not None:
        return (
            ["-ss", f"{seg.in_point:.3f}", "-t", f"{seg.duration:.3f}", "-i", str(src)],
            True,
        )
    colour = SLATE_PALETTE[index % len(SLATE_PALETTE)]
    return (
        [
            "-f", "lavfi",
            "-t", f"{seg.duration:.3f}",
            "-i", f"color=c={colour}:s={edl.width}x{edl.height}:r={edl.fps}",
        ],
        False,
    )


def _normalise_chain(edl: Edl, idx: int, duration: float, real: bool) -> str:
    """Force any input to exactly duration @ target resolution, fps and SAR."""
    steps = []
    if real:
        steps.append(
            f"scale={edl.width}:{edl.height}:force_original_aspect_ratio=increase,"
            f"crop={edl.width}:{edl.height}"
        )
    steps.append(f"fps={edl.fps},setsar=1,format=yuv420p")
    # Hold the last frame if the clip is short, then cut to exact length.
    steps.append(f"tpad=stop_mode=clone:stop_duration={duration:.3f}")
    steps.append(f"trim=duration={duration:.3f},setpts=PTS-STARTPTS")
    return f"[{idx}:v]" + ",".join(steps) + f"[v{idx}]"


def build_command(
    edl: Edl,
    ass_path: Path,
    out_path: Path,
    animatic: bool = False,
    crf: int = 19,
    preset: str = "medium",
) -> list[str]:
    exe = require_ffmpeg()
    total = edl.duration

    inputs: list[str] = []
    chains: list[str] = []
    labels: list[str] = []

    for i, seg in enumerate(edl.segments):
        args, real = _video_input(edl, seg, i)
        inputs += args
        chains.append(_normalise_chain(edl, i, seg.duration, real))
        labels.append(f"[v{i}]")

    if edl.end_card:
        i = len(edl.segments)
        dur = edl.end_card.end - edl.end_card.start
        inputs += [
            "-f", "lavfi", "-t", f"{dur:.3f}",
            "-i", f"color=c=black:s={edl.width}x{edl.height}:r={edl.fps}",
        ]
        chains.append(_normalise_chain(edl, i, dur, real=False))
        labels.append(f"[v{i}]")

    n_video = len(labels)
    chains.append(f"{''.join(labels)}concat=n={n_video}:v=1:a=0[vcat]")
    chains.append(f"[vcat]ass='{_escape_filter_path(ass_path)}'[vout]")

    # ---- audio -------------------------------------------------------------
    vo = edl.resolve(edl.audio.get("vo"))
    music = edl.resolve(edl.audio.get("music"))
    vo = vo if vo and vo.is_file() else None
    music = music if music and music.is_file() else None

    audio_labels: list[str] = []
    if vo:
        inputs += ["-i", str(vo)]
        chains.append(f"[{n_video}:a]aresample=48000,apad[avo]")
        audio_labels.append("[avo]")
    if music:
        inputs += ["-i", str(music)]
        idx = n_video + (1 if vo else 0)
        gain = float(edl.audio.get("music_gain_db", -19))
        # Duck the bed further when there is VO to sit under.
        if vo:
            gain += float(edl.audio.get("duck_db", -6))
        chains.append(f"[{idx}:a]aresample=48000,volume={gain:.1f}dB,apad[amus]")
        audio_labels.append("[amus]")

    if not audio_labels:
        inputs += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
        chains.append(f"[{n_video}:a]atrim=duration={total:.3f}[aout]")
    elif len(audio_labels) == 1:
        chains.append(f"{audio_labels[0]}atrim=duration={total:.3f}[aout]")
    else:
        chains.append(
            f"{''.join(audio_labels)}amix=inputs=2:duration=longest:normalize=0,"
            f"atrim=duration={total:.3f}[aout]"
        )

    cmd = [exe, "-hide_banner", "-y"]
    cmd += inputs
    cmd += [
        "-filter_complex", ";".join(chains),
        "-map", "[vout]", "-map", "[aout]",
        "-t", f"{total:.3f}",
        "-c:v", "libx264", "-preset", preset, "-crf", str(crf),
        "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-r", str(edl.fps), "-g", str(edl.fps * 2),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        str(out_path),
    ]
    return cmd


def run(cmd: list[str], verbose: bool = False) -> None:
    result = subprocess.run(
        cmd,
        capture_output=not verbose,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        tail = (result.stderr or "").strip().splitlines()[-25:]
        raise RenderError("ffmpeg failed:\n" + "\n".join(tail))
