#!/usr/bin/env python3
"""SEC EDGAR — first-party funding signals, captured not judged, strictly inside the funding boundary.

The traction approach's #4 build: the *easy, first-party* slice of capital signal, and nothing past it.
EDGAR is free, keyless, and authoritative — so it's the one funding source that fits the engine's
anti-paid-data-swamp line. Three keyless GETs:
  1. company_tickers.json   ticker -> CIK            -> a State prior (ticker/exchange) for profile.md
  2. data.sec.gov/submissions/CIK….json             -> the dated filing stream (8-K/10-K/10-Q/D) -> Signals
  3. efts.sec.gov full-text search, forms=D          -> Form-D existence by issuer name (private rounds)

What it emits (both, per the build call): the **raw EDGAR signals** beside the shared spine, AND a
**`funding_signals[]`** list of FACTUAL cards (event + date + identity-match state). What it deliberately
does NOT do — the boundary that keeps this honest and out of the swamp:
  - **No amount from EDGAR.** A Form D's existence + date is the signal; `amount` stays `null` (the dollar
    figure lives on the company's own newsroom card, captured separately and never reconciled here).
  - **No valuation, post-money, cap table, related-person, or investor-graph resolution.** Co-investors,
    if ever recorded, stay verbatim strings on a newsroom card — not here.
  - **No verdict.** No `evidence_label` / `signal_polarity` / "strong traction" — those are consumer-side.
  - **Identity match is contained.** Asserting a Form D belongs to *this* private startup is best-effort
    name-matching — the thin end of entity-resolution. So: collapse filers by CIK, and a name that resolves
    to >1 distinct CIK (or only an investor SPV/fund wrapper) is `name_match_unconfirmed` — existence-only,
    never a forced assert. A single distinctive-name CIK is `confirmed`.

Generic on purpose: emits JSON to stdout; promoting the State prior to `profile.md` or merging these
Signals with a newsroom card is the caller's job (capture, not judgment; propose, don't write).

CLI:
  python3 tools/sec_edgar.py "Commonwealth Fusion Systems"              # private: Form-D existence by name
  python3 tools/sec_edgar.py "Tesla" --ticker TSLA                     # public: ticker State + filing stream
  python3 tools/sec_edgar.py "Sora Fuel" --domain sorafuel.com         # stamp the card subject as the domain

Exit codes:
  0  clean capture (INCLUDING a factual no-match / not-public — that's data, not failure)
  2  transport error (network/HTTP after one retry; SEC 403 if the User-Agent is missing)
  (no exit 3: EDGAR is a stable government JSON contract — no version-pinned parser to drift, like Wayback CDX.)

Auth: none. SEC fair-access requires only a descriptive User-Agent header (they 403 without one).
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

# SEC fair-access: a descriptive UA is mandatory (403 without). Identifies this tool + a contact.
USER_AGENT = "web-research-tools/sec_edgar (contact: brianbolze@gmail.com)"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
FTS_URL = "https://efts.sec.gov/LATEST/search-index"
SIGNAL_FORMS = ("8-K", "10-K", "10-Q", "D", "D/A")  # the dated filings worth a Signal card
FILINGS_CAP = 10  # most-recent N per capture — a stream pointer, not an archive
# Filer-name tokens that mark an investor vehicle wrapping the subject ("VXI Evoloh SPV LP"), not the issuer.
_VEHICLE_RE = re.compile(r"\b(SPV|Fund|Partners|Feeder|Holdings|L\.?P\.?|LLC Series)\b", re.IGNORECASE)


def _now_utc() -> str:
    """This invocation's capture wall-clock (UTC ISO) — the envelope's `captured_at`, not a filing date.
    Filing dates are the signal; they live inside payload items under their own names (the library rule)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _get_json(url: str, retries: int = 1) -> Any:
    """Keyless GET -> parsed JSON, with one back-off retry (EFTS returns transient 500s — observed in the
    gettability probe). Decompresses gzip. Raises on a non-200 after the retry (main() maps to exit 2)."""
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    body = gzip.decompress(body)
                return json.loads(body)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            last_err = e
            if attempt < retries:
                time.sleep(2.0)  # transient (500/timeout/rate) — one back-off, then give up
    raise RuntimeError(f"EDGAR GET failed after {retries + 1} tries: {url} -> {last_err}")


# --------------------------------------------------------------------------- identity (State prior)
def resolve_ticker(ticker: str) -> dict[str, Any] | None:
    """ticker -> {cik, registered_name}. The public-company identity prior; None if the ticker is unknown."""
    data = _get_json(TICKERS_URL)
    for row in data.values():
        if row["ticker"].upper() == ticker.upper():
            return {"cik": f"{row['cik_str']:010d}", "registered_name": row["title"]}
    return None


