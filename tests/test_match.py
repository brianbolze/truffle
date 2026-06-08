#!/usr/bin/env python3
"""Regression tests for `_match.py`'s hard-won domain/text split.

These cases are small on purpose: they pin the mistakes that would corrupt downstream reads, not a
giant taxonomy of possible brands. Run with:

    python3 tools/test_match.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from _match import domain_from_url, match_domain, match_output, match_record, normalize_domain

COHORT = [
    {
        "slug": "ro",
        "domain": "ro.co",
        "aliases": ["Ro", "Roman"],
        "disambiguate_regex": r"\b(?:Ro Health|Ro\.co|Roman|ro\.co)\b",
    },
    {
        "slug": "hims-and-hers",
        "domain": "hims.com",
        "aliases": ["Hims", "Hims & Hers"],
    },
]


SERPAPI_FIXTURE = {
    "tool": "serpapi",
    "source": "serpapi.com",
    "captured_at": "2026-06-08T18:16:11Z",
    "ok": True,
    "input": {"query": "Ro Hims comparison", "gl": "us", "hl": "en", "device": "desktop"},
    "schema_drift": [],
    "parser_version": "v2",
    "cost": {"credits": 1},
    "ranked_brands": [],
    "organic_results": [
        {
            "position": 1,
            "title": "Ro vs. Hims for ED in 2025: A Comparison Guide",
            "link": "https://ro.co/erectile-dysfunction/ro-vs-hims/",
            "snippet": "Ro's pricing is transparent, while Hims appears to charge more.",
        },
        {
            "position": 2,
            "title": "Hims vs. Roman for ED 2025: How Do They Compare?",
            "link": "https://www.hims.com/blog/hims-vs-roman",
            "snippet": "Both Hims and Roman offer access to standard ED pills.",
        },
        {
            "position": 3,
            "title": "Hims vs. Ro: Comparison and Review",
            "link": "https://www.medicalnewstoday.com/articles/hims-vs-roman",
            "snippet": "Hims and Ro offer prescription treatments for erectile dysfunction.",
        },
    ],
}


class MatchTests(unittest.TestCase):
    def test_domain_extraction_and_www_normalization(self) -> None:
        self.assertEqual(domain_from_url("https://www.hims.com/blog/hims-vs-roman"), "hims.com")
        self.assertEqual(domain_from_url("ro.co/erectile-dysfunction"), "ro.co")
        self.assertEqual(normalize_domain("https://www.ro.co/"), "ro.co")

    def test_serpapi_organic_classifies_own_pages_and_mentions(self) -> None:
        summary = {
            (m["where"]["position"], m["slug"]): (m["kind"], m["match_method"], m["first_channel"])
            for m in match_output(SERPAPI_FIXTURE, COHORT)
        }

        self.assertEqual(summary[(1, "ro")], ("own_page", "both", "domain"))
        self.assertEqual(summary[(1, "hims-and-hers")], ("mention", "text", "text"))
        self.assertEqual(summary[(2, "hims-and-hers")], ("own_page", "both", "domain"))
        self.assertEqual(summary[(2, "ro")], ("mention", "text", "text"))
        self.assertEqual(summary[(3, "ro")], ("mention", "text", "text"))
        self.assertEqual(summary[(3, "hims-and-hers")], ("mention", "text", "text"))

    def test_ranked_brands_are_alias_aware_text_mentions(self) -> None:
        output = {
            "tool": "serpapi",
            "ranked_brands": [
                {"position": 1, "raw_snippet": "Best Overall: Hims & Hers", "after_colon": "Hims & Hers"},
                {"position": 2, "raw_snippet": "Other Notable: Ro, Keeps", "after_colon": "Ro, Keeps"},
            ],
        }

        summary = {(m["where"]["position"], m["slug"]): (m["kind"], m["match_method"]) for m in match_output(output, COHORT)}

        self.assertEqual(summary[(1, "hims-and-hers")], ("mention", "text"))
        self.assertEqual(summary[(2, "ro")], ("mention", "text"))

    def test_exa_neighbor_url_is_an_own_page_domain_hit(self) -> None:
        output = {
            "tool": "exa_similar",
            "neighbors": [{"rank": 1, "title": "Hims", "url": "https://www.hims.com/blog/hims-vs-roman"}],
        }

        self.assertEqual(
            [(m["where"]["rank"], m["slug"], m["kind"], m["match_method"]) for m in match_output(output, COHORT)],
            [(1, "hims-and-hers", "own_page", "domain")],
        )

    def test_open_text_uses_strict_disambiguation_for_short_names(self) -> None:
        self.assertEqual(match_record(cohort=COHORT, text="I installed a 5-stage RO water filter", text_mode="open_text"), [])
        self.assertEqual(match_record(cohort=COHORT, text="I used ro.co for ED", text_mode="open_text")[0]["slug"], "ro")

    def test_resolver_hook_can_fold_domain_aliases_without_store_import(self) -> None:
        def resolver(query: str) -> str | None:
            key = normalize_domain(query) or query.strip().lower()
            return {"eden.health": "eden-health", "tryeden.com": "eden-health"}.get(key)

        hit = match_domain(
            "https://tryeden.com/glp1",
            [{"slug": "eden", "domain": "eden.health", "aliases": ["Eden"]}],
            resolver=resolver,
        )

        self.assertEqual(hit[0]["slug"], "eden")
        self.assertIsNone(hit[0]["matched_domain"])
        self.assertEqual(hit[0]["resolved_key"], "eden-health")
        self.assertTrue(hit[0]["via_resolver"])


if __name__ == "__main__":
    unittest.main()
