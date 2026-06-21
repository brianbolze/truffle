# Market Read

## Question

Across the captured store, can a downstream reader tell which profiles' market-sensitive
State (pricing, offers, availability, policy) is at risk of being stale — and is the
capture clock (`captured_at`) plus existing point-in-time prose plus signals recency
enough to flag that risk, or is there a freshness-grain gap the store cannot self-report?

## Result

**Yes — a reader can rank staleness *risk*, and better than expected, but only by crossing
two already-greppable surfaces; neither alone works, and the store can never self-report
actual *drift* (whether a fact really changed since capture). No new field is needed.**

The store carries exactly **two** freshness-relevant surfaces, and they answer different
questions (`C1`–`C4`):

1. **`captured_at` — the "how old" axis.** Present on **130/130** profiles, span
   **2026-05-30 → 06-20 (age 0–21 days, median 16d)**; **79/130 are ≥15 days old** (the
   05-31 and 06-04 capture batches). This is the only *universal* freshness datum. **But
   age alone is a false staleness proxy:** the oldest captures include Casio, Cartier,
   Nike, Swatch, Apple, AWS, Datadog — MSRP / published rate-card brands whose facts are
   *stable*, so "20 days old" is not "stale." Ranking by age alone over-flags them (`C4`).

2. **The literal `point-in-time snapshot, not fixed` token — the "how volatile at capture"
   axis.** Present on **47** profiles as the SCHEMA-contracted literal (SCHEMA.md:112), +10
   that use the phrase loosely ≈ **57** total. It is the store's *only* structured volatility
   surface, and it is greppable. **But it marks capture-*instability* (A/B tests, promo
   rotation, geolocation — "will differ next run"), not staleness-*since-capture*.** It is
   present regardless of age, and concentrates in **health/telehealth 36/69 vs non-health
   11/61** (`C2`) — because telehealth runs intake-gated, promo-coded, rotating pricing.

**Cross the two → a query-time staleness-RISK filter the store can already produce:**
**34 profiles are both old (≥14d) AND volatility-flagged** (`C3`) — the highest real-risk set,
overwhelmingly telehealth GLP-1 / hormone promo pricing (agelessrx, gogeviti, gethealthspan,
mylifeforce, nurx, rexmd, getpetermd, joinfridays, …) plus a few volatile-pricing SaaS
(notion, typeform, gong, alpha-sense). This cross is `query-time-grouping-enough`: it needs
**no new durable marker** — both inputs already exist and are greppable.

So the honest answer a "trust the cache" reader gets:
- **"How old is this?"** — always answerable (`captured_at`, 130/130).
- **"Is this the *kind* of fact that goes stale fast?"** — answerable for the 57 volatility-
  flagged profiles via the point-in-time token.
- **"Risk-rank what to re-check"** — answerable by crossing the two (the 34-profile set).
- **"Has this fact *actually changed* since capture?"** — **NOT answerable store-only.** No
  surface measures real drift; signals don't help (G1). That is MRL-012's re-capture/diff
  cadence — parked, spend-gated — not a missing marker.

## Gap Map

| Reader question | Store answer | Surface | Verdict |
|---|---|---|---|
| How old is this capture? | Yes, all 130 | `captured_at` | clean |
| Which facts are volatile-by-nature? | 57 flagged | point-in-time token | clean-but-partial (token = capture-flicker, a *correlate* of staleness risk, not a measure) |
| Risk-rank stale-prone profiles | Yes, query-time | `captured_at` age × point-in-time token (34 high-risk) | **query-time-grouping-enough — no primitive** |
| Has a specific fact drifted since capture? | **No** | — | **G1: unobservable store-only; needs re-capture/diff (MRL-012)** |
| Grep all freshness data reliably | Mostly | `captured_at` format inconsistent | **G3: 4 quoted / 126 unquoted silently drop from a naive grep** |

**G1 — Signals do not refresh State.** 49 profiles carry a `signals/` dir, but in **0** cases
is any signal clock newer than the profile's `captured_at` (`C5`) — signals were co-captured in
the same campaign window, not re-run since. So "signals recency" is **not** an independent
freshness re-read of State today; it cannot tell a reader a profile fact has changed. Actual
drift-detection requires re-capture + diff (MRL-012), which is spend/approval-gated, not store-only.

**G2 — The volatility token is not a drift measure.** It correctly flags "this price will flicker
run-to-run," which *correlates* with going stale, but never says a value *has* moved. Reading the
57-token set as "these are stale" would over-claim.

