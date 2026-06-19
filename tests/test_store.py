#!/usr/bin/env python3
"""Regression tests for scripts/store.py name resolution."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import store  # noqa: E402

PROFILES = {
    "telolife-com": {"domain": "telolife.com", "name": "TeloLife", "aliases": []},
    "alpha-sense-com": {"domain": "alpha-sense.com", "name": "AlphaSense", "aliases": ["AlphaSense, Inc."]},
    "hims-com": {"domain": "hims.com", "name": "Hims", "aliases": ["hims & hers", "forhims"]},
    "alange-soehne-com": {"domain": "alange-soehne.com", "name": "A. Lange & Söhne", "aliases": []},
    "noom-com": {"domain": "noom.com", "name": "Noom", "aliases": []},
    "ro-co": {"domain": "ro.co", "name": "Ro", "aliases": ["Roman"]},
    "usertesting-com": {"domain": "usertesting.com", "name": "UserTesting", "aliases": []},
}


class StoreResolveTests(unittest.TestCase):
    def test_spaced_camelcase_brand_resolves(self) -> None:
        self.assertEqual(store.resolve("Telo Life", PROFILES), "telolife-com")
        self.assertEqual(store.resolve("Alpha Sense", PROFILES), "alpha-sense-com")

    def test_punctuation_and_and_variants_resolve(self) -> None:
        self.assertEqual(store.resolve("Hims and Hers", PROFILES), "hims-com")
        self.assertEqual(store.resolve("A Lange Sohne", PROFILES), "alange-soehne-com")

    def test_domain_and_slug_resolution_still_work(self) -> None:
        self.assertEqual(store.resolve("telolife.com", PROFILES), "telolife-com")
        self.assertEqual(store.resolve("telolife-com", PROFILES), "telolife-com")


class StoreSuggestTests(unittest.TestCase):
    def test_typo_suggestions_do_not_change_exact_resolution(self) -> None:
        self.assertIsNone(store.resolve("Tello Life", PROFILES))
        self.assertEqual(store.suggest("Tello Life", PROFILES)[0].slug, "telolife-com")
        self.assertEqual(store.suggest("UserTestng", PROFILES)[0].slug, "usertesting-com")
        self.assertEqual(store.suggest("Alfa Sense", PROFILES)[0].slug, "alpha-sense-com")

    def test_short_generic_queries_do_not_suggest(self) -> None:
        self.assertEqual(store.suggest("Rho", PROFILES), [])
        self.assertEqual(store.suggest("Nom", PROFILES), [])
        self.assertEqual(store._miss_line("Rho", PROFILES), "Rho → NOT in store")

    def test_short_substring_prefix_still_surfaces_candidate(self) -> None:
        # The min-key-len gate governs fuzzy suggestions only — a sub-5-char prefix of a real
        # name must still surface through the exact substring path (e.g. `find user`).
        self.assertIn("usertesting-com", store._miss_line("user", PROFILES))

    def test_find_labels_likely_and_ambiguous_suggestions(self) -> None:
        self.assertIn("likely candidate: telolife-com", store._miss_line("Tello Life", PROFILES))

        ambiguous = {
            "telo-life-com": {"domain": "telo-life.com", "name": "Telo Life", "aliases": []},
            "telo-live-com": {"domain": "telo-live.com", "name": "Telo Live", "aliases": []},
        }
        self.assertIn("ambiguous candidates:", store._miss_line("Telo Livf", ambiguous))

    def test_human_name_key_collisions_are_detectable(self) -> None:
        collisions = store.name_key_collisions(
            {
                "alpha-sense-com": {"domain": "alpha-sense.com", "name": "AlphaSense", "aliases": []},
                "alphasense-ai": {"domain": "alphasense.ai", "name": "Alpha Sense", "aliases": []},
            }
        )
        self.assertEqual({slug for slug, _ in collisions["alphasense"]}, {"alpha-sense-com", "alphasense-ai"})


if __name__ == "__main__":
    unittest.main()
