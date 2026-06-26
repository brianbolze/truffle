#!/usr/bin/env python3
"""Tests for source_page.py — the stdlib reducer, the envelope shape, the load-bearing `ok` floor,
the single-call-no-retry Firecrawl spend boundary, and the negative checks that prove the tool stays
a capture primitive (no page_role / classification / store-write). No live network calls."""

from __future__ import annotations

import gzip
import re
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import _firecrawl as fc
import source_page as sp


def _scrape_result(*, reached: bool, raw: dict | None = None, error: str | None = None) -> fc.ScrapeResult:
    """Build a `_firecrawl.ScrapeResult` so the fallback path can be exercised without network/spend."""
    return fc.ScrapeResult(reached=reached, raw=raw or {}, error=error)


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "source_page"
BASE_URL = "https://list.example.com/best/widgets/"

# Required envelope keys, per tools/README.md + the packet acceptance checks.
REQUIRED_KEYS = {
    "tool",
    "source",
    "captured_at",
    "ok",
    "input",
    "schema_drift",
    "status",
    "content_type",
    "error",
    "title",
    "text",
    "text_chars",
    "links",
    "link_count",
}
# Tokens that would mean the tool crossed from capture into judgment/classification/routing.
FORBIDDEN_KEY_TOKENS = ("page_role", "role", "cohort", "candidate", "classif", "worth", "membership")


def _fetch(
    status: int | None = 200,
    content_type: str | None = "text/html; charset=utf-8",
    content_encoding: str | None = None,
    final_url: str = BASE_URL,
    body: bytes = b"",
    error: str | None = None,
) -> sp.FetchResult:
    """Build a canned FetchResult so capture_direct can be exercised with no network."""
    return sp.FetchResult(
        status=status,
        content_type=content_type,
        content_encoding=content_encoding,
        final_url=final_url,
        body=body,
        error=error,
    )


def _load_fixture(name: str) -> bytes:
    with open(FIXTURES / name, "rb") as handle:
        return handle.read()


class ReducerBehavior(unittest.TestCase):
    """The stdlib HTMLParser reduction: title, normalized text, absolute links, skipped chrome."""

    def setUp(self) -> None:
        self.reduction = sp.reduce_html(_load_fixture("listicle.html").decode("utf-8"), BASE_URL)

    def test_title_extracted(self) -> None:
        self.assertEqual(self.reduction.title, "Best Widgets 2026 - Example List")

    def test_script_style_noscript_svg_are_skipped(self) -> None:
        for junk in ("SKIP_ME_TRACKER", "tracking_beacon", ".promo", "enable JavaScript", "SVG_SKIP_TEXT"):
            self.assertNotIn(junk, self.reduction.text)

    def test_text_is_real_evidence_and_normalized(self) -> None:
        self.assertIn("The 7 Best Widget Providers for 2026", self.reduction.text)
        self.assertIn("best value", self.reduction.text)
        self.assertGreater(len(self.reduction.text), sp.MIN_TEXT_CHARS)
        self.assertNotIn("  ", self.reduction.text)  # whitespace runs collapsed

    def test_links_absolutized_with_domain_and_position(self) -> None:
        by_text = {link.text: link for link in self.reduction.links}
        # Absolute link: www stripped from the canonical domain.
        self.assertEqual(by_text["Brand A"].href, "https://www.brand-a.com/")
        self.assertEqual(by_text["Brand A"].domain, "brand-a.com")
        self.assertEqual(by_text["Brand B Pricing"].domain, "brand-b.io")
        # Relative href absolutized against the page's final URL.
        self.assertEqual(by_text["methodology page"].href, "https://list.example.com/methodology/2026")
        self.assertEqual(by_text["Home"].href, "https://list.example.com/")
        positions = [link.position for link in self.reduction.links]
        self.assertEqual(positions, list(range(1, len(positions) + 1)))


