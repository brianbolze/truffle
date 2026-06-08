#!/usr/bin/env python3
"""Fixture tests for Wayback tenure and content-diff capture mechanics."""

from __future__ import annotations

import hashlib
import sys
import unittest
import urllib.parse
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import wayback


class WaybackTests(unittest.TestCase):
    def test_bare_domain_is_documented_cdx_canonicalization_not_tool_rewrite(self) -> None:
        parsed = urllib.parse.urlparse(wayback.build_cdx_url("example.com"))
        query = urllib.parse.parse_qs(parsed.query)

        self.assertEqual(query["url"], ["example.com"])

    def test_raw_replay_url_uses_original_mode_suffix(self) -> None:
        self.assertEqual(
            wayback._raw_replay_url("20200102030405", "http://example.com/"),
            "https://web.archive.org/web/20200102030405id_/http://example.com/",
        )

    def test_text_extraction_and_hashes_are_mechanical(self) -> None:
        body = (
            b"<html><head><style>.hidden{display:none}</style><script>ignore()</script></head>"
            b"<body><h1>Hello&nbsp;world</h1><p>Price: $10</p></body></html>"
        )
        fetched = wayback.FetchedContent(
            fetch_status=200,
            final_url="https://web.archive.org/web/20200102030405id_/http://example.com/",
            content_type="text/html; charset=utf-8",
            body=body,
        )
        record = wayback.CdxRecord(
            raw_timestamp="20200102030405",
            original_url="http://example.com/",
            status="200",
            digest="CDXDIGEST",
            mimetype="text/html",
            length=str(len(body)),
        )

        text = wayback.extract_text_content(body, "text/html; charset=utf-8")
        summary = wayback.summarize_fetched_snapshot(record, fetched)

        self.assertEqual(text, "Hello world\nPrice: $10")
        self.assertEqual(summary["content_sha256"], hashlib.sha256(body).hexdigest())
        self.assertEqual(summary["text_sha256"], hashlib.sha256(text.encode("utf-8")).hexdigest())
        self.assertEqual(summary["byte_count"], len(body))
        self.assertEqual(summary["text_line_count"], 2)

    def test_diff_output_on_two_synthetic_snapshots(self) -> None:
        rows = [
            ["timestamp", "original", "statuscode", "digest", "mimetype", "length"],
            ["20200101000000", "http://example.com/", "200", "OLD", "text/html", "30"],
            ["20210101000000", "http://example.com/", "200", "NEW", "text/html", "30"],
        ]
        bodies = [
            wayback.FetchedContent(
                fetch_status=200,
                final_url="old",
                content_type="text/html",
                body=b"<h1>Product</h1><p>Price: $10</p>",
            ),
            wayback.FetchedContent(
                fetch_status=200,
                final_url="new",
                content_type="text/html",
                body=b"<h1>Product</h1><p>Price: $12</p>",
            ),
        ]

        with patch.object(wayback, "fetch_cdx", return_value=rows):
            with patch.object(wayback, "fetch_replay_content", side_effect=bodies):
                result = wayback.diff_lookup("example.com", context_lines=1, max_diff_lines=20)

        self.assertTrue(result["ok"])
        self.assertEqual(result["selection"]["state"], "selected")
        self.assertEqual(len(result["selected_snapshots"]), 2)
        self.assertTrue(result["text_changed"])
        self.assertEqual(result["contents"][0]["content_sha256"], hashlib.sha256(bodies[0].body).hexdigest())
        self.assertIn("-Price: $10", result["diff"]["lines"])
        self.assertIn("+Price: $12", result["diff"]["lines"])
        self.assertEqual(result["diff"]["line_counts"]["common"], 1)
        self.assertEqual(result["diff"]["line_counts"]["added"], 1)
        self.assertEqual(result["diff"]["line_counts"]["removed"], 1)

    def test_partial_target_dates_select_nearest_valid_timestamps(self) -> None:
        records = [
            wayback.CdxRecord("20090101000000", "http://example.com/", "200", "OLD"),
            wayback.CdxRecord("20110201000000", "http://example.com/", "200", "NEW"),
        ]

        selected, state, note = wayback.select_diff_records(records, from_timestamp="2010", to_timestamp="2011")

        self.assertEqual(state, "selected")
        self.assertIsNone(note)
        self.assertEqual([record.raw_timestamp for record in selected], ["20090101000000", "20110201000000"])

    def test_no_snapshot_diff_is_empty_data_not_failure(self) -> None:
        with patch.object(wayback, "fetch_cdx", return_value=[]):
            result = wayback.diff_lookup("missing.example")

        self.assertTrue(result["ok"])
        self.assertEqual(result["selection"]["state"], "no_snapshots")
        self.assertEqual(result["selected_snapshots"], [])
        self.assertEqual(result["contents"], [])
        self.assertIsNone(result["diff"])

    def test_one_snapshot_diff_is_insufficient_data_not_failure(self) -> None:
        rows = [
            ["timestamp", "original", "statuscode", "digest", "mimetype", "length"],
            ["20200101000000", "http://example.com/", "200", "ONLY", "text/html", "30"],
        ]

        with patch.object(wayback, "fetch_cdx", return_value=rows):
            result = wayback.diff_lookup("example.com")

        self.assertTrue(result["ok"])
        self.assertEqual(result["selection"]["state"], "insufficient_snapshots")
        self.assertEqual(len(result["selected_snapshots"]), 1)
        self.assertEqual(result["contents"], [])
        self.assertIsNone(result["diff"])


if __name__ == "__main__":
    unittest.main()
