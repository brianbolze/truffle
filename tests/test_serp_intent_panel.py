#!/usr/bin/env python3
"""Smoke tests for `serp_intent_panel.py` using fixture captures, not live SerpAPI calls."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
FIXTURES = ROOT / "tests" / "fixtures" / "serp_intent_panel"
sys.path.insert(0, str(TOOLS))

from serp_intent_panel import build_panel, load_capture_index, load_cohort, load_query_set  # noqa: E402


class SerpIntentPanelTests(unittest.TestCase):
    def test_panel_counts_own_pages_mentions_aio_and_labels(self) -> None:
        queries = load_query_set(str(FIXTURES / "queries.json"))
        cohort = load_cohort(str(FIXTURES / "cohort.json"))
        captures = load_capture_index([str(FIXTURES / "captures")])

        panel = build_panel(queries, cohort, captures)
        rows = {row["id"]: row for row in panel["queries"]}

        payroll = rows["payroll-software"]
        self.assertEqual(payroll["organic_top10_match_count"], 4)
        self.assertEqual(len(payroll["own_page_matches"]), 2)
        self.assertEqual(len(payroll["third_party_mention_matches"]), 2)
        self.assertEqual(payroll["ai_overview"]["ranked_brand_match_count"], 2)
        self.assertEqual(payroll["ai_overview"]["reference_match_count"], 3)
        self.assertEqual(payroll["query_usefulness_labels"], ["clean"])

        retail = rows["payroll-tax-forms"]
        self.assertIn("no cohort signal", retail["query_usefulness_labels"])
        self.assertIn("supplement/retail drift", retail["query_usefulness_labels"])
        self.assertEqual(retail["organic_top10_match_count"], 0)

    def test_markdown_cli_smoke_uses_existing_captures(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TOOLS / "serp_intent_panel.py"),
                "--queries",
                str(FIXTURES / "queries.json"),
                "--cohort",
                str(FIXTURES / "cohort.json"),
                "--captures",
                str(FIXTURES / "captures"),
                "--format",
                "markdown",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# SERP Intent Panel", result.stdout)
        self.assertIn("online payroll software", result.stdout)
        self.assertIn("AIO reference matches", result.stdout)
        self.assertIn("supplement/retail drift", result.stdout)


if __name__ == "__main__":
    unittest.main()
