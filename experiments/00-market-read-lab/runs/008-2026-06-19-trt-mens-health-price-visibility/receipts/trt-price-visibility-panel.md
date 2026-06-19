# Receipt - TRT / hormone-optimization price-visibility panel

Derived per-brand price-visibility classification for the men's-health / TRT / hormone cohort,
read from each brand's captured `offerings.md` (Roster `Visibility` column + verbatim prices +
`site_notes`).

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 | store/getpetermd-com/offerings.md | 2026-06-04 | store file | derived (from captured company pages) | no | C1, C3 |
| S2 | store/maximustribe-com/offerings.md | 2026-06-03 | store file | derived | no | C1, C3 |
| S3 | store/trtnation-com/offerings.md | 2026-06-04 | store file | derived | no | C1, C3 |
| S4 | store/vitalityrx-com/offerings.md | 2026-06-04 | store file | derived | no | C1, C3 |
| S5 | store/sermorelin-com/offerings.md | 2026-06-16 | store file | derived | no | C1, C3 |
| S6 | store/getopt-com/offerings.md | 2026-06-16 | store file | derived | no | C2, C3 |
| S7 | store/honehealth-com/offerings.md | 2026-06-18 | store file | derived | no | C2, C3 |
| S8 | store/hormonemd-com/offerings.md | 2026-06-04 | store file | derived | no | C2, C3 |
| S9 | store/mylifeforce-com/offerings.md | 2026-06-04 | store file | derived | no | C2, C3 |
| S10 | store/defymedical-com/offerings.md | 2026-06-04 | store file | derived | no | C2, C4 |
| S11 | store/marekhealth-com/offerings.md | 2026-06-04 | store file | derived | no | C2, C4 |
| S12 | store/kingsbergmedical-com/offerings.md | 2026-06-17 | store file | derived | no | C2, C4 |

## Method

1. Re-derived the cohort from `telehealth.md` frontmatter (`anchor_category`, `audience`) across the
   54 telehealth packs: kept brands whose anchor is **TRT / hormone-optimization / peptides** and
   whose audience is men-first or men-only. Working set = 12 core brands below. A secondary men-only
   **ED / hair** band (bluechew, rexmd, rugiet, keeps, malemd, joiandblokes) was inspected but held
   out of the core score because its anchor is sexual-health/hair, not hormone therapy.
2. For each brand, read the `offerings.md` Roster `Visibility` column + verbatim `Price` on the
   **testosterone / hormone anchor row(s)** and the `site_notes`. Classified the brand's *therapeutic*
   price posture (not its lab/consult anchor) into: **publishes** (real per-drug $ public),
   **membership-floor** (a headline $/mo is public but membership/consult-gated and drug cost often
   sits on top), or **gated** (no public per-drug therapeutic price; only intake/labs/consult priced).
