# Market Read

## Question

In the men's-health / TRT / hormone telehealth cohort already in the store, which brands publish
price vs gate it behind intake, and what offer structures (membership, labs-included, compounded vs
brand) are becoming table stakes?

Governing capture clocks: offerings.md captures **2026-06-03 → 2026-06-18**, oldest ~16d. Store-only,
no live fetch, no mutation.

## Direct Answer

**Price visibility here tracks the *business model*, not the molecule — and it splits much like GLP-1
did.** Across a 12-brand TRT/hormone-optimization working set, **5 publish a real per-drug price
(~42%), 5 publish only a membership floor with the drug cost on top (~42%), and 2 gate the therapeutic
entirely behind a paid intake/consult (~17%)** [C1, C2]. *(These bands were corrected during Loop 2 —
see note below.)* Run 000's GLP-1 cohort split 33% / 42% / 25% — a broadly similar shape, and **two
brands (Defy Medical, Marek)** gate fully in **both** categories [C3, C4]. The gate is a property of
the clinic/high-touch optimization model, not of testosterone.

> **Loop 2 correction:** the original Loop 1 read scored 5/4/3 (~42/33/25) and named Defy/Marek/
> Kingsberg as the cross-category gaters. The adversarial verifier caught that **Kingsberg actually
> publishes partial price ranges** ($500–$1000/mo HGH, $70–$100/mo testosterone, both `partial` on
> public FAQ/cost pages) — a partial disclosure, not a full gate. Kingsberg moved gated → membership-
> floor (→ 5/5/2, ~42/42/17), and the two-category-gater claim narrowed to Defy + Marek. The
> business-model finding (C3) is unchanged and survived scrutiny.

- **Publish a real number** — the **commodity-compounded / enclomiphene flat-monthly** brands, where
  price *is* the pitch: getPeterMD (Injectable TRT `$79–$139/mo`, full per-drug ladder), Maximus
  (`$99.99–$289.99/mo`, 1/3/12-mo ladders), TRT Nation (`$99.99/mo`; hero "#1 IN THE NATION… $99/mo"),
  Vitality Rx (`$199/mo`), Sermorelin.com (`$149–$199/mo`). *Caveat:* Vitality and Sermorelin sell
  **enclomiphene/peptides — endogenous-T stimulants, not exogenous TRT** — so they publish partly
  because it's a more commodity product; counting them slightly inflates "TRT" transparency.
- **Publish a moving membership floor** — "$X/mo **+ membership**" or "+ meds separate," where the
  real cost is finalized after gating: getOpt (`$245/mo + $195 lab fee`), Hone Health
  (`From $28/mo + membership`), HormoneMD (`$84/mo`, med cost separate), Lifeforce (`$80` members-only;
  HRT-membership PDP shows *no* price), **Kingsberg** (`$500–$1000+/mo` HGH range + `$70–$100/mo`
  testosterone on public FAQ/cost pages — a wide range, but a real partial disclosure).
- **Gate the drug fully** — the **clinic / consult-first** model: Defy Medical (TRT "consult + portal-
  gated"; only its `$299` lab panel is public) and Marek (TRT "behind the $299 intake/login"; only the
  `$299` intake + `$450` lab floor public). These two publish *labs and consults* freely while hiding
  every therapeutic price — the opposite of the compounded DTC brands.

**Table stakes (offer structure) for TRT/hormone in 2026:**
1. **An enclomiphene / "fertility-friendly" alternative beside traditional injectable TRT** — now
   near-universal (Maximus, getPeterMD, TRT Nation, Vitality, Sermorelin, Hone, HormoneMD all carry
   enclomiphene or clomiphene). This is the *newest* table stake — the TRT analog of GLP-1's
   microdose/oral tier. **(Judgment, from the rosters below.)**
2. **A three-form testosterone menu** — injectable + cream/topical + oral/troche — standard among the
   full-line brands (Defy, Maximus, Hone, Lifeforce).
3. **Labs as the paid gate (or included)** — a qualifying lab panel `$45–$299` is the funnel spine
   (getPeterMD `$45`, Vitality `$149`, Defy `$299`, Marek `$450`). Often the *only* published price.
4. **Membership architecture as the real differentiator** — all-in flat monthly vs "$X/mo + meds
   separate" vs members-only Rx — the same pricing-architecture split run 000 named for GLP-1.
