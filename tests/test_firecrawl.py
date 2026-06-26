#!/usr/bin/env python3
"""Tests for _firecrawl.py — the shared `/v2/scrape` caller's failure classification.

This is where the source_page review's finding-1 fix actually lives: the inlined callers used to
crash on a missing key or a non-JSON Firecrawl response (the exception escaped before an envelope was
built). The helper turns each of the four failure modes into a ScrapeResult instead — and the
`reached` bit is what lets a caller bill honestly. The source_page tests mock the helper, so they
don't exercise this layer; these do, by mocking urlopen + the key loader. No live network calls."""

from __future__ import annotations

import json
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import _firecrawl as fc

BODY = {"url": "https://example.com/x", "formats": ["markdown", "links"]}


class _FakeResponse:
    """A urlopen() context manager whose .read() returns canned bytes."""

    def __init__(self, payload: bytes) -> None:
        self._payload = payload

    def __enter__(self) -> _FakeResponse:
        return self

    def __exit__(self, *exc: object) -> bool:
        return False

    def read(self) -> bytes:
        return self._payload


def _urlopen_returning(payload: bytes) -> MagicMock:
    return MagicMock(return_value=_FakeResponse(payload))


class CleanCall(unittest.TestCase):
    """A 2xx with a JSON object body: reached, raw carried through, no error."""

    def test_good_json_is_reached_with_raw(self) -> None:
        payload = json.dumps({"success": True, "data": {"markdown": "hi"}}).encode()
        with patch.object(fc, "load_key", return_value="k"), patch("urllib.request.urlopen", _urlopen_returning(payload)):
            result = fc.scrape(BODY, timeout=30)
        self.assertTrue(result.reached)
        self.assertIsNone(result.error)
        self.assertEqual(result.raw["data"]["markdown"], "hi")

    def test_request_carries_auth_header_and_endpoint(self) -> None:
        captured: dict[str, object] = {}

        def _spy(request: object, timeout: int = 0) -> _FakeResponse:
            captured["url"] = request.full_url  # type: ignore[attr-defined]
            captured["auth"] = request.get_header("Authorization")  # type: ignore[attr-defined]
            return _FakeResponse(b'{"success": true}')

        with patch.object(fc, "load_key", return_value="secret"), patch("urllib.request.urlopen", _spy):
            fc.scrape(BODY, timeout=30)
        self.assertEqual(captured["url"], fc.SCRAPE_ENDPOINT)
        self.assertEqual(captured["auth"], "Bearer secret")

    def test_explicit_api_key_skips_load_key(self) -> None:
        load = MagicMock()
        with patch.object(fc, "load_key", load), patch("urllib.request.urlopen", _urlopen_returning(b'{"success": true}')):
            result = fc.scrape(BODY, timeout=30, api_key="preloaded")
        load.assert_not_called()  # the caller's key is used directly (trustpilot's path)
        self.assertTrue(result.reached)


class FailureModes(unittest.TestCase):
    """The four classified failures — the finding-1 fix. None of these may raise."""

    def test_missing_key_is_unreached_and_never_calls_urlopen(self) -> None:
        # _env.load_key fails loud (RuntimeError) on a missing key; the helper softens it to a result.
        opener = MagicMock()
        with (
            patch.object(fc, "load_key", side_effect=RuntimeError("Missing FIRECRAWL_API_KEY — set it in the environment")),
            patch("urllib.request.urlopen", opener),
        ):
            result = fc.scrape(BODY, timeout=30)
        self.assertFalse(result.reached)  # no call made -> nothing charged
        self.assertIn("Missing FIRECRAWL_API_KEY", result.error)
        opener.assert_not_called()

    def test_transport_error_is_unreached(self) -> None:
        opener = MagicMock(side_effect=urllib.error.URLError("connection refused"))
        with patch.object(fc, "load_key", return_value="k"), patch("urllib.request.urlopen", opener):
            result = fc.scrape(BODY, timeout=30)
        self.assertFalse(result.reached)
        self.assertIn("transport error", result.error)

    def test_http_error_is_unreached_with_code(self) -> None:
        err = urllib.error.HTTPError(fc.SCRAPE_ENDPOINT, 429, "Too Many Requests", {}, None)  # type: ignore[arg-type]
        with patch.object(fc, "load_key", return_value="k"), patch("urllib.request.urlopen", MagicMock(side_effect=err)):
            result = fc.scrape(BODY, timeout=30)
        self.assertFalse(result.reached)  # API error status -> no successful scrape -> no credit
        self.assertIn("429", result.error)

    def test_unparseable_body_is_reached_and_charged(self) -> None:
        # The exact bug class the inlined callers crashed on: a body Firecrawl billed for but we can't
        # parse. reached=True (charged), raw empty, error set — never an escaped JSONDecodeError.
        with patch.object(fc, "load_key", return_value="k"), patch("urllib.request.urlopen", _urlopen_returning(b"<html>not json</html>")):
            result = fc.scrape(BODY, timeout=30)
        self.assertTrue(result.reached)
        self.assertEqual(result.raw, {})
        self.assertIn("unparseable", result.error)

    def test_non_object_json_is_reached_with_error(self) -> None:
        with patch.object(fc, "load_key", return_value="k"), patch("urllib.request.urlopen", _urlopen_returning(b"[1, 2, 3]")):
            result = fc.scrape(BODY, timeout=30)
        self.assertTrue(result.reached)
        self.assertEqual(result.raw, {})
        self.assertIn("non-object", result.error)


if __name__ == "__main__":
    unittest.main(verbosity=2)
