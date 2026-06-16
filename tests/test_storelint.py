#!/usr/bin/env python3
"""Tests for scripts/storelint.py — the leaked-harness-tag guard, and the one duplication we can't delete.

`LEAK_RE` lives canonically in storelint, but `fc.py` keeps its own copy because it ships self-contained with
the `/research-company` skill across the repo boundary (it can't import a sibling). That copy is the only
"keep in sync" mirror we accept — so it gets the test that makes the sync mechanical instead of a code comment:
the two source lines must stay byte-identical. Everything else collapses to one home; this one is asserted."""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import storelint  # noqa: E402 — after the sys.path insert above


def _leak_re_line(path: Path) -> str:
    """The verbatim `LEAK_RE = re.compile(...)` source line, so the compare catches a pattern OR flag drift."""
    m = re.search(r"^LEAK_RE = re\.compile\(.*\)\s*$", path.read_text(encoding="utf-8"), re.M)
    return m.group(0).rstrip() if m else ""


class LeakReMirror(unittest.TestCase):
    def test_fc_mirror_is_byte_identical(self) -> None:
        canonical = _leak_re_line(ROOT / "scripts" / "storelint.py")
        mirror = _leak_re_line(ROOT / "skills" / "research-company" / "scripts" / "fc.py")
        self.assertTrue(canonical, "no LEAK_RE line found in storelint.py")
        self.assertTrue(mirror, "no LEAK_RE line found in fc.py")
        self.assertEqual(canonical, mirror, "fc.py's LEAK_RE drifted from storelint's — change both together.")


class LeakedTags(unittest.TestCase):
    def test_catches_harness_tag_ignores_url_placeholder(self) -> None:
        hits = storelint.leaked_tags("ok line\n</invoke> trailing\nvisit /drug/<slug>/dose")
        self.assertEqual([tag for _, tag in hits], ["</invoke>"])  # the placeholder <slug> must not match


if __name__ == "__main__":
    unittest.main()
