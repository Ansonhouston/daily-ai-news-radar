"""Unit tests — run with `python3 -m unittest discover -s tests` from reel-cutter/."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from reel_cutter import edl as edl_mod  # noqa: E402
from reel_cutter import subtitles  # noqa: E402

REPO_EDL = Path(__file__).resolve().parent.parent / "edl" / "ai-agent-3-levels-52s.json"


def write_edl(segments, **extra):
    data = {"title": "t", "resolution": [1080, 1920], "fps": 30, "segments": segments}
    data.update(extra)
    tmp = Path(tempfile.mkdtemp()) / "edl"
    tmp.mkdir()
    path = tmp / "x.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


class TestUnitCount(unittest.TestCase):
    def test_counts_cjk_chars_individually(self):
        self.assertEqual(edl_mod.count_units("你仲係"), 3)

    def test_counts_latin_runs_as_one_unit(self):
        self.assertEqual(edl_mod.count_units("用 ChatGPT"), 2)

    def test_ignores_punctuation(self):
        self.assertEqual(edl_mod.count_units("你好，世界！"), 4)

    def test_empty(self):
        self.assertEqual(edl_mod.count_units(""), 0)


class TestValidation(unittest.TestCase):
    def test_rejects_gap_between_segments(self):
        path = write_edl([
            {"id": "A", "start": 0, "end": 2},
            {"id": "B", "start": 3, "end": 4},
        ])
        with self.assertRaisesRegex(edl_mod.EdlError, "gap"):
            edl_mod.load(path)

    def test_rejects_overlap(self):
        path = write_edl([
            {"id": "A", "start": 0, "end": 3},
            {"id": "B", "start": 2, "end": 4},
        ])
        with self.assertRaisesRegex(edl_mod.EdlError, "runs to"):
            edl_mod.load(path)

    def test_rejects_zero_length_segment(self):
        path = write_edl([{"id": "A", "start": 1, "end": 1}])
        with self.assertRaisesRegex(edl_mod.EdlError, "must be after"):
            edl_mod.load(path)

    def test_rejects_end_card_before_last_segment(self):
        path = write_edl(
            [{"id": "A", "start": 0, "end": 5}],
            end_card={"start": 3, "end": 6, "text": "x"},
        )
        with self.assertRaisesRegex(edl_mod.EdlError, "end_card"):
            edl_mod.load(path)

    def test_accepts_contiguous_segments(self):
        path = write_edl([
            {"id": "A", "start": 0, "end": 2},
            {"id": "B", "start": 2, "end": 4},
        ])
        self.assertEqual(edl_mod.load(path).duration, 4.0)


class TestPacing(unittest.TestCase):
    def test_flags_vo_that_is_too_fast(self):
        path = write_edl([{"id": "A", "start": 0, "end": 1, "vo": "一二三四五六七八九十"}])
        warnings = edl_mod.pacing_warnings(edl_mod.load(path))
        self.assertTrue(any("too fast" in w for w in warnings))

    def test_flags_vo_that_is_too_slow(self):
        path = write_edl([{"id": "A", "start": 0, "end": 10, "vo": "一二"}])
        warnings = edl_mod.pacing_warnings(edl_mod.load(path))
        self.assertTrue(any("very slow" in w for w in warnings))

    def test_silent_segment_is_never_flagged(self):
        path = write_edl([{"id": "A", "start": 0, "end": 10, "vo": ""}])
        self.assertEqual(edl_mod.pacing_warnings(edl_mod.load(path)), [])

    def test_shipped_script_is_deliverable(self):
        """The 52s reel must stay recordable at a natural Cantonese pace."""
        e = edl_mod.load(REPO_EDL)
        self.assertEqual(edl_mod.pacing_warnings(e), [])
        self.assertAlmostEqual(e.duration, 52.5, places=2)


class TestSubtitles(unittest.TestCase):
    def setUp(self):
        self.edl = edl_mod.load(REPO_EDL)

    def test_ass_declares_target_resolution(self):
        ass = subtitles.build_ass(self.edl)
        self.assertIn("PlayResX: 1080", ass)
        self.assertIn("PlayResY: 1920", ass)

    def test_hook_and_body_use_different_alignment(self):
        ass = subtitles.build_ass(self.edl)
        body = next(l for l in ass.splitlines() if l.startswith("Style: BODY"))
        hook = next(l for l in ass.splitlines() if l.startswith("Style: HOOK"))
        self.assertEqual(body.split(",")[18], "2")   # bottom centre
        self.assertEqual(hook.split(",")[18], "5")   # dead centre

    def test_newlines_become_ass_line_breaks(self):
        ass = subtitles.build_ass(self.edl)
        self.assertIn("\\N", ass)
        dialogue = [l for l in ass.splitlines() if l.startswith("Dialogue:")]
        self.assertTrue(all("\n" not in l for l in dialogue))

    def test_braces_cannot_inject_ass_override_tags(self):
        path = write_edl([{"id": "A", "start": 0, "end": 2, "sub": "{\\fs200}boom"}])
        ass = subtitles.build_ass(edl_mod.load(path))
        self.assertNotIn("{\\fs200}", ass)

    def test_animatic_adds_slates_and_default_does_not(self):
        self.assertIn(",SLATE,", subtitles.build_ass(self.edl, animatic=True))
        self.assertNotIn(",SLATE,", subtitles.build_ass(self.edl, animatic=False))

    def test_end_card_is_emitted(self):
        self.assertIn(",ENDCARD,", subtitles.build_ass(self.edl))

    def test_ass_time_format(self):
        self.assertEqual(subtitles.ass_time(0), "0:00:00.00")
        self.assertEqual(subtitles.ass_time(52.5), "0:00:52.50")
        self.assertEqual(subtitles.ass_time(3671.25), "1:01:11.25")

    def test_srt_time_format(self):
        self.assertEqual(subtitles.srt_time(0), "00:00:00,000")
        self.assertEqual(subtitles.srt_time(52.5), "00:00:52,500")

    def test_srt_carries_every_spoken_line(self):
        srt = subtitles.build_srt(self.edl)
        spoken = [s for s in self.edl.segments if s.vo]
        self.assertEqual(srt.count("-->"), len(spoken))
        self.assertIn(spoken[0].vo, srt)


if __name__ == "__main__":
    unittest.main()
