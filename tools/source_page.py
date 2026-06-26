#!/usr/bin/env python3
"""Source-page capture + reduce — one URL in, one reduced-evidence envelope out.

Scope is deliberately narrow: fetch ONE web page, reduce it to source-page evidence (title,
normalized visible text, absolute outbound links), and print one JSON envelope to stdout.
That's the whole job. It lifts the proven generic primitive from the cohort-discovery page
extraction probe — opening a listicle/source page and reducing it to text + links materially
improves later evidence reuse — without any of the probe's cohort/qrel/ranking machinery.

What this tool does NOT do — on purpose, so it stays a reusable primitive:
  - No page classification. It never decides whether a page is a listicle, directory, owned
    comparison page, or source artifact. No `page_role`. Caller context may ride under `input`.
  - No cohort / candidate / capture-worthiness / membership / entity-extraction logic.
  - No store/cohort/experiment writes. It PRINTS one envelope; the caller redirects if it wants
    a file. No caller-provided output path (shell redirection already solves persistence).
  - No batching (one URL per invocation), no retry loop, no auto-fallback.

Capture path:
  - Direct HTTP by default: real browser UA, bounded body read, stdlib HTML reduction. Zero spend.
  - Firecrawl scrape ONLY behind --firecrawl-fallback, ONLY when direct HTTP failed to yield
    useful evidence. One paid scrape call per invocation, no retry, markdown+links only (no LLM /
    json format, no enhanced proxy), via the shared `_firecrawl` caller. EVERY fallback failure —
    missing key, transport error, HTTP error, unparseable/`success:false`/thin response — becomes an
    ok:false envelope, never a crash. Credit is billed iff Firecrawl actually answered.

`ok` semantics (load-bearing): `ok:true` means "captured useful reduced evidence", NOT "a
transport returned some bytes". A non-2xx/3xx status, a non-text/binary body, an undecodable or
garbled (e.g. wrongly-compressed) body, or a reduction below the usefulness floor
(MIN_TEXT_CHARS) all return `ok:false` with `error` populated.

CLI:
  python3 tools/source_page.py https://example.com/best-things-2026/
  python3 tools/source_page.py https://www.forbes.com/health/...  --firecrawl-fallback
  python3 tools/source_page.py <url> --timeout 30 --max-bytes 4000000 --max-text-chars 200000 --max-links 300

Exit codes:
  0  useful reduced evidence captured (ok:true)
  2  capture did not yield useful evidence (ok:false): transport/HTTP block, non-text/binary body,
     undecodable/garbled body, or a reduction below the usefulness floor. One envelope is STILL
     printed to stdout — the failure is loud (non-zero + stderr) but the evidence stays inspectable.
  (No exit 3: generic HTML has no pinned upstream schema, so `schema_drift` is always [] and there
   is no shape validator — don't cargo-cult one onto an open-ended reducer.)

Auth: only the Firecrawl fallback needs a key — FIRECRAWL_API_KEY via _env.load_key (env first,
repo-root `.env` fallback). The direct-HTTP path needs no key.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
import zlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urljoin, urlparse

import _firecrawl

# A real browser UA, not a bot string: the prior probe's bot UA is exactly what got it blocked on
# Forbes/U.S. News. A plausible desktop Chrome UA clears most polite anti-bot gates on direct HTTP.
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

DEFAULT_TIMEOUT = 25
DEFAULT_MAX_BYTES = 2_500_000  # bound the body read so a giant page can't blow up memory
DEFAULT_MAX_TEXT_CHARS = 300_000  # cap the EMITTED text; text_chars still reports the full length
DEFAULT_MAX_LINKS = 400  # cap the EMITTED links; link_count still reports the full count
MIN_TEXT_CHARS = 500  # usefulness floor: a reduction below this is a thin shell, not evidence -> ok:false
GARBLE_RATIO = 0.05  # >5% U+FFFD replacement chars => the decode is garbage (wrong/failed compression)


@dataclass
class LinkRecord:
    """One absolute anchor extracted from a fetched page."""

    href: str
    text: str
    domain: str | None
    position: int


@dataclass
class Reduction:
    """Reduced title / normalized text / absolute links from one HTML body."""

    title: str | None
    text: str
    links: list[LinkRecord] = field(default_factory=list)


@dataclass
class FetchResult:
    """One direct-HTTP fetch outcome (transport-level, pre-reduction)."""

    status: int | None
    content_type: str | None
    content_encoding: str | None
    final_url: str
    body: bytes
    error: str | None


class PageParser(HTMLParser):
    """Small stdlib HTML reducer: visible text + absolute links, skipping non-content tags.

    Deliberately the probe's parser, hardened only at the edges: script/style/noscript/svg are
    dropped wholesale, the <title> is captured, anchors are absolutized against the page's final
    URL, and emitted text is whitespace-normalized. No DOM, no JS — a thin-but-honest reduction.
    """

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.skip_depth = 0
        self.title_depth = 0
        self.link_href: str | None = None
        self.link_text: list[str] = []
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.links: list[LinkRecord] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.title_depth += 1
        if tag == "a":
            href = attr.get("href")
            self.link_href = urljoin(self.base_url, href) if href else None
            self.link_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "a" and self.link_href:
            text = clean_text(" ".join(self.link_text))
            self.links.append(
                LinkRecord(
                    href=self.link_href,
                    text=text,
                    domain=canonical_domain(self.link_href),
                    position=len(self.links) + 1,
                )
            )
            self.link_href = None
            self.link_text = []

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        cleaned = clean_text(data)
        if not cleaned:
            return
        if self.title_depth:
            self.title_parts.append(cleaned)
        if self.link_href is not None:
            self.link_text.append(cleaned)
        self.text_parts.append(cleaned)

    def result(self) -> Reduction:
        """Return the reduced page: normalized text, title, absolute links."""
        text = clean_text(" ".join(self.text_parts))
        title = clean_text(" ".join(self.title_parts)) or None
        return Reduction(title=title, text=text, links=self.links)


def utc_now() -> str:
    """This invocation's capture time, UTC ISO 8601 — the envelope's `captured_at` (a wall-clock,
    never a source-reported date)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clean_text(value: str) -> str:
    """Normalize extracted text enough for matching and reuse: collapse all whitespace runs."""
    return re.sub(r"\s+", " ", value).strip()


