#!/usr/bin/env python3
"""Tests for signal_delta.py — the alignment fence (a hard guard, per the traction approach), the
source-aware branch deltas/vetoes, and the structural no-score property. Inline fixtures, no live calls."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import signal_delta as sd


def tp(slug: str, captured_at: str, *, state: str = "active", review_count: int | None = None,
       last_12m: int | None = None, reviews: list | None = None, drift: list | None = None,
       merged: bool = False, paid: bool = False) -> dict:
    """A minimal trustpilot envelope carrying only the fields the branch reads."""
    return {
        "tool": "trustpilot", "source": "trustpilot.com", "captured_at": captured_at,
        "ok": not drift, "input": {"slug": slug}, "schema_drift": drift or [],
        "profile_state": state, "review_count": review_count, "reviews_last_12m": last_12m,
        "trust_score": 4.5, "profile_flags": {"merged_profile": merged, "paid_profile": paid},
        "recent_reviews": reviews or [],
    }


def serp(query: str, captured_at: str, *, organic: list | None = None, aio: bool = True,
         skipped: bool = False) -> dict:
    return {
        "tool": "serpapi", "source": "serpapi.com", "captured_at": captured_at, "ok": True,
        "input": {"query": query}, "schema_drift": [],
        "ai_overview_present": aio, "ai_overview_skipped": skipped,
        "organic_results": organic or [],
    }


def wb(url: str, captured_at: str, *, count: int, last_seen: str, digest: str) -> dict:
    """A minimal wayback tenure envelope carrying the fields the branch reads."""
    return {
        "tool": "wayback", "source": "web.archive.org/cdx", "captured_at": captured_at, "ok": True,
        "input": {"url": url}, "schema_drift": [], "snapshot_count": count, "last_seen": last_seen,
        "snapshots": [{"timestamp": last_seen, "digest": digest}],
    }


def trends_env(captured_at: str, items: list[dict]) -> dict:
    return {"tool": "trends", "source": "trends.google.com", "captured_at": captured_at, "ok": True,
            "input": {}, "schema_drift": [], "series": items}


def kw(query: str, *, peak_value: float, peak_date: str, first: str, last: str,
       traj: str = "flat", d7: float | None = 0.0) -> dict:
    return {"label": query, "query": query, "ok": True, "peak_value": peak_value, "peak_date": peak_date,
            "trajectory": traj, "delta_7d_vs_prior_7d_pct": d7,
            "points": [{"date": first, "value": 10}, {"date": last, "value": 20}]}


def sec_card(event_type: str, date: str, **extra: object) -> dict:
    """A factual EDGAR card: event + date, deliberately amount-free."""
    return {"subject": "x.com", "source_type": "sec", "event_type": event_type, "date": date,
            "amount": None, "observation": "factual", **extra}


def sec(captured_at: str, *, subject: str = "x.com", state: dict | None = None,
        form_d: dict | None = None, filings: list[dict] | None = None,
        cards: list[dict] | None = None, domain: str | None = "x.com") -> dict:
    """A minimal sec_edgar envelope carrying only the fields the branch reads."""
    return {
        "tool": "sec_edgar", "source": "efts.sec.gov + data.sec.gov", "captured_at": captured_at,
        "ok": True, "input": {"name": "X Inc", "ticker": None, "domain": domain}, "schema_drift": [],
        "subject": subject,
        "state": state or {"is_public": False, "ticker": None, "cik": None, "exchange": None, "registered_name": None},
        "filings": filings or [],
        "form_d": form_d or {"match": "no_match", "candidates": []},
        "funding_signals": cards or [],
    }


def only(rows: list[dict], subject: str) -> dict:
    return next(r for r in rows if r["subject"] == subject)


def write_env(root: Path, rel: str, env: dict) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(env), encoding="utf-8")
    return path


class LoaderTests(unittest.TestCase):
    def test_file_and_flat_dir_loader_still_work(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = write_env(root, "a.json", tp("a.com", "2026-06-08T00:00:00Z", review_count=10))
            write_env(root, "b.json", tp("b.com", "2026-06-08T00:00:00Z", review_count=20))

            self.assertEqual([e["input"]["slug"] for e in sd._load_envelopes(first)], ["a.com"])
            self.assertEqual([e["input"]["slug"] for e in sd._load_envelopes(root)], ["a.com", "b.com"])

    def test_directory_loader_recurses_wayback_page_subdirs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            run_a, run_b = base / "run-a", base / "run-b"
            write_env(
                run_a,
                "a-root/20260608T000000Z.json",
                wb("https://x.com", "2026-06-08T00:00:00Z", count=1, last_seen="2026-05-01T00:00:00Z", digest="AAA"),
            )
            write_env(
                run_a,
                "b-sermorelin/20260608T000000Z.json",
                wb("https://x.com/sermorelin", "2026-06-08T00:00:00Z", count=2, last_seen="2026-05-02T00:00:00Z", digest="BBB"),
            )
            write_env(
                run_b,
                "a-root/20260615T000000Z.json",
                wb("https://x.com", "2026-06-15T00:00:00Z", count=2, last_seen="2026-06-01T00:00:00Z", digest="CCC"),
            )
            write_env(
                run_b,
                "b-sermorelin/20260615T000000Z.json",
                wb("https://x.com/sermorelin", "2026-06-15T00:00:00Z", count=3, last_seen="2026-06-02T00:00:00Z", digest="DDD"),
            )

            loaded_a = sd._load_envelopes(run_a)
            self.assertEqual([e["input"]["url"] for e in loaded_a], ["https://x.com", "https://x.com/sermorelin"])

            out = sd.compare(loaded_a, sd._load_envelopes(run_b))
            self.assertEqual(
                sorted(r["subject"] for r in out["comparisons"]),
                ["https://x.com", "https://x.com/sermorelin"],
            )
            self.assertTrue(all(r["source_type"] == "wayback" and r["grain"] == "page" for r in out["comparisons"]))


class FenceTests(unittest.TestCase):
    def test_cross_source_pairing_is_a_veto(self) -> None:
        a = tp("honehealth.com", "2026-06-08T12:00:00Z", review_count=100)
        b = serp("honehealth", "2026-06-15T12:00:00Z")
        out = sd.compare([a], [b])
        # Different source_types never reach the same branch; each is level-read alone, never falsely paired.
        self.assertTrue(all(r["read_mode"] in ("level",) or r["vetoes"] for r in out["comparisons"]))
        self.assertEqual(sorted(out["source_types"]), ["serpapi", "trustpilot"])

    def test_explicit_cross_subject_pairing_vetoes(self) -> None:
        a = tp("honehealth.com", "2026-06-08T12:00:00Z", review_count=100)
        b = tp("getpetermd.com", "2026-06-15T12:00:00Z", review_count=120)
        # Same source, different subject -> the fence refuses; both level-read, neither falsely diffed.
        out = sd.compare([a], [b])
        self.assertEqual(len(out["comparisons"]), 2)
        self.assertTrue(all(r["read_mode"] == "level" for r in out["comparisons"]))

    def test_direct_fence_helper_refuses_drift(self) -> None:
        a = tp("x.com", "2026-06-08T12:00:00Z", review_count=100)
        b = tp("x.com", "2026-06-15T12:00:00Z", drift=["anchor missing"])
        self.assertIsNotNone(sd._fence(a, b))
        self.assertIn("schema_drift", sd._fence(a, b))

    def test_direct_fence_helper_refuses_cross_grain(self) -> None:
        a = tp("x.com", "2026-06-08T12:00:00Z", review_count=100)
        b = serp("x", "2026-06-15T12:00:00Z")
        self.assertIn("mismatch", sd._fence(a, b))


class TrustpilotTests(unittest.TestCase):
    def test_velocity_off_cumulative_not_rolling_window(self) -> None:
        a = tp("hone.com", "2026-06-08T12:00:00Z", review_count=11200, last_12m=3100)
        b = tp("hone.com", "2026-06-15T12:00:00Z", review_count=11380, last_12m=3050)  # rolling FELL
        row = only(sd.compare([a], [b])["comparisons"], "hone-com")
        rc = next(m for m in row["metrics"] if m["metric"] == "review_count")
        l12 = next(m for m in row["metrics"] if m["metric"] == "reviews_last_12m")
        self.assertEqual(rc["delta"], 180)
        self.assertEqual(rc["velocity_per_day"], round(180 / 7, 2))
        self.assertIsNone(l12["delta"])  # rolling window is level-read only, never diffed

    def test_removed_profile_is_veto_with_empty_metrics(self) -> None:
        a = tp("g.com", "2026-06-08T12:00:00Z", review_count=850)
        b = tp("g.com", "2026-06-15T12:00:00Z", state="removed")
        row = only(sd.compare([a], [b])["comparisons"], "g-com")
        self.assertEqual(row["metrics"], [])
        self.assertTrue(any("profile_removed" in v for v in row["vetoes"]))

    def test_templated_reviews_flag_on_the_delta(self) -> None:
        dupes = [{"body": "Great service, highly recommend!"} for _ in range(3)]
        a = tp("b.co", "2026-06-08T12:00:00Z", review_count=200)
        b = tp("b.co", "2026-06-15T12:00:00Z", review_count=360, reviews=dupes)
        row = only(sd.compare([a], [b])["comparisons"], "b-co")
        self.assertTrue(any(f["flag"] == "templated_reviews" for f in row["comparability_flags"]))


class SerpOutageVetoTests(unittest.TestCase):
    def _run(self, drop_count: int) -> dict:
        queries = ["q1", "q2", "q3", "q4"]
        d0 = [serp(q, "2026-06-08T12:00:00Z", aio=True) for q in queries]
        d7 = [serp(q, "2026-06-11T12:00:00Z", aio=(i >= drop_count)) for i, q in enumerate(queries)]
        return sd.compare(d0, d7)

    def test_lone_drop_does_not_trigger_outage(self) -> None:
        out = self._run(drop_count=1)  # 1/4
        self.assertEqual(out["run_vetoes"], [])
        movements = [sd._aio_metric(r)["movement"] for r in out["comparisons"]]
        self.assertIn("dropped", movements)  # reported as a real per-query movement

    def test_high_fraction_drop_triggers_outage(self) -> None:
        out = self._run(drop_count=3)  # 3/4 >= 0.6
        self.assertTrue(out["run_vetoes"])
        self.assertIn("probable_aio_surface_outage", out["run_vetoes"][0])
        movements = [sd._aio_metric(r)["movement"] for r in out["comparisons"]]
        self.assertIn("dropped_OUTAGE_SUSPECTED", movements)

    def test_organic_and_aio_are_separate_metrics(self) -> None:
        d0 = [serp("q", "2026-06-08T12:00:00Z", organic=[{"link": "https://a.com", "position": 1}])]
        d7 = [serp("q", "2026-06-11T12:00:00Z", organic=[{"link": "https://a.com", "position": 3}])]
        row = sd.compare(d0, d7)["comparisons"][0]
        metrics = {m["metric"] for m in row["metrics"]}
        self.assertEqual(metrics, {"organic_rank", "aio_presence"})  # diffed independently, never blended


class TrendsBasisTests(unittest.TestCase):
    def test_shared_anchor_allows_point_level_delta(self) -> None:
        a = trends_env("2026-06-08T12:00:00Z", [kw("hone", peak_value=80, peak_date="2026-05-20", first="2026-05-01", last="2026-06-08")])
        b = trends_env("2026-06-15T12:00:00Z", [kw("hone", peak_value=100, peak_date="2026-05-25", first="2026-05-10", last="2026-06-15")])
        row = only(sd.compare([a], [b])["comparisons"], "hone")
        self.assertEqual(row["vetoes"], [])
        self.assertTrue(any(m["metric"] == "peak_value" for m in row["metrics"]))

    def test_peak_outside_overlap_vetoes_renorm_mismatch(self) -> None:
        # D0's peak (2026-05-02) is before the overlap start (2026-05-10) -> different normalization anchor.
        a = trends_env("2026-06-08T12:00:00Z", [kw("hone", peak_value=80, peak_date="2026-05-02", first="2026-05-01", last="2026-06-08")])
        b = trends_env("2026-06-15T12:00:00Z", [kw("hone", peak_value=100, peak_date="2026-05-25", first="2026-05-10", last="2026-06-15")])
        row = only(sd.compare([a], [b])["comparisons"], "hone")
        self.assertTrue(any("renorm_basis_mismatch" in v for v in row["vetoes"]))
        # trajectory is the robust read — still emitted even when point levels are vetoed
        self.assertTrue(any(m["metric"] == "within_capture_trajectory" for m in row["metrics"]))


class WaybackTests(unittest.TestCase):
    def test_content_change_and_snapshot_growth(self) -> None:
        a = wb("https://x.com/p", "2026-06-08T00:00:00Z", count=3, last_seen="2026-05-01T00:00:00Z", digest="AAA")
        b = wb("https://x.com/p", "2026-06-15T00:00:00Z", count=5, last_seen="2026-06-10T00:00:00Z", digest="BBB")
        row = only(sd.compare([a], [b])["comparisons"], "https://x.com/p")
        sc = next(m for m in row["metrics"] if m["metric"] == "snapshot_count")
        cd = next(m for m in row["metrics"] if m["metric"] == "content_digest")
        ls = next(m for m in row["metrics"] if m["metric"] == "last_seen")
        self.assertEqual(sc["delta"], 2)
        self.assertTrue(cd["changed"])
        self.assertTrue(ls["advanced"])

    def test_lost_presence(self) -> None:
        a = wb("https://x.com/p", "2026-06-08T00:00:00Z", count=2, last_seen="2026-05-01T00:00:00Z", digest="AAA")
        b = {**wb("https://x.com/p", "2026-06-15T00:00:00Z", count=0, last_seen="", digest=""), "snapshots": []}
        row = only(sd.compare([a], [b])["comparisons"], "https://x.com/p")
        ap = next(m for m in row["metrics"] if m["metric"] == "archive_presence")
        self.assertEqual(ap["movement"], "lost")


class SecEdgarTests(unittest.TestCase):
    def test_sec_subject_alignment_is_scoped_to_sec_branch(self) -> None:
        env = sec("2026-06-08T00:00:00Z", subject="stamped.com", domain="ignored.example")
        unknown = {
            "tool": "mystery_tool",
            "source": "mystery.source",
            "captured_at": "2026-06-08T00:00:00Z",
            "ok": True,
            "input": {"domain": "should-not-align.example"},
            "schema_drift": [],
        }

        self.assertEqual(sd.subject_of(env), "stamped-com")
        self.assertEqual(sd.subject_of(unknown), "mystery-source")

    def test_new_funding_card_and_state_change_are_reported(self) -> None:
        a = sec("2026-06-08T00:00:00Z")
        b = sec(
            "2026-06-15T00:00:00Z",
            state={"is_public": True, "ticker": "X", "cik": "0000000001", "exchange": "NYSE",
                   "registered_name": "X Inc"},
            form_d={"match": "confirmed", "candidates": [{"cik": "0000000001"}]},
            cards=[sec_card("form_d", "2026-06-12", cik="0000000001", filer="X Inc",
                            match="confirmed", flags=["existence_only"], citation="efts.sec.gov forms=D")],
        )

        row = only(sd.compare([a], [b])["comparisons"], "x-com")
        self.assertEqual(row["source_type"], "sec_edgar")
        self.assertEqual(row["grain"], "company")
        state = next(m for m in row["metrics"] if m["metric"] == "issuer_state")
        events = next(m for m in row["metrics"] if m["metric"] == "funding_events")
        match = next(m for m in row["metrics"] if m["metric"] == "form_d_match")

        self.assertEqual(state["changed"]["is_public"], {"d0": False, "d7": True})
        self.assertEqual(events["d0_count"], 0)
        self.assertEqual(events["d7_count"], 1)
        self.assertEqual(events["new"][0]["event_type"], "form_d")
        self.assertNotIn("amount", events["new"][0])  # EDGAR branch preserves the no-amount boundary
        self.assertEqual(match["movement"], "changed")

    def test_identity_and_capped_stream_flags_travel_with_sec_delta(self) -> None:
        filings = [{"form": "8-K", "date": f"2026-06-{day:02d}", "url": f"https://sec.test/{day}"}
                   for day in range(1, 11)]
        a = sec("2026-06-08T00:00:00Z")
        b = sec(
            "2026-06-15T00:00:00Z",
            domain=None,
            form_d={
                "match": "name_match_unconfirmed",
                "candidates": [{"cik": "0000000001"}, {"cik": "0000000002"}],
            },
            filings=filings,
        )

        row = only(sd.compare([a], [b])["comparisons"], "x-com")
        events = next(m for m in row["metrics"] if m["metric"] == "funding_events")
        flags = {f["flag"] for f in row["comparability_flags"]}
        self.assertEqual(events["new"], [])  # Form-D caveats travel even when no attributed card is emitted
        self.assertEqual(events["d7_count"], 0)
        self.assertIn("form_d_identity_unconfirmed", flags)
        self.assertIn("multiple_form_d_candidates", flags)
        self.assertIn("filings_cap", flags)
        self.assertIn("name_subject", flags)

    def test_capped_churn_is_labeled_as_not_visible_not_negative_movement(self) -> None:
        a = sec(
            "2026-06-08T00:00:00Z",
            cards=[sec_card("form_d", "2026-05-01", cik="0000000001", filer="X Inc", match="confirmed")],
        )
        b = sec(
            "2026-06-15T00:00:00Z",
            filings=[{"form": "8-K", "date": f"2026-06-{day:02d}", "url": f"https://sec.test/{day}"}
                     for day in range(1, 11)],
        )

        row = only(sd.compare([a], [b])["comparisons"], "x-com")
        events = next(m for m in row["metrics"] if m["metric"] == "funding_events")
        self.assertIn("not_visible_in_this_capture_window", events)
        self.assertNotIn("no_longer_in_capture", events)
        self.assertEqual(events["not_visible_in_this_capture_window"][0]["event_type"], "form_d")
        self.assertTrue(any(f["flag"] == "filings_cap" for f in row["comparability_flags"]))

    def test_sec_event_summaries_do_not_surface_amounts_or_verdicts(self) -> None:
        b = sec(
            "2026-06-15T00:00:00Z",
            cards=[sec_card(
                "form_d",
                "2026-06-12",
                cik="0000000001",
                filer="X Inc",
                match="confirmed",
                amount=5_000_000,
                valuation="post-money",
                score=99,
                verdict="strong traction",
            )],
        )

        row = only(sd.compare([sec("2026-06-08T00:00:00Z")], [b])["comparisons"], "x-com")
        events = next(m for m in row["metrics"] if m["metric"] == "funding_events")
        blob = repr(events).lower()
        for forbidden in ("amount", "valuation", "score", "verdict"):
            self.assertNotIn(forbidden, blob)

    def test_unpaired_sec_edgar_capture_is_level_read(self) -> None:
        row = sd.compare([], [sec("2026-06-15T00:00:00Z")])["comparisons"][0]
        self.assertEqual(row["read_mode"], "level")
        self.assertEqual(row["source_type"], "sec_edgar")
        self.assertTrue(any(f["flag"] == "unpaired_capture" for f in row["comparability_flags"]))


class NoScoreTests(unittest.TestCase):
    def test_no_score_field_anywhere_and_metrics_are_source_bound(self) -> None:
        a = tp("hone.com", "2026-06-08T12:00:00Z", review_count=100, last_12m=90)
        b = tp("hone.com", "2026-06-15T12:00:00Z", review_count=130, last_12m=95)
        out = sd.compare([a], [b])
        blob = repr(out).lower()
        self.assertNotIn("score", blob.replace("trust_score", ""))  # no traction/blended score (trust_score is a raw metric)
        for row in out["comparisons"]:
            self.assertIn("source_type", row)
            for m in row["metrics"]:
                self.assertIn("unit", m)  # every number carries a unit -> bound to one axis, not blendable


if __name__ == "__main__":
    unittest.main(verbosity=2)
