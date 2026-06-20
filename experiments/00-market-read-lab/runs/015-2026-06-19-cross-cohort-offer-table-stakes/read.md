# Market Read

## Question

Across all captured telehealth cohorts (GLP-1, TRT, longevity/NAD, sexual-health,
multi/none, peptides, womens-HRT, hair, primary-care, labs), which acquisition and
commitment mechanics — intake-gating / **modality**, the **membership/bundling wedge**,
**compounded-vs-FDA-brand** dispensing, the **payment rail** (cash vs insurance), and
**price publication** — are *cohort-agnostic table-stakes* versus *cohort-specific*? And
does any cohort-agnostic pattern argue for durable cross-cohort State, or is query-time
grouping enough?

First **cross-cohort** read in the lab (runs 008–014 are each single-cohort). Evidence is
store-only over 54 brands with structured `telehealth.md` frontmatter.

## Direct Answer

Two mechanics are **cohort-agnostic table-stakes**, three are **cohort-specific**, and the
split itself is the design finding.

**Cohort-agnostic (near-constant across every cohort):**

1. **Cash-pay is the rail; insurance billing is the exception.** Only **5 of 54** brands
   bill insurance (`joinfound, lifemd, nurx, onemedical, ro`) [C1]. Every cohort is
   dominated by cash-pay / HSA-FSA-eligible pricing. "We don't take insurance" is not a
   GLP-1 thing — it is the DTC-telehealth default.
2. **Compounding capability is table-stakes; FDA-brand-only is vanishingly rare.**
   `compounding_posture: both` dominates **every** cohort (GLP-1 15/19, TRT 6/8, longevity
   5/8, sexual-health 2/3, multi/none 8/10); only **2 of 54** are `FDA-brand-only`
   (`nurx, onemedical`) [C2]. Offering a compounded option is the price of entry across
   conditions; `compounded-only` (regulatory-exposed) is a meaningful minority that
   **clusters in GLP-1** (4 brands) but appears in every cohort.

   *Coherent outlier finding:* the two FDA-brand-only brands (`nurx, onemedical`) are also
   2 of the 5 insurance-billers [C1][C2]. The exceptions on both "agnostic" axes are **the
   same brands** — the insurance-taking, FDA-only "real clinic" model (One Medical, Nurx)
   sitting inside an otherwise cash-pay / compounding-capable DTC store.

**Cohort-specific (varies by cohort, and the variation tracks the condition's clinical
shape, not brand taste):**

3. **Modality is a cohort property, not a brand choice.** The sharpest contrast in the
   data: **TRT is 0/8 async, 2/8 hybrid, 6/8 sync**; **GLP-1 is 12/19 async, 5/19 hybrid,
   2/19 sync** [C3].
   TRT requires bloodwork + dose titration → synchronous clinician contact; GLP-1 is
   protocol-driven → asynchronous intake. longevity/multi sit in between (mixed). You can
   predict a brand's modality better from its cohort than from anything brand-specific.
4. **The `membership-required` / `all-in` bundling wedge is cohort-shaped.** GLP-1 skews
   **all-in** (12/19 — one bundled price hides the drug-vs-service split); TRT, longevity,
   and multi/none skew **à-la-carte/both + membership-required** [C4]. (`membership-required`
   is the stored enum value; abbreviated "membership" in the count tables below.) The "where does the
   recurring charge live" wedge is set by the cohort's offer logic, not chosen freely.
5. **Audience is condition-determined.** TRT men-first (6/8), sexual-health men-only
   (3/3), longevity all-genders (8/8), GLP-1 all-genders (14/19) [C5]. `audience` is
   essentially a restatement of the condition.

**Price publication** (the 5th mechanic in the question) is **not resolved in this run**
— it lives as a per-SKU `Visibility` column in 66 `offerings.md` files, not a clean
frontmatter enum, and re-deriving it cross-cohort risks the re-derive-from-prose trap
(MRL-009/010). Prior single-cohort runs (000 GLP-1, 008 TRT, 013 sexual-health) each found
price-visibility **mixed within the cohort** — i.e., a brand property, not a cohort
property. Treated here as secondary/prior-run evidence, not re-verified. [C6]

**Design answer:** *No new cross-cohort primitive earns its keep.* See Market Pattern.

## Evidence Used

All evidence is store-local, derived from `telehealth.md` frontmatter captured 2026-06-04
→ 2026-06-18 (store clock). Source grade: **derived** from primary store State. See
`receipts/cross-cohort-structural-matrix.md`.

- **C1** — 5/54 brands `pay_model: bills insurance` (`joinfound, lifemd, nurx,
  onemedical, ro`); all other cohorts cash-pay/HSA-FSA-dominant. Receipt S1.
- **C2** — `compounding_posture`: 38/54 `both`, 12 `compounded-only`, **2** `FDA-brand-only`
  (`nurx, onemedical`), 1 OTC, 1 N/A. `compounded-only` by cohort: GLP-1 4, TRT 2,
  longevity 2, sexual-health 1, multi/none 1. Receipt S1.
- **C3** — modality: GLP-1 async 12 / hybrid 5 / sync 2; **TRT async 0 / hybrid 2 /
  sync 6**. Receipt S1.
