# Market Read

## Question

Across the captured telehealth store, what does each brand disclose about geographic /
US-state availability (serves all 50 states, names specific exclusions/limits, or is
silent), and can the store answer **"can I get this in my state?"** at all — or is
availability a structural gap?

## Result

**Gap-probe verdict: the store cannot answer "can I get this in my state?" as a query
for any brand — and the honest reason is not thin coverage, it is grain mismatch.**
Geographic availability is **not** one of the telehealth cohort's 8 structured cuts
(`value_chain_role`, `pharmacy_model`, `audience`, `compounding_posture`,
`anchor_category`, `modality`, `access_model`, `pay_model`). It survives only as
**scattered, unevenly-graded prose** in `telehealth.md` bodies and `profile.md`
Overview / `site_notes` / `unverified_fields`. (C1)

The load-bearing finding is **grain**, not absence. The 54 cohort brands partition
exactly (9 + 2 + 8 + 6 + 29 = 54):

- **9 brands carry decision-grade patient-availability disclosure** — a named state
  exclusion or an enumerated state-count limit. But each is at a *different grain*:
  - **Per-SKU exclusion** — joiandblokes: testosterone cypionate **cannot ship to 16
    states** (AL/AR/CT/DE/GA/HI/LA/MN/MO/MS/NC/ND/OK/PA/RI/SC); the brand's other lines
    are unrestricted. (C2)
  - **Per-line split** — vitalityrx: the **Rx Reboot Program is limited to 25 named
    states** (AL, AZ, CA, CO, CT, FL, GA, IL, IN, MD, MI, MN, MT, NJ, NY, NC, OH, OK,
    PA, SC, TN, TX, VT, VA, WI) while the at-home test kit ships all 50. (C3)
    henrymeds: KYZATREX oral TRT **"not available in California"** while the rest of the
    catalog is not so flagged (+ CA-specific compounding-test shipping delay). (C4)
    marekhealth: diagnostics **"not available in NY/NJ/RI"**, "Guided Optimization in
    all 50 states (specific treatments/diagnostics state-limited)." (C5)
  - **Per-program (audience × state) split** — hevahealth: **men's programs 45 states,
    women's-with-testosterone 30 states, women's-without-testosterone all 50** — the
    same brand's coverage varies by *which program and which audience*. (C5a)
  - **Per-brand exclusion** — trtnation: every US state **except AL, AK, AR, MO, HI**;
    struthealth: all states **except Arkansas** ("as of Sept 2024"); bluechew: all US
    **except North Dakota** (+ no territories: Guam/PR/USVI); niagenplus: at-home Rx kit
    **not shipped to AL, CA, IA, MA, TX, WA, WV** (7-state exclusion, re-confirmed
    2026-06-16). (C6)