**G3 — `captured_at` format inconsistency (tooling).** 4 profiles quote the value
(`captured_at: "2026-06-09"`: anazaohealth, goinfusive, jinfiniti, millspharmacy); 126 leave it
bare. A naive `captured_at:\s*\d` freshness grep **silently drops the 4** — my own Loop-1 parser
did exactly this and mislabeled them "undated" until corrected (`V1`). A one-line normalization
(or a `querycheck` lint) fixes it; MRL-008 "bare field isn't self-describing / parse-hazard" family.

## Evidence Used

Store-only; no external sources. All counts re-derivable from `store/*/profile.md` frontmatter +
`store/*/signals/` clocks as of the 2026-06-20 session. Receipt: `receipts/freshness-census.md`.

| ID | Claim | Basis |
|---|---|---|
| C1 | 130/130 profiles dated; age span 0–21d, median 16d; 79 are ≥15d old | `captured_at` parse over all profiles (robust to quoting) |
| C2 | 57 carry point-in-time prose (47 literal SCHEMA token + 10 loose); token skews health 36/69 vs non-health 11/61 | grep of literal token + phrase; primary_industry cross-tab |
| C3 | 34 profiles are ≥14d old AND carry the literal point-in-time token | age × literal-token cross |
| C4 | Age-alone over-flags stable brands (Casio/Cartier/Nike/Swatch/AWS/Datadog at 20d are not stale) | oldest-12 list vs content type; Casio frontmatter shows stable retail MSRP, no volatility token |
| C5 | 49 profiles have signals/; 0 have a signal clock newer than profile `captured_at` | signals clock max vs `captured_at` per profile |

## Companies Seen

All 130 profiled companies (cross-vertical: telehealth, SaaS/Technology, watches/Consumer Goods,
Automotive, Retail, Finance). High-staleness-risk exemplars (≥14d + volatility token): agelessrx,
gogeviti, gethealthspan, mylifeforce, nurx, rexmd, getpetermd, joinfridays, struthealth, ivimhealth,
notion, typeform, gong, alpha-sense (34 total — `C3`). Stable-but-old anchors (age ≠ staleness):
casio, cartier, nike, swatch, apple, aws, datadog.

## Missing / Stale Coverage

- The 9 capture-only stubs (run-027 list) carry no `profile.md` and so no `captured_at` — they sit
  *outside* the freshness denominator entirely (directory ≠ profiled, MRL-001). Not a freshness gap;
  a coverage gap already logged.
- No profile is genuinely undated once quoting is handled (G3); the earlier "4 undated" read was a
  parser artifact, corrected.

## Source Gaps

- **No drift surface.** Store-only cannot answer "did this fact change?" — only "how old / how
  volatile." Closing it needs the parked re-capture+diff cadence (MRL-012), which is spend-gated.
- Signals, as captured, do not function as a State-freshness re-read (G1) — they would only if
  re-run on a cadence independent of the initial profile capture.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger: O1 (two-surface freshness model), O2 (signals never refresh
State / 0-fresher), O3 (token = capture-volatility not staleness, health-skewed), S1 (query-time
cross is enough — no marker), G1/G3 (drift-unobservable; format parse-hazard), W1 (persistence-
boundary verdict), V1 (own-parser over-flag and quoted-date miss — failure mode reproduced & caught).

## External Completeness Check

Not applicable — store-only calibration of the store's own freshness surfaces; no outside
denominator is load-bearing. (The relevant completeness check is internal: 130/130 dated, done.)

## Market Pattern

Volatility-of-content, not age, is the real staleness axis — and it is **vertical-shaped**:
telehealth's promo-coded / intake-gated / rotating pricing makes it the genuinely stale-prone
slice (token 36/69), while published-MSRP watches and published-rate-card SaaS are old-but-stable.
A "trust the cache" reader should risk-rank by *content volatility × age*, which the store already
supports at query time — not by age alone, which inverts the truth for stable brands.

## What Would Change This Answer

- A **re-capture + diff cadence** (MRL-012) would convert "risk" into observed "drift" — the only
  thing that would make actual staleness (not risk) store-answerable. Spend/approval-gated.
- If the volatility token were ever extended to **non-price volatile State** (availability, policy,
  roster) it would widen the risk filter; today it is price/IA-scoped by SCHEMA-112.
- A **`captured_at` format-normalization lint** would make the freshness grep fully reliable (G3) —
  a tooling fix, not a primitive.

**Persistence-boundary verdict: no new durable freshness/volatility marker.** Staleness-*risk* is a
query-time cross of two existing greppable surfaces (`captured_at` × point-in-time token); the two
real gaps are the parked re-capture cadence (drift, MRL-012) and a one-line format lint (G3).
`query-time-grouping-enough` fires **TRUE** for risk-ranking, **FALSE** only for actual-drift —
which no store-only surface can answer by design.