- **C4** — access_model: GLP-1 all-in 12 / membership 4 / à-la-carte 3; TRT à-la-carte 3 /
  membership 3 / all-in 2; longevity à-la-carte 4 / membership 3 / per-visit 1; multi/none
  à-la-carte 7 / all-in 2 / membership 1. Receipt S1.
- **C5** — audience: TRT men-first 6/8; sexual-health men-only 3/3; longevity all-genders
  8/8; GLP-1 all-genders 14/19. Receipt S1.
- **C6** — price-publication NOT re-derived this run; prior-run secondary evidence
  (runs 000/008/013) that within-cohort price-visibility is mixed. Direction-finding /
  secondary; not decision-grade for this run.

## Companies Seen

54 brands with structured `telehealth.md` frontmatter, grouped by `anchor_category`:
**GLP-1** 19, **multi/none** 10, **longevity/NAD** 8, **TRT** 8, **sexual-health** 3,
**peptides** 2, and singletons **labs / womens-HRT / hair / primary-care** (1 each).
Cohort-level claims are made only for the five cohorts with n ≥ 3; peptides (n=2) and the
four singletons are reported as too thin to carry a cohort claim.

## Missing / Stale Coverage

- **Anchored-only denominator (MRL-001, 5th cohort sighting — now cross-cohort).** The
  per-cohort census is the *anchored* set (`anchor_category:` grep). Generalists that
  sell into a cohort without anchoring to it (LifeMD, Nurx, Wisp for GLP-1; etc.) are
  counted only under `multi/none`, so each cohort's n is a floor. The cohort-agnostic
  claims (C1/C2) are *strengthened* by this gap (the generalists are even more cash-pay /
  insurance-mixed), but the cohort-specific n's are partial.
- **81 store companies have no structured `telehealth.md`** (135 total − 54). Captures
  span 06-04 → 06-18; structural enums are the durable part, but front-door A/B changes
  could re-sort access/modality at the margin.
- **`pay_model: unclear` 7/54** and concentrated in longevity (3) and sexual-health (1) —
  the cash-pay claim is "not stated otherwise," reported as a captured value, not absence.

## Source Gaps

Price publication (C6) is the one question-mechanic left on secondary/prior-run footing.
A clean cross-cohort price-visibility read would need the 66 `offerings.md` `Visibility`
columns extracted and labeled — a heavier, prose-adjacent pass deliberately not run here
to stay bounded and avoid re-derivation error.

## External Completeness Check

Not performed — `store-only` by contract, and completeness is **not** load-bearing for
the design finding (the read's conclusion is "no new primitive," which a larger
denominator would only reinforce). The anchored-set partiality is named, not papered over.

## Market Pattern

**State (captured):** Across 54 brands, two structural mechanics are near-constant
(cash-pay rail; compounding-capable) and three vary by cohort in a way that tracks the
condition's clinical/regulatory shape (modality, bundling wedge, audience). [C1–C5]

**Judgment (labeled, tied to C1–C5):**

- **"Table-stakes" and "durable-State candidate" are in tension.** A mechanic reads as
  cohort-agnostic table-stakes *precisely because* it is near-constant across the store —
  and a near-constant field carries almost no discriminating information. Storing
  "telehealth DTC is cash-pay and compounding-capable" as durable cross-cohort State would
  be true-but-useless as a cut. So the cohort-agnostic mechanics **do not** earn a durable
  cross-cohort object.
- **The cohort-specific mechanics are already query-time-groupable.** Modality, bundling,
  and audience are captured per-brand and partition cleanly by `anchor_category` with a
  one-line grep (the MRL-002 State-read recipe, here run on a *cross-cohort* axis for the
  first time). They don't need a new primitive either — `query-time-grouping-enough`
  holds across cohorts, not just within one.
- **The genuinely reusable nugget is interpretive, not structural:** a cohort's *condition*
  predicts its modality and bundling better than any brand attribute (TRT→sync→labs;
  GLP-1→async→compounded). That is a *Judgment pattern* a strategist can carry, not a field
  to store.

**Design-test outcome: no new cross-cohort primitive needed.** The cross-cohort axis's
contribution is the meta-finding above, plus a 5th-cohort confirmation of the anchored-only
denominator caveat — now demonstrated to bite *cross-cohort*, not just within a cohort.

## What Would Change This Answer

- A cohort-agnostic mechanic that is **near-constant *and* high-stakes to query** (e.g., a
  binary regulatory-exposure flag that consumers filter on constantly) could justify
  promoting it to a first-class field even at low entropy — but `compounding_posture`
  already *is* that field, captured per-brand, so even this resolves to "already have it."
- If price-publication, fully re-derived cross-cohort, turned out to be a **cohort**
  property (not the brand property prior runs found), that would be a new cohort-agnostic-vs-
  specific data point worth a durable note. Current evidence (C6) says brand property.
- A second cross-cohort read finding the *same* "near-constant ⇒ low-information ⇒ don't
  store" tension on a different field family would harden this from a one-run Judgment into
  a documented persistence-boundary heuristic for MRL-002.
