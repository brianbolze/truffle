#!/usr/bin/env python3
"""Internet Archive CDX first-seen / tenure lookup + scoped archived-content diff.

Give it ONE URL; it asks the Wayback Machine's CDX Server "show me every archived capture of this
page" and emits the tenure signal: when it was first seen, when last seen, how many distinct content
snapshots exist, and the status lifecycle (200 -> 301 -> 404 = launched, moved, died). That's the
default job. In `diff` mode it fetches two raw archived snapshots and mechanically compares their
text. No key. The caller loops over a roster; this tool does one page.

Why it earns a place: page/SKU *tenure* is the strongest age proxy we have, and a first-seen date
doesn't rot — unlike a price or a roster line, it's a fact about the past that only accretes. It's
the Tenure axis of the candidate-SKU ledger (the `first_seen_*` fields).

first-seen is a LOWER BOUND, and the output says so. It is "first *archived*," never "first
existed" — fresh or obscure pages are under-archived (and robots/exclusions can suppress archiving
entirely), so a page can predate its earliest snapshot. `first_seen_confidence` mirrors the SKU
ledger's labels and reacts to corroboration, NOT to calendar age:
  - insufficient — 0 captures. Never archived: too new, too obscure, or archiving-blocked. Tenure
    is unmeasurable here (this is data, not an error — empty CDX -> ok:true, exit 0).
  - provisional  — exactly 1 capture. A first-seen exists but is uncorroborated; the page may well
    predate its lone snapshot, or that snapshot may be a one-off crawl.
  - measured     — >=2 distinct-content captures. Archived tenure is real; first_seen is a solid
    lower bound. (This is the ledger's "at least 2 real captures" tenure rule.)
  NOTE: confidence is about *how many* captures corroborate, not *how far apart* they sit. A caller
  that needs "first seen >=6 months ago" reads `first_seen` / `tenure_days` itself — two captures a
  day apart are still `measured`. That time-span judgment is the caller's, kept out on purpose.

THE captured_at SPLIT (this tool is the exact case the library convention warns about): the Wayback
snapshot dates ARE the signal, so they live *inside the payload* under their own names (`first_seen`,
`last_seen`, per-snapshot `timestamp`). The envelope's `captured_at` is THIS lookup's wall-clock —
when we asked CDX — never an archive date. Conflating the two would destroy the whole field.

Generic on purpose: emits parsed JSON to stdout, no cohort / Notion / vertical baked in. Matching a
page back to a roster is the caller's job, never this tool's.

CLI:
  python3 tools/wayback.py https://www.henrymeds.com/
  python3 tools/wayback.py example.com                       # passed to CDX as-is; CDX canonicalizes
  python3 tools/wayback.py https://brand.com/products/sermorelin
  python3 tools/wayback.py diff https://brand.com/products/sermorelin
  python3 tools/wayback.py diff https://brand.com/products/sermorelin --from 2023 --to 2025

Exit codes:
  0  clean capture (INCLUDING a never-archived URL -> first_seen:null, confidence:"insufficient" — data, not failure)
  2  fetch error (network, IA HTTP error, or an unexpected/garbled CDX body)
  (no exit 3: CDX is a stable, frozen feed — no version-pinned parser, so no schema-drift path.
   `schema_drift` is still emitted as `[]` for envelope uniformity across the library.)

No key (CDX is free + unauthenticated — no `_env` call). No `parser_version` (frozen feed). No `cost`
(free). The lookup is exact-URL only; whole-section history (matchType=prefix/domain) is a latent
growth path, not v1 — see wayback.md.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html.parser
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

SOURCE = "web.archive.org/cdx"
CDX_BASE = "https://web.archive.org/cdx/search/cdx"
USER_AGENT = "web-research-tools/wayback"
# The CDX columns we request (and the order). `collapse=digest` folds *adjacent* identical-content
# captures, so a row means "content that differs from the row before it" and snapshot_count is a
# distinct-content count, not a raw crawl count.
CDX_FIELDS = "timestamp,original,statuscode,digest,mimetype,length"
REQUIRED_COLUMNS = ("timestamp", "original", "statuscode", "digest")
# Bulk safety bound on the *emitted* snapshots list (oldest first — this tool's first-seen focus).
# Summary fields (first_seen / last_seen / snapshot_count / status_trail) are ALWAYS computed over
# the full set, so a cap here never hides the headline or the lifecycle — only trims the audit tail.
SNAPSHOTS_CAP = 500
DEFAULT_DIFF_CONTEXT_LINES = 3
DEFAULT_MAX_DIFF_LINES = 400


@dataclass(frozen=True)
class CdxRecord:
    """One CDX row with just enough metadata to preserve snapshot provenance."""

    raw_timestamp: str
    original_url: str
    status: str
    digest: str
    mimetype: str | None = None
    length: str | None = None


@dataclass(frozen=True)
class FetchedContent:
    """Replay fetch result, including HTTP failures that still returned a response body."""

    fetch_status: int | None
    final_url: str
    content_type: str | None
    body: bytes
    error: str | None = None


class _HTMLTextExtractor(html.parser.HTMLParser):
    """Small stdlib text extractor for archived HTML; no browser-rendering claims."""

    _block_tags = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "dd",
        "div",
        "dl",
        "dt",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "td",
        "th",
        "tr",
        "ul",
    }
    _skip_tags = {"script", "style", "noscript", "svg", "canvas"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        tag = tag.lower()
        if tag in self._skip_tags:
            self._skip_depth += 1
            return
        if tag in self._block_tags:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self._skip_tags and self._skip_depth:
            self._skip_depth -= 1
            return
        if tag in self._block_tags:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self._parts.append(data)

    def text(self) -> str:
        return "".join(self._parts)


def _utc_now() -> datetime:
    """This invocation's wall-clock (UTC) — the envelope's `captured_at` AND the clock `tenure_days`
    counts back from. Never an archive timestamp: those ARE the signal and live in the payload
    (`first_seen` / `last_seen` / `snapshots[].timestamp`) under their own names. The whole point of
    this tool's design is keeping the two apart."""
    return datetime.now(timezone.utc)


