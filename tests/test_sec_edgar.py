#!/usr/bin/env python3
"""Tests for sec_edgar.py — the name-match seam (confirmed vs name_match_unconfirmed vs related-vehicle,
CIK collapse), filing extraction, and the factual-card boundary (no amount, no verdict). No live calls."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import sec_edgar as se


def fts(hits: list[dict]) -> dict:
    """A canned EFTS full-text-search response. Each hit: (ciks, file_date, display_names)."""
    return {"hits": {"total": {"value": len(hits)},
                     "hits": [{"_source": {"ciks": h[0], "file_date": h[1], "display_names": h[2]}} for h in hits]}}


class FormDMatchSeam(unittest.TestCase):
    def test_single_distinctive_cik_is_confirmed_and_collapses_case_variants(self) -> None:
        # 'Sora Fuel Corp' and 'SORA FUEL Corp' are the SAME CIK -> one candidate, confirmed.
        resp = fts([(["2014480"], "2026-03-31", ["Sora Fuel Corp"]),
                    (["2014480"], "2024-03-08", ["SORA FUEL Corp"])])
        with patch.object(se, "_get_json", return_value=resp):
            out = se.search_form_d("Sora Fuel")
        self.assertEqual(out["match"], "confirmed")
        self.assertEqual(out["distinct_ciks"], 1)
        self.assertEqual(out["candidates"][0]["dates"], ["2024-03-08", "2026-03-31"])

    def test_many_ciks_is_name_match_unconfirmed(self) -> None:
        resp = fts([(["1"], "2025-10-30", ["Electra Therapeutics, Inc."]),
                    (["2"], "2023-01-04", ["Electra America Hospitality REIT LLC"]),
                    (["3"], "2023-01-26", ["Electra Capital PM Sub REIT LLC"])])
        with patch.object(se, "_get_json", return_value=resp):
            out = se.search_form_d("Electra")
        self.assertEqual(out["match"], "name_match_unconfirmed")
        self.assertEqual(out["distinct_ciks"], 3)

    def test_only_investor_vehicle_is_unconfirmed_and_flagged(self) -> None:
        # 'VXI Evoloh SPV LP' is an investor wrapper, not the issuer -> not a confirmed company raise.
        resp = fts([(["2048282"], "2024-12-26", ["VXI Evoloh SPV LP"])])
        with patch.object(se, "_get_json", return_value=resp):
            out = se.search_form_d("EVOLOH")
        self.assertEqual(out["match"], "name_match_unconfirmed")
        self.assertTrue(out["candidates"][0]["is_vehicle"])

    def test_issuer_suffix_is_not_mistaken_for_a_vehicle(self) -> None:
        # 'VerdeGo Aero, Inc.' starts with the query root -> a real issuer, not a vehicle, -> confirmed.
        resp = fts([(["1714832"], "2024-07-25", ["VerdeGo Aero, Inc."])])
        with patch.object(se, "_get_json", return_value=resp):
            out = se.search_form_d("VerdeGo Aero")
        self.assertEqual(out["match"], "confirmed")
        self.assertFalse(out["candidates"][0]["is_vehicle"])

    def test_zero_hits_is_no_match_not_an_error(self) -> None:
        with patch.object(se, "_get_json", return_value=fts([])):
            out = se.search_form_d("Euclid Power")
        self.assertEqual(out["match"], "no_match")
        self.assertEqual(out["candidates"], [])


class FilingExtraction(unittest.TestCase):
    def test_extract_filings_filters_forms_and_builds_urls(self) -> None:
        subs = {"cik": "1318605", "filings": {"recent": {
            "form": ["10-Q", "4", "8-K"], "filingDate": ["2026-04-23", "2026-04-20", "2026-04-22"],
            "primaryDocument": ["tsla-q.htm", "form4.xml", "tsla-8k.htm"],
            "accessionNumber": ["0001-26-001", "0001-26-002", "0001-26-003"]}}}
        out = se.extract_filings(subs)
        forms = [f["form"] for f in out]
        self.assertEqual(forms, ["10-Q", "8-K"])  # form 4 filtered out
        self.assertIn("/data/1318605/000126001/tsla-q.htm", out[0]["url"])


class CardBoundary(unittest.TestCase):
    def test_cards_carry_facts_not_amounts_or_verdicts(self) -> None:
        state = {"cik": "1714832", "is_public": False}
        form_d = {"match": "confirmed", "candidates": [
            {"cik": "1714832", "filer": "VerdeGo Aero, Inc.", "dates": ["2024-07-25"], "is_vehicle": False}]}
        filings = [{"form": "8-K", "date": "2026-01-10", "url": "https://sec.gov/x"}]
        cards = se.build_funding_signals("verdegoaero.com", state, filings, form_d)
        blob = repr(cards).lower()
        self.assertNotIn("evidence_label", blob)
        self.assertNotIn("signal_polarity", blob)
        self.assertNotIn("formidable", blob)
        for c in cards:
            self.assertIsNone(c["amount"])  # EDGAR never carries the amount (the seam)
            self.assertEqual(c["source_type"], "sec")
            self.assertEqual(c["observation"], "factual")
        kinds = {c["event_type"] for c in cards}
        self.assertEqual(kinds, {"form_d", "filing"})

    def test_single_unconfirmed_candidate_emits_one_flagged_card(self) -> None:
        # A single probable-but-unproven candidate -> existence-only card, not_promoted (never an abort).
        form_d = {"match": "name_match_unconfirmed", "candidates": [
            {"cik": "1", "filer": "Electra Therapeutics, Inc.", "dates": ["2025-10-30"], "is_vehicle": False}]}
        cards = se.build_funding_signals("electra.aero", {"cik": None}, [], form_d)
        self.assertEqual(len(cards), 1)
        self.assertIn("not_promoted", cards[0]["flags"])

    def test_multi_cik_swamp_emits_no_attributed_cards(self) -> None:
        # >1 distinct issuer CIK -> can't pin the subject -> NO manufactured event cards (the seam).
        form_d = {"match": "name_match_unconfirmed", "candidates": [
            {"cik": "1", "filer": "Electra Therapeutics", "dates": ["2025-10-30"], "is_vehicle": False},
            {"cik": "2", "filer": "Electra REIT", "dates": ["2023-01-04"], "is_vehicle": False}]}
        cards = se.build_funding_signals("electra.aero", {"cik": None}, [], form_d)
        self.assertEqual(cards, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
