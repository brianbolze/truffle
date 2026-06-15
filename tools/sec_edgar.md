# sec_edgar.py — first-party funding signals from SEC EDGAR

The easy, first-party slice of capital signal — and nothing past it. Free, keyless, authoritative; the one
funding source that fits the engine's anti-paid-data-swamp line. Emits **both** the raw EDGAR signals and a
list of **factual** funding cards (the build call). De-risked by the [gettability probe](../experiments/2026-06-15-capital-firstparty-gettability/FINDINGS.md).

```
python3 tools/sec_edgar.py "Commonwealth Fusion Systems"          # private: Form-D existence by name
python3 tools/sec_edgar.py "Tesla" --ticker TSLA --domain tesla.com   # public: ticker State + filing stream
python3 tools/sec_edgar.py "Sora Fuel" --domain sorafuel.com      # stamp card subject = the domain
```

## Output shape (trimmed)

```jsonc
{
  "tool": "sec_edgar", "source": "efts.sec.gov + data.sec.gov", "captured_at": "…Z",
  "ok": true, "input": { "name": "Sora Fuel", "ticker": null, "domain": "sorafuel.com" }, "schema_drift": [],
  "subject": "sorafuel.com",
  "state": { "is_public": false, "ticker": null, "cik": "0002014480", "exchange": null,
             "registered_name": "Sora Fuel Corp" },          // the State prior for profile.md (a caller promotes it)
  "filings": [ { "form": "D", "date": "2026-03-31", "url": "https://www.sec.gov/Archives/…" } ],
  "form_d": { "query_name": "Sora Fuel", "total_hits": 2, "distinct_ciks": 1, "match": "confirmed",
              "candidates": [ { "cik": "0002014480", "filer": "Sora Fuel Corp",
                                "dates": ["2024-03-08","2026-03-31"], "is_vehicle": false } ] },
  "funding_signals": [                                          // FACTUAL cards (amount always null — the seam)
    { "subject": "sorafuel.com", "source_type": "sec", "event_type": "form_d", "date": "2026-03-31",
      "amount": null, "observation": "factual", "cik": "0002014480", "match": "confirmed",
      "flags": ["existence_only"], "citation": "efts.sec.gov forms=D" }
  ]
}
```

## What it emits

| Block | Kind | Goes to |
|---|---|---|
| `state` (ticker/exchange/CIK/name) | **State** prior (rarely changes) | `profile.md` — a caller promotes it; the tool never writes |
| `filings[]` (dated 8-K/10-K/10-Q/D) | **Signal** | a Signal card per dated filing |
| `form_d` (existence by name + match verdict) | raw discovery / the identity seam | inspected by a caller |
| `funding_signals[]` (factual cards) | **Signal** | merged with a newsroom card by a caller (never here) |

## The identity-match seam (the de-risked core)

Asserting a Form-D belongs to *this* private startup is best-effort name-matching — the thin end of
entity-resolution. So it's contained: filers collapse by CIK, then a verdict.

| `match` | When | Cards emitted |
|---|---|---|
| `confirmed` | one distinctive-name CIK (Sora, VerdeGo, CFS); or the ticker-resolved CIK | one per dated Form-D |
| `name_match_unconfirmed` | a single probable-but-unproven candidate, or only an investor vehicle (`VXI Evoloh SPV LP`) | one, flagged `not_promoted` (+ `related_vehicle`) |
| `name_match_unconfirmed` (swamp) | >1 distinct issuer CIK (Electra → 64) | **none** — can't attribute; raw `form_d.candidates` still listed |
| `no_match` / `no_issuer_form_d` | zero hits; or a public CIK with no Form-Ds | none |

## Gotchas / boundary (the value)

- **No amount, ever.** EDGAR gives existence + date; `amount` is always `null`. The dollar figure lives on
  the company's own **newsroom** card (captured separately, e.g. via Firecrawl) and is **never reconciled** here.
- **No valuation / cap table / related-person / investor-graph.** Co-investors, if recorded, stay verbatim
  strings on a newsroom card. **No verdict** (`evidence_label`/`signal_polarity`) — consumer-side.
- **Collapse filers by CIK before judging.** `Sora Fuel Corp` / `SORA FUEL Corp` are one filer; raw hit
  count lies, distinct-CIK count is the truth.
- **Public name → scope Form-D to the ticker CIK.** A blind `"Tesla"` Form-D search hits 13 CIKs; once the
  ticker pins CIK 1318605, the search scopes to it (Tesla's own 7 Form-Ds) and the swamp drops out.
- **Form-D ⇄ newsroom corroborate, never reconcile.** Sora's Form-D (2026-03-31) sits a week before its
  "$14.6M" newsroom round (Apr 8) — recorded side by side. VerdeGo's Form-Ds *recover* a dated signal its
  newsroom lacked.
- **SEC needs a descriptive `User-Agent`** (403 without). EFTS returns transient 500s → one back-off retry.

## Exit codes

`0` clean capture (a factual no-match / not-public is data, not failure) · `2` transport error after one
retry. No exit 3 — EDGAR is a stable government JSON contract (no version-pinned parser to drift, like Wayback CDX).