class EnvelopeShape(unittest.TestCase):
    """A useful direct capture produces the reserved spine + payload, ok:true, no cost, no drift path."""

    def setUp(self) -> None:
        with patch.object(sp, "fetch_url", return_value=_fetch(body=_load_fixture("listicle.html"))):
            self.env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)

    def test_required_keys_present(self) -> None:
        self.assertTrue(REQUIRED_KEYS.issubset(self.env.keys()))

    def test_provenance_and_payload(self) -> None:
        self.assertEqual(self.env["tool"], "source_page")
        self.assertEqual(self.env["source"], "direct_http")
        self.assertTrue(self.env["ok"])
        self.assertIsNone(self.env["error"])
        self.assertEqual(self.env["input"]["url"], BASE_URL)
        self.assertGreater(self.env["text_chars"], sp.MIN_TEXT_CHARS)
        self.assertGreater(self.env["link_count"], 0)

    def test_schema_drift_always_empty(self) -> None:
        self.assertEqual(self.env["schema_drift"], [])

    def test_direct_path_carries_no_cost_key(self) -> None:
        # `cost` is "only where the source meters credits" — direct HTTP meters nothing.
        self.assertNotIn("cost", self.env)

    def test_emitted_text_capped_but_text_chars_is_full_length(self) -> None:
        self.assertLessEqual(len(self.env["text"]), 1000)
        self.assertGreater(self.env["text_chars"], len(self.env["text"]))


class OkFloorAndGuards(unittest.TestCase):
    """ok:true means useful evidence — thin shells, HTTP errors, binary, and garbled bodies fail loud."""

    def test_thin_shell_fails_floor_but_keeps_parsed_text(self) -> None:
        shell = b"<html><head><title>Loading</title></head><body><div id='app'>Loading...</div></body></html>"
        with patch.object(sp, "fetch_url", return_value=_fetch(body=shell)):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("thin reduction", env["error"])
        self.assertEqual(env["title"], "Loading")  # parsed text is kept — a thin page is real, just not useful

    def test_http_error_is_loud(self) -> None:
        blocked = b"<html><body><h1>Access Denied</h1>" + b"<p>blocked</p>" * 60 + b"</body></html>"
        with patch.object(sp, "fetch_url", return_value=_fetch(status=403, body=blocked, error="HTTP 403: Forbidden")):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("403", env["error"])
        self.assertEqual(env["status"], 403)

    def test_transport_failure_emits_envelope_not_crash(self) -> None:
        with patch.object(sp, "fetch_url", return_value=_fetch(status=None, content_type=None, body=b"", error="timed out")):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("fetch failed", env["error"])
        self.assertEqual(env["text"], "")
        self.assertEqual(env["link_count"], 0)

    def test_binary_content_type_is_rejected_unparsed(self) -> None:
        with patch.object(sp, "fetch_url", return_value=_fetch(content_type="image/png", body=b"\x89PNG\r\n\x1a\n" + b"\x00" * 200)):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("non-text", env["error"])
        self.assertIsNone(env["title"])
        self.assertEqual(env["text"], "")

    def test_gzip_body_decompresses_when_encoding_declared(self) -> None:
        gz = gzip.compress(_load_fixture("listicle.html"))
        with patch.object(sp, "fetch_url", return_value=_fetch(content_encoding="gzip", body=gz)):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertTrue(env["ok"])
        self.assertIn("Widget Providers", env["text"])

    def test_garbled_body_fails_loud(self) -> None:
        # Server gzipped the body but did NOT set Content-Encoding -> undecodable bytes, not evidence.
        gz = gzip.compress(_load_fixture("listicle.html"))
        with patch.object(sp, "fetch_url", return_value=_fetch(content_encoding=None, body=gz)):
            env = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("garbled", env["error"])
        self.assertEqual(env["text"], "")


