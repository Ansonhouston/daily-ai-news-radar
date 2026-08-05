"""reel-cutter — EDL-driven 9:16 reel assembly with burned-in Cantonese subs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import edl as edl_mod
from . import render as render_mod
from . import subtitles
from .fonts import resolve as resolve_font


def _load(path: str) -> edl_mod.Edl:
    try:
        return edl_mod.load(path)
    except (OSError, ValueError) as exc:
        sys.exit(f"error: {exc}")


def cmd_validate(args) -> int:
    e = _load(args.edl)
    print(f"{e.title}")
    print(f"  {len(e.segments)} segments · {e.duration:.2f}s · "
          f"{e.width}x{e.height} @ {e.fps}fps · font: {resolve_font(e.style.get('font'))}")
    print()
    print(f"  {'seg':<5}{'span':<16}{'dur':>6}{'units':>7}{'u/s':>7}  beat")
    for s in e.segments:
        flag = "  " if edl_mod.MIN_UPS <= s.ups <= edl_mod.MAX_UPS or not s.vo else "! "
        print(f"{flag}{s.id:<5}{f'{s.start:.1f}–{s.end:.1f}s':<16}"
              f"{s.duration:>5.1f}s{s.units:>7}{s.ups:>7.1f}  {s.beat}")

    warnings = edl_mod.pacing_warnings(e)
    missing = edl_mod.missing_media(e)
    print()
    if warnings:
        print("pacing:")
        for w in warnings:
            print(f"  ! {w}")
    else:
        print("pacing: every segment sits in a comfortable Cantonese delivery range")

    if missing:
        print(f"\nfootage: {len(missing)}/{len(e.segments)} segments still need a clip")
        for s in missing:
            print(f"  · {s.id} {s.source or '(no source set)'} — {s.shot}")
        print("  → `animatic` renders these as timed slates so you can check pacing now")
    else:
        print("\nfootage: all segments have media")
    return 1 if warnings else 0


def cmd_subs(args) -> int:
    e = _load(args.edl)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(subtitles.build_ass(e, animatic=args.animatic), encoding="utf-8")
    print(f"wrote {out}")
    if args.srt:
        srt = Path(args.srt)
        srt.parent.mkdir(parents=True, exist_ok=True)
        srt.write_text(subtitles.build_srt(e), encoding="utf-8")
        print(f"wrote {srt}")
    return 0


def _render(args, animatic: bool) -> int:
    e = _load(args.edl)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    ass_path = out.with_suffix(".ass")
    ass_path.write_text(subtitles.build_ass(e, animatic=animatic), encoding="utf-8")

    try:
        cmd = render_mod.build_command(
            e, ass_path, out, animatic=animatic, crf=args.crf, preset=args.preset
        )
    except render_mod.RenderError as exc:
        sys.exit(f"error: {exc}")

    if args.dry_run:
        print(" ".join(cmd))
        return 0

    missing = edl_mod.missing_media(e)
    if missing and not animatic:
        print(f"note: {len(missing)} segment(s) have no footage — rendering them as slates")

    print(f"rendering {e.duration:.2f}s → {out}")
    try:
        render_mod.run(cmd, verbose=args.verbose)
    except render_mod.RenderError as exc:
        sys.exit(f"error: {exc}")
    print(f"done: {out} ({out.stat().st_size / 1_000_000:.1f} MB)")
    print(f"subs: {ass_path}")
    return 0


def cmd_animatic(args) -> int:
    return _render(args, animatic=True)


def cmd_render(args) -> int:
    return _render(args, animatic=False)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="reel-cutter", description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)

    v = sub.add_parser("validate", help="check timing, VO pacing and missing footage")
    v.add_argument("edl")
    v.set_defaults(func=cmd_validate)

    s = sub.add_parser("subs", help="write burn-in .ass (and optional .srt)")
    s.add_argument("edl")
    s.add_argument("-o", "--output", required=True)
    s.add_argument("--srt")
    s.add_argument("--animatic", action="store_true", help="include shot slates")
    s.set_defaults(func=cmd_subs)

    for name, fn, helptext in (
        ("animatic", cmd_animatic, "timed preview with slates — no footage needed"),
        ("render", cmd_render, "final cut from the EDL's footage"),
    ):
        r = sub.add_parser(name, help=helptext)
        r.add_argument("edl")
        r.add_argument("-o", "--output", required=True)
        r.add_argument("--crf", type=int, default=19)
        r.add_argument("--preset", default="medium")
        r.add_argument("--dry-run", action="store_true", help="print the ffmpeg command only")
        r.add_argument("--verbose", action="store_true", help="stream ffmpeg output")
        r.set_defaults(func=fn)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