def canonical_domain(value: str | None) -> str | None:
    """Normalize a URL (or bare domain) to host form, dropping a leading www."""
    if not value:
        return None
    parsed = urlparse(value if "://" in value else f"https://{value}")
    host = parsed.netloc.lower().removeprefix("www.")
    return host or None


def _charset_from_content_type(content_type: str | None) -> str | None:
    """Pull `charset=` from a Content-Type header, e.g. 'text/html; charset=iso-8859-1' -> 'iso-8859-1'."""
    if not content_type:
        return None
    match = re.search(r"charset=([\w\-]+)", content_type, re.IGNORECASE)
    return match.group(1).lower() if match else None


def _looks_text(content_type: str | None, body: bytes) -> bool:
    """Is this body a text/HTML page we should reduce — not an image/pdf/binary blob?

    Gate on the declared Content-Type when present (accept html/xml/text, reject the rest). When the
    header is absent, sniff for NUL bytes in the head as a binary tell. Reject early so we never feed
    a binary blob through the HTML parser and emit plausible-but-garbage text.
    """
    if content_type:
        ct = content_type.lower()
        return any(token in ct for token in ("html", "xml", "text"))
    return b"\x00" not in body[:2048]


def _decompress(body: bytes, content_encoding: str | None) -> bytes:
    """Decompress a body the server compressed despite our `Accept-Encoding: identity`.

    Handles gzip and deflate (stdlib). Anything else (br, truncated streams) is left as-is — the
    downstream garble check then flags the undecodable bytes as ok:false rather than crashing.
    """
    enc = (content_encoding or "").lower()
    try:
        if "gzip" in enc:
            return gzip.decompress(body)
        if "deflate" in enc:
            try:
                return zlib.decompress(body)
            except zlib.error:
                return zlib.decompress(body, -zlib.MAX_WBITS)
    except (OSError, zlib.error):
        return body
    return body


