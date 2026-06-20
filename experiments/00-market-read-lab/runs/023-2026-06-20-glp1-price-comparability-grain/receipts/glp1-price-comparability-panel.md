# Receipt - GLP-1 entry-price comparability panel

Per-brand captured GLP-1 entry price, its verbatim unit, what it bundles, the captured
visibility flag, and promo status — the substrate for the comparability audit. All values
read verbatim from each brand's captured `store/<domain>/offerings.md` (no external sources).

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: primary        # captured State, read verbatim from store files
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | store/ (19 GLP-1-anchored `offerings.md`, listed in Evidence) | per-file `captured_at` 2026-06-03 → 2026-06-18 | local-store / store file | primary (captured State) | none | no | C1–C5 |
| S2 | runs/012-…/read.md + runs/010-…/read.md | 2026-06-19 | local-store / prior lab artifact | secondary (prior run) | none | no | C1 (cohort membership), C3 |

## Method

Denominator = the 19 `anchor_category: GLP-1` brands enumerated in run 012 (itself from a
store grep), re-verified present in `store/` this run. For each, the GLP-1 weight-loss
**entry** offer's price row was extracted verbatim from `offerings.md` (Roster `Price
(verbatim)` + `Visibility` columns and `site_notes`), via three mechanical extraction passes.
No price was normalized, converted, or ranked at capture; effective-monthly figures in the
read are explicitly labeled **derived [J]**.

## Evidence

Per-brand (verbatim entry price · unit · includes · visibility · promo):

- **brellohealth** (2026-06-04): `~~$599~~ $399 every 3 months ("$133 Per Month")` · 3-month total billed upfront, renews every 10wk · med+supplies+app+classes+community · **published** · **promo** (Deadline Funnel countdown).
- **directmeds** (2026-06-04): `$179.10/mo.` (sublingual semaglutide listing) vs `$347/month` (injection PDP); the genuine *same-SKU* conflict is `$297` listing vs `$347` PDP · per-month, **conflicting across surfaces** · visits+meds+supplies+support · **partial** · promo (.10 = ~10% off).
- **eden-health** (2026-06-03): `$99/mo*` med-only · per-month + **separate mandatory $99/mo membership** ($39 first mo) · medication only · **partial** · no. "Same Price at Every Dose."
- **effecty** (2026-06-04): `$160/month` (after promo) · per-month recurring; grid collapses GLP-1 ($160) vs GLP-1+GIP ($240) · med, no membership · **published** · promo (EFFECTY100: $60 first mo).
- **goodlifemeds** (2026-06-04): Microdose `$149` / Semaglutide `$199` / Tirzepatide `$297` · per-month (plan-dependent) · med+supplies+consult · **published** · promo (SUMMER30 sitewide 30% off).
- **henrymeds** (2026-06-04): `starts at $179/month` floor (all 6 GLP-1 SKUs) · per-month **floor, moves with dose**, exact price intake-gated · visits+med+supplies+support, no membership · **partial** · no.
- **hims** (2026-06-18): `From $149/mo†` (Wegovy pill) · per-month **med-only + mandatory $149/mo membership** ($39 first mo); "not available without a membership" · medication only · **partial** · no.
- **home-medvi** (2026-06-04): `Starting at $179` first month, `$299` refills · per-month, first-month ≠ refill · all-in, "no membership or hidden fees" · **published** · promo ("SUMMER Sale").
- **ivimhealth** (2026-06-04): `starting at $75/mo` med + `$74.99/mo Program Fee`; also `$499 (4-mo)`/`$600 (6-mo)` · per-month **med floor + separate program fee** · med+program · **partial** · promo ("first month free").
- **ivyrx** (2026-06-04): `From ~~$197~~ $175 (4 doses/month)` · per-month **assuming 12-month prepay**, scales by dose · medication · **partial** · promo (struck).
- **joinamble** (2026-06-18): `$135/mo` (12-mo) · `$145` (6-mo) · `$160` (3-mo) · `$179/mo` (1-mo) · per-month **subscription ladder, commitment-dependent**; "From $179" homepage · all-in · **published** · no. "Same price, every dose."
- **joinfound** (2026-06-04): `$149/mo` (insurance,12-mo) / `$199` (cash,12-mo) / `$299/mo` (cash monthly) · per-month **program membership, medication billed separately** · program only · **partial** · no.
- **joinfridays** (2026-06-04): `Starting at $150/mo` (annual) / `$249/mo` (month-to-month) · per-month, commitment-dependent, **moves with dose** · all-in (med+coaching+care, membership free) · **partial** · promo (codes floor to $117/mo).
- **mydrhank** (2026-06-03): `From $171/mo` (oral semaglutide) · per-month **floor, all-in hidden behind intake** · med+consult+delivery, no membership · **partial** · no.
- **noom** (2026-06-04): `from $149 … then $349 per month … for 12 week subscription thereafter` · **mixed**: $149 initial then $349/mo program, billed upfront quarterly, **med cost separately variable** · program floor · **partial** · no.
- **remedymeds** (2026-06-03): `$299/month` ("Less than $9/day") · per-month all-in, billed every 28 days · med+care+labs+shipping · **published** · no. (T&Cs call the all-in a "membership.")
- **ro** (2026-06-18): `$149 first month`, `$199–$299 thereafter` (Wegovy pill) + **separate Ro Body membership $39/$74/$149** · per-month cash-pay **med + separate membership line** · medication only · **partial** · no.
- **telolife** (2026-06-18): `$199/mo` (or `$597` 3-mo bundle = prepaid monthlies) · per-month all-in · med+titration+shipping, "no membership fees… no hidden charges" · **published** · no. "ALL-INCLUSIVE REGARDLESS OF DOSAGE."
- **tryshed** (2026-06-04): card `Starting at $299/month`; PDP `1 Month $249` (6-mo $199 / 12-mo $175) · per-month, **commitment-dependent**; card ≠ PDP · med · **published** · no. (Entry compounded-semaglutide SKU is membership-free; some non-entry SKUs — Foundayo/zepbound — carry a separate $125/mo Shed Membership per `site_notes`, so all-in holds at the entry tier, not brand-wide.)

## Limits

- Entry-offer only: each brand's *lowest/leading* GLP-1 price; dose ladders and longer plans
  not exploded into per-dose rows (intake-gated for ~half the cohort).
- Captures span 2026-06-03 → 2026-06-18; promo prices are point-in-time by definition and
  several brands flag "subject to change."
- Where a brand shows conflicting numbers across surfaces (directmeds listing vs PDP; tryshed
  card vs PDP) the conflict is reported, not resolved — the captured State holds both.
- This panel proves how the captured *units differ*; it does not assert any brand's all-in
  effective price (those reconstructions are derived [J] in the read).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 19-brand GLP-1 cohort all carry a captured entry price | S1, S2 | denominator partial (anchor cut) |
| C2 | Entry-price units are incommensurable across ≥5 distinct denominations | S1 | within captured cohort |
| C3 | ~half the cohort's "price" excludes a mandatory membership/program fee billed separately | S1 | per-file verbatim |
| C4 | ~8/19 entry prices are promotional or point-in-time | S1 | capture-date bound |
| C5 | `visibility: published/partial` flag already encodes self-contained-vs-cost-on-top | S1 | existing captured field |
