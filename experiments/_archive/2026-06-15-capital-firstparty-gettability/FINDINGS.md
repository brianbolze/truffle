# FINDINGS — Probe #2 (capital / first-party funding gettability)

**Verdict: PASS. `tools/sec_edgar.py` is cleared** — the boundary holds and the name-match seam is containable. Design requirements + the shaken-out card schema below.

## Pass check (against the approach's bar)

| Criterion | Result |
|---|---|
| ≥4/7 startups yield a dated first-party card | **6/7** (newsroom: sora, blue, electra, euclid[M&A], evoloh; EDGAR Form-D recovers verdego). Only euclid lacks a Form-D — but has the dated M&A. ✅ |
| Control (TSLA) → ticker-State + filing-Signal | TSLA → CIK 0001318605, Tesla Inc., Nasdaq + dated 10-Q/8-K/10-K. ✅ |
| CFS "$2B" stays a flagged baseline | Cumulative, undated → captured verbatim + `cumulative_undated`, **not** promoted to an event. EDGAR shows only early dated Form-Ds, never "$2B". ✅ |
| VC nulls → zero company raises | Sequoia 281 / First Round 34 hits = **fund + portfolio noise**, no company raise. `name_match_unconfirmed`. ✅ |

**The cross-source win:** EDGAR and the newsroom *cover each other's gaps*. VerdeGo named investors but no dated round on-site → EDGAR Form-Ds (2017–2024) recover a dated signal. Sora's newsroom round (Apr 8 2026) is *corroborated* by a Form-D filed 2026-03-31 (the classic Reg-D-then-announce sequence). Neither is reconciled — recorded side by side.

## Half A — newsroom (from cached profiles, $0)

| Startup | First-party funding signal | Card type |
|---|---|---|
| sorafuel.com | "$14.6 million round" Apr 8 2026, co-led Spero Ventures + Inspired Capital | **round** (dated) ✅ |
| blueenergy.co | "$380 million in financing" Apr 21 2026, led VXI Capital + Engine Ventures | **round** (dated) ✅ |
| electra.aero | "$115 million in Series B" Apr 2025; USAF "$85M" Jan 2023 | **round** (dated) ✅ |
| euclidpower.com | Acquired Thresh Power, Apr 30 2026 | **m&a** (dated) ✅ |
| evoloh.com | "over forty million dollars ($40 million)" (Dec 2024 page) | **round** (dated-ish) ✅ |
| cfs.energy | "over $2 billion in capital" (undated) | **cumulative_total** — flagged, NOT an event |
| verdegoaero.com | investors named (RTX Ventures, DiamondStream…), no dated round | newsroom **null** → EDGAR recovers it |

## Half B — EDGAR (keyless, $0)

| Name (Form-D FTS) | Hits / distinct filers | Read |
|---|---|---|
| Sora Fuel | 2 / 1 CIK | **confirmed** — Sora Fuel Corp (CIK …480), Form-D 2026-03-31 |
| Commonwealth Fusion Systems | 5 / 2 | **confirmed** — CFS LLC (CIK …079), 2018→2021 + an SPV |
| VerdeGo Aero | 7 / 1 CIK | **confirmed** — VerdeGo Aero Inc (CIK …832), 2017→2024 |
| Euclid Power | 0 | **null** — no Form-D (missing ≠ none; M&A is its signal) |
| EVOLOH | 1 | **related-vehicle** — only "VXI Evoloh SPV LP" (an investor SPV, not the issuer) → unconfirmed |
| Blue Energy | 5 / 4 | **name_match_unconfirmed** — common name (World Energy…, Blue Energy Fuels, Tamarack Blue Energy) |
| Electra | 77 / 64 | **name_match_unconfirmed** — swamp (Electra Therapeutics, Electra REITs, Electra Capital…) |
| Sequoia Capital (VC) | 281 / 76 | fund swamp — never a company raise |
| First Round Capital (VC) | 34 (after a transient 500) | fund + portfolio (Karuna Health) noise |

## Draft card schema (shaken out here — stays draft/project-side, NOT a graduated contract)

One dated event = one card, `grain=company`, `observation: factual`. Verbatim terms; co-leads stay strings (no entity resolution). Representative cards:

```yaml
# clean dated round (newsroom)
- subject: sorafuel.com
  source_type: newsroom            # newsroom | sec
  event_type: round                # round | m&a | form_d | filing | cumulative_total
  date: 2026-04-08
  amount: "$14.6 million"          # verbatim, as stated
  round_label: "round"             # verbatim (they did NOT say "Series A")
  co_leads: ["Spero Ventures", "Inspired Capital"]   # verbatim strings, no graph resolution
  participants: ["Engine Ventures", "Wireframe Ventures"]
  flags: [self_reported]
  citation: "store/sorafuel-com/profile.md (Strategic read) + key_page /news/sora-fuel-closes-14-6m-round…"

# cumulative total — captured but NOT an event
- subject: cfs.energy
  source_type: newsroom
  event_type: cumulative_total
  date: null
  amount: "over $2 billion in capital"
  flags: [self_reported, cumulative_undated, not_an_event]
  citation: "store/cfs-energy/profile.md (story page)"

# EDGAR Form-D — confirmed (distinctive name, single CIK)
- subject: verdegoaero.com
  source_type: sec
  event_type: form_d
  date: 2024-07-25                  # latest; existence + date only — NO amount extracted
  filer: "VerdeGo Aero, Inc."
  cik: "0001714832"
  match: confirmed
  citation: "efts.sec.gov forms=D"

# EDGAR Form-D — name_match_unconfirmed (the contained seam)
- subject: electra.aero
  source_type: sec
  event_type: form_d
  match: name_match_unconfirmed     # 64 distinct CIKs for "Electra"; issuer not isolable
  flags: [existence_only, not_promoted]
  note: "'Electra' is a common name — Electra Therapeutics, Electra REITs… never assert a match"
```

## Design requirements for `tools/sec_edgar.py` (the de-risk dividends)

1. **Two emission kinds, cleanly split:** ticker/exchange → `profile.md` **State** (rarely changes); every dated filing / Form-D → a **Signal** card (`source_type=sec`), never edited into the snapshot.
2. **Collapse filer duplicates by CIK** before judging a match — Sora showed as 2 "filers" (case variants) but 1 CIK. Match confidence keys on *distinct CIK count*, not raw hit count.
3. **`name_match_unconfirmed` is a first-class state, not an abort.** >1 distinct CIK after collapse (Blue Energy=4, Electra=64) → existence-only, never promoted, mandatory caveat. A single distinctive-name CIK (Sora, CFS, VerdeGo) → `confirmed`.
4. **Related-vehicle guard:** a filer whose name is an SPV/fund wrapper around the subject ("VXI **Evoloh** SPV LP") is the *investor's* vehicle, not the issuer's raise → `name_match_unconfirmed`, flag `related_vehicle`. (Heuristic: filer name ≠ issuer root, contains SPV/Fund/Partners/LP.)
5. **Form-D is existence + date ONLY** — no amount/cap-table/related-person extraction (the seam). Amounts come from the newsroom card, kept separate and unreconciled.
6. **Transport robustness:** EFTS returned a transient 500 (First Round) that cleared on retry → one back-off retry, then exit-2 transport error (not a false null). SEC requires a descriptive `User-Agent` (403 without).
7. **Keyless, stdlib urllib** — fits the tools spine; `source_type=sec`, `source=efts.sec.gov` / `data.sec.gov`. No paid aggregator, no valuation, no investor graph.