class FirecrawlEnvelope(unittest.TestCase):
    """The fallback path: ok read off success+markdown, one metered credit, links normalized."""

    def _good_response(self) -> dict:
        return {
            "success": True,
            "data": {
                "markdown": "# Best Providers\n\n" + ("Useful captured evidence about providers. " * 30),
                "links": [
                    "https://brand-a.com/",
                    {"url": "https://brand-b.io/pricing", "text": "Brand B"},
                    {"href": "https://www.brand-c.org/"},
                ],
                "metadata": {"title": "Best Providers 2026", "statusCode": 200},
            },
        }

    def test_good_response_is_ok_with_one_credit(self) -> None:
        with patch.object(sp._firecrawl, "scrape", return_value=_scrape_result(reached=True, raw=self._good_response())) as scrape:
            env = sp.capture_firecrawl(BASE_URL, args_echo={"firecrawl_fallback": True}, timeout=120, max_text_chars=5000, max_links=50)
        self.assertEqual(scrape.call_count, 1)
        self.assertTrue(env["ok"])
        self.assertEqual(env["source"], "firecrawl.dev/scrape")
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 1})
        self.assertEqual(env["title"], "Best Providers 2026")
        self.assertEqual(env["link_count"], 3)
        self.assertEqual(env["links"][1]["domain"], "brand-b.io")
        self.assertEqual(env["links"][2]["domain"], "brand-c.org")  # www stripped

    def test_billed_credits_used_is_honored_over_estimate(self) -> None:
        # firecrawl-capture.md: metadata.creditsUsed is the attribution-grade billed number — a
        # multi-page PDF bills >1. When present, the cost reflects it, not the flat reached-estimate.
        raw = self._good_response()
        raw["data"]["metadata"]["creditsUsed"] = 3
        with patch.object(sp._firecrawl, "scrape", return_value=_scrape_result(reached=True, raw=raw)):
            env = sp.capture_firecrawl(BASE_URL, args_echo={"firecrawl_fallback": True}, timeout=120, max_text_chars=5000, max_links=50)
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 3})


class SpendBoundary(unittest.TestCase):
    """The negative spend check (proposal-review finding 1): at most ONE Firecrawl call, no retry,
    no fallback unless asked, no spend when direct already worked."""

    def _blocked(self) -> sp.FetchResult:
        blocked = b"<html><body><h1>Access Denied</h1>" + b"<p>blocked</p>" * 60 + b"</body></html>"
        return _fetch(status=403, body=blocked, error="HTTP 403: Forbidden")

    def test_direct_success_never_spends_even_with_flag(self) -> None:
        with (
            patch.object(sp, "fetch_url", return_value=_fetch(body=_load_fixture("listicle.html"))),
            patch.object(sp._firecrawl, "scrape") as scrape,
        ):
            env = sp.capture(BASE_URL, firecrawl_fallback=True, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertEqual(scrape.call_count, 0)
        self.assertTrue(env["ok"])
        self.assertEqual(env["source"], "direct_http")

    def test_blocked_without_flag_fails_loud_no_spend(self) -> None:
        with patch.object(sp, "fetch_url", return_value=self._blocked()), patch.object(sp._firecrawl, "scrape") as scrape:
            env = sp.capture(BASE_URL, firecrawl_fallback=False, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertEqual(scrape.call_count, 0)
        self.assertFalse(env["ok"])
        self.assertEqual(env["source"], "direct_http")
        self.assertNotIn("cost", env)

    def test_unusable_firecrawl_answer_is_one_call_no_retry(self) -> None:
        # The crux: a returned-but-unusable answer (reached, success:false) must NOT trigger a second
        # paid call — and it bills the one credit it spent.
        scrape = MagicMock(return_value=_scrape_result(reached=True, raw={"success": False, "error": "blocked upstream"}))
        with patch.object(sp, "fetch_url", return_value=self._blocked()), patch.object(sp._firecrawl, "scrape", scrape):
            env = sp.capture(BASE_URL, firecrawl_fallback=True, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertEqual(scrape.call_count, 1)  # exactly one — no retry on an unusable response
        self.assertFalse(env["ok"])
        self.assertEqual(env["source"], "firecrawl.dev/scrape")
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 1})  # the call was made -> credit spent

    def test_firecrawl_transport_error_spends_nothing(self) -> None:
        # The shared caller swallows the transport error into an unreached result; the tool must still
        # emit one envelope, ok:false, zero credits (finding 1: never a crash).
        scrape = MagicMock(return_value=_scrape_result(reached=False, error="firecrawl transport error: connect timeout"))
        with patch.object(sp, "fetch_url", return_value=self._blocked()), patch.object(sp._firecrawl, "scrape", scrape):
            env = sp.capture(BASE_URL, firecrawl_fallback=True, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertEqual(scrape.call_count, 1)
        self.assertFalse(env["ok"])
        self.assertIn("transport error", env["error"])
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 0})  # no answer reached us -> no credit

    def test_missing_key_emits_envelope_no_crash_no_spend(self) -> None:
        # Finding 1, first half: a missing FIRECRAWL_API_KEY must be an ok:false envelope, not a raise.
        scrape = MagicMock(return_value=_scrape_result(reached=False, error="Missing FIRECRAWL_API_KEY — set it in the environment"))
        with patch.object(sp, "fetch_url", return_value=self._blocked()), patch.object(sp._firecrawl, "scrape", scrape):
            env = sp.capture(BASE_URL, firecrawl_fallback=True, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertEqual(env["source"], "firecrawl.dev/scrape")
        self.assertIn("Missing FIRECRAWL_API_KEY", env["error"])
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 0})

    def test_unparseable_firecrawl_response_is_one_credit_not_crash(self) -> None:
        # Finding 1, second half: a body Firecrawl answered with but we couldn't parse — charged, but
        # an ok:false envelope, never an escaped JSONDecodeError.
        scrape = MagicMock(return_value=_scrape_result(reached=True, error="firecrawl returned unparseable JSON: Expecting value"))
        with patch.object(sp, "fetch_url", return_value=self._blocked()), patch.object(sp._firecrawl, "scrape", scrape):
            env = sp.capture(BASE_URL, firecrawl_fallback=True, timeout=25, max_bytes=10_000, max_text_chars=5000, max_links=50)
        self.assertFalse(env["ok"])
        self.assertIn("unparseable", env["error"])
        self.assertEqual(env["cost"], {"firecrawl_credits_estimate": 1})


