# Receipt - store freshness census

Supports the freshness/staleness-grain read: capture-clock distribution, point-in-time
token census, the age×token high-risk cross, and the signals-never-refresh-State finding.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter (`captured_at`, `primary_industry`, `site_notes`, `unverified_fields`) | per-profile `captured_at`, 2026-05-30→06-20 | local-store | derived | none | no | C1,C2,C3,C4 |
| S2 | `store/*/signals/**/*.json` filename clocks | session 2026-06-20 | local-store | derived | none | no | C5 |
| S3 | `SCHEMA.md:112` (point-in-time / A/B contract) | SCHEMA v2.x | owned/official contract | primary | none | no | C2 |

## Method

Two Python passes over `store/` (`/tmp/freshness.py` → `/tmp/fresh4.py`, robust-quoting fix):
1. Enumerate `store/*` dirs (139) → 130 with `profile.md`, 9 stubs (run-027 list).
2. Parse `captured_at` with `^captured_at:\s*"?(\d{4}-\d{2}-\d{2})"?` (handles quoted+bare) →
   130/130 dated; age = (2026-06-20 − captured_at). Distribution + buckets.
3. Census the literal `point-in-time snapshot, not fixed` token (47) and the loose phrase (+10 ≈ 57);
   cross-tab token presence by health vs non-health `primary_industry` bucket.
4. Cross age≥14d × literal token → 34 high-risk profiles.
5. Per profile with a `signals/` dir (49), compare max signal clock vs `captured_at` → 0 fresher.

## Evidence

- **C1:** 130 dated; min 0d / max 21d / mean 13.2 / median 16; buckets {0-3d:14, 4-7d:22, 8-14d:15, 15-21d:79}.
- **C2:** literal token 47; phrase-only +10 = 57; by vertical — health/telehealth 36/69, non-health 11/61. SCHEMA.md:112 defines the literal token as the price/IA capture-volatility flag.
- **C3:** 34 profiles with literal token AND age≥14d; majority Healthcare/telehealth (GLP-1/hormone promo pricing), a few Technology (notion/typeform/gong/alpha-sense).
- **C4:** oldest captures (21–20d) include casio/cartier/nike/swatch/apple/aws/datadog — stable MSRP/rate-card brands; casio frontmatter carries no point-in-time token (stable retail). A loose keyword grep (`promo|discount|coupon|rotate`) over-counted the high-risk set to 57 by sweeping these stable brands in — the literal token drops it to the disciplined 34.
- **C5:** 49 `signals/` dirs; 0 profiles where max signal clock > `captured_at`.
- **Format hazard (G3):** 4 profiles quote `captured_at` (anazaohealth, goinfusive, jinfiniti, millspharmacy = "2026-06-09"); 126 bare. First parser (`\s*\d`) silently dropped the 4 → mislabeled "undated"; corrected in `fresh4.py`.

## Limits

- The 57/34 counts depend on the point-in-time token being *applied at capture*; an unflagged
  volatile profile would be under-counted (token coverage, not measured here — capture-discipline gap).
- The volatility token measures capture-instability, a *correlate* of staleness risk, not actual
  drift; this receipt cannot prove any specific fact changed since capture.
- The health/non-health bucket is a coarse keyword cut on `primary_industry`, a derived grouping.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 130/130 dated; median age 16d; 79 ≥15d | S1 | age ≠ staleness (see C4) |
| C2 | 57 point-in-time (47 literal); health-skewed 36/69 vs 11/61 | S1,S3 | token = price/IA volatility, SCHEMA-scoped |
| C3 | 34 high-risk = age≥14d × literal token | S1 | depends on token being applied at capture |
| C4 | Age-alone over-flags stable old brands | S1 | demonstrated via loose-grep over-count |
| C5 | Signals never newer than profile capture (0/49) | S2 | signals co-captured, not re-run |
