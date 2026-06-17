#!/usr/bin/env python3
"""Tests for fc.py's source_stamp() — the capture-side provenance header.

The cleaned `.md` is the durable home for each page's source URL (the `.payloads` manifest
that also holds it is gitignored + pruned). Tier-B (`shoot.py`) reads it back to re-render the
right page; the bug it fixes is a body-link grep that mis-picked a nav/CTA URL. So the
load-bearing guarantees are: the body stays byte-verbatim below the header, and a first-match
`^source_url:` read returns OUR URL even when the body opens with link soup."""

from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "research-company" / "scripts"))

import fc  # noqa: E402 — after the sys.path insert above


def _read_source_url(text: str) -> str | None:
    """How a consumer extracts it — first `^source_url:` line wins (the grep -m1 in SKILL.md)."""
    m = re.search(r"^source_url:\s*(\S+)", text, re.M)
    return m.group(1) if m else None


class SourceStamp(unittest.TestCase):
    def test_block_shape(self) -> None:
        stamp = fc.source_stamp("https://www.functionhealth.com/pricing", "2026-06-17")
        self.assertEqual(
            stamp,
            "<!--\nsource_url: https://www.functionhealth.com/pricing\ncaptured: 2026-06-17\n-->\n\n",
        )

    def test_body_preserved_verbatim(self) -> None:
        body = "# Pricing\n\nTest twice a year for $365.\n\n---\n\nFooter line.\n"
        out = fc.source_stamp("https://x.com/pricing", "2026-06-17") + body
        # Everything after the closing comment fence + blank line is the untouched body.
        self.assertTrue(out.endswith(body))
        self.assertEqual(out[out.index("-->\n\n") + len("-->\n\n"):], body)

    def test_grep_picks_our_url_not_body_links(self) -> None:
        # The functionhealth failure: the body opens with nav/CTA links. A first-match read of
        # the stamped file must return the stamped page URL, never the my.* signup CTA.
        link_soup = (
            "[Use your HSA/FSA funds](https://my.functionhealth.com/signup?code=ABC)\n\n"
            "[Pricing](https://www.functionhealth.com/pricing)\n\n# Check your health.\n"
        )
        stamped = fc.source_stamp("https://www.functionhealth.com", "2026-06-17") + link_soup
        self.assertEqual(_read_source_url(stamped), "https://www.functionhealth.com")

    def test_map_manifest_records_verb(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            old_root = fc.ROOT
            fc.ROOT = Path(tmp)
            try:
                with patch.object(fc, "post", return_value={"links": ["https://example.com"]}):
                    fc.do_map("https://example.com", "example-com", None, 500, "2026-06-17", verb="research-company")
                manifest = Path(tmp) / "store" / "example-com" / "captures" / "2026-06-17" / ".payloads" / "manifest.jsonl"
                rec = json.loads(manifest.read_text().strip())
                self.assertEqual(rec["verb"], "research-company")
            finally:
                fc.ROOT = old_root


if __name__ == "__main__":
    unittest.main()