def _decode(body: bytes, content_type: str | None) -> tuple[str, str, bool]:
    """Decode bytes -> (text, encoding_used, garbled).

    Prefer the header charset, default utf-8, decode with errors='replace', then judge garble by the
    U+FFFD replacement ratio: a normal page has ~none, a wrongly-compressed/binary body is mostly
    replacements. This is the silent-mojibake guard the probe lacked (it decoded utf-8/replace blind).
    """
    charset = _charset_from_content_type(content_type) or "utf-8"
    try:
        text = body.decode(charset, errors="replace")
    except LookupError:  # unknown charset name in the header
        charset = "utf-8"
        text = body.decode(charset, errors="replace")
    ratio = text.count("�") / max(len(text), 1)
    return text, charset, ratio > GARBLE_RATIO


def reduce_html(html: str, base_url: str) -> Reduction:
    """Parse one decoded HTML string into reduced title/text/links."""
    parser = PageParser(base_url)
    parser.feed(html)
    return parser.result()


def fetch_url(url: str, timeout: int, max_bytes: int) -> FetchResult:
    """Fetch one page over direct HTTP with a real UA and a bounded body read.

    Asks for `identity` encoding (we want to parse the raw HTML), but tolerates servers that ignore
    it (see _decompress). Network/timeout failures and HTTP errors are captured into the result as
    `error`/`status` rather than raised — the tool always emits one envelope, even for a dead URL.
    """
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "identity",
        },
    )
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            body = response.read(max_bytes)
            return FetchResult(
                status=response.status,
                content_type=response.headers.get("content-type"),
                content_encoding=response.headers.get("content-encoding"),
                final_url=response.geturl(),
                body=body,
                error=None,
            )
    except urllib.error.HTTPError as exc:
        body = exc.read(max_bytes) if hasattr(exc, "read") else b""
        return FetchResult(
            status=exc.code,
            content_type=exc.headers.get("content-type") if exc.headers else None,
            content_encoding=exc.headers.get("content-encoding") if exc.headers else None,
            final_url=getattr(exc, "url", url) or url,
            body=body,
            error=f"HTTP {exc.code}: {exc.reason}",
        )
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as exc:
        return FetchResult(status=None, content_type=None, content_encoding=None, final_url=url, body=b"", error=str(exc))


def _envelope_base(url: str, source: str, args_echo: dict[str, Any]) -> dict[str, Any]:
    """The reserved envelope spine shared with every tools/ tool (see tools/README.md)."""
    return {
        "tool": "source_page",
        "source": source,  # direct_http | firecrawl.dev/scrape — the capture mechanism actually used
        "captured_at": utc_now(),
        "ok": False,  # set True only on useful reduced evidence
        "input": {"url": url, **args_echo},
        "schema_drift": [],  # always []: open-ended HTML has no pinned upstream schema (no exit-3 path)
    }


def _emit_links(links: list[LinkRecord], max_links: int) -> list[dict[str, Any]]:
    """Render reduced links to the emitted (capped) JSON shape."""
    return [{"href": link.href, "text": link.text, "domain": link.domain, "position": link.position} for link in links[:max_links]]


