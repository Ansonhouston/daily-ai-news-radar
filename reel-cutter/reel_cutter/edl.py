"""Load, validate and measure a reel EDL (edit decision list)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# Cantonese VO pacing, measured in "units" per second. A unit is one CJK
# character or one run of Latin/digits — roughly one spoken syllable-group.
COMFORTABLE_UPS = 5.5
MAX_UPS = 6.8
MIN_UPS = 3.0

_CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿]")
_LATIN_RUN = re.compile(r"[A-Za-z0-9]+")


def count_units(text: str) -> int:
    """Approximate spoken length of mixed Cantonese/English VO."""
    if not text:
        return 0
    return len(_CJK.findall(text)) + len(_LATIN_RUN.findall(text))


@dataclass
class Segment:
    id: str
    start: float
    end: float
    vo: str = ""
    sub: str = ""
    sub_style: str = "body"
    beat: str = ""
    shot: str = ""
    source: str | None = None
    in_point: float = 0.0
    sfx: str = ""

    @property
    def duration(self) -> float:
        return round(self.end - self.start, 3)

    @property
    def units(self) -> int:
        return count_units(self.vo)

    @property
    def ups(self) -> float:
        """Units per second — how hard the VO has to be rushed."""
        return self.units / self.duration if self.duration > 0 else 0.0


@dataclass
class EndCard:
    start: float
    end: float
    text: str


@dataclass
class Edl:
    title: str
    segments: list[Segment]
    width: int = 1080
    height: int = 1920
    fps: int = 30
    style: dict = field(default_factory=dict)
    audio: dict = field(default_factory=dict)
    end_card: EndCard | None = None
    root: Path = field(default_factory=Path)

    @property
    def duration(self) -> float:
        last = self.segments[-1].end if self.segments else 0.0
        if self.end_card:
            last = max(last, self.end_card.end)
        return round(last, 3)

    def resolve(self, relative: str | None) -> Path | None:
        if not relative:
            return None
        p = Path(relative)
        return p if p.is_absolute() else (self.root / p)

    def source_for(self, seg: Segment) -> Path | None:
        """The segment's footage, or None when it has not been shot yet."""
        p = self.resolve(seg.source)
        return p if p and p.is_file() else None


class EdlError(ValueError):
    pass


def load(path: str | Path) -> Edl:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))

    segments = [
        Segment(
            id=s["id"],
            start=float(s["start"]),
            end=float(s["end"]),
            vo=s.get("vo", ""),
            sub=s.get("sub", ""),
            sub_style=s.get("sub_style", "body"),
            beat=s.get("beat", ""),
            shot=s.get("shot", ""),
            source=s.get("source"),
            in_point=float(s.get("in", 0.0)),
            sfx=s.get("sfx", ""),
        )
        for s in data.get("segments", [])
    ]

    res = data.get("resolution", [1080, 1920])
    ec = data.get("end_card")

    edl = Edl(
        title=data.get("title", path.stem),
        segments=segments,
        width=int(res[0]),
        height=int(res[1]),
        fps=int(data.get("fps", 30)),
        style=data.get("style", {}),
        audio=data.get("audio", {}),
        end_card=EndCard(float(ec["start"]), float(ec["end"]), ec["text"]) if ec else None,
        # EDL paths are relative to the EDL file's parent's parent, i.e. the
        # project root, so `edl/foo.json` can point at `media/bar.mov`.
        root=path.resolve().parent.parent,
    )
    validate(edl)
    return edl


def validate(edl: Edl) -> None:
    """Structural checks. Pacing problems are warnings, not errors."""
    if not edl.segments:
        raise EdlError("EDL has no segments")

    prev: Segment | None = None
    for seg in edl.segments:
        if seg.end <= seg.start:
            raise EdlError(f"{seg.id}: end ({seg.end}) must be after start ({seg.start})")
        if prev is not None:
            if seg.start < prev.end - 1e-6:
                raise EdlError(f"{seg.id} starts at {seg.start} but {prev.id} runs to {prev.end}")
            if seg.start > prev.end + 1e-6:
                raise EdlError(
                    f"gap of {seg.start - prev.end:.2f}s between {prev.id} and {seg.id}; "
                    "segments must be contiguous"
                )
        if seg.sub_style not in ("body", "hook"):
            raise EdlError(f"{seg.id}: unknown sub_style {seg.sub_style!r}")
        prev = seg

    if edl.end_card:
        if edl.end_card.end <= edl.end_card.start:
            raise EdlError("end_card: end must be after start")
        if edl.end_card.start < edl.segments[-1].end - 1e-6:
            raise EdlError("end_card must start at or after the last segment ends")


def pacing_warnings(edl: Edl) -> list[str]:
    """Segments whose VO cannot be delivered comfortably in the time given."""
    warnings: list[str] = []
    for seg in edl.segments:
        if not seg.vo:
            continue
        if seg.ups > MAX_UPS:
            need = seg.units / COMFORTABLE_UPS
            warnings.append(
                f"{seg.id}: {seg.ups:.1f} units/s is too fast "
                f"(cut ~{seg.units - int(seg.duration * COMFORTABLE_UPS)} units "
                f"or give it {need:.1f}s)"
            )
        elif seg.ups < MIN_UPS:
            warnings.append(
                f"{seg.id}: {seg.ups:.1f} units/s is very slow — "
                f"tighten to ~{seg.units / COMFORTABLE_UPS:.1f}s or add a line"
            )
    return warnings


def missing_media(edl: Edl) -> list[Segment]:
    return [s for s in edl.segments if edl.source_for(s) is None]
