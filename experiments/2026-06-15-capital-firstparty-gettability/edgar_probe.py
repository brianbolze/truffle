#!/usr/bin/env python3
"""Probe #2 (Half B) — is first-party funding gettable from FREE EDGAR, and where's the name-match seam?

Throwaway. Gates tools/sec_edgar.py. Keyless GETs (SEC requires only a descriptive User-Agent), ~$0:
  1. company_tickers.json   ticker -> CIK         (the public-company State prior)
  2. data.sec.gov/submissions/CIK##########.json  filing stream (dated 8-K/10-K -> Signal)
  3. efts.sec.gov full-text search, forms=D        Form-D existence by issuer name (the seam)

Tests the funding boundary from the approach:
  - TSLA control -> ticker/exchange State + a dated filing Signal.
  - 7 private startups -> Form-D existence+date only; a common name (Blue Energy, Electra) yields many
    filers => name_match_unconfirmed, never a forced assert.
  - 2 VC nulls -> their own Form-Ds are FUND filings, not a company raise => the noise the seam must contain.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

UA = "web-research-probe brian@example.com"  # SEC fair-access: a descriptive UA is mandatory (403 without)

STARTUPS = ["Sora Fuel", "Blue Energy", "Electra", "Euclid Power",
            "Commonwealth Fusion Systems", "EVOLOH", "VerdeGo Aero"]
VC_NULLS = ["First Round Capital", "Sequoia Capital"]


def _get(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                import gzip
                body = gzip.decompress(body)
            return r.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def ticker_to_cik(ticker: str) -> str | None:
    status, body = _get("https://www.sec.gov/files/company_tickers.json")
    if status != 200:
        return None
    for row in json.loads(body).values():
        if row["ticker"].upper() == ticker.upper():
            return f"{row['cik_str']:010d}"
    return None


def latest_filings(cik: str, forms: tuple[str, ...] = ("8-K", "10-K", "10-Q")) -> list[dict]:
    status, body = _get(f"https://data.sec.gov/submissions/CIK{cik}.json")
    if status != 200:
        return []
    data = json.loads(body)
    recent = data.get("filings", {}).get("recent", {})
    out = []
    for form, date, doc in zip(recent.get("form", []), recent.get("filingDate", []), recent.get("primaryDocument", [])):
        if form in forms:
            out.append({"form": form, "date": date, "doc": doc})
        if len(out) >= 5:
            break
    return {"name": data.get("name"), "exchanges": data.get("exchanges"), "sic": data.get("sicDescription"), "filings": out}


def formd_search(name: str) -> dict:
    """EDGAR full-text search for Form D by issuer name. Returns hit count + distinct filer names + date span."""
    q = urllib.parse.quote(f'"{name}"')
    status, body = _get(f"https://efts.sec.gov/LATEST/search-index?q={q}&forms=D")
    if status != 200:
        return {"status": status, "error": body[:200].decode("utf-8", "replace")}
    data = json.loads(body)
    hits = data.get("hits", {})
    total = hits.get("total", {}).get("value", 0)
    filers: dict[str, list[str]] = {}
    for h in hits.get("hits", []):
        src = h.get("_source", {})
        for disp in src.get("display_names", []):
            filers.setdefault(disp, []).append(src.get("file_date", "?"))
    return {"status": 200, "total_hits": total, "distinct_filers": len(filers),
            "filers": {k: (min(v), max(v)) for k, v in list(filers.items())[:6]}}


def main() -> None:
    print("=" * 78, "\n1. CONTROL — TSLA: ticker -> CIK (State) + dated filings (Signal)\n", "=" * 78)
    cik = ticker_to_cik("TSLA")
    print(f"  ticker TSLA -> CIK {cik}")
    if cik:
        sub = latest_filings(cik)
        print(f"  name={sub['name']}  exchanges={sub['exchanges']}  sic={sub['sic']}")
        for f in sub["filings"]:
            print(f"    {f['form']:6s} {f['date']}  {f['doc']}")
    time.sleep(0.3)

    print("\n", "=" * 78, "\n2. STARTUPS — Form-D existence by name (the seam: common names => name_match_unconfirmed)\n", "=" * 78)
    for name in STARTUPS:
        r = formd_search(name)
        if r.get("status") != 200:
            print(f"  {name:30s} -> ERROR {r.get('status')}: {r.get('error')}")
        else:
            verdict = "clean-ish" if r["distinct_filers"] <= 2 else "AMBIGUOUS (name_match_unconfirmed)"
            print(f"  {name:30s} hits={r['total_hits']:<4} distinct_filers={r['distinct_filers']:<3} {verdict}")
            for fn, span in r["filers"].items():
                print(f"        - {fn}  [{span[0]}..{span[1]}]")
        time.sleep(0.3)

    print("\n", "=" * 78, "\n3. VC NULLS — own Form-Ds are FUND filings, not a company raise (must not assert a 'round')\n", "=" * 78)
    for name in VC_NULLS:
        r = formd_search(name)
        if r.get("status") != 200:
            print(f"  {name:30s} -> ERROR {r.get('status')}: {r.get('error')}")
        else:
            print(f"  {name:30s} hits={r['total_hits']:<4} distinct_filers={r['distinct_filers']}")
            for fn, span in r["filers"].items():
                print(f"        - {fn}  [{span[0]}..{span[1]}]")
        time.sleep(0.3)


if __name__ == "__main__":
    main()