def _ts_to_iso(raw: str) -> str:
    """CDX `YYYYMMDDhhmmss` (UTC) -> ISO 8601 `2019-03-04T12:30:45Z`. Pads a short/garbled stamp
    defensively rather than crashing the row."""
    digits = _complete_timestamp(raw)
    return f"{digits[0:4]}-{digits[4:6]}-{digits[6:8]}T{digits[8:10]}:{digits[10:12]}:{digits[12:14]}Z"


def _ts_to_dt(raw: str) -> datetime:
    """CDX `YYYYMMDDhhmmss` (UTC) -> aware datetime, for the tenure arithmetic."""
    digits = _complete_timestamp(raw)
    return datetime.strptime(digits, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)


def _complete_timestamp(raw: str) -> str:
    """Wayback-ish partial timestamps -> valid `YYYYMMDDhhmmss`, using earliest missing fields."""
    digits = re.sub(r"\D", "", raw)[:14]
    if len(digits) < 4:
        digits = digits.ljust(4, "0")
    year = digits[0:4]
    month = digits[4:6] if len(digits) >= 6 and digits[4:6] != "00" else "01"
    day = digits[6:8] if len(digits) >= 8 and digits[6:8] != "00" else "01"
    hour = digits[8:10] if len(digits) >= 10 else "00"
    minute = digits[10:12] if len(digits) >= 12 else "00"
    second = digits[12:14] if len(digits) >= 14 else "00"
    return f"{year}{month}{day}{hour}{minute}{second}"


def _clean_ts(raw: str) -> str:
    """Wayback timestamp digits, capped at the 14-digit capture precision CDX uses."""
    return re.sub(r"\D", "", raw)[:14]


def _replay_url(raw_ts: str, original: str) -> str:
    """The human-viewable Wayback replay URL for a capture; `diff` also emits the raw `id_` URL."""
    return f"https://web.archive.org/web/{_clean_ts(raw_ts)}/{original}"


def _raw_replay_url(raw_ts: str, original: str) -> str:
    """The raw archived-content replay URL (`id_` mode), with no Wayback chrome."""
    return f"https://web.archive.org/web/{_clean_ts(raw_ts)}id_/{original}"


def _int_or_none(raw: str | None) -> int | None:
    """CDX sometimes uses `-`/blank for unavailable numeric fields; preserve that as null."""
    if raw is None:
        return None
    raw = raw.strip()
    if not raw or raw == "-":
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def _parse_charset(content_type: str | None) -> str:
    """Best-effort charset from an HTTP Content-Type header; UTF-8 is the boring fallback."""
    if not content_type:
        return "utf-8"
    match = re.search(r"charset=([^\s;]+)", content_type, flags=re.IGNORECASE)
    if not match:
        return "utf-8"
    return match.group(1).strip("\"'")


