# Probe #2 — capital / first-party funding gettability

**Gates:** `tools/sec_edgar.py`. Per the [traction approach](../../_design/2026-06-15-traction-approach.md) (#4), no funding-tool code lands until this reads clean.

**Hypothesis.** First-party, dated funding is gettable cheaply inside the boundary (own-newsroom rounds/M&A + free EDGAR ticker/filings/Form-D), and the name-match seam (asserting a Form-D belongs to *this* private startup) can be *contained* to existence + date + a `name_match_unconfirmed` state — without drifting into the paid-data swamp (valuation, cap tables, investor-graph resolution).

**Method (~$0 — cached store + keyless EDGAR GETs, no spend).**
- **Half A (newsroom):** read the cached `store/<domain>/profile.md` for the 7 energy/aero startups + 2 VC nulls; hand-write funding cards per the boundary (existence + date + *verbatim* terms; cumulative-undated totals flagged, never promoted to an event). Cards in [`FINDINGS.md`](FINDINGS.md).
- **Half B (EDGAR):** [`edgar_probe.py`](edgar_probe.py) — keyless GETs to `company_tickers.json` (ticker→CIK State), `data.sec.gov/submissions` (dated 8-K/10-K Signal), and `efts.sec.gov` full-text search `forms=D` (Form-D existence by issuer name). TSLA as the public control; the 2 VCs as nulls. SEC needs only a descriptive `User-Agent`.

**Pass bar** (from the approach): ≥4/7 startups yield a dated first-party card · control yields ticker-State + filing-Signal · CFS "$2B" stays a flagged baseline · VC nulls yield zero company raises. **Caveat:** a missing newsroom page is *missing data*, not *no funding*.

**Run:** `python3 edgar_probe.py`

**Result:** PASS — see [`FINDINGS.md`](FINDINGS.md).