def capture_direct(url: str, *, timeout: int, max_bytes: int, max_text_chars: int, max_links: int) -> dict[str, Any]:
    """Direct-HTTP capture: fetch, reduce, and judge usefulness into one envelope.

    `ok:true` requires ALL of: a 2xx/3xx status, a text/HTML body (not binary), a clean decode (not
    garbled), and a reduction at or above MIN_TEXT_CHARS. Otherwise `ok:false` with the first failing
    reason in `error`. Parsed fields are suppressed for binary/garbled bodies (parsing them yields
    junk); for HTTP errors / thin shells the parsed text is kept (a block page's text is real evidence).
    """
    fetched = fetch_url(url, timeout=timeout, max_bytes=max_bytes)
    envelope = _envelope_base(
        url,
        "direct_http",
        {"firecrawl_fallback": False, "timeout": timeout, "max_bytes": max_bytes, "max_text_chars": max_text_chars, "max_links": max_links},
    )
    envelope["status"] = fetched.status
    envelope["content_type"] = fetched.content_type
    envelope["final_url"] = fetched.final_url

    # Transport failure: no body to reduce.
    if fetched.status is None:
        return _finish(
            envelope,
            error=f"fetch failed: {fetched.error}",
            reduction=Reduction(None, "", []),
            max_text_chars=max_text_chars,
            max_links=max_links,
        )

    # Non-text / binary body: refuse to parse it into plausible-but-garbage text.
    if not _looks_text(fetched.content_type, fetched.body):
        return _finish(
            envelope,
            error=f"non-text/binary content_type: {fetched.content_type!r}",
            reduction=Reduction(None, "", []),
            max_text_chars=max_text_chars,
            max_links=max_links,
        )

    body = _decompress(fetched.body, fetched.content_encoding)
    text, _encoding, garbled = _decode(body, fetched.content_type)
    if garbled:
        return _finish(
            envelope,
            error="undecodable/garbled body (wrong or unsupported content-encoding)",
            reduction=Reduction(None, "", []),
            max_text_chars=max_text_chars,
            max_links=max_links,
        )

    reduction = reduce_html(text, fetched.final_url)

    # First failing usefulness reason wins; None means ok.
    error: str | None = None
    if not (200 <= fetched.status < 400):
        error = fetched.error or f"HTTP {fetched.status}"
    elif len(reduction.text) < MIN_TEXT_CHARS:
        error = f"thin reduction: {len(reduction.text)} chars below usefulness floor {MIN_TEXT_CHARS}"
    return _finish(envelope, error=error, reduction=reduction, max_text_chars=max_text_chars, max_links=max_links)


def _finish(envelope: dict[str, Any], *, error: str | None, reduction: Reduction, max_text_chars: int, max_links: int) -> dict[str, Any]:
    """Attach the reduced payload + ok/error to a direct-capture envelope and return it."""
    envelope["ok"] = error is None
    envelope["error"] = error
    envelope["title"] = reduction.title
    envelope["text"] = reduction.text[:max_text_chars]
    envelope["text_chars"] = len(reduction.text)  # full reduced length; `text` above may be capped
    envelope["links"] = _emit_links(reduction.links, max_links)
    envelope["link_count"] = len(reduction.links)
    return envelope


def _firecrawl_body(url: str) -> dict[str, Any]:
    """The source-page scrape recipe: markdown + links only, no LLM/json format, no enhanced proxy.

    The recipe stays here (source_page owns what it asks Firecrawl for); the call + parse + error
    classification live in the shared `_firecrawl` caller, lifted on this, the second Firecrawl tool.
    """
    return {
        "url": url,
        "formats": ["markdown", "links"],
        "maxAge": 0,
        "waitFor": 3500,
        "timeout": 60000,
        "onlyMainContent": False,
        "location": {"country": "US", "languages": ["en-US"]},
    }


def _firecrawl_links(raw: dict[str, Any]) -> list[LinkRecord]:
    """Normalize Firecrawl's link payload (strings or dicts) to the same reduced link shape."""
    data = raw.get("data") if isinstance(raw.get("data"), dict) else raw
    links = data.get("links") or []
    normalized: list[LinkRecord] = []
    for index, item in enumerate(links, start=1):
        if isinstance(item, str):
            href, text = item, item
        elif isinstance(item, dict):
            href = str(item.get("url") or item.get("href") or item.get("link") or "")
            text = str(item.get("text") or item.get("title") or href)
        else:
            continue
        if not href:
            continue
        normalized.append(LinkRecord(href=href, text=clean_text(text), domain=canonical_domain(href), position=index))
    return normalized


