#!/usr/bin/env python3
"""Internet Archive CDX first-seen / tenure lookup — how long a page has *demonstrably* existed.

Give it ONE URL; it asks the Wayback Machine's CDX Server "show me every archived capture of this
page" and emits the tenure signal: when it was first seen, when last seen, how many distinct content
snapshots exist, and the status lifecycle (200 -> 301 -> 404 = launched, moved, died). That's the
whole job. One free GET, no key. The caller loops over a roster; this tool does one page.

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
  python3 tools/wayback.py example.com                       # bare domain -> the homepage (exact match)
  python3 tools/wayback.py https://brand.com/products/sermorelin

Exit codes:
  0  clean capture (INCLUDING a never-archived URL -> first_seen:null, confidence:"insufficient" — data, not failure)
  2  fetch error (network, IA HTTP error, or an unexpected/garbled CDX body)
  (no exit 3: CDX is a stable, frozen feed — no version-pinned parser, so no schema-drift path.
   `schema_drift` is still emitted as `[]` for envelope uniformity across the library.)

No key (CDX is free + unauthenticated — no `_env` call). No `parser_version` (frozen feed). No `cost`
(free). The lookup is exact-URL only; whole-section history (matchType=prefix/domain) and historical
*content* fetch + diff are latent growth paths, not v1 — see wayback.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

SOURCE = "web.archive.org/cdx"
CDX_BASE = "https://web.archive.org/cdx/search/cdx"
USER_AGENT = "web-research-tools/wayback"
# The CDX columns we request (and the order). `collapse=digest` folds *adjacent* identical-content
# captures, so a row means "content that differs from the row before it" and snapshot_count is a
# distinct-content count, not a raw crawl count.
CDX_FIELDS = "timestamp,original,statuscode,digest"
REQUIRED_COLUMNS = ("timestamp", "original", "statuscode", "digest")
# Bulk safety bound on the *emitted* snapshots list (oldest first — this tool's first-seen focus).
# Summary fields (first_seen / last_seen / snapshot_count / status_trail) are ALWAYS computed over
# the full set, so a cap here never hides the headline or the lifecycle — only trims the audit tail.
SNAPSHOTS_CAP = 500


def _utc_now() -> datetime:
    """This invocation's wall-clock (UTC) — the envelope's `captured_at` AND the clock `tenure_days`
    counts back from. Never an archive timestamp: those ARE the signal and live in the payload
    (`first_seen` / `last_seen` / `snapshots[].timestamp`) under their own names. The whole point of
    this tool's design is keeping the two apart."""
    return datetime.now(timezone.utc)


def _ts_to_iso(raw: str) -> str:
    """CDX `YYYYMMDDhhmmss` (UTC) -> ISO 8601 `2019-03-04T12:30:45Z`. Pads a short/garbled stamp
    defensively rather than crashing the row."""
    digits = re.sub(r"\D", "", raw)[:14].ljust(14, "0")
    return f"{digits[0:4]}-{digits[4:6]}-{digits[6:8]}T{digits[8:10]}:{digits[10:12]}:{digits[12:14]}Z"


def _ts_to_dt(raw: str) -> datetime:
    """CDX `YYYYMMDDhhmmss` (UTC) -> aware datetime, for the tenure arithmetic."""
    digits = re.sub(r"\D", "", raw)[:14].ljust(14, "0")
    return datetime.strptime(digits, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)


def _replay_url(raw_ts: str, original: str) -> str:
    """The human-viewable Wayback replay URL for a capture. (The latent content-diff path wants the
    `/web/<ts>id_/<url>` raw-content variant instead — see wayback.md; this is the eyeball link.)"""
    return f"https://web.archive.org/web/{re.sub(r'[^0-9]', '', raw_ts)[:14]}/{original}"


def fetch_cdx(url: str, timeout: int = 60) -> list[list[str]]:
    """GET the CDX feed for `url` -> rows (a header row then data rows), or [] when never archived.

    Stdlib urllib, no `requests` dep — the HTTP layer the tools/ library copies. A never-archived URL
    returns HTTP 200 with an EMPTY body (not `[]`), so empty-body is normalized to [] here, NOT
    treated as an error. Network / HTTP errors (urlopen raises HTTPError on 4xx/5xx) bubble to
    main()'s exit-2 handler.
    """
    params = {"url": url, "output": "json", "fl": CDX_FIELDS, "collapse": "digest"}
    full_url = f"{CDX_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(full_url, headers={"User-Agent": USER_AGENT})
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


def parse_records(rows: list[list[str]]) -> list[tuple[str, str, str, str]]:
    """CDX rows -> [(raw_ts, original, statuscode, digest)], sorted oldest-first.

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
    ti, oi, si, di = idx["timestamp"], idx["original"], idx["statuscode"], idx["digest"]
    records = [(row[ti], row[oi], row[si], row[di]) for row in rows[1:]]
    records.sort(key=lambda r: r[0])
    return records


def build_status_trail(records: list[tuple[str, str, str, str]]) -> list[dict[str, str]]:
    """Collapse consecutive captures with the same HTTP status into runs -> the lifecycle signal.

    `[{status:"200", from:.., to:..}, {status:"301", ..}, {status:"404", ..}]` reads as launched,
    moved, died. Computed over the FULL record set (never the capped snapshots list) and surfaced
    top-level, so the cap on `snapshots` can't hide a page's death. `status` is kept verbatim — CDX
    uses `-` for revisit / unknown-status records; we report it, we don't normalize it.
    """
    trail: list[dict[str, str]] = []
    for raw_ts, _original, status, _digest in records:
        iso = _ts_to_iso(raw_ts)
        if trail and trail[-1]["status"] == status:
            trail[-1]["to"] = iso
        else:
            trail.append({"status": status, "from": iso, "to": iso})
    return trail


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
        first_seen = _ts_to_iso(records[0][0])
        last_seen = _ts_to_iso(records[-1][0])
        first_snapshot_url = _replay_url(records[0][0], records[0][1])
        last_snapshot_url = _replay_url(records[-1][0], records[-1][1])
        tenure_days = (now_dt - _ts_to_dt(records[0][0])).days  # lower bound: first_seen is itself one

    snapshots = [
        {"timestamp": _ts_to_iso(raw_ts), "url": original, "status": status, "digest": digest}
        for raw_ts, original, status, digest in records[:SNAPSHOTS_CAP]
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
        "first_snapshot_url": first_snapshot_url,  # replay link to the earliest capture (eyeball / latent diff seed)
        "last_snapshot_url": last_snapshot_url,
        "snapshots": snapshots,  # oldest-first; capped at SNAPSHOTS_CAP rows (see snapshots_truncated)
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="The page to look up (full URL, or a bare domain for the homepage)")
    args = parser.parse_args()

    try:
        result = lookup(args.url.strip())
    except Exception as exc:
        sys.stderr.write(f"Error looking up {args.url!r}: {exc}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))
    if result.get("schema_drift"):  # never fires today; kept uniform with the drift-prone tools
        sys.exit(3)


if __name__ == "__main__":
    main()
