"""Resolve a usable Traditional-Chinese font family for libass."""

from __future__ import annotations

import shutil
import subprocess

# Order matters: first family actually installed wins.
PREFERRED = [
    "Noto Sans HK",
    "Noto Sans CJK HK",
    "Noto Sans TC",
    "Noto Sans CJK TC",
    "Source Han Sans HC",
    "Source Han Sans TC",
    "PingFang HK",
    "Hiragino Sans CNS",
    "Microsoft JhengHei",
    "WenQuanYi Zen Hei",
]

FALLBACK = "sans-serif"


def installed_families() -> set[str]:
    """Every font family fontconfig knows about, lowercased."""
    if not shutil.which("fc-list"):
        return set()
    out = subprocess.run(
        ["fc-list", "--format", "%{family}\n"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout
    families: set[str] = set()
    for line in out.splitlines():
        for name in line.split(","):
            name = name.strip()
            if name:
                families.add(name.lower())
    return families


def resolve(preferred: str | None = None) -> str:
    """Pick a font family name to hand to libass.

    An explicit `preferred` is honoured even when fontconfig cannot confirm it —
    the caller may be rendering on a machine whose fonts differ from this one.
    """
    if preferred:
        return preferred
    have = installed_families()
    for family in PREFERRED:
        if family.lower() in have:
            return family
    return FALLBACK