def _looks_like_html(body: bytes, content_type: str | None) -> bool:
    """Classify content as HTML only when the header or first bytes say so."""
    if content_type and "html" in content_type.lower():
        return True
    prefix = body[:200].lstrip().lower()
    return prefix.startswith((b"<!doctype html", b"<html", b"<head", b"<body"))


def _normalize_text(text: str) -> str:
    """Collapse whitespace for line-stable diffs without pretending to semantically clean the page."""
    lines = []
    for line in text.splitlines():
        cleaned = re.sub(r"[^\S\n]+", " ", line).strip()
        if cleaned:
            lines.append(cleaned)
    return "\n".join(lines)


def extract_text_content(body: bytes, content_type: str | None) -> str:
    """Raw replay bytes -> normalized text for mechanical comparison."""
    decoded = body.decode(_parse_charset(content_type), errors="replace")
    if not _looks_like_html(body, content_type):
        return _normalize_text(decoded)
    parser = _HTMLTextExtractor()
    parser.feed(decoded)
    parser.close()
    return _normalize_text(parser.text())


def sha256_hex(data: bytes | str) -> str:
    """Stable content hash for bytes or normalized text."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def build_cdx_url(url: str) -> str:
    """Build the CDX request URL without rewriting the caller's `url` argument."""
    params = {"url": url, "output": "json", "fl": CDX_FIELDS, "collapse": "digest"}
    return f"{CDX_BASE}?{urllib.parse.urlencode(params)}"