5. **HCG / testicular-support add-on** (getPeterMD, TRT Nation `TRT+HCG $180/mo`, Defy).
6. **Term-laddered 1/3/12-month discounting** as standard price presentation (Maximus, getPeterMD).

## Evidence Used

All claims are store-derived from captured `offerings.md` Roster `Visibility` columns + verbatim
prices + `site_notes`. Full per-brand table and method in
[`receipts/trt-price-visibility-panel.md`](receipts/trt-price-visibility-panel.md).

- **C1** — 5/12 publish real per-drug price: getpetermd, maximustribe, trtnation, vitalityrx,
  sermorelin (captures 06-03…06-16).
- **C2** — 7/12 gate the drug price (**5 membership-floor**: getopt, honehealth, hormonemd, mylifeforce,
  kingsbergmedical; **2 fully gated**: defymedical, marekhealth). *(Loop 2 reclassified Kingsberg.)*
- **C3** — split tracks business model, not molecule (commodity-compounded DTC publish; high-touch
  clinics gate). **Labeled Judgment**, grounded in the per-brand postures; **survived adversarial review**.
- **C4** — Defy + Marek gate fully in both GLP-1 (run 000 read) and TRT (this run). Two-category
  sighting, n=2 (Kingsberg dropped in Loop 2; it gates in GLP-1 but is partial in TRT).

No external/current/news claims are made; no snippet evidence used.

## Companies Seen

**Core TRT/hormone working set (12):** defymedical, getopt, getpetermd, hormonemd, marekhealth,
maximustribe, trtnation, vitalityrx, sermorelin, kingsbergmedical, honehealth, mylifeforce.

**Secondary men-only ED/hair band (inspected, held out of the core score):** bluechew (1 pub / 7
partial — subscription-floor), keeps (17 pub — price-forward), malemd (6 pub / 4 partial), rexmd
(10 pub / 4 partial / 5 on-req), rugiet (5 pub / 5 on-req — quiz-gated), joiandblokes (37 pub). This
ED/hair band skews **price-forward** like compounded GLP-1, reinforcing C3: consumer-commodity
sub-verticals publish; clinical-optimization models gate.

## Missing / Stale Coverage

- mdpep-com is in the store as a bare directory (no profile/offerings/telehealth) — not scorable.
- No capture older than ~16 days in the scored set; freshness is not a limiter this run. Several
  `site_notes` (Marek, Maximus) flag A/B-volatile pricing — treat numbers as a captured floor.
- Generalist **all-gender** brands that also run TRT lines (henrymeds, lifemd, invigormedical,
  struthealth) were **not scored** — their hormone price-visibility is an open gap that would move the
  ratios.

## Source Gaps

None requiring external fetch. The read is fully answerable from captured State. The one structural
gap is denominator coverage (above), not source grade — `offerings.md`'s `Visibility` column is
exactly the right captured field for this question and carried the load cleanly.

## External Completeness Check

Not run against a live external denominator (would require approval/spend). Internal cross-check: the
cohort was re-derived from `telehealth.md` frontmatter rather than ported from run 001's list, and
the three full-gaters reconcile with run 000's independent GLP-1 read — a weak internal corroboration,
not an external census. **Completeness is explicitly partial; the 12-brand set is a working set, not
"the market."**

## Market Pattern

The durable pattern is **price-visibility as a business-model tell**: a brand that leads with a
published flat monthly is signaling a commodity-compounded / DTC model; a brand that publishes only a
lab panel and gates every drug is signaling a high-touch clinic that monetizes the consult. The
molecule (testosterone vs semaglutide) doesn't predict the posture — the model does, which is why
Defy and Marek behave identically across GLP-1 and TRT. The fastest-moving offer change is the
**enclomiphene "fertility-friendly" tier** becoming table stakes, mirroring how oral/microdose GLP-1
spread — a cheaper, fertility-preserving on-ramp that lets a brand publish a low headline number.

This is a **query-time grouping** of existing store State, not a new durable category — `pressure_lenses_fired`
reflects that (`query-time-grouping-enough`).

## What Would Change This Answer

- Scoring the generalist all-gender TRT lines (henry, lifemd, invigor, strut) — could shift the 42/33/25
  split materially.
- A live re-capture (A/B-volatile pricing on Marek/Maximus may have moved since 06-03).
- Treating enclomiphene/peptide brands as *not* TRT — would drop the "publishes" band toward ~3/12 of
  exogenous-T sellers and sharpen the "clinics gate testosterone" finding.
