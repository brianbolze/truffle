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


if __name__ == "__main__":
    unittest.main()
