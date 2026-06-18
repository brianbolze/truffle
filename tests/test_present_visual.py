#!/usr/bin/env python3
"""Regression tests for the brief's visual-evidence tile handling."""

from __future__ import annotations

import base64
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from present import assets, model  # noqa: E402


class VisualTileAssetTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._orig_store = assets.STORE
        self._orig_imgcache = assets.IMGCACHE
        assets.STORE = str(self.root / "store")
        assets.IMGCACHE = str(self.root / "_out" / ".imgcache")

    def tearDown(self) -> None:
        assets.STORE = self._orig_store
        assets.IMGCACHE = self._orig_imgcache
        self._tmp.cleanup()

    def test_load_tile_falls_back_to_archived_capture_date(self) -> None:
        tile_path = "store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
        archived = self.root / "store" / "ro-co" / "captures" / "_archive" / "2026-06-04" / "tiles" / "homepage"
        archived.mkdir(parents=True)
        (archived / "tile-00-y00000.png").write_bytes(b"fake png")

        with patch.object(assets.subprocess, "run", return_value=SimpleNamespace(returncode=1)):
            data = assets.load_tile(tile_path)

        self.assertEqual(data, "data:image/png;base64," + base64.b64encode(b"fake png").decode())


class VisualTileSelectionTests(unittest.TestCase):
    def test_warns_when_cards_have_tile_paths_but_none_resolve(self) -> None:
        cards_md = """```yaml
- id: typography_01
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: Strong hero hierarchy.
- id: layout_01
  polarity: mixed
  page_or_region: pricing cards
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: Pricing cards are consistent.
```"""
        err = io.StringIO()
        with patch.object(model, "load_tile", return_value=None), contextlib.redirect_stderr(err):
            self.assertEqual(model._select_visual_tiles(cards_md, slug="ro-co"), [])

        self.assertIn("warning: visual tile strip for ro-co requested 2 tile path(s), resolved 0", err.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
