# Market Read

## Question

For **Hone Health** as the anchor brand, who are its true **substitutes** (same job-to-be-done)
versus **adjacent peers** (overlapping offerings but a different core job), and what captured
store evidence surfaces make that substitute-vs-adjacent distinction knowable?

## Direct Answer

**Anchor job-to-be-done (Hone).** From `store/honehealth-com/profile.md` (C0): Hone's core job is
*"diagnose my hormones/healthspan with a biomarker lab panel, then put me on a physician-supervised,
membership-based optimization protocol spanning hormones + longevity + adjacent lines, for either
sex."* The load-bearing mechanics: **biomarker panel is the wedge** (~every journey starts at a $65
biomarker test; panel size is stated inconsistently as 40+ vs 50+ across pages — an A/B/copy
artifact per `profile.md`, not load-bearing here), **physician-led membership** care model, **multi-line breadth** (hormones,
weight, longevity, sexual health, thyroid, heart, hair), **both sexes**, **longevity/healthspan
framing** ("Longevity engineered around your biology").

**The substitute test used:** a brand is a **substitute** if a Hone shopper would genuinely
cross-shop it for that same *lab/physician-led hormone-and/or-healthspan optimization* job — not
merely if its catalog overlaps. A brand is **adjacent** if it overlaps on a *component* of Hone's
bundle (diagnostics-only, a single longevity ingredient, or a single-mechanism TRT alternative) but
sells a different core job.

**Result — three tiers (16 captured neighbors):**

**Tier 1 — True substitutes (broad, lab/physician-led optimization; a Hone shopper cross-shops).**
Closeness to Hone, head-to-head: **mylifeforce** (closest mirror — same panel wedge + both-sex +
longevity) > **gogeviti** (diagnostic-led, both-sex) > **gethealthspan** (both-sex longevity, but
protocol/molecule-led wedge not a panel) > **defymedical** (broadest clinical hormone alternative, but
less longevity-branded):**
- **mylifeforce-com** (C2) — closest mirror: "America's largest longevity medicine program," **50+
  biomarker diagnostic wedge**, sync consult, both sexes (men Testosterone + women Menopause),
  membership, longevity-framed. Same wedge, same breadth, both sexes.
- **gogeviti-com** (C3) — "we map your body / longevity," **data-first diagnostic intake**, both
  sexes, hybrid, longevity front door over hormone protocols. Same diagnostic-led optimization job.
- **gethealthspan-com** (C4) — "1st digital longevity clinic," parallel men's + women's hormone
  health + longevity (rapamycin/senescence), async. Same job; wedge is protocol/molecule-led rather
  than a panel (a within-substitute variation, not an adjacency).
- **defymedical-com** (C5) — "World's Leading Hormone Replacement Clinic," men-first **+ full
  women's line**, broad hormone optimization, sync + Tampa in-person. Broad hormone-clinic
  substitute; less longevity-branded, more clinical.