def fetch_submissions(cik: str) -> dict[str, Any]:
    """The issuer's filing history + identity (exchanges, name, SIC). cik is the 10-digit zero-padded form."""
    return _get_json(SUBMISSIONS_URL.format(cik=cik))


def extract_filings(submissions: dict[str, Any], forms: tuple[str, ...] = SIGNAL_FORMS) -> list[dict[str, Any]]:
    """The most-recent dated filings of the given forms, each with a resolvable archive URL. Newest first."""
    recent = submissions.get("filings", {}).get("recent", {})
    cik_int = str(int(submissions.get("cik", "0")))
    out: list[dict[str, Any]] = []
    for form, date, doc, acc in zip(recent.get("form", []), recent.get("filingDate", []),
                                    recent.get("primaryDocument", []), recent.get("accessionNumber", [])):
        if form not in forms:
            continue
        acc_nodash = acc.replace("-", "")
        out.append({
            "form": form, "date": date,
            "url": f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/{doc}" if doc else None,
        })
        if len(out) >= FILINGS_CAP:
            break
    return out


# --------------------------------------------------------------------------- Form-D existence (the seam)
def search_form_d(name: str) -> dict[str, Any]:
    """Full-text search for Form D by issuer name -> candidates grouped by CIK, with a match verdict.

    The seam: a name that resolves to >1 distinct CIK (Electra -> 64) or only an investor vehicle
    (VXI Evoloh SPV LP) is `name_match_unconfirmed` — existence-only, never a forced assert. One
    distinctive CIK (Sora Fuel, VerdeGo Aero) is `confirmed`. Collapsing case variants by CIK first is
    load-bearing: 'Sora Fuel Corp' / 'SORA FUEL Corp' are one filer, not two.
    """
    q = urllib.parse.urlencode({"q": f'"{name}"', "forms": "D"})
    data = _get_json(f"{FTS_URL}?{q}")
    hits = data.get("hits", {})
    total = hits.get("total", {}).get("value", 0)

    by_cik: dict[str, dict[str, Any]] = {}
    for h in hits.get("hits", []):
        src = h.get("_source", {})
        cik = (src.get("ciks") or [None])[0]
        date = src.get("file_date")
        names = src.get("display_names", [])
        if not cik:
            continue
        entry = by_cik.setdefault(cik, {"cik": f"{int(cik):010d}", "filer_names": set(), "dates": set()})
        entry["filer_names"].update(names)
        if date:
            entry["dates"].add(date)

    candidates = []
    for entry in by_cik.values():
        filer = sorted(entry["filer_names"])[0] if entry["filer_names"] else None
        candidates.append({
            "cik": entry["cik"],
            "filer": filer,
            "dates": sorted(entry["dates"]),
            "is_vehicle": bool(filer and _VEHICLE_RE.search(filer) and not _name_root_matches(name, filer)),
        })
    candidates.sort(key=lambda c: c["dates"][-1] if c["dates"] else "", reverse=True)

    real = [c for c in candidates if not c["is_vehicle"]]
    if not candidates:
        match = "no_match"
    elif len(real) == 1:
        match = "confirmed"
    elif not real:  # only investor vehicles matched the name
        match = "name_match_unconfirmed"
    else:
        match = "name_match_unconfirmed"  # >1 distinct issuer CIK — can't isolate the subject
    return {"query_name": name, "total_hits": total, "distinct_ciks": len(candidates),
            "match": match, "candidates": candidates}


def _name_root_matches(query: str, filer: str) -> bool:
    """Does the filer start with the query's distinctive root? ('Sora Fuel' vs 'Sora Fuel Corp' -> yes;
    'Evoloh' vs 'VXI Evoloh SPV LP' -> no). Keeps a real issuer suffix ('Corp', 'Inc') from reading as a vehicle."""
    root = query.strip().lower()
    return filer.strip().lower().startswith(root)


# --------------------------------------------------------------------------- card shaping (factual, EDGAR-only)
def _card(subject: str, event_type: str, date: str | None, **extra: Any) -> dict[str, Any]:
    """One FACTUAL SEC funding-signal card. `amount` is always null here — EDGAR gives existence + date, never
    the dollar figure (the seam); the amount rides a newsroom card, merged by a caller, never reconciled here.
    No evidence_label / signal_polarity: a verdict is consumer-side."""
    return {"subject": subject, "source_type": "sec", "event_type": event_type, "date": date,
            "amount": None, "observation": "factual", **extra}