- **2 brands carry a real but un-enumerated limit** — defymedical ("licensed to
  prescribe in **most** US states"); kingsbergmedical ("services are available **only
  where the physicians are licensed**"). Honest, but unqueryable. (C7)
- **8 brands carry only a brand-level "all 50 states" claim** — goodlifemeds, hims,
  invigormedical ("50 States Licensed"), joinamble, lifemd, malemd, hellowisp, eden.
  This is **marketing boilerplate, not verified per-product coverage** (see Market
  Pattern). (C8)
- **6 brands' "nationwide / 50-state" language describes a *sub-component*, not the
  buyable program** — hellopepti, hormonemd, maximustribe (labs); hydramed ("Chief
  Medical Director licensed in 13 states") (clinician licensure); ro-co, directmeds
  (pharmacy fulfillment). Reading these as patient state-availability would be a category
  error. (C9)
- **The remaining 29 brands are silent on geography** in captured pages — correctly
  read as **not-found, not "available everywhere."** (C10)

So even the 9 best-disclosing brands cannot be joined into one "available in {state}"
answer, because the splits are *within* a brand: joiandblokes (per-SKU), vitalityrx /
henrymeds / marek (per-line), and hevahealth (per-program/audience) all make availability
a **product × state** (or even audience × state) fact, not a **brand × state** fact. The
same brand is 50-state for one line and 16-/25-/30-state-restricted for another. And the
hard exclusions are **not random** — they cluster on controlled-substance / compounded
lines (testosterone, KYZATREX, compounded Rx) whose state availability tracks shifting
state pharmacy and controlled-substance law, not a brand business choice (S1).

## Gap Map

| Sub-question | Did the store answer? | Evidence / why not |
|---|---|---|
| Is geographic availability a structured cut? | **No** | Not among the 8 telehealth cuts; no `available_states`/`service_area` field anywhere in SCHEMA/TAXONOMIES. (C1) |
| Can I filter brands by "serves my state"? | **No** | Sparse prose at 4 mismatched grains (per-SKU / per-line / per-program / per-brand) + sub-component noise; 29 silent. |
| For a brand with a real limit, is the limit captured verbatim? | **Yes, where disclosed (9 brands)** | joiandblokes 16 states, vitalityrx 25 states, hevahealth 45/30/50 per-program, niagenplus 7-state exclusion, trtnation 5-state exclusion, struthealth/bluechew single-state exclusion all captured verbatim with source pages. (C2–C6) |
| Is "all 50 states" trustworthy as coverage? | **No** | It is brand-claim State, not verified truth; often describes clinician licensure or pharmacy reach, not the Rx program; co-exists with undisclosed per-line state limits. (C8, C9) |
| Did the store flag its own availability gap? | **Yes (one brand)** | henrymeds `unverified_fields`: *"site says 'one of the states we support' but does not enumerate a list."* The store recorded the gap honestly rather than inventing a list. (C4) |
| What grain is the *right* answer? | **Product × state, point-in-time** | The decision-grade question is per-line and time-varying (controlled-substance state law, brand expansion), so a brand-level field would be false-precise. |

## Evidence Used

All store-only; no external sources. Citations are local paths + store capture clocks
(the profile/cohort-pack capture dates). Claims are **captured brand State (claims),
not verified truth** — a site saying "all 50 states" is recorded, never adjudicated.

| ID | Claim | Source (local) | Grade |
|---|---|---|---|
| C1 | Availability is not one of the 8 telehealth cuts; no geo field in schema | `SCHEMA.md`, `modules/cohort-packs/TELEHEALTH.md`, all `store/*/telehealth.md` | primary (store contract) |
| C2 | joiandblokes testosterone cannot ship to 16 named states | `store/joiandblokes-com/telehealth.md:26` | primary (page-attested claim) |
| C3 | vitalityrx Rx program limited to 25 named states; kit all 50 | `store/vitalityrx-com/profile.md:20,66,73`, `telehealth.md:26` | primary |
| C4 | henrymeds KYZATREX not available in CA; no enumerated state list | `store/henrymeds-com/profile.md:33,68,76` | primary |
| C5 | marekhealth diagnostics not in NY/NJ/RI; treatments state-limited | `store/marekhealth-com/telehealth.md:19,30` | primary |
| C5a | hevahealth per-program/audience state split: men's 45 / women's-with-T 30 / women's-without-T 50 | `store/hevahealth-com/telehealth.md:34` | primary |
| C6 | trtnation excl. AL/AK/AR/MO/HI; struthealth excl. AR; bluechew excl. ND; niagenplus at-home kit excl. AL/CA/IA/MA/TX/WA/WV | `store/trtnation-com/profile.md:65`, `store/struthealth-com/profile.md:125`, `store/bluechew-com/profile.md:85`, `store/niagenplus-com/profile.md:22,81` | primary |
| C7 | defymedical "most US states"; kingsbergmedical "where physicians licensed" | `store/defymedical-com/profile.md:76`, `store/kingsbergmedical-com/profile.md:54` | primary |
| C8 | 8 brands carry only brand-level "all 50 states" boilerplate | `telehealth.md`/`profile.md` for goodlifemeds, hims, invigormedical, joinamble, lifemd, malemd, hellowisp, eden | primary (claims) |
| C9 | 6 brands' "nationwide/50-state" is a sub-component (labs/pharmacy/clinician), not the Rx program | `telehealth.md` for hellopepti, hormonemd, maximustribe, hydramed, ro-co, directmeds | primary |
| C10 | 29 brands silent on geography in captured pages | absence across `store/*/{telehealth,profile}.md` | not-found (absence) |

## Companies Seen

54 telehealth-cohort brands (carry `telehealth.md`): agelessrx, bluechew, brellohealth,
defymedical, directmeds, eden-health, effecty, functionhealth, gethealthspan, getopt,
getpetermd, gogeviti, goodlifemeds, hellopepti, hellowisp, henrymeds, hevahealth, hims,
home-medvi, honehealth, hormonemd, hydramed, innerbalance, invigormedical, ivimhealth,
ivyrx, joiandblokes, joinamble, joinfound, joinfridays, keeps, kingsbergmedical, lifemd,
malemd, marekhealth, maximustribe, mydrhank, mylifeforce, niagenplus, noom, nurx,
onemedical, prohealth, remedymeds, rexmd, ro, rugiet, sermorelin, struthealth, telolife,
trtnation, truniagen, tryshed, vitalityrx.

## Missing / Stale Coverage

- **No structural availability surface.** Even where a brand publishes a state list
  on-site (wisp's `/provider-credentials` lists per-state license numbers; vitalityrx
  enumerates its 25 states), the store holds only a prose mention, not a queryable list.
  This is a **depth-backfill candidate at the per-line grain**, *not* a frontmatter-field
  candidate (see persistence-boundary in Market Pattern).
- **Staleness risk is high and intrinsic.** struthealth's exclusion is explicitly dated
  ("as of Sept 2024"); controlled-substance state availability (joiandblokes,
  henrymeds, trtnation) tracks shifting state pharmacy law and brand expansion. Any
  captured state list is point-in-time by nature.
- **No write-back proposed** — this is informational; capturing availability lists would
  be a `/deepen-offerings`-class per-brand effort and a TAXONOMIES question, both
  human-gated.

## Source Gaps

- The decision-grade source for "can I get X in my state" is each brand's **own
  eligibility/checkout state-gate or `/provider-credentials` page** — a per-brand live
  surface the store does not capture at list grain. Verifying real coverage would need a
  per-brand live sweep across 54 brands (far beyond a light bounded-live ceiling), so
  store-only is the honest scope for *mapping the gap*; it cannot *fill* it.
- No external denominator was needed: this is a calibration of the store's own surface,
  not a market-membership question.

## Raw Learning to Preserve

For Loop 2 to append to `discovery-ledger.md`. Run-notes Discovery ledger IDs:
`O1` (grain-mismatch / product×state), `O2` ("all 50 states" boilerplate confound),
`O3` (sub-component vs program "nationwide" confound), `O4` (store self-flagged the gap,
henrymeds), `G1` (availability not a captured surface), `W1` (per-line availability would
be the right depth grain if anything), `S1` (controlled-substance lines drive the only
hard state exclusions).

## External Completeness Check

Not run — completeness of a market denominator is not load-bearing for a gap-probe about
the store's *own* availability surface. The 54-brand cohort is the denominator and is
treated as the captured cohort, not the market (corpus selection bias per MRL-001 still
bounds any generalization to "telehealth").

## Market Pattern

Three patterns, all labeled Judgments tied to the State above:

1. **"Can I get this in my state?" is a product × state question, not a brand × state
   one.** The only hard, enumerated exclusions in the entire store attach to specific
   **controlled-substance or compounded lines** (joiandblokes testosterone, henrymeds
   KYZATREX, vitalityrx's compounded Rx, trtnation TRT), while the same brands' other
   lines are unrestricted. A brand-level `available_states` field would be **false-
   precise** — it would force one answer onto a brand that has several. (Judgment ← C2–C6)

2. **"All 50 states" is a confound, two ways** (a clean MRL-008 flavor). (a) It is
   *brand-claim State, not verified coverage* — recorded, never adjudicated. (b) For
   ~half the brands that say it, the phrase actually scopes a **sub-component** —
   clinician licensure ("400+ providers in all 50 states"), a pharmacy network ("service
   to all 50 states"), or lab draw ("at-home testing in all 50 states") — **not** the
   buyable Rx program, whose real state-availability is undisclosed. A naive reader who
   tallied "50 states" mentions would over-count national availability and miss that
   controlled-substance lines almost certainly face undisclosed state limits. (Judgment
   ← C8, C9)

3. **The store's honest posture is the right one.** henrymeds' `unverified_fields` note
   — *the site doesn't enumerate its states* — is the model behavior: record the claim,
   flag the gap, don't invent a list. The gap is a **capture-depth + intrinsic-staleness**
   property, not a schema defect. **No new primitive is needed**; if anything graduates,
   it is a per-line availability *depth-backfill* (quote the verbatim state list/exclusion
   on the offering line, dated), never a brand-level field or a stored service-area
   object — that would rot and would lie about multi-line brands. (Judgment ← C1, C4, and
   the persistence-boundary reasoning)

## What Would Change This Answer

- A brand-level `available_states` frontmatter field **would not** improve this — it would
  encode a false grain. Only a **per-offering-line** verbatim availability note (dated)
  would, and even that is volatile.
- If a future read found a *second* cohort where availability splits the same way
  (controlled-substance lines state-limited, everything else national), it would harden
  "availability is a per-line, controlled-substance-driven property" from a one-cohort
  Judgment into a documented depth-backfill rule.
- A bounded-live or `/deepen-offerings` sweep of the 9 disclosing brands' own
  eligibility-gate pages would convert prose mentions into queryable lists — but that is
  human-gated (per-brand spend + a TAXONOMIES decision) and out of scope here.

---

*Loop-2 correction (2026-06-20): the evidence verifier reclassified **hevahealth**
(per-program 45/30/50-state split, `telehealth.md:34`) and **niagenplus** (at-home Rx kit
excludes AL/CA/IA/MA/TX/WA/WV, `profile.md:22,81`) from the sub-component bucket into
decision-grade — they carry real per-program state exclusions. Counts updated: decision-
grade 7→9, sub-component (C9) 8→6, buckets now sum exactly to 54 (9+2+8+6+29). The fix
strengthens the core finding — hevahealth adds an audience×state sub-flavor.*
