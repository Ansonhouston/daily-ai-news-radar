"""Build burn-in ASS subtitles (and a plain SRT) from an EDL."""

from __future__ import annotations

from .edl import Edl
from .fonts import resolve as resolve_font

WHITE = "&H00FFFFFF"
BLACK = "&H00000000"
SLATE_GREY = "&H00C8C8C8"
SHADOW = "&H80000000"


def ass_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int(seconds % 3600 // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def srt_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int(seconds % 3600 // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms == 1000:  # rounding spilled over
        s, ms = s + 1, 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _escape(text: str) -> str:
    return text.replace("\\", "").replace("\n", "\\N").replace("{", "(").replace("}", ")")


def build_ass(edl: Edl, animatic: bool = False) -> str:
    """Full ASS document.

    `animatic` adds a slate line at the top of frame naming the segment, its
    beat and its shot, so a footage-free preview still reads as a plan.
    """
    st = edl.style
    font = resolve_font(st.get("font"))
    body = int(st.get("body_size", 68))
    hook = int(st.get("hook_size", 108))
    slate = int(st.get("slate_size", 40))
    outline = int(st.get("outline", 6))
    margin_v = int(st.get("body_margin_v", 320))
    side = int(st.get("side_margin", 90))

    def style_line(name, size, align, mv, primary=WHITE, bold=-1):
        return (
            f"Style: {name},{font},{size},{primary},{primary},{BLACK},{SHADOW},"
            f"{bold},0,0,0,100,100,0,0,1,{outline},0,{align},{side},{side},{mv},1"
        )

    head = [
        "[Script Info]",
        f"; {edl.title}",
        "ScriptType: v4.00+",
        f"PlayResX: {edl.width}",
        f"PlayResY: {edl.height}",
        "WrapStyle: 0",
        "ScaledBorderAndShadow: yes",
        "YCbCr Matrix: TV.709",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour,"
        " BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle,"
        " BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        style_line("BODY", body, 2, margin_v),          # bottom centre
        style_line("HOOK", hook, 5, 0),                 # dead centre
        style_line("ENDCARD", hook, 5, 0),
        style_line("SLATE", slate, 8, 120, SLATE_GREY), # top centre, animatic only
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]

    events: list[str] = []

    def event(start, end, style, text, layer=0):
        events.append(
            f"Dialogue: {layer},{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{_escape(text)}"
        )

    for seg in edl.segments:
        if seg.sub:
            style = "HOOK" if seg.sub_style == "hook" else "BODY"
            # Pull in 80ms so the cut lands before the words do.
            event(seg.start + 0.08, seg.end - 0.04, style, seg.sub)
        if animatic:
            label = f"{seg.id}  {seg.start:.1f}–{seg.end:.1f}s  ·  {seg.beat}"
            if seg.shot:
                label += f"\n{seg.shot}"
            event(seg.start, seg.end, "SLATE", label, layer=1)

    if edl.end_card:
        event(edl.end_card.start, edl.end_card.end, "ENDCARD", edl.end_card.text)

    return "\n".join(head + events) + "\n"


def build_srt(edl: Edl) -> str:
    """Plain SRT of the spoken VO — for captions, repurposing, or Filmora."""
    out: list[str] = []
    n = 0
    for seg in edl.segments:
        if not seg.vo:
            continue
        n += 1
        out.append(str(n))
        out.append(f"{srt_time(seg.start)} --> {srt_time(seg.end)}")
        out.append(seg.vo)
        out.append("")
    return "\n".join(out) + "\n" if out else ""
