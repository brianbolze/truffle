#!/usr/bin/env python3
"""Tests for scripts/signals.py persist() — path derivation per tool, the wayback page-slug, slash-variant
dedup, and the company/page-grain guard. Writes to a temp root; no real store, no network."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import signals as sg


def env(tool: str, captured_at: str, **payload: object) -> dict:
    return {"tool": tool, "source": f"{tool}.x", "captured_at": captured_at, "ok": True,
            "schema_drift": [], **payload}


class PersistPaths(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def rel(self, p: Path) -> str:
        return str(p.relative_to(self.root))

    def test_trustpilot_lands_under_domain(self) -> None:
        e = env("trustpilot", "2026-06-15T12:00:00Z", input={"slug": "honehealth.com"})
        dest = sg.persist(e, root=self.root)
        self.assertEqual(self.rel(dest), "honehealth-com/signals/trustpilot/20260615T120000Z.json")
        self.assertEqual(json.loads(dest.read_text()), e)  # verbatim

    def test_wayback_uses_a_page_slug_subdir(self) -> None:
        e = env("wayback", "2026-06-15T12:00:00Z", input={"url": "https://honehealth.com/longevity/nad"})
        dest = sg.persist(e, root=self.root)
        self.assertEqual(self.rel(dest), "honehealth-com/signals/wayback/longevity-nad/20260615T120000Z.json")

    def test_wayback_strips_www_to_match_the_store_slug(self) -> None:
        e = env("wayback", "2026-06-15T12:00:00Z", input={"url": "https://www.hims.com/testosterone/enclomiphene"})
        dest = sg.persist(e, root=self.root)
        self.assertEqual(self.rel(dest), "hims-com/signals/wayback/testosterone-enclomiphene/20260615T120000Z.json")

    def test_wayback_slash_variants_collapse_to_one_path(self) -> None:
        a = env("wayback", "2026-06-15T12:00:00Z", input={"url": "https://honehealth.com/longevity/nad"})
        b = env("wayback", "2026-06-15T12:00:00Z", input={"url": "https://honehealth.com/longevity/nad/"})
        self.assertEqual(sg.persist(a, root=self.root), sg.persist(b, root=self.root))  # same file

    def test_sec_edgar_uses_input_domain(self) -> None:
        e = env("sec_edgar", "2026-06-15T12:00:00Z", subject="hims.com", input={"name": "Hims", "domain": "hims.com"})
        self.assertEqual(self.rel(sg.persist(e, root=self.root)), "hims-com/signals/sec_edgar/20260615T120000Z.json")

    def test_trends_requires_an_explicit_domain(self) -> None:
        e = env("trends", "2026-06-15T12:00:00Z", input={"keywords": [{"label": "Hims", "query": "hims"}]})
        with self.assertRaises(ValueError):
            sg.persist(e, root=self.root)
        # but with one supplied, it lands:
        dest = sg.persist(e, domain="hims.com", root=self.root)
        self.assertEqual(self.rel(dest), "hims-com/signals/trends/20260615T120000Z.json")

    def test_category_grain_serpapi_is_refused(self) -> None:
        e = env("serpapi", "2026-06-15T12:00:00Z", input={"query": "trt online prescription"})
        with self.assertRaises(ValueError) as cm:
            sg.persist(e, root=self.root)
        self.assertIn("category-grain", str(cm.exception))

    def test_distinct_captured_at_accumulates(self) -> None:
        a = env("trustpilot", "2026-06-08T12:00:00Z", input={"slug": "hims.com"})
        b = env("trustpilot", "2026-06-15T12:00:00Z", input={"slug": "hims.com"})
        d0, d7 = sg.persist(a, root=self.root), sg.persist(b, root=self.root)
        self.assertNotEqual(d0, d7)
        self.assertEqual(len(list(d0.parent.glob("*.json"))), 2)  # a real two-point series


class VerbTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._orig_store, sg.STORE = sg.STORE, self.root / "store"

    def tearDown(self) -> None:
        sg.STORE = self._orig_store
        self._tmp.cleanup()

    def test_import_lands_raw_envelopes_and_skips_cards(self) -> None:
        from argparse import Namespace
        src = self.root / "src"
        src.mkdir()
        (src / "real.json").write_text(json.dumps(env("trustpilot", "2026-06-15T12:00:00Z", input={"slug": "hims.com"})))
        (src / "card.json").write_text(json.dumps({"card_id": "x", "evidence_label": "visibility"}))  # not a raw envelope
        self.assertEqual(sg.cmd_import(Namespace(paths=[str(src)], domain=None)), 0)
        landed = [p.name for p in (sg.STORE).glob("**/*.json")]
        self.assertEqual(landed, ["20260615T120000Z.json"])  # the card was skipped

    def test_run_pins_interpreter_persists_and_logs_cost(self) -> None:
        import contextlib
        import io
        from argparse import Namespace
        from unittest.mock import MagicMock, patch
        panel = self.root / "panel.jsonl"
        panel.write_text(json.dumps({"id": "hims-tp", "tool": "trustpilot", "args": ["hims.com"]}) + "\n")
        fake = env("trustpilot", "2026-06-15T12:00:00Z", input={"slug": "hims.com"}, cost={"firecrawl_credits": 1})
        proc = MagicMock(returncode=0, stdout=json.dumps(fake), stderr="")
        with patch.object(sg.subprocess, "run", return_value=proc) as m:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                self.assertEqual(sg.cmd_run(Namespace(panel=str(panel), dry_run=False)), 0)
        self.assertEqual(m.call_args[0][0][0], sys.executable)  # interpreter pin, not bare python3
        self.assertTrue((sg.STORE / "hims-com/signals/trustpilot/20260615T120000Z.json").exists())
        self.assertEqual(json.loads(buf.getvalue())["records"][0]["cost"], {"firecrawl_credits": 1})

    def test_run_dry_run_spends_nothing(self) -> None:
        import contextlib
        import io
        from argparse import Namespace
        from unittest.mock import patch
        panel = self.root / "panel.jsonl"
        panel.write_text(json.dumps({"id": "x", "tool": "trustpilot", "args": ["hims.com"]}) + "\n")
        with patch.object(sg.subprocess, "run") as m:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                self.assertEqual(sg.cmd_run(Namespace(panel=str(panel), dry_run=True)), 0)
        m.assert_not_called()  # preview only — no capture invoked
        self.assertIn("would run: trustpilot", buf.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