**Tier 2 — Substitutes for the *male hormone-optimization* buyer only (TRT-anchored, optimization-
framed, men-first; narrower than Hone's both-sex/longevity job):**
- **getopt-com** (C6) — TRT "wrapped in a longevity/optimization frame," men-first.
- **marekhealth-com** (C7) — TRT, **labs-first 2026 redesign** (870 ng/dL hero biomarker), men-first
  but male/female panels. Lab-led — closest Tier-2 to Hone's wedge.
- **maximustribe-com** (C8) — "next-generation testosterone optimization," men-first → now both.
- **getpetermd-com** (C9) — TRT founding line + "For Her" women's line, hybrid.
- **hormonemd-com** (C10) — TRT, both sexes, sync, cash-pay.
- **trtnation-com** (C11) — TRT namesake ("#1 in the nation $99/mo"), men-first, adds weight-loss +
  labs lines. Borderline Tier-2/3: single-vertical-led but broadening.

These are substitutes *for the male buyer who wants T optimization* but **adjacent** for the buyer
Hone explicitly courts (both-sexes, longevity-platform, diagnostics-first). The distinction is the
buyer's job, not the catalog.

**Tier 3 — Adjacent peers (overlap a component; different core job):**
- **functionhealth-com** (C12) — **labs anchor** ("160+ lab tests, $365/yr"), *no gating consult; no
  Rx hormone/optimization prescriptions — testing + clinician result-review only* (it does deliver a
  reviewed "personalized protocol," but stops short of prescribing the medications Hone's job centers
  on). Shares Hone's **diagnostic wedge** but the job is "comprehensive testing/tracking," not "put me
  on Rx treatment." This is the single cleanest adjacency: it is the diagnostic layer Hone bundles,
  sold standalone.
- **vitalityrx-com** (C13) — "A Smarter Alternative To TRT" (**enclomiphene, not exogenous T**),
  **men-only**. Single-mechanism, fertility-preserving — overlaps the male-hormone shopper but the
  job is narrower ("raise T without TRT").
- **agelessrx-com** (C14) — longevity-**Rx** (rapamycin/NAD/metformin), all-genders, **no biomarker-
  panel wedge, no hormone flagship**. Job is "buy longevity prescriptions," not lab-led hormone
  optimization.
- **prohealth-com** (C15) — NMN/NAD+ **supplement** hero + secondary GLP-1/pharma. Supplement-led
  longevity.
- **niagenplus-com** (C16) / **truniagen-com** (C17) — **single-ingredient NAD+ precursor**
  sellers; truniagen is straight **OTC e-commerce (no clinician gating)**. They sell one longevity
  *ingredient*, not an optimization service — the weakest peers; truniagen is barely a peer at all.

**Design finding — what makes the split knowable, and is a primitive warranted?**
- **Enumerating** the neighbor set is cheap and store-native: `anchor_category ∈ {TRT, longevity/NAD,
  labs}` grep returns the candidate field in one pass (C1).
- **The substitute-vs-adjacent *judgment* is NOT derivable from frontmatter enums.** `anchor_category`
  alone lumps every TRT brand as equivalent — it would rank single-mechanism **vitalityrx**
  (adjacent) identically to broad **defymedical** (substitute), and would miss that **functionhealth**
  (`anchor_category: labs`) is adjacent-not-substitute despite sharing Hone's exact diagnostic wedge.
  The discriminator is the **positioning/wedge prose + a stated buyer job**: *is the lab panel the
  front door? is it optimization-framed (broad) or fix-one-thing (narrow)? both sexes or men-only?*
  Those are captured in `telehealth.md` positioning comments and `profile.md` prose, but as
  **judgment inputs, not enum values**.
- **Conclusion: query-time grouping + a job-criterion judgment is enough; no durable
  `competitors:`/`similar_to:` primitive is warranted from one read.** And the read shows *why* such a
  primitive would be hard if it ever graduated: it could not be auto-derived from `anchor_category`
  (necessary but not sufficient) — the substitute/adjacent line is a per-anchor positioning judgment,
  and "substitute" is even **buyer-relative** (Tier 2 flips between substitute and adjacent depending
  on which Hone buyer you mean). This is a *relation-as-judgment* signal, distinct from the backend
  *relation-as-fact* edges in MRL-005/006.

## Evidence Used

All store-only; no external sources, no spend. Source grade = captured State (firecrawl). Store
clocks 2026-05-31 → 2026-06-18 (all fresh). Judgments (tiering, job criterion) are labeled and tie
back to the cited State below.

| ID | Claim | Source | Grade |
|---|---|---|---|
| C0 | Hone's job/mechanics: biomarker-panel wedge, physician membership, multi-line, both sexes, longevity-framed | `store/honehealth-com/profile.md` (captured_at 2026-06-18) | State |
| C1 | Candidate neighbor field = `anchor_category ∈ {TRT, longevity/NAD, labs}` | `grep ^anchor_category store/*/telehealth.md` | State (derived) |
| C2 | mylifeforce: longevity program, 50+ biomarker wedge, sync, both sexes | `store/mylifeforce-com/telehealth.md` (2026-06-04) | State |
| C3 | gogeviti: data-first diagnostic intake, both sexes, longevity front door | `store/gogeviti-com/telehealth.md` (2026-06-04) | State |
| C4 | gethealthspan: 1st digital longevity clinic, parallel M/W hormone health, async | `store/gethealthspan-com/telehealth.md` (2026-06-04) | State |
| C5 | defymedical: "World's Leading HRT Clinic," men-first + full women's, sync + in-person | `store/defymedical-com/telehealth.md` (2026-06-04) | State |
| C6 | getopt: TRT in a longevity/optimization frame, men-first | `store/getopt-com/telehealth.md` (2026-06-04) | State |
| C7 | marekhealth: TRT, labs-first 2026 redesign, men-first w/ male+female panels | `store/marekhealth-com/telehealth.md` (2026-06-04) | State |
| C8 | maximustribe: "next-gen testosterone optimization," men-first→both | `store/maximustribe-com/telehealth.md` (2026-06-04) | State |
| C9 | getpetermd: TRT founding line + "For Her," hybrid | `store/getpetermd-com/telehealth.md` (2026-06-04) | State |
| C10 | hormonemd: TRT, both sexes, sync, cash-pay | `store/hormonemd-com/telehealth.md` (2026-06-04) | State |
| C11 | trtnation: TRT namesake men-first, adds weight-loss + labs | `store/trtnation-com/telehealth.md` (2026-06-04) | State |
| C12 | functionhealth: labs anchor, no gating consult, no Rx prescribing (testing + result-review only) | `store/functionhealth-com/telehealth.md` (2026-06-01) | State |
| C13 | vitalityrx: enclomiphene "alternative to TRT," men-only | `store/vitalityrx-com/telehealth.md` (2026-06-04) | State |
| C14 | agelessrx: longevity-Rx (rapamycin/NAD/metformin), no panel wedge, no hormone flagship | `store/agelessrx-com/telehealth.md` (2026-05-31) | State |
| C15 | prohealth: NMN/NAD+ supplement hero + secondary GLP-1/pharma | `store/prohealth-com/telehealth.md` (2026-06-07) | State |
| C16 | niagenplus: single-ingredient NAD+ precursor (Niagen), async intake | `store/niagenplus-com/telehealth.md` (2026-06-04) | State |
| C17 | truniagen: single-ingredient NAD+ (Niagen), OTC e-commerce, no clinician | `store/truniagen-com/telehealth.md` (2026-06-16) | State |

## Companies Seen

17 captured brands total: Hone (anchor) + 16 candidate neighbors across TRT (8), longevity/NAD (7),
labs (1). Tiering above. Hone itself is `anchor_category: longevity/NAD` in `telehealth.md` (matching
its longevity front-door positioning) while `profile.md` describes the multi-line hormone+longevity
breadth — so the anchor sits at the TRT↔longevity straddle, exactly where substitute/adjacent
boundaries are most contested.

## Missing / Stale Coverage

- **Anchored-only floor (MRL-001).** The candidate field is the *anchored* TRT/longevity/labs set.
  **Generalists that sell hormone or longevity lines without anchoring to them are silently excluded**
  — e.g. multi/none brands and any GLP-1/primary-care generalist with a hormone module. The neighbor
  set is a **floor, not Hone's full competitive universe**.
- All captures are fresh (2026-05-31 → 06-18); no staleness concern this run.
- Per-SKU offering overlap was read at the line level (profile/telehealth frontmatter + positioning
  comments), not SKU-by-SKU from each `offerings.md`. Sufficient for a substitute/adjacent *job*
  judgment; not a catalog-overlap census.

## Source Gaps

- **No demand-side evidence.** "Would a buyer actually cross-shop these" is inferred from positioning
  State, not from search co-occurrence, owned "vs" pages, or review/forum mentions. A bounded-live
  Exa-neighbor / "alternatives to Hone" SERP panel would convert the substitute judgment from
  *supply-side positioning inference* to *demand-side corroboration*. (Deliberately out of scope:
  store-only contract.)
- **Buyer-relativity is unresolved by State alone.** Tier 2's substitute/adjacent status depends on
  which Hone buyer (male-T vs both-sex-longevity) — State can't pick the buyer; the reader must.

## External Completeness Check

Not run (store-only contract). The load-bearing completeness caveat is the anchored-only floor above,
not an external denominator reconciliation — this read is about *classifying* a neighbor set, not
proving the set is exhaustive. Flagged rather than silently closed.

## Market Pattern

The men's-hormone/longevity field stratifies by **how much of Hone's bundle a brand reproduces**:
(1) a **broad lab-led optimization** core (mylifeforce/gogeviti/gethealthspan/defymedical) that
genuinely substitutes; (2) a dense **TRT-optimization** middle (getopt/marek/maximus/petermd/
hormonemd/trtnation) that substitutes only for the male-T buyer; and (3) **unbundled components** —
diagnostics-only (functionhealth), single-mechanism T (vitalityrx), longevity-Rx (agelessrx), and
NAD+ supplements (prohealth/niagenplus/truniagen) — that are adjacent. Hone's defensibility read:
its moat is the **bundle** (panel + physician + breadth + both sexes), since each *component* is
attacked by a focused adjacent player, but few brands reproduce the whole bundle (only Tier 1).

## What Would Change This Answer

- A bounded-live demand-side panel (Exa neighbors / "alternatives to Hone" listicles / owned "vs"
  pages) naming a different cross-shop set — especially if it surfaces generalists the anchored-only
  grep missed (MRL-001 floor), which would *expand* Tier 1/2.
- Re-capturing the multi/none generalists' hormone modules to test how many un-anchored brands belong
  in the neighbor set (the floor's size is the biggest uncertainty).
- A different stated buyer job (e.g. "menopause-first woman") would re-rank the tiers — the
  substitute set is buyer-relative, so the answer is contingent on the job, not absolute.