def build_funding_signals(subject: str, state: dict[str, Any], filings: list[dict[str, Any]],
                          form_d: dict[str, Any]) -> list[dict[str, Any]]:
    """Shape the raw EDGAR signals into factual cards (the 'both' — beside the raw payload). One card per
    dated Form-D (carrying its match state) and per dated filing; never an amount, never a verdict."""
    cards: list[dict[str, Any]] = []
    # Form-D cards only when the issuer is attributable: a confirmed match, or a single candidate
    # (probable-but-unproven -> not_promoted). A multi-CIK name swamp (Electra: 64 CIKs) yields NO attributed
    # cards — manufacturing events we can't pin to the subject is exactly what the seam forbids; the raw
    # `form_d` block still lists the candidates for a caller to inspect.
    if form_d["match"] == "confirmed" or len(form_d["candidates"]) == 1:
        for cand in form_d["candidates"]:
            flags = ["existence_only"]
            if form_d["match"] != "confirmed":
                flags.append("not_promoted")
            if cand["is_vehicle"]:
                flags.append("related_vehicle")
            for date in cand["dates"]:
                cards.append(_card(subject, "form_d", date, cik=cand["cik"], filer=cand["filer"],
                                   match=form_d["match"], flags=flags, citation="efts.sec.gov forms=D"))
    for f in filings:
        if f["form"] in ("D", "D/A"):
            continue  # Form-D already carried above via the FTS match (existence + match state)
        cards.append(_card(subject, "filing", f["date"], form=f["form"], cik=state.get("cik"),
                           match="confirmed", flags=["material_filing"], citation=f["url"]))
    cards.sort(key=lambda c: c["date"] or "", reverse=True)
    return cards


def capture(name: str, ticker: str | None = None, domain: str | None = None) -> dict[str, Any]:
    """Full pipeline: identity (ticker State if public) + filing stream + Form-D existence -> envelope.

    subject keys the cards: the domain when given (so they slot under store/<domain>/signals/), else the name.
    """
    subject = domain or name
    state: dict[str, Any] = {"is_public": False, "ticker": ticker, "cik": None, "exchange": None, "registered_name": None}
    filings: list[dict[str, Any]] = []

    resolved_cik: str | None = None
    if ticker:
        ident = resolve_ticker(ticker)
        if ident:
            resolved_cik = ident["cik"]
            state.update(is_public=True, cik=resolved_cik, registered_name=ident["registered_name"])

    form_d = search_form_d(name)
    # If not public but the Form-D match is a single confirmed issuer, adopt its CIK for the filing stream.
    if not resolved_cik and form_d["match"] == "confirmed":
        resolved_cik = next((c["cik"] for c in form_d["candidates"] if not c["is_vehicle"]), None)

    if resolved_cik:
        subs = fetch_submissions(resolved_cik)
        exchanges = subs.get("exchanges") or []
        state.update(cik=resolved_cik, registered_name=state["registered_name"] or subs.get("name"),
                     exchange=exchanges[0] if exchanges else None, sic=subs.get("sicDescription"))
        if state["is_public"] is False and exchanges:
            state["is_public"] = True
        filings = extract_filings(subs)
        # Identity is now resolved (ticker, or a single confirmed match) — so scope the Form-D name-search
        # to that CIK. Otherwise a public name like "Tesla" reports the 13-CIK name swamp as funding
        # ambiguity, when the ticker already pinned the issuer; the filing stream carries its real signal.
        scoped = [c for c in form_d["candidates"] if c["cik"] == resolved_cik]
        form_d = {**form_d, "candidates": scoped, "distinct_ciks": len(scoped),
                  "match": "confirmed" if scoped else "no_issuer_form_d", "scoped_to_cik": resolved_cik}

    funding_signals = build_funding_signals(subject, state, filings, form_d)
    return {
        # --- shared envelope spine (tools/README.md), identical across the library ---
        "tool": "sec_edgar",
        "source": "efts.sec.gov + data.sec.gov",  # the SEC systems hit (keyless)
        "captured_at": _now_utc(),  # this invocation's wall-clock — filing dates live in the payload
        "ok": True,
        "input": {"name": name, "ticker": ticker, "domain": domain},
        "schema_drift": [],  # EDGAR is a stable government JSON contract — no version-pinned parser (no exit 3)
        # --- raw EDGAR signals (the capture) ---
        "subject": subject,
        "state": state,  # the State prior (ticker/exchange) for profile.md — a caller promotes it; the tool won't
        "filings": filings,  # dated filing-stream Signals (newest first)
        "form_d": form_d,  # Form-D existence by name + the identity-match verdict (the seam)
        # --- factual cards (the 'both' — shaped beside the raw, amounts/verdicts deliberately excluded) ---
        "funding_signals": funding_signals,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("name", help="Company/issuer name for the Form-D full-text search (the subject)")
    p.add_argument("--ticker", help="Stock ticker, if public — resolves ticker/exchange State + the filing stream")
    p.add_argument("--domain", help="Stamp the card subject as this domain (so cards slot under store/<domain>/signals/)")
    args = p.parse_args()

    try:
        result = capture(args.name, ticker=args.ticker, domain=args.domain)
    except Exception as e:
        sys.stderr.write(f"Error capturing SEC footprint for {args.name!r}: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