def fetch_cdx(url: str, timeout: int = 60) -> list[list[str]]:
    """GET the CDX feed for `url` -> rows (a header row then data rows), or [] when never archived.

    Stdlib urllib, no `requests` dep — the HTTP layer the tools/ library copies. A never-archived URL
    returns HTTP 200 with an EMPTY body (not `[]`), so empty-body is normalized to [] here, NOT
    treated as an error. Network / HTTP errors (urlopen raises HTTPError on 4xx/5xx) bubble to
    main()'s exit-2 handler.
    """
    req = urllib.request.Request(build_cdx_url(url), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace").strip()
    if not body:  # never-archived URL -> empty body, the "insufficient" signal
        return []
    parsed = json.loads(body)
    if not isinstance(parsed, list):
        # CDX is a frozen feed; an unexpected body is transport-class noise, not schema drift (no
        # version-pinned parser exists to drift). Surface it loud -> exit 2, mirroring exa_similar.
        raise RuntimeError(f"CDX returned a non-list body ({type(parsed).__name__}): {str(parsed)[:200]}")
    return parsed


def parse_records(rows: list[list[str]]) -> list[CdxRecord]:
    """CDX rows -> records, sorted oldest-first.

    Columns are mapped by the header row's NAMES (not by position) so a future reordering of `fl`
    can't silently misalign fields. A header missing a required column is an unexpected body -> exit 2.
    CDX already returns ascending-by-timestamp; we re-sort anyway so first/last/trail can't depend on
    that promise holding.
    """
    if not rows:
        return []
    header = rows[0]
    if not isinstance(header, list):
        raise RuntimeError(f"CDX first row is not a header list: {str(header)[:200]}")
    idx = {name: i for i, name in enumerate(header)}
    missing = [c for c in REQUIRED_COLUMNS if c not in idx]
    if missing:
        raise RuntimeError(f"CDX header missing columns {missing}: {header}")
    records = [
        CdxRecord(
            raw_timestamp=row[idx["timestamp"]],
            original_url=row[idx["original"]],
            status=row[idx["statuscode"]],
            digest=row[idx["digest"]],
            mimetype=row[idx["mimetype"]] if "mimetype" in idx and len(row) > idx["mimetype"] else None,
            length=row[idx["length"]] if "length" in idx and len(row) > idx["length"] else None,
        )
        for row in rows[1:]
    ]
    records.sort(key=lambda record: record.raw_timestamp)
    return records


def build_status_trail(records: list[CdxRecord]) -> list[dict[str, str]]:
    """Collapse consecutive captures with the same HTTP status into runs -> the lifecycle signal.

    `[{status:"200", from:.., to:..}, {status:"301", ..}, {status:"404", ..}]` reads as launched,
    moved, died. Computed over the FULL record set (never the capped snapshots list) and surfaced
    top-level, so the cap on `snapshots` can't hide a page's death. `status` is kept verbatim — CDX
    uses `-` for revisit / unknown-status records; we report it, we don't normalize it.
    """
    trail: list[dict[str, str]] = []
    for record in records:
        iso = _ts_to_iso(record.raw_timestamp)
        if trail and trail[-1]["status"] == record.status:
            trail[-1]["to"] = iso
        else:
            trail.append({"status": record.status, "from": iso, "to": iso})
    return trail


def snapshot_provenance(record: CdxRecord) -> dict[str, Any]:
    """CDX provenance for one selected snapshot, including both replay URL forms."""
    return {
        "timestamp": _ts_to_iso(record.raw_timestamp),
        "raw_timestamp": _clean_ts(record.raw_timestamp),
        "original_url": record.original_url,
        "replay_url": _replay_url(record.raw_timestamp, record.original_url),
        "raw_replay_url": _raw_replay_url(record.raw_timestamp, record.original_url),
        "status": record.status,
        "digest": record.digest,
        "mimetype": record.mimetype,
        "length": _int_or_none(record.length),
    }


def _nearest_record_index(records: list[CdxRecord], target_timestamp: str) -> int:
    """Find the CDX record nearest to a caller's target timestamp."""
    target = _ts_to_dt(target_timestamp)
    return min(range(len(records)), key=lambda index: abs(_ts_to_dt(records[index].raw_timestamp) - target))


def select_diff_records(
    records: list[CdxRecord],
    from_timestamp: str | None = None,
    to_timestamp: str | None = None,
) -> tuple[list[CdxRecord], str, str | None]:
    """Pick two records for content diff: first/last by default, nearest-to-targets when supplied."""
    if not records:
        return [], "no_snapshots", "CDX returned no snapshots for this URL."
    if len(records) == 1:
        return [records[0]], "insufficient_snapshots", "Only one distinct snapshot is available; diff needs two."

    from_index = _nearest_record_index(records, from_timestamp) if from_timestamp else 0
    to_index = _nearest_record_index(records, to_timestamp) if to_timestamp else len(records) - 1

    if from_index == to_index:
        return [records[from_index]], "insufficient_distinct_selection", "The requested targets resolved to the same snapshot."

    selected = [records[from_index], records[to_index]]
    selected.sort(key=lambda record: record.raw_timestamp)
    return selected, "selected", None


def fetch_replay_content(record: CdxRecord, timeout: int = 60) -> FetchedContent:
    """GET one raw Wayback replay; HTTP error responses are captured as snapshot fetch metadata."""
    raw_url = _raw_replay_url(record.raw_timestamp, record.original_url)
    req = urllib.request.Request(raw_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return FetchedContent(
                fetch_status=getattr(resp, "status", None),
                final_url=resp.geturl(),
                content_type=resp.headers.get("Content-Type"),
                body=body,
            )
    except urllib.error.HTTPError as exc:
        body = exc.read()
        return FetchedContent(
            fetch_status=exc.code,
            final_url=exc.geturl(),
            content_type=exc.headers.get("Content-Type") if exc.headers else None,
            body=body,
            error=str(exc),
        )


def summarize_fetched_snapshot(record: CdxRecord, fetched: FetchedContent) -> dict[str, Any]:
    """Fetched replay bytes -> provenance, byte hash, normalized text hash, and counts."""
    text = extract_text_content(fetched.body, fetched.content_type)
    lines = text.splitlines() if text else []
    return {
        **snapshot_provenance(record),
        "fetch_status": fetched.fetch_status,
        "fetch_ok": fetched.fetch_status is not None and 200 <= fetched.fetch_status < 400,
        "fetch_error": fetched.error,
        "final_url": fetched.final_url,
        "content_type": fetched.content_type,
        "byte_count": len(fetched.body),
        "content_sha256": sha256_hex(fetched.body),
        "text_char_count": len(text),
        "text_line_count": len(lines),
        "text_sha256": sha256_hex(text),
        "_text": text,
    }


def build_text_diff(
    from_text: str,
    to_text: str,
    from_label: str,
    to_label: str,
    context_lines: int = DEFAULT_DIFF_CONTEXT_LINES,
    max_diff_lines: int = DEFAULT_MAX_DIFF_LINES,
) -> dict[str, Any]:
    """Create a bounded unified diff plus line-count summary, without interpreting changes."""
    from_lines = from_text.splitlines()
    to_lines = to_text.splitlines()
    matcher = difflib.SequenceMatcher(a=from_lines, b=to_lines, autojunk=False)
    added = removed = common = 0
    for tag, from_start, from_end, to_start, to_end in matcher.get_opcodes():
        if tag == "equal":
            common += from_end - from_start
        elif tag == "delete":
            removed += from_end - from_start
        elif tag == "insert":
            added += to_end - to_start
        elif tag == "replace":
            removed += from_end - from_start
            added += to_end - to_start

    diff_lines = list(
        difflib.unified_diff(
            from_lines,
            to_lines,
            fromfile=from_label,
            tofile=to_label,
            lineterm="",
            n=context_lines,
        )
    )
    truncated = len(diff_lines) > max_diff_lines
    if truncated:
        diff_lines = diff_lines[:max_diff_lines]

    return {
        "format": "unified_diff",
        "context_lines": context_lines,
        "max_diff_lines": max_diff_lines,
        "truncated": truncated,
        "line_counts": {
            "from": len(from_lines),
            "to": len(to_lines),
            "common": common,
            "added": added,
            "removed": removed,
        },
        "lines": diff_lines,
    }


def lookup(url: str) -> dict[str, Any]:
    """Full pipeline: CDX GET for one URL -> the shared envelope + the tenure payload beside it."""
    now_dt = _utc_now()
    records = parse_records(fetch_cdx(url))
    count = len(records)

    if count == 0:
        confidence = "insufficient"  # never archived
    elif count == 1:
        confidence = "provisional"  # a lone capture — uncorroborated
    else:
        confidence = "measured"  # >=2 distinct-content captures — the ledger's "real captures" bar

    first_seen = last_seen = None
    first_snapshot_url = last_snapshot_url = None
    tenure_days = None
    if records:
        first_seen = _ts_to_iso(records[0].raw_timestamp)
        last_seen = _ts_to_iso(records[-1].raw_timestamp)
        first_snapshot_url = _replay_url(records[0].raw_timestamp, records[0].original_url)
        last_snapshot_url = _replay_url(records[-1].raw_timestamp, records[-1].original_url)
        tenure_days = (now_dt - _ts_to_dt(records[0].raw_timestamp)).days  # lower bound: first_seen is itself one

    snapshots = [
        {
            "timestamp": _ts_to_iso(record.raw_timestamp),
            "url": record.original_url,
            "status": record.status,
            "digest": record.digest,
        }
        for record in records[:SNAPSHOTS_CAP]
    ]

    return {
        # --- the reserved envelope spine (tools/README.md), identical across the library ---
        "tool": "wayback",
        "source": SOURCE,  # the external system hit (the Wayback CDX Server)
        "captured_at": now_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),  # THIS lookup's wall-clock — NOT an archive date
        "ok": True,  # transport failures exit 2 before here; a never-archived URL is still a clean capture
        "input": {"url": url},
        "schema_drift": [],  # always [] — frozen feed, no version-pinned parser (kept for uniformity)
        # (no parser_version: CDX is frozen. no cost: it's free. no _env key: it's unauthenticated.)
        # --- payload, beside the spine (the archive dates the envelope must NOT carry) ---
        "first_seen": first_seen,  # ISO datetime of the earliest archived capture, or null if never archived
        "last_seen": last_seen,  # ISO datetime of the most recent capture (a still-alive proxy)
        "first_seen_confidence": confidence,  # insufficient | provisional | measured
        "tenure_days": tenure_days,  # captured_at - first_seen, in days; a LOWER BOUND (first_seen is one)
        "snapshot_count": count,  # distinct-content captures (post collapse=digest) — full count, not capped
        "snapshots_truncated": count > SNAPSHOTS_CAP,  # the `snapshots` list below is capped; summary fields aren't
        "status_trail": build_status_trail(records),  # full lifecycle runs (launched/moved/died) — top-level, never capped
        "first_snapshot_url": first_snapshot_url,  # replay link to the earliest capture (eyeball / diff seed)
        "last_snapshot_url": last_snapshot_url,
        "snapshots": snapshots,  # oldest-first; capped at SNAPSHOTS_CAP rows (see snapshots_truncated)
    }


def diff_lookup(
    url: str,
    from_timestamp: str | None = None,
    to_timestamp: str | None = None,
    timeout: int = 60,
    context_lines: int = DEFAULT_DIFF_CONTEXT_LINES,
    max_diff_lines: int = DEFAULT_MAX_DIFF_LINES,
) -> dict[str, Any]:
    """Fetch two archived snapshots for one URL and emit mechanical content hashes + diff."""
    now_dt = _utc_now()
    records = parse_records(fetch_cdx(url, timeout=timeout))
    selected, selection_state, selection_note = select_diff_records(records, from_timestamp, to_timestamp)

    base: dict[str, Any] = {
        "tool": "wayback",
        "source": SOURCE,
        "captured_at": now_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ok": True,
        "input": {
            "mode": "diff",
            "url": url,
            "from": from_timestamp,
            "to": to_timestamp,
            "context_lines": context_lines,
            "max_diff_lines": max_diff_lines,
        },
        "schema_drift": [],
        "selection": {
            "strategy": "nearest_targets" if from_timestamp or to_timestamp else "first_last",
            "state": selection_state,
            "note": selection_note,
            "snapshot_count": len(records),
        },
        "selected_snapshots": [snapshot_provenance(record) for record in selected],
        "contents": [],
        "text_changed": None,
        "diff": None,
    }

    if selection_state != "selected":
        return base

    contents = [summarize_fetched_snapshot(record, fetch_replay_content(record, timeout=timeout)) for record in selected]
    public_contents = [{key: value for key, value in content.items() if key != "_text"} for content in contents]
    base["contents"] = public_contents

    failed = [content for content in contents if not content["fetch_ok"]]
    if failed:
        base["ok"] = False
        base["selection"]["state"] = "fetch_failed"
        base["selection"]["note"] = "At least one selected snapshot could not be fetched cleanly."
        return base

    from_content, to_content = contents
    base["text_changed"] = from_content["text_sha256"] != to_content["text_sha256"]
    base["diff"] = build_text_diff(
        from_content["_text"],
        to_content["_text"],
        from_label=f"{from_content['timestamp']} {from_content['original_url']}",
        to_label=f"{to_content['timestamp']} {to_content['original_url']}",
        context_lines=context_lines,
        max_diff_lines=max_diff_lines,
    )
    return base


def _parse_tenure(argv: list[str]) -> argparse.Namespace:
    """Parse legacy tenure args; `wayback.py <url>` stays valid."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="The page to look up (full URL, or a bare domain; CDX canonicalizes)")
    return parser.parse_args(argv)


def _parse_diff(argv: list[str]) -> argparse.Namespace:
    """Parse the scoped content-diff mode args."""
    parser = argparse.ArgumentParser(
        prog="wayback.py diff",
        description="Fetch two raw Wayback snapshots for one exact URL and emit text hashes + unified diff.",
    )
    parser.add_argument("url", help="The page to diff (full URL, or a bare domain; CDX canonicalizes)")
    parser.add_argument("--from", dest="from_timestamp", help="Target Wayback timestamp/date for the older side (YYYY[MM[DD[hhmmss]]])")
    parser.add_argument("--to", dest="to_timestamp", help="Target Wayback timestamp/date for the newer side (YYYY[MM[DD[hhmmss]]])")
    parser.add_argument("--timeout", type=int, default=60, help="Per-request timeout in seconds (default: 60)")
    parser.add_argument("--context-lines", type=int, default=DEFAULT_DIFF_CONTEXT_LINES, help="Unified diff context lines (default: 3)")
    parser.add_argument("--max-diff-lines", type=int, default=DEFAULT_MAX_DIFF_LINES, help="Cap emitted unified diff lines (default: 400)")
    return parser.parse_args(argv)


def main() -> None:
    argv = sys.argv[1:]
    mode = "tenure"
    if argv and argv[0] in {"diff", "tenure"}:
        mode = argv.pop(0)
    args = _parse_diff(argv) if mode == "diff" else _parse_tenure(argv)

    try:
        if mode == "diff":
            result = diff_lookup(
                args.url.strip(),
                from_timestamp=args.from_timestamp,
                to_timestamp=args.to_timestamp,
                timeout=args.timeout,
                context_lines=args.context_lines,
                max_diff_lines=args.max_diff_lines,
            )
        else:
            result = lookup(args.url.strip())
    except Exception as exc:
        sys.stderr.write(f"Error looking up {args.url!r}: {exc}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))
    if result.get("schema_drift"):  # never fires today; kept uniform with the drift-prone tools
        sys.exit(3)


if __name__ == "__main__":
    main()