class CapturePrimitiveBoundary(unittest.TestCase):
    """Proves the tool never grows page_role / classification / routing / store-writes (acceptance #9)."""

    def _both_envelopes(self) -> list[dict]:
        with patch.object(sp, "fetch_url", return_value=_fetch(body=_load_fixture("listicle.html"))):
            direct = sp.capture_direct(BASE_URL, timeout=25, max_bytes=10_000, max_text_chars=1000, max_links=50)
        raw = {"success": True, "data": {"markdown": "x " * 400, "links": [], "metadata": {"title": "t"}}}
        with patch.object(sp._firecrawl, "scrape", return_value=_scrape_result(reached=True, raw=raw)):
            firecrawl = sp.capture_firecrawl(
                BASE_URL, args_echo={"firecrawl_fallback": True}, timeout=120, max_text_chars=1000, max_links=50
            )
        return [direct, firecrawl]

    def test_no_classification_keys_in_output(self) -> None:
        def keys(node: object) -> set[str]:
            found: set[str] = set()
            if isinstance(node, dict):
                for key, value in node.items():
                    found.add(key)
                    found |= keys(value)
            elif isinstance(node, list):
                for item in node:
                    found |= keys(item)
            return found

        for env in self._both_envelopes():
            all_keys = {key.lower() for key in keys(env)}
            for token in FORBIDDEN_KEY_TOKENS:
                offenders = [key for key in all_keys if token in key]
                self.assertEqual(offenders, [], f"forbidden key token {token!r} in output: {offenders}")

    def test_source_makes_no_file_writes_and_no_schema_validator(self) -> None:
        with open(sp.__file__, encoding="utf-8") as handle:
            source = handle.read()
        for write_token in (".write_text(", ".write_bytes(", ".mkdir(", "Path("):
            self.assertNotIn(write_token, source, f"unexpected file-write surface: {write_token}")
        # A bare builtin open( for file IO — but NOT urllib's urlopen( (network, not disk).
        self.assertIsNone(re.search(r"(?<![A-Za-z_.])open\(", source), "unexpected builtin open() for file IO")
        # No exit-3 / schema-drift validator on an open-ended reducer.
        self.assertNotIn("sys.exit(3)", source)
        self.assertNotIn("PARSER_VERSION", source)
        # No classification literals ever emitted as JSON keys/values.
        for token in ('"page_role"', '"cohort"', '"candidate"', '"page_class"'):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