def capture_firecrawl(url: str, *, args_echo: dict[str, Any], timeout: int, max_text_chars: int, max_links: int) -> dict[str, Any]:
    """Firecrawl-fallback capture: exactly one paid scrape via the shared `_firecrawl` caller, then
    reduce its markdown/links to an envelope.

    Every failure is an ok:false envelope, never a crash (the tool's one-envelope contract): a missing
    key or a pre-answer transport/HTTP error -> 0 credits; a returned-but-unusable answer
    (`success:false`, unparseable JSON, or thin markdown) -> 1 credit, ok:false, and NO second call.
    """
    envelope = _envelope_base(url, "firecrawl.dev/scrape", args_echo)
    result = _firecrawl.scrape(_firecrawl_body(url), timeout=max(timeout, 120))

    data = result.raw.get("data") if isinstance(result.raw.get("data"), dict) else result.raw
    markdown = clean_text(str(data.get("markdown") or "")) if isinstance(data, dict) else ""
    metadata = data.get("metadata") if isinstance(data, dict) and isinstance(data.get("metadata"), dict) else {}
    links = _firecrawl_links(result.raw)

    # Prefer Firecrawl's own per-call billed number (metadata.creditsUsed — the attribution-grade truth
    # per firecrawl-capture.md; catches a multi-page PDF's >1 charge), falling back to the reached-based
    # estimate when the field is absent. Billed the moment Firecrawl answered, usable or not.
    billed = metadata.get("creditsUsed") if isinstance(metadata, dict) else None
    envelope["cost"] = {"firecrawl_credits_estimate": billed if isinstance(billed, int) else (1 if result.reached else 0)}

    envelope["status"] = metadata.get("statusCode") or (200 if result.reached else None)
    envelope["content_type"] = "text/markdown"

    success = bool(result.raw.get("success"))
    if result.error:  # the call/parse itself failed (missing key, transport, HTTP error, bad JSON)
        error: str | None = result.error
    elif not success:
        error = f"firecrawl returned no usable result: {result.raw.get('error') or 'success=false'}"
    elif len(markdown) < MIN_TEXT_CHARS:
        error = f"thin firecrawl reduction: {len(markdown)} chars below usefulness floor {MIN_TEXT_CHARS}"
    else:
        error = None

    envelope["ok"] = error is None
    envelope["error"] = error
    envelope["title"] = (metadata.get("title") if isinstance(metadata, dict) else None) or None
    envelope["text"] = markdown[:max_text_chars]
    envelope["text_chars"] = len(markdown)
    envelope["links"] = _emit_links(links, max_links)
    envelope["link_count"] = len(links)
    return envelope


def capture(url: str, *, firecrawl_fallback: bool, timeout: int, max_bytes: int, max_text_chars: int, max_links: int) -> dict[str, Any]:
    """Top-level capture: direct HTTP, then Firecrawl ONLY if direct failed AND the flag is set.

    Spend-conscious: a successful direct capture never spends a Firecrawl credit, even with the flag
    on. The fallback fires once, on a direct miss, and only when the caller opted in.
    """
    direct = capture_direct(url, timeout=timeout, max_bytes=max_bytes, max_text_chars=max_text_chars, max_links=max_links)
    if direct["ok"] or not firecrawl_fallback:
        return direct
    args_echo = {
        "firecrawl_fallback": True,
        "timeout": timeout,
        "max_bytes": max_bytes,
        "max_text_chars": max_text_chars,
        "max_links": max_links,
        "direct_http_error": direct["error"],
    }
    return capture_firecrawl(url, args_echo=args_echo, timeout=timeout, max_text_chars=max_text_chars, max_links=max_links)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="The single page URL to capture and reduce.")
    parser.add_argument(
        "--firecrawl-fallback", action="store_true", help="Spend ONE Firecrawl scrape credit if direct HTTP fails to yield useful evidence."
    )
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help=f"Per-request timeout, seconds (default: {DEFAULT_TIMEOUT}).")
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES, help=f"Max body bytes read (default: {DEFAULT_MAX_BYTES}).")
    parser.add_argument(
        "--max-text-chars",
        type=int,
        default=DEFAULT_MAX_TEXT_CHARS,
        help=f"Max EMITTED text chars; text_chars still reports the full length (default: {DEFAULT_MAX_TEXT_CHARS}).",
    )
    parser.add_argument(
        "--max-links",
        type=int,
        default=DEFAULT_MAX_LINKS,
        help=f"Max EMITTED links; link_count still reports the full count (default: {DEFAULT_MAX_LINKS}).",
    )
    args = parser.parse_args()

    result = capture(
        args.url,
        firecrawl_fallback=args.firecrawl_fallback,
        timeout=args.timeout,
        max_bytes=args.max_bytes,
        max_text_chars=args.max_text_chars,
        max_links=args.max_links,
    )
    print(json.dumps(result, indent=2))
    if not result["ok"]:
        sys.stderr.write(f"source_page: ok=false for {args.url!r}: {result.get('error')}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