3. The publish/gate split was *recorded by the original capture*, not inferred here: the gaters'
   `site_notes` explicitly document intake/portal gating (e.g. Marek "gated behind the $299
   intake/login"; Defy "consult + portal-gated"), so "on-request" here = **company intake-gate**, not
   a capture miss.

## Evidence

| Brand | TRT/hormone anchor (verbatim) | Posture | Note |
|---|---|---|---|
| getpetermd | Injectable TRT "$79"–"$139"/mo; Oral/enclomiphene "$278"/bimo; HCG "$147" | **publishes** | full per-drug ladder public |
| maximustribe | Enclomiphene/Cream/Injectable "$99.99–$289.99/mo" (1/3/12-mo ladders) | **publishes** | full PDP ladders |
| trtnation | Testosterone "$99.99/mo"; TRT+HCG "$180/mo" | **publishes** | "#1 IN THE NATION… $99/mo" hero |
| vitalityrx | Reboot Program "$199/mo"; Vitality Test "$149" | **publishes** | enclomiphene, not exogenous T |
| sermorelin | Sermorelin "$149–$199/mo"; Enclomiphene "$149–$179/mo" | **publishes** | peptide / SERM, "alternative to TRT" |
| getopt | TRT "starting at $245/mo + $195 lab fee" | membership-floor | Optimization-tier-gated; med fees may sit on top |
| honehealth | TRT cypionate "From $28/mo + membership"; cream/troche "From $60/mo + membership" | membership-floor | biomarker+consult gated; "+ membership" |
| hormonemd | TRT "$84/mo" (partial) | membership-floor | membership Rx; "med cost separate" |
| mylifeforce | Testosterone injectable/cream "$80"; HRT membership — no price | membership-floor | members-only Rx; membership PDP shows no price |
| kingsbergmedical | HGH "$500.00 to $1000.00 or more per month" (family range, `partial`); testosterone "$70-$100/month without insurance" (`partial`) | membership-floor | **[corrected in Loop 2 — see note]** a wide range *is* a partial disclosure, not a full gate |
| defymedical | TRT family — "on-request" (consult + portal-gated); only labs ($299 panel) public | **gated** | therapeutics behind consult/portal |
| marekhealth | TRT — "behind intake"; only $299 intake + "$450" lab floor + diagnostics public | **gated** | "gated behind the $299 intake/login" |

Cohort split (n=12 core): **publishes 5 · membership-floor 5 · gated 2** (~42% / 42% / 17%).
Run 000's GLP-1 split for comparison: **33% real number / 42% moving floor / 25% gate fully**
(229 priced SKUs). **Defy and Marek** gate fully in **both** categories (n=2); Kingsberg gated in
GLP-1 (run 000) but shows partial price ranges for TRT here.

> **Loop 2 correction (2026-06-19):** the adversarial evidence verifier caught that Kingsberg's own
> captured file marks its HGH and testosterone rows `partial` with public price *ranges*
> ($500–$1000/mo HGH; $70–$100/mo testosterone on FAQ/cost pages), which is a partial disclosure, not
> a full intake-gate. Kingsberg was moved from **gated → membership-floor**, dropping the gated tier to
> 2 (Defy, Marek) and lifting membership-floor to 5. C4 (two-category gaters) accordingly narrows to
> Defy + Marek (n=2). The original Loop 1 call over-read "prices not on PDPs" as "no price exists."

Roster-wide `Visibility` tallies (all rows, context only): getpetermd 22/0/0 · trtnation 17/0/0 ·
vitalityrx 11/0/0 · sermorelin 8/0/0 · maximustribe 5/6/0 · hormonemd 1/6/0 · honehealth 46/11/0 ·
getopt 4/3/17 · mylifeforce 15/26/1 · defymedical 13/1/26 · marekhealth 9/3/11 · kingsberg 0/7/6
(published / partial / on-request).

## Limits

- **Partial denominator.** This is a re-derived working set of 12 men-first TRT/hormone-anchored
  brands, **not a census**. Generalist all-gender brands also run TRT lines (e.g. henrymeds, lifemd,
  invigormedical, struthealth) and were not scored here; their inclusion would shift the ratios. The
  cohort boundary (where "hormone optimization" ends and "longevity/NAD" begins — hone, mylifeforce,
  getopt straddle) is a judgment, not a closed set.
- Posture is read at the **therapeutic** anchor, deliberately ignoring each brand's published lab/
  consult anchor. A brand can publish a $299 lab while gating every drug (Defy, Marek) — that is the
  point, not a contradiction.
- Captures span **2026-06-03 → 2026-06-18** (≤16 days old as of 2026-06-19); several `site_notes`
  flag A/B-volatile pricing (Marek, Maximus). Numbers are a captured floor, not a live quote.
- Enclomiphene/sermorelin "publishers" (vitality, sermorelin, partly maximus/trtnation) sell
  endogenous-T stimulants, **not** exogenous TRT — they publish partly because that is a different,
  more commodity product. Lumping them with injectable-T publishers slightly overstates "TRT" price
  transparency.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 5 of 12 core brands publish a real per-drug price; only ~3/10 of *exogenous-T* sellers do (Vitality/Sermorelin are enclomiphene/SERM, not TRT) | S1–S5 | counting SERM/peptide sellers inflates "TRT" transparency by ~a third |
| C2 | 7 of 12 hide the drug price behind membership or intake (**5 membership-floor, 2 fully gated** after Loop 2 correction) | S6–S12 | membership-floor still flashes a headline $/mo |
| C3 | The publish/gate split tracks business model (commodity-compounded DTC vs high-touch clinic), not molecule | S1–S12 | brand-level, not proven causal — **survived adversarial review** |
| C4 | Defy + Marek gate fully in both GLP-1 (run 000) and TRT | S10–S11 + run 000 read | two-category sighting, n=2 (Kingsberg dropped in Loop 2) |
