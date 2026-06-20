# Market Read Lab Triage

**Status**: Active.

**Priorities**: `P0`, `P1`, `P2`, `P3`, `Low`, `Out-of-scope`.

**Statuses**: `Submitted`, `Researching`, `Acknowledged`, `Duplicated`, `Resolved`.

## Operating Convention

Run agents are additive. They may submit new candidates or append dated **Evidence Log**
entries to existing items, but should not rewrite canonical item state.

The triage steward curates. On periodic passes, the steward may update priority/status,
reorder the Queue, merge duplicates, and rewrite `title`, `evidence_summary`, or
`proposed_next_step` so each item reflects the current best framing.

Actual graduation into Truffle system changes remains human-gated.

## Item Template

```yaml
id:
title:
priority:
status:
created_from_run:
created_from_review:
area:
evidence_summary:
proposed_next_step:
linked_items:
```

Use the YAML block as the canonical item state. If a run adds evidence or color,
append a short dated **Evidence Log** under the item instead of adding new YAML keys.
The steward can later fold recurring evidence into the canonical YAML summary.

Never touch or add **Human Notes**. That's only for Brian / humans.

## Steward Pass Log

- **2026-06-19:** Folded recurring evidence into current `evidence_summary` fields, reclassified accepted pressure to `Acknowledged`, fixed missing `MRL-009` heading, and kept graduation as human-gated. No `Human Notes` touched.

---

## Queue

### MRL-002 - Market-read query recipes for State and Signals reads

```yaml
id: MRL-002
title: Market-read query recipes for State and Signals reads
priority: P1
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: operator-observation
area: query
evidence_summary: Six reviewed runs now show recurring in-run query machinery. Runs 000/001/004 hand-built State-read patterns for entity-set union, relation grep, and category grouping. Runs 005/006/007 hand-built the same Signals-read pattern across Trustpilot, Wayback, and SEC-EDGAR captures - latest-per-dir, field extraction, integrity/confound sibling fields, and frontmatter joins. The pressure has crossed from watch to acknowledged recipe need; still docs/recipe level, not a helper script or stored taxonomy.
proposed_next_step: Candidate for human-approved graduation - add lightweight QUERYING recipes for category grouping and Signals reads. Keep them pattern-level with anti-footguns, captured-floor language, latest-per-dir idiom, and confound-sibling rule. Do not build a helper or entity-resolution table.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/operator-observation-latency.md
  - runs/001-2026-06-19-mens-health-backend-relations/run-notes.md
  - runs/004-2026-06-19-scout-candidates/run-notes.md
  - runs/005-2026-06-19-trustpilot-signals-reputation-landscape/run-notes.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
```

**Human Notes**
- **2026-06-19**: [Brian] After run 004, I decided to upgrade the priority to P1. 

**Evidence Log**

- **2026-06-19 · State-read recurrence:** Runs 000/001/004 each reinvented a different store-query surface in-run. The shared pressure is a documented query recipe layer, not a hard-coded GLP-1 helper or stored per-SKU category taxonomy.
- **2026-06-19 · Signals-read trigger met:** Runs 005/006/007 repeated the same raw Signals consumption loop across three signal grains. This earns a human look at a QUERYING signals-read recipe; the SEC CIK collision stays only a watch item unless a second cross-domain issuer collision appears.
- **2026-06-19 · State price-posture recipe recurred (run 008):** The TRT/hormone price-visibility read reused the exact State-read loop from run 000 (frontmatter grep → latest-capture + `offerings.md` `Visibility`-column extract → group/label), now on a second cohort. The recipe is "filter `telehealth.md` by `anchor_category`/`audience`, read the `Visibility` row per brand, label by business model." Confirms the *State* half of MRL-002 at recipe-level; still no helper script wanted.
- **2026-06-19 · State *positioning*-read recurrence + a field-fidelity guard (run 009):** The longevity/NAD positioning read extended the recipe family beyond pricing to a *positioning/credibility* surface — `anchor_category` grep → `Credibility & access` + `Notes` section read → supply↔diagnostic axis labeling. Same latest-capture + field-extract + group/label idiom, different captured surface. Loop 2's adversarial verifier caught **two field-read errors** (a "three of four" vs "four of four" Schedule-III count contradicted by the read's own table; gethealthspan's `access_model`/`Labs` re-derived from prose as "membership/required" when frontmatter says `à-la-carte/both` + `optional`). Both trace to *re-deriving fields from prose*. Adds a concrete guard to the recipe: **panel cells must quote frontmatter (`access_model`, `Labs:`) verbatim, never paraphrase from `Notes`.** Still recipe-level; no helper or stored taxonomy wanted.
- **2026-06-19 · State *offer-structure*-read recurrence + a prose-surface flavor (run 010):** The GLP-1 offer-ladder read (`anchor_category: GLP-1` grep → 19 brands → `site_notes`/Portfolio/Visibility-rule read → entry-offer/commitment/membership-wedge/price-visibility classification) is the **third** State-read surface, after price-posture (008, the `Visibility` *column*) and positioning (009, `access_model`/`Credibility` *frontmatter*). The new wrinkle: offer-structure attributes (billing cadence, upfront-multi-month, membership wedge) live in **narrative `site_notes` prose, not a greppable field** — extraction was read-prose-then-extract, not field-lookup. Loop 2's adversarial verifier re-checked 14 load-bearing sub-claims: **13 confirmed verbatim, 1 partial (the ≈9/≈7 split count, defensible), 0 contradicted** — 009's "quote, don't re-derive" guard held. Two refinements for the recipe: (a) a **prose-surface variant** — when the attribute isn't a discrete field, quote the sentence verbatim and label the interpretation as a Judgment cell; (b) an **ambiguous-cell flag** — when a classification overrides a brand's own surface signal (e.g., remedymeds' homepage "No Memberships" vs. its internal "membership" charge; tryshed/joinfound mixed lanes), say so. Still recipe-level; no helper or stored taxonomy wanted.
- **2026-06-19 · First *cross-cohort* axis + a persistence-boundary heuristic (run 015):** The State-read recipe (frontmatter grep → field-extract → group/label) was run on a **cross-cohort axis** for the first time — `group by anchor_category` across *all* cohorts in one pass over 54 brands — rather than within a single cohort. This is the **fifth State-read surface** after price-posture (008), positioning (009), offer-structure (010), and access-structure (013), and confirms the recipe family generalizes across the cohort axis with no new toil (one parse pass). The generalizable nugget is a **persistence-boundary heuristic**: a mechanic that is cohort-agnostic *because* near-constant (cash-pay 49/54; compounding-capable 52/54) is simultaneously a *poor* durable-State candidate — low entropy means a stored cross-cohort cut would be true-but-useless as a filter ("table-stakes ≠ durable-State candidate"). Loop 2's evidence verifier independently re-derived all five load-bearing counts with **zero factual discrepancies** (two cosmetic label-shortenings, fixed in `read.md`); State/Judgment boundary held cleanly at cross-cohort grain. **This is a one-run Judgment, not a documented rule** — a second cross-cohort read finding the same "near-constant ⇒ low-information ⇒ don't store" tension on a *different* field family would harden it into an MRL-002 sub-heuristic. Recipe-level only; no helper, no stored cross-cohort object wanted.
- **2026-06-19 · State *access-structure* read on discrete enum cells + a fill-rate sub-caveat (run 013):** The sexual-health access/identity map is the **fourth** State-read surface, after price-posture (008), positioning (009), and offer-structure (010). New flavor: the load-bearing cut is entirely **discrete enum frontmatter fields** (`pay_model`/`modality`/`compounding_posture`/`access_model`) rather than pricing prose or narrative `site_notes`. The "quote, don't re-derive" guard (009/010) was *trivially* satisfied — discrete cells have nothing to paraphrase; Loop 2's verifier confirmed all 30 scored cells across 6 brands verbatim-correct. The new, generalizable sub-caveat is the **fill-rate ceiling**: a structural read's confidence is bounded by `filled cells / total cells` for the load-bearing field, not by reasoning quality — here `pay_model` at ~67% (4/6; bluechew + keeps `unclear`) capped the access claim at 4/6 regardless of reasoning. Recipe addends: (a) report the fill-rate fraction for the load-bearing structural field; (b) `unclear` is a store-captured value, report it as such, not as absence. One verifier catch (now fixed in `read.md`): the cohort's `ED-tier` labels (origin/companion) came from *body* prose, not the `anchor_category` `#` comment, so the "all cells verbatim frontmatter" claim was overstated for that one descriptive column — relabeled as a hand-drawn Judgment. Still recipe-level; no helper or stored taxonomy wanted.

- **2026-06-20 · Relation/neighborhood flavor — recipe generalizes beyond attribute extraction (run 017):** The State-read recipe (anchor read → `anchor_category` grep → field/positioning extract → group/label) was applied for the first time to a **relation/neighborhood** operation rather than attribute extraction — building Hone Health's substitute/adjacent neighbor set. Enumeration was one grep (16 candidates); the substitute-vs-adjacent **tiering** was read-time judgment. Confirms the recipe family generalizes from the five attribute surfaces (price/positioning/offer/access/cross-cohort) to a *competitive-set* operation with no new toil. New wrinkle that lives in the new item MRL-011, not here: the classification is **not enum-derivable** (`anchor_category` is necessary but not sufficient) and is **buyer-relative**. Still recipe-level; no helper wanted.

- **2026-06-20 · First *orthogonal-axis* read — `audience` as the primary cut (run 019→020, watch):** The State-read recipe family was run, for the first time, with a **non-`anchor_category` enum as the primary axis**: run 020 cut all 54 telehealth brands by `audience` (men-only/men-first/women-only/women-first/all-genders) and cross-tabbed *against* `anchor_category`. Every prior State-read (008–019) organized *by* category — even cross-cohort run 015 still grouped by category. The generalizable signal: the MRL-002 family is **"clean-enum-primary-axis reads," not "category-reads only,"** and a *second* clean enum serves as the primary axis with no new toil (one parse pass; both fields are discrete enums so the "quote-don't-re-derive" guard is trivially satisfied, as in run 013). **Explicitly a watch, not a recipe addition** — one sighting of a two-enum cross-tab; do not brand it a surface-count milestone (counts rot). Hold for a 2nd audience-axis or two-enum cross-tab read before any QUERYING recipe graduates; no helper, no `audience_cluster` field, no persisted cohort object. The interesting new flavor lives mostly in MRL-001 (a selection-bias denominator); see that entry.

- **2026-06-20 · Sixth read surface = the `visual.md` layer, with a prose-grain twist (run 019):** First lab consumption of `visual.md` (the per-company visual-evidence layer) as a **cross-company** ingredient — the State/Judgment-read recipe family now spans a **sixth surface** after price-posture (008), positioning (009), offer-structure (010), access (013), cross-cohort (015), and competitive-set (017). New, generalizable wrinkle: on this layer the **aggregatable unit is prose, not a greppable field** — the cross-brand signal came from reading 34 `## Visual & brand impression` paragraphs and finding *independent convergence* on the same "owned-controlled core / borrowed-asset frays" language, whereas the structured `polarity`/`family` fields do **not** roll up (see MRL-008 entry below). So the recipe-if-recurs is an **impression-concatenation** shape — glob `visual.md` → pull `## Visual & brand impression` → join `anchor_category` — explicitly **not** a polarity-score rollup, a `visual_cluster:` field, or a durable cluster object. Two recipe addends: (a) **independent convergence** of separately-mined captures is the trust mechanism for a Judgment-dense layer (the miners didn't coordinate, so verbatim agreement is evidence the layer captures something real); (b) **anti-footgun** — pin the instance polarity vocab (strong/mixed/**poor**) and distinguish it from the parked-score vocab (`weak`, which appears only in `modules/VISUAL.md`'s scoring-history prose, never in instances); a first parse miscounted `weak`→0. The **no-score boundary held and was workable** — a brief-grade creative-director read was produced with zero score/grade/leaderboard, evidence the parked-scoring line is not a consumption blocker. Loop-2 evidence verifier reproduced the panel (34), polarity tally (485/366/148=999, 15% poor), depth spread (9–51), 6 verbatim impression quotes, and the anchor_category cross-tab clean; it caught one rationale error (the price-transparency decline was wrongly justified as "unparseable" — the `| Visibility |` column is parseable for all 34; re-framed in `read.md` as a decline on *scope*/not-well-formed grounds). Still recipe-level; **no new MRL item** (Loop-2 developer downgraded the run's proposed item — one sighting; absorbed here + MRL-008). Hold for a 2nd cross-brand visual read before any QUERYING recipe graduates.

- **2026-06-20 · Eighth read surface — cohort-pack credibility cut, with a quantified prose-classification polarity-error rate (run 021):** The trust/proof-device read aggregated the `telehealth.md` "Health-merchant credibility" + "Payment & commitment" prose lines (LegitScript / named-clinician / pharmacy-accreditation / commercial-trust flags) across 54 packs — the **eighth** State-read surface in this family (after price-posture/008, positioning/009, offer-structure/010, access/013, cross-cohort/015, competitive-set/017, visual-impression/019). Decisive finding: the cut already exists as an explicit `y`/`n`/`not-shown` checklist in cohort-pack prose, so the read was aggregation, not extraction — confirms `query-time-grouping-enough`. The new, quantified recipe sub-finding: the Loop-2 evidence verifier re-derived the five load-bearing device tallies and found **4 of 5 fell outside the read's own ±2–3 bar** (errors 4–9), the largest from positive-vs-negated **polarity** confusion on the LegitScript field (~9 over-counted positive: lines reading "…not shown / not observed" were counted as present). Extends the run-010 "quote, don't re-derive prose" guard with a sharper rule: **for a prose checklist where each cell carries an explicit `y`/`n`/`not-shown` flag, read the flag verbatim then tally — do not re-classify the cell from surrounding prose.** Still recipe-level; no helper or stored frontmatter field wanted (a `proof_devices:` promotion is one sighting — held as watch).

- **2026-06-20 · Second sighting of the *bounded-live external coverage-radar* recipe (run 022) — a distinct member of the read-recipe family:** Every MRL-002 entry so far (008–021) is a **store-only State-read** surface. Run 022 reuses run 012's **bounded-live** shape on a new category: SERP → ≥2 authoritative listicles → JSON-extract verbatim named sets → **cross-source intersection** → store **token-match diff**. Run 012 ran it on GLP-1 (U.S. News / Forbes); run 022 ran it identically on women's menopause/HRT (Everyday Health / Flow Space), and the cross-recurrence rule + affiliate-confound caveat held identically. This is structurally **distinct** from the store-only surfaces — it answers a *selection-bias* question (which the store cannot, see MRL-001 run-022 entry) by reaching outside the corpus. Two sightings earns **naming** the recipe shape (a bounded-live coverage-radar variant of the MRL-002 family); it does **not** earn building a helper or template — it is a few searches + 2 JSON scrapes + a grep. Recipe/pattern-level only; does not move the graduation clock. Pairs with the MRL-001 + MRL-009 run-022 entries.
- **2026-06-20 · A *normalization-rubric* read flavor — comparability as a query, not a field (run 023):** The GLP-1 price-comparability read is the first MRL-002 surface where the load-bearing output is a **normalization rubric** rather than a group/label cut. Across the 19 GLP-1-anchored brands, captured entry "prices" denominate ≥5 incommensurable things (all-in per-month / med-only-plus-mandatory-fee / dose-floor / cadence-disguised 3-mo-upfront / promo), so a verbatim sort is false confidence (Eden's `$99` headline → ~$198 effective once the mandatory $99 membership is added — *inverts* the naive ascending order). The generalizable recipe: a "comparable price" is reconstructed at **query time** over four axes — (1) what's-included via the existing `visibility: published/partial` flag, (2) billing cadence + commitment, (3) steady-state vs promo, (4) binding-price vs floor — all derivable from existing State (`visibility` + verbatim price string + `site_notes`). New nuance for the recipe: `visibility` is being read as a price-**completeness** gate, adjacent to its price-**transparency** origin, and `partial` spans both the fee-unbundle and dose-floor/conflict cases (so it is a comparability gate, not solely a "cost-on-top" marker). Friction worth folding in: GLP-1 price lives in ≥3 `offerings.md` surfaces (Roster `Price (verbatim)` row / `site_notes` prose / Verbatim-anchors block) — read per-file, prefer the `Price (verbatim)` + `Visibility` columns. Carries an **explicit anti-graduation flag:** do not persist a derived effective-monthly price field — it is point-in-time (8/19 prices are promo), judgment-laden (every axis collapse is a modeling choice), and would rot; the flag + verbatim string + query-time rubric is the lighter, truer substrate. Loop-2 evidence verifier spot-checked 5 brands' prices, the 6-brand fee count, and the derived-figure labeling against the files with all load-bearing claims surviving (two cosmetic imprecisions — a C5 over-read of `partial` and a directmeds same-SKU misquote — fixed in `read.md`/receipt). Recipe-level only; no helper, no field. Pairs with the MRL-008 run-023 entry.

- **2026-06-20 · Third sighting of the bounded-live coverage-radar recipe (run 024) — name it, don't build it:** The run-012 / run-022 shape ran identically on a **third lane** — behavioral/mental-health telehealth: SERP → ≥2 authoritative listicles (Forbes Health / Healthline) → JSON-extract verbatim named sets → cross-source intersection → token-match store diff. Stop rule fired after two listicles; 12 net Firecrawl credits; result maximally lopsided (5-brand cross-recurrence head, **0/5** captured; full union also store-absent). Three sightings across three maximally different verticals (GLP-1 / women's-menopause / behavioral) make the bounded-live coverage-radar a stable, **nameable** member of the read-recipe family — a QUERYING recipe at the level of "a few searches + 2 JSON scrapes + a token diff," **not** a helper, field, or stored object. One concrete new prerequisite surfaced this run (folds into MRL-008): filter the JSON-extracted named set to **care-delivery platforms only** (exclude payers/carriers) before taking the intersection. Loop-2 evidence verifier independently re-derived the store floor (0/54), the 0/135 directory diff, the strict S1∩S2 intersection (5), and the payer exclusion — overall PASS (one cosmetic receipt fix). Pairs with the MRL-001 + MRL-008 + MRL-009 run-024 entries. Recipe-level only; does not move a graduation clock.

### MRL-008 - Captured-signal source-rigor and confound convention

```yaml
id: MRL-008
title: Captured-signal source-rigor and confound convention
priority: P1
status: Acknowledged
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: run-notes; Loop 2 developer review (Dev Agent)
area: source-rigor
evidence_summary: Source-rigor pressure has matured from external snippet discipline into a broader Signals-consumption convention. Run 002 showed snippets/news are leads, not evidence for policy/pricing claims. Runs 005/006/007 then showed three captured Signal headline fields that mislead unless their integrity context travels with them - Trustpilot trust score needs paid-profile/review-volume flags, Wayback tenure days needs continuity/snapshot-density context, and SEC total hits needs match/vehicle/CIK/existence-only flags. The family is real, but the root causes differ, so the convention must name the confound flavor instead of flattening them.
proposed_next_step: Candidate for human-approved graduation - document a flavor-aware rule that headline Signal fields must travel with their integrity/confound siblings before a read uses confident language. Keep verdicts such as trusted, established, or funded as labeled Judgments. No monitor, score, or new schema yet.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - runs/005-2026-06-19-trustpilot-signals-reputation-landscape/run-notes.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
  - MRL-002
  - MRL-007
  - runs/012-2026-06-19-glp1-default-brand-leaderboard/run-notes.md
```

**Evidence Log**

- **2026-06-19 · External-current rigor:** Run 002 showed lazy news/snippet sourcing can make a store read overconfident. Primary URLs, capture dates, and source grade are required for current/news/policy/pricing claims.
- **2026-06-19 · Captured-signal confounds:** Runs 005/006/007 repeated the same consumer risk across different signal types. The headline field is captured correctly, but a naive read is wrong unless the confound/integrity fields are surfaced with it.
- **2026-06-19 · Review-score vs review-body confound flavor (run 011):** A new flavor within the Trustpilot family. The store captures the *headline Trustpilot score* in profile.md Credibility blocks (e.g., remedymeds "Excellent 4.7" badge) without the paid-subscription/invited-review/merged-profile integrity siblings — and without the review *bodies* the score obscures. A score-only read concludes remedymeds (4.6) is near-excellent and hims (3.0) is the trust problem; the bodies show remedymeds' dominant objection cluster is billing-after-cancel, structurally identical to hims'. The score gap reflects invitation posture, not a quality gap. Reinforces the flavor-aware rule: the headline Signal (score) and the decision-grade Signal (body) are different grains, and the store currently holds only the former. Pairs with the MRL-010 third sighting (same run).
- **2026-06-19 · Listicle-inclusion confound flavor (run 012):** Another flavor of the same family, on a *third-party named-set* signal. A single "best GLP-1 telehealth 2026" listicle reads as an objective ranking, but **inclusion and order are affiliate/SEO-driven** (both U.S. News and Forbes carry commission disclosures), and the *head is stable while the tail is bought* — low-authority affiliate pages name a wholly disjoint tail. The integrity sibling that must travel with listicle inclusion is **affiliate-disclosure + cross-source recurrence**: only a name appearing on ≥2 *authoritative* sources (Mochi, here) is a defensible "default" signal; a single-listicle name is a weak nominee. Same "headline signal misleads without its confound sibling" rule as the Trustpilot score→body flavor, different signal grain (editorial-listicle naming vs review score). Additive flavor; does not move this item's graduation clock.
- **2026-06-20 · Confounds travel onto the TEMPORAL/delta axis — two flavors (run 018):** The lab's first change-pulse/diff read shows MRL-008's "headline metric misleads without its confound sibling" rule applies to *deltas*, not just level reads, and surfaces two new facts. (1) **Only `review_count` is delta-able for Trustpilot** — `reviews_last_12m` returns `delta:null` (rolling window) and `trust_score` is level-only — so the one metric that diffs cleanly is the *least* decision-relevant one, and it sits on `paid_profile` profiles, making a "+66 reviews / +10/day" velocity a *solicitation-cadence* read, not sentiment/demand. The decision-grade surfaces (score trend, review bodies per MRL-010) are not temporally tracked at all. (2) **A new source-mechanics confound flavor:** Wayback `onemedical` showed `snapshot_count 2517→2516` (−1) with `last_seen` moving *backwards* (2026-06-15→2026-06-09) and an identical content digest — impossible for a monotone archive, i.e. **CDX API nondeterminism**, which a naive read would report as a lost archived snapshot. So the confound convention now spans two more source families on the change axis (review-score velocity, archive-state count). Reinforces (does not move) the graduation clock; pairs with new item MRL-012.

- **2026-06-20 · A new *flavor*: a Judgment-dense layer's structured field should not be aggregated at all (run 019):** The first cross-brand consumption of `visual.md` surfaces a confound flavor categorically distinct from every prior MRL-008 entry. Prior entries (Trustpilot score, Wayback tenure, SEC hits, review velocity, archive-state) are all **State/Signal** fields whose headline value misleads *until its integrity sibling travels with it* — the fix is to surface the sibling. The `visual.md` **`polarity`** field is different: it is a per-card direction indicator on a **Judgment-dense** layer, and the problem is not missing context but that it **should not be summed across companies at all** — capture-depth variance (9–51 cards per brand) plus rater drift make a cross-brand `polarity` rollup (e.g. `%poor`, which ranges 0–56% and is pure noise on a 9-card file) a meaningless discriminator, not a fixable-with-a-sibling one. The trustworthy grain on this layer is the **cited prose synthesis** (`## Visual & brand impression`), trusted via independent convergence (see MRL-002 run-019 entry), not the structured field. So the source-rigor convention should distinguish *"surface the integrity sibling"* (State/Signal fields) from *"do not aggregate this field; read the prose"* (Judgment-layer fields). Additive flavor; does not move the graduation clock. Pairs with the MRL-002 run-019 entry and the run's anti-footgun (pin instance vocab strong/mixed/poor vs the parked-score `weak`).

- **2026-06-20 · Proof-device flavor — State/Judgment boundary on a credibility-checklist layer + a polarity-error recurrence (run 021):** The trust/proof-device read adds a flavor that pairs with the run-019 visual entry on a different axis. (1) **State/Judgment boundary:** device-*presence* on a captured page (a LegitScript seal in the footer, a named clinician on /about) is owned-page **State** and is correctly capturable; device-*credibility / differentiation* (whether the pharmacy is actually in good standing, whether the named clinician holds an active license) is a **Judgment** the store must not harden or score. The read applied this boundary cleanly throughout — "not shown" was framed as *not-found-on-captured-pages*, never *absent*, and no device-presence was read as claim-truth. (2) **Polarity-error recurrence:** the Loop-2 verifier found 4 of 5 tallies outside the read's ±2–3 bar, driven by the same positive-vs-negated misclassification that miscounted run 019's visual polarity — ~9 LegitScript-absent domains read as positive; 4 of 7 named pharmacy-accreditation positives were explicitly "not shown" in their packs; the named-clinician shown/not-shown split was off by ~9; and a **ghost exemplar** appeared (struthealth "180-day money-back," no such language in the pack). All corrected in `read.md`/receipt. The common failure mode and fix match run 019's anti-footgun: **when a layer has explicit value flags (`y`/`n`/`not-shown`; strong/mixed/poor), read the flag verbatim — do not re-derive from surrounding prose.** Additive flavor; does not move this item's graduation clock. Pairs with the MRL-002 run-021 entry.
- **2026-06-20 · Promotional / point-in-time price as a within-kind confound (run 023):** The GLP-1 price-comparability read adds a price-specific member of the confound family. Prior entries fix a confound by *surfacing the integrity sibling* (a level metric's freshness, a count's window). The promo flavor is a **within-kind** confound: even after the unit is normalized (axis 1–2 of the MRL-002 rubric), a promo-framed number still isn't the steady-state price — ~8/19 captured GLP-1 entry prices are struck-through / code-gated / "SUMMER sale" framed, and 2 brands (directmeds, tryshed) carry intra-brand conflicts across their own surfaces (the store faithfully *holds both*, framing "which bills" as not-found, not absent). The convention addend: a captured price that is promo-framed should be treated **snippet-grade for any "cheapest/ranking" claim** until reduced to the recurring rate — distinct from the unit-incomparability problem, and it stacks on top of it. Overlaps the run-012 listicle/affiliate entry (headline misleads without its integrity context); the narrow novelty is that promo decay is a *price-level* point-in-time confound bounded by capture date. Additive flavor; does not move this item's graduation clock. Pairs with the MRL-002 run-023 entry.

- **2026-06-20 · Platforms-vs-payers extraction confound (run 024, F1):** A new, concrete flavor in the listicle confound family, on the *named-set extraction* step. Healthline's JSON extract of "best online therapy platforms" returned **7 insurance payers** (Cigna, Anthem, UnitedHealthcare, Aetna, Humana, BCBS, Kaiser) **as members of the named-brand set** — a ~60% inflation if taken naively. Hand-excluded by inspection; the read flagged it as F1. The integrity guard for any listicle where care-delivery platforms co-appear with carriers/payers: **filter the extracted named set to care-delivery platforms only before taking the cross-source intersection.** Structurally distinct from the run-012 affiliate-ordering confound — that one corrupts *rank/tail order*; this one corrupts *set membership* at extraction time, silently inflating the market denominator and over-reporting store absence. Becomes a named prerequisite of the MRL-002 bounded-live coverage-radar recipe (run-024 entry). Loop-2 verifier confirmed the exclusion was justified and the strict 5-brand intersection correct. Additive flavor; does not move this item's graduation clock. Pairs with the MRL-001 + MRL-002 + MRL-009 run-024 entries.

- **2026-06-20 · "All 50 states" availability claim is a two-way confound (run 025):** The first geographic/availability read adds a confound flavor on a brand-new field — geographic/US-state availability. The headline marketing claim "available in all 50 states" misleads two distinct ways. (a) **Claim-not-truth:** it is brand-claim State, recorded but never adjudicated — same discipline as every prior entry. (b) **Sub-component-scope (the novel part):** for 6 of the ~14 brands that say "nationwide/50 states," the phrase actually scopes a *sub-component* — clinician licensure ("400+ providers in all 50 states," hims), a pharmacy fulfillment network ("service to all 50 states," eden/ro/directmeds), or at-home lab draw (hellopepti/hormonemd/maximustribe) — **not** the buyable Rx program, whose real per-line state availability is undisclosed. A naive reader tallying "50 states" mentions over-counts national availability and misses that controlled-substance lines almost certainly face undisclosed state limits. The integrity guard: **for an availability claim, pin which noun it scopes (program vs clinician-licensure vs pharmacy-network vs lab-draw) before reading it as patient coverage.** Loop-2 evidence verifier (PASS_WITH_FIXES) caught two brands (hevahealth, niagenplus) initially misfiled as sub-component when the store actually records *per-program* state exclusions — corrected in read.md (decision-grade 7→9). Additive flavor; does not move this item's graduation clock. Pairs with the new MRL-014 (run-025 entry).

- **2026-06-20 · A bare *State* field that isn't self-describing (run 026):** Every prior MRL-008 entry is about a **Signal/level metric whose headline misleads until its integrity sibling travels with it** (Trustpilot score, Wayback tenure, SEC hits, review velocity, archive-state) or a **listicle/price within-kind confound**. Run 026 adds a categorically different flavor on a **State** field: `parent: []` is **not self-describing** — of 109 empties, only **6** carry a `#` comment distinguishing *verified-independent* (IDEO "independent"; Rugiet "operates independently") from *not-stated/uncaptured* (Swatch "not stated, see unverified_fields"; Notion "operating co not parent"; alliahealth "not stated"). The other **103 are bare**, so a reader cannot tell independence from undisclosure at the field level, and a naive consolidation read treating every empty as "independent" would badly overstate the independent share. The fix is **not** an integrity sibling (the State/Signal pattern) and **not** "don't aggregate" (the run-019 Judgment-layer pattern) — it is an **absence-disambiguation convention**: when a relation field is empty, mark whether absence means *asserted-independent* or *not-found-on-captured-pages* (the store already does this in 6 cases and in `unverified_fields`, just inconsistently). Distinct third branch of the source-rigor family: *surface the sibling* (State/Signal) / *read the prose, don't aggregate* (Judgment layer) / *disambiguate the empty* (relation State). Additive flavor; does not move the graduation clock. Pairs with the MRL-005 + MRL-006 run-026 entries.

### MRL-001 - Market denominator reconciliation convention

```yaml
id: MRL-001
title: Market denominator reconciliation convention for market reads
priority: P2
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: run-notes; Loop 2 consumer + developer review
area: denominator-reconciliation
evidence_summary: Run 000 showed the market denominator can be slow, partial, and method-sensitive. The internal store out-completed Notion Organizations for the GLP-1 read, and the store-to-Notion symmetric diff was useful both as missing-company radar and as a Pantry write-back/capture worklist. Later runs touched denominator issues but mostly strengthened MRL-002's query-recipe case; MRL-001 remains the artifact/convention for naming sources checked, inclusion/exclusion rules, resolver/dedupe method, known gaps, and confidence language.
proposed_next_step: Acknowledge as a lightweight market-read section or receipt convention. External SERP/listicle panels should be fallback sources when internal curated lists are thin, not the default denominator source.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/notion-organizations-glp1-denominator-seed.md
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
  - MRL-002
  - runs/008-2026-06-19-trt-mens-health-price-visibility/run-notes.md
  - runs/012-2026-06-19-glp1-default-brand-leaderboard/run-notes.md
```

**Evidence Log**

- **2026-06-19 · Cohort-boundary labor recurred (run 008):** The TRT/hormone price-visibility read's only real toil was drawing the denominator — TRT-vs-longevity and exogenous-T-vs-SERM edges, plus excluding generalist all-gender brands that also run TRT lines. The headline 42/42/17 split *depends* on those calls, and multi-cohort straddlers (Hone, getOpt, Lifeforce) are named concretely for the first time. Reinforces the convention need: name sources checked, inclusion/exclusion rules, and known gaps, and surface straddlers for human judgment rather than forcing a silent call.
- **2026-06-19 · Positive contrast — clean frontmatter cut nearly erases the labor (run 009):** The longevity/NAD positioning read drew its cohort with a *single grep* on `anchor_category: longevity/NAD` (8 brands), needing only two straddlers (getopt, joinfridays) hand-called. The opposite of run 008's hand-drawn TRT boundary. Useful contrast: when a clean closed-set frontmatter cut exists, denominator reconciliation is cheap; the labor MRL-001 names is real only where the boundary is fuzzy (molecule/audience edges), not where a frontmatter field already partitions the set.
- **2026-06-19 · External panel *operationalized* + an internal under-count surfaced (run 012):** The GLP-1 "default-brand leaderboard" read is the first to actually *test* the standing note that external SERP/listicle panels are a fallback denominator source. Verdict: a 2-authoritative-listicle panel (U.S. News 23 / Forbes 6) is a usable **coverage radar — not a clean denominator**. It is affiliate/SEO-confounded and **head-stable / tail-divergent**: the two authoritative sources agree on a ~5-brand head (Ro, Hims/Hers, Mochi, Remedy Meds, Found) but their tails diverge, and *low*-authority affiliate pages name a wholly disjoint tail. The only trustworthy ranking sub-signal is **cross-source recurrence** (named on ≥2 authoritative sources) — Mochi is the single store-absent brand clearing that bar. Concrete output: a *tiered* capture-candidate list (Mochi strong; PlushCare/WeightWatchers/SkinnyRX/… single-source nominees), exactly the "name sources checked, inclusion rule, known gaps" artifact this item wants. **New, generalizable internal-denominator finding:** the `anchor_category: GLP-1` grep *silently under-counts* GLP-1 offerers — multi/none brands (LifeMD, Nurx, Wisp) and module-thin brands (altRx) offer GLP-1 without being anchored to it, so they fall out of every cohort grep. This will distort *any* multi-service cohort read (GLP-1, hormones, longevity). The MRL-001 convention should eventually name **both** the external inclusion rule (cross-source recurrence + affiliate caveat) **and** the internal "anchored-only vs all-offerers" cut. Still recipe/convention-level; no helper, no stored leaderboard object. Loop 2 verifier caught two count-presentation errors (now fixed); membership findings held.
- **2026-06-19 · Fifth-cohort recurrence + first *cross-cohort* exposure of the anchored-only under-count (run 015):** The cross-cohort table-stakes read confirms the `anchor_category`-grep under-count across a **fifth** cohort context, with a new flavor: when a read spans *all* cohorts at once, the under-count bites **every per-cohort `n` simultaneously** — the multi/none generalists (LifeMD, Nurx, Wisp) fall out of every cohort census at the same time, not one at a time. Consequence specific to this run: the cohort-*agnostic* claims (cash-pay dominance, compounding-capability) are *strengthened* by the excluded generalists (the multi/none set is even more cash-pay/insurance-mixed), but the cohort-*specific* `n`'s (modality, bundling, audience) are floors. Five-cohort recurrence makes this the most consistently surfaced denominator caveat in the lab; any future documented QUERYING recipe for cohort-level reads should carry the anchored-only-vs-all-offerers cut as a **named first-class note**, not a per-run footnote. Reinforces (does not move) the convention.
- **2026-06-19 · Fourth-cohort recurrence of the anchored-only under-count (run 014):** The GLP-1 backend-counterparty read is the **fourth cohort** to carry the same caveat: `anchor_category: GLP-1` returns 19 while multi/none generalists (LifeMD, Nurx, Wisp) sell GLP-1 without anchoring and fall out of the census. Same mechanism as runs 012/013/008; **no new flavor** — but the four-cohort recurrence makes the anchored-only-vs-all-offerers distinction a *standard* denominator note. Reinforces (does not move) the MRL-001 convention: any future documented QUERYING recipe should name the anchor-only-vs-all-offerers cut as a first-class denominator caveat. Run 014's denominator was correctly scoped and labeled (relation census limited to the anchored cohort, not the whole GLP-1 universe).
- **2026-06-20 · Recurrence across the whole non-GLP-1 set (run 016):** The non-GLP-1 backend read scoped its cohort with the anchored-only `anchor_category` grep (35 brands) and explicitly framed all recurrence counts as **floors** — generalists that sell into TRT/longevity/sexual-health without anchoring fall out, and brands routing to an *unnamed* partner pharmacy are invisible, so the named-backend substrate is larger than measured. No new flavor; reinforces naming the anchored-only-vs-all-offerers cut as a first-class denominator caveat. **Method note worth folding into any QUERYING recipe (Loop-2 verifier catch):** filtering cohorts by `grep -v GLP-1` on the *full* `anchor_category` line silently drops brands whose inline `#` comment mentions GLP-1 (here nurx-com, prohealth-com → 33 instead of 35); the correct method parses the value field separately from the comment. Reinforces (does not move).
- **2026-06-19 · Third-cohort recurrence of the anchored-only under-count (run 013):** The sexual-health access/identity read is the **third cohort** to hit the same internal under-count — `anchor_category: sexual-health` returns **3** (rugiet, rexmd, bluechew) while an ED-term grep returns **24** store ED-sellers. Same mechanism as GLP-1 (run 012: LifeMD/Nurx/Wisp offer GLP-1 without anchoring to it) and the fuzzy TRT boundary (run 008). Cohort had to be hand-drawn into **3 tiers** (anchored / ED-franchise [hims/keeps/ro] / straddler tail), and the access↔anchor *correlation* — the run's headline finding — *depends* on that tier boundary, so a different tier call would move the result. Loop 2 verifier independently confirmed both grep counts (3 and 24; the `\bED\b` token is load-bearing for the 24). This confirms MRL-001's proposed convention across three cohorts: name **both** the external inclusion rule **and** the internal anchored-only-vs-all-offerers cut. The recurring 3-step derivation (anchor grep → term grep → hand-draw tiers) is now a candidate for a documented QUERYING recipe if a fourth run re-invents it. Still convention-level; no helper, no stored cohort object.

- **2026-06-20 · Competitive-set flavor of the anchored-only floor (run 017):** The Hone substitute/adjacent map drew its candidate neighbor field with the anchored-only `anchor_category ∈ {TRT, longevity/NAD, labs}` grep (16 brands) and framed it explicitly as a **floor** — un-anchored generalists (multi/none) that sell hormone/longevity lines without anchoring fall out of the neighbor set, so Hone's true competitive universe is larger than the 16 captured neighbors. Same mechanism as runs 012/013/014/015/016, now on a **competitive-set** grain rather than a cohort census. No new flavor; reinforces naming the anchored-only-vs-all-offerers cut as a first-class denominator caveat. Reinforces (does not move).
- **2026-06-20 · A *temporal-denominator* flavor + a subject-identity prerequisite (run 018):** The first change-pulse/diff read exposes a denominator kind the existing convention doesn't name: a **capture-cadence denominator** — "which subjects have ≥2 comparable captures *with a real time gap and stable identity*" — is structurally distinct from a market-membership denominator ("which brands are in a category"). Here it is 13 distinct domains (of 135) with a second capture, only ~6 usable. **The load-bearing new lesson is subject-identity, not just thinness:** SERP "pairs" turned out unpaired because the second capture was a *different query* under the same `domain/serpapi/` dir — so **"same domain + same source_type" is NOT sufficient to guarantee a diffable pair**; SERP/SEC need a pinned canonical subject (query string / issuer) at capture time. This is a capture-contract prerequisite, distinct from the anchored-only membership under-count this item has tracked across runs 008/012–017. Any future QUERYING signals-read recipe must carry the subject-identity requirement, not just a "temporal denominator is smaller" note. Reinforces (does not move); pairs with new item MRL-012. One enumeration-method catch worth folding in (Loop-2 verifier): "what's diffable" is **grain-dependent** — a company-grain glob (`<domain>/signals/<type>/*.json`) silently drops page-grain Wayback subjects (`signals/wayback/<page-slug>/*.json`); walk to the envelope.

- **2026-06-20 · A *selection-bias* denominator flavor — distinct from the anchored-only under-count (run 020):** The first audience-axis whitespace read surfaces a denominator risk **structurally distinct from every prior MRL-001 entry**, which all track the *anchored-only under-count* (a brand *in the store* falls out of a per-category `anchor_category` grep because it is `multi/none`). That bias enters at **query time** and is fixable with a wider grep / tier annotation. Run 020's risk enters at **corpus-construction time**: the captured telehealth cohort was seeded men's-hormone-heavy by prior lab runs (001/008/014/016), so the headline 15-men-leaning-vs-5-women-leaning brand asymmetry is bounded *before any grep runs* — the input set is non-representative by construction, and **no query-time fix touches it** (it needs a different capture campaign or an external denominator). The load-bearing consequence for any future QUERYING whitespace/asymmetry recipe: the two bounds are **independent and must travel together** — a reader who correctly applies the anchored-only fix (widen to `multi/none`) can *still* get a misleading men/women ratio. So a whitespace/asymmetry read shape is **doubly coverage-bounded**, and the compound caveat is a synthesis/guardrails requirement, not a footnote. The run correctly refused to read any empty audience×category cell as market whitespace or the asymmetry as a market fact (Loop-2 evidence verifier reproduced all counts — 54/54, buckets 34/8/7/3/2, the full grid, column totals 15/5/34 — with zero discrepancies and clean caveat discipline). Reinforces + sharpens (does not graduate); pairs with the MRL-002 run-020 watch entry. Still convention-level; no helper, no stored object.

- **2026-06-20 · Selection-bias flavor is now LIVE-CONFIRMED (run 022) — and the two flavors need two different tools:** Run 020 *hypothesized* the selection-bias denominator from store-only data and explicitly said it couldn't test it. Run 022 tested it with a 14-credit bounded-live panel: two authoritative menopause listicles (Everyday Health 17 / Flow Space 15) yielded a **9-brand cross-source-recurrence head**; **8 of 9 are absent from the store**, and the 1 present (Wisp) is captured `all-genders`, not women-anchored. The store's 5 women-leaning brands are nearly **disjoint by category** from the market menopause set (store women-leaning = 3/5 GLP-1/weight-loss-framed; market women-anchored = menopause/HRT specialists — Midi, Winona, Evernow, Gennev, Stella, HerMD, Allara, +Alloy/Elektra/Pandia). The **generalizable, now-evidenced rule:** the two MRL-001 denominator flavors require **different resolution tools** — the *anchored-only under-count* is query-time fixable (widen the grep to `multi/none`); the *selection-bias under-count* is invisible to **every** store-only query by construction and needs **outside evidence or new capture**. Any future QUERYING whitespace/asymmetry recipe must carry both as a first-class compound guardrail, not a footnote. Loop-2 evidence verifier independently reproduced the store-5 grep, the 9-brand intersection (with a name-variant normalization note now folded into the receipt: 7 exact + 2 `" Health"`-suffix matches), and the 8-of-9-absent token-match — zero substantive discrepancies; State/Judgment boundary clean; membership-vs-size discipline held. **Hardens the convention (clock moves toward first-class-guardrail status); does not graduate.** Pairs with the MRL-002 + MRL-009 run-022 entries.

- **2026-06-20 · Selection-bias flavor confirmed at CARE-MODALITY scale (run 024) — the largest gap yet, and scale-invariant:** Runs 020/022 confirmed the selection-bias denominator at **audience** scale (women's menopause). Run 024 confirms it at **care-modality** scale: a bounded-live panel (Forbes Health / Healthline, 12 net credits) yields a 5-brand cross-source-recurrence behavioral-telehealth head (BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive); **0 of 5 are in the store**, 0 body mentions across 54 packs, and a local grep independently corroborates **0** behavioral `anchor_category` values. The entire care modality (talk-therapy + psychiatry/medication-management) is absent — the corpus's "telehealth" label overstates scope by ~one modality (it is really **DTC Rx-commerce**: metabolic/hormone). The generalizable sharpening: the selection-bias under-count is **scale-invariant** — same mechanism (corpus seeded hormone/Rx-commerce-heavy by construction, runs 000/001/008/014/016), same resolution tool (bounded-live panel at 12–14 credits), operating from audience slices up to entire care modalities, and **invisible to every store-only query** at every scale. The compound QUERYING guardrail (the anchored-only grep fix is *necessary but not sufficient*; a selection-bias under-count needs outside evidence or new capture) now has **three-run** evidence. Loop-2 evidence verifier re-derived the 0/54 floor, the 0/135 directory diff, and the State/Judgment "gap-vs-scope" separation clean — overall PASS. **Hardens the convention; does not graduate.** Pairs with the MRL-002 + MRL-008 + MRL-009 run-024 entries.

### MRL-003 - Depth-backfill in-cohort module gaps

```yaml
id: MRL-003
title: Depth-backfill in-cohort module gaps (altRx, Marque)
priority: P2
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: run-notes; Loop 2 developer review (Steward)
area: corpus-health
evidence_summary: altrx-com and marquelongevitylab-com are in-cohort but not queryable on the module cuts needed for market reads. altRx is GLP-1-led by profile but lacks telehealth.md/offerings.md; Marque lacks telehealth.md. This silently shrinks cohort queries and is concrete corpus-health work rather than a new primitive.
proposed_next_step: Human-approved quick win candidate - run /deepen-offerings plus telehealth.md capture for altrx-com, and telehealth.md for marquelongevitylab-com. Keep it bounded to backfill, not schema work.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
```

### MRL-009 - Standard write-back candidates receipt section

```yaml
id: MRL-009
title: Standard write-back candidates receipt section
priority: P2
status: Acknowledged
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: Loop 2 consumer review (Pantry)
area: operator-ergonomics
evidence_summary: Three consecutive runs produced Pantry-useful write-back candidates that were buried inside system notes rather than surfaced consistently - Run 000 had a store-to-Notion node diff, Run 001 had brand-to-backend relation candidates, and Run 002 had a dated staleness/market note. The repeated value is a visible proposed-writeback section, not auto-execution.
proposed_next_step: Acknowledge as a documented market-read receipt section for write-back candidates. Keep propose-dont-write across the project boundary; do not build a writer or mutate Notion.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - runs/022-2026-06-20-womens-telehealth-whitespace-corroboration/read.md
```

**Evidence Log**

- **2026-06-20 · Concrete tiered capture-candidate worklist (run 022):** The women's-telehealth bounded-live read produced exactly the propose-don't-write artifact this item names — a tiered `/research-company` worklist of brands the store is missing. **Tier-1** (cross-source recurrence across 2 authoritative listicles, not in store): Midi Health, Winona, Evernow, Gennev, Stella, HerMD, Allara. **Tier-2** (strong single-source + SERP-confirmed live brand): Alloy, Elektra Health, Pandia Health. It is surfaced as a visible worklist in `read.md` (Missing/Stale Coverage + Triage submissions), **not** written back to `store/` or Notion. Capturing it would (a) convert membership → captured State, (b) let run 020's audience grid be recomputed honestly (the `womens-HRT` cell could move from 1 to ~8–11), and (c) give the lab the "second cohort with real depth" runs 020/021 both named as the other under-tested direction. **Highest-value follow-up, but NOT autonomous-safe** (Firecrawl spend → human approval). Reinforces the visible-proposed-writeback convention; does not graduate. Pairs with MRL-001 + MRL-002 run-022 entries.

- **2026-06-20 · Second tiered capture worklist from a bounded-live whitespace read (run 024):** The behavioral-health coverage-radar produced exactly the propose-don't-write artifact this item names, the second after run 022's menopause worklist. **Tier-1** (cross-source recurrence across 2 authoritative listicles, store-absent): BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive. **Tier-2** (single authoritative listicle, store-absent): Grow Therapy, Amwell, Teladoc Health, Sesame Care, LiveHealth Online. **Tier-3** (SERP-surfaced psychiatry/medication-management sub-lane not on the therapy-led lists, store-absent): Cerebral, Talkiatry, Brave Health. Surfaced as a visible worklist in `read.md` (Missing/Stale Coverage + Triage submissions), **not** written back to `store/` or Notion. New nuance vs run 022: a **scope decision precedes capture** — behavioral health may be intentionally out of scope for this store, in which case the worklist is informational, not a backlog; the read explicitly refuses to adjudicate. Also: several Tier-1/2 names (Teladoc, Amwell, MDLive, Doctor on Demand, LiveHealth) are multi-service virtual-care platforms, so they would enter as `multi/none` with behavioral as one line, not as behavioral pure-plays. **Highest-value follow-up but NOT autonomous-safe** (Firecrawl spend → human approval, and the scope call first). Reinforces the visible-proposed-writeback convention; does not graduate. Pairs with the MRL-001 + MRL-002 + MRL-008 run-024 entries.

### MRL-005 - Named-counterparty relation edge

```yaml
id: MRL-005
title: Named-counterparty relation edge - hold for passive recurrence
priority: P3
status: Submitted
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: run-notes; Loop 2 developer review (Founder + Steward)
area: relations
evidence_summary: Across 18 men-led/hormone telehealth brands, named pharmacy/clinical counterparties already resolve to store profiles, so a brand-to-backend edge could join cleanly and supplier concentration is a useful market read. But named counterparties were the minority, the claims are contaminated by ambiguous possessive language, and existing parent/owns plus pharmacy_model already cover the cleaner relation cases.
proposed_next_step: Hold as a passive evidence condition, not a queued run. If a future reader-valued relation-shaped market read independently lands on a backend-naming-dense cohort, use it to reassess whether named counterparties deserve joinable capture. If it later graduates, implement only as joinable dotted-domain frontmatter mirroring parent/owns, not a new edge table or relation-type registry. MRL-006 remains the capture-grain prerequisite.
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-006
  - MRL-002
  - runs/014-2026-06-19-glp1-backend-counterparty-concentration/run-notes.md
```

**Evidence Log**

- **2026-06-19 · Relation-surface recurrence on compounded GLP-1 (run 014) — partial fire, different axis:** Run 014 tested this relation surface on a backend-naming-dense GLP-1 cohort. Findings: (1) **"named is the minority" confirmed on a second cohort** — only 5/19 anchored GLP-1 brands name *any* counterparty; 14/19 route to an unnamed "partner pharmacy" (the run-001 possessive-language contamination pattern holds). (2) **First concrete, store-joinable, cross-brand shared counterparty:** **OpenLoop Health** (`store/openloophealth-com`, a B2B clinician-staffing platform) is named by **both** `home-medvi-org` and `joinfridays-com` as their clinical-delivery network; both edges would join cleanly today. (3) Every *pharmacy* name in the cohort (CraftedRx, Triad Rx, RedRock, Beaker, Eden Pharmacy) is **named-but-dangling** — no store profile exists for any, so the pharmacy-supplier-concentration question this item *originally framed* is currently un-answerable at join depth. The recurrence is real but on the **clinical-provider axis, not the pharmacy axis**. Two brands sharing one clinical vendor is a *lead, not concentration* (the read refused "concentration" language, correctly). An independent Loop 2 evidence-verifier reproduced all counts (19; 16/3; OpenLoop ×2 and only those two; 3 dangling pharmacies; 14 unnamed) with no overclaims. Implication for graduation: **hold, but shift the framing from "pharmacy edge" to "clinical-provider edge" as the higher-signal surface.** Suggested bar: a 3rd brand naming OpenLoop (or any clinical network recurring across ≥2 brands in a 2nd cohort). Minimal shape stays a dotted-domain frontmatter mirror of `parent`/`owns` (`clinical_provider: openloophealth-com`) populated only when the entity resolves to a profile — **not** an edge table. Graduation remains human-gated.
- **2026-06-20 · Recurrence test fires OUTSIDE GLP-1 — on the opposite axis (run 016):** The non-GLP-1 backend-relation read (the test runs 014 *and* 015 both named as highest-value next) settles the "GLP-1 artifact vs telehealth-wide" question: **backend sharing is telehealth-wide, but the joinable axis flips.** Outside GLP-1, the shared *pharmacy* layer carries the signal: **Strive Pharmacy** (`store/strivepharmacy-com`, has `profile.md`) is named by **both** `hevahealth-com` and `invigormedical-com` — a clean store-joinable cross-brand pharmacy edge, the mirror of run 014's clinical OpenLoop. Three more compounders recur ×2 but dangle (Curexa: bluechew+malemd; Tailor Made: invigormedical+mylifeforce; Olympia: hydramed+invigormedical). Meanwhile the only named third-party *clinical* group outside GLP-1 is **Beluga Health** (prohealth, singleton), and no shared clinical network (OpenLoop/SteadyMD/Wheel/Curai) appears in any non-GLP-1 `telehealth.md`. **Net: the lab now has two joinable cross-brand backend edges across two cohorts and two axes (clinical→GLP-1, pharmacy→non-GLP-1).** This **moves graduation**: the minimal shape must cover **both** a `clinical_provider:` AND a `pharmacy_partner:` dotted-domain mirror — clinical-only (the 014 framing) is insufficient. The item's stated recurrence bar (a backend recurrence outside GLP-1) is **met**; graduation remains human-gated. Still a *lead, not concentration* (each pharmacy ×2 brands; "concentration" language withheld). Loop-2 verifier reproduced every co-occurrence count clean; it caught one overclaim — `belmarpharmasolutions-com` was listed as joinable but has `captures/` only and no `profile.md` (corrected in `read.md`), so among the *cited* compounders only **Strive** is truly joinable today.
- **2026-06-20 · Ordering dependency holds on the ownership axis (run 026):** The ownership read confirms the run-014 "capture target first, then the edge already exists" ordering on the `parent`/`owns` axis: the field is populated on 13+15 brands, but 18-of-21 targets dangle because the parent/sibling profile doesn't exist (Thirty Madison, Niagen Bioscience, the LifeMD siblings shapiromd/navamd all named-but-uncaptured). The single working edge (`lifemd ↔ rexmd`) works precisely because *both* ends were independently captured. No new relation surface — the disclosed-but-dangling pattern is identical to the backend-pharmacy danglers this item tracks, now on the corporate-ownership axis. Reinforces the passive-hold framing; graduation remains human-gated. Pairs with the MRL-006 + MRL-008 run-026 entries.

### MRL-006 - Named-counterparty capture-grain gap

```yaml
id: MRL-006
title: Named-counterparty capture-grain gap
priority: P3
status: Submitted
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: run-notes (clinical-only P3); Loop 2 developer review (Steward, generalized to pharmacy)
area: capture-grain
evidence_summary: Relation data is split by shape. Parent/owns are clean joinable frontmatter, while pharmacy/clinical partners are prose claims in telehealth.md bodies, so "what does brand X depend on" requires structured plus unstructured reading. The few named counterparties prove the grain is capturable, but this is still a one-cohort/prerequisite sighting.
proposed_next_step: Watch for recurrence. If acknowledged later, capture named pharmacy and medical-group counterparties into joinable frontmatter when the page names them, recording explicit absence when useful and never treating possessive language like "our pharmacy" as a named entity.
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-005
  - runs/014-2026-06-19-glp1-backend-counterparty-concentration/run-notes.md
```

**Evidence Log**

- **2026-06-19 · Second cohort confirms the grain split + adds a join-target ordering finding (run 014):** Run 014 reconfirmed the split across a second cohort: `parent`/`owns` (the clean joinable relations) live in `profile.md` frontmatter — eden's owned-pharmacy link sits there, not in `telehealth.md` — while pharmacy/clinical partners live in `telehealth.md` *prose*, requiring a body read, not a field lookup. **New finding:** the only named counterparty in the entire cohort that resolves to a store profile is OpenLoop Health (clinical); every named *pharmacy* entity dangles. This adds a concrete **ordering** dependency to the capture-grain gap — even if a `pharmacy_partner:` frontmatter field existed and were populated, it would dangle for this cohort because the downstream profiles don't exist. Practical order of operations if MRL-005/006 ever graduate: (1) capture the named counterparty as a store profile first, (2) then add the dotted-domain frontmatter pointing to it. You cannot build the edge before the join target exists. Still a prerequisite/grain sighting; no schema change.
- **2026-06-20 · Pharmacy-side grain split + a "join fails both directions" finding + a contract sharpening (run 016):** The non-GLP-1 read reconfirms the grain split from the *pharmacy* side across a third cohort context: named compounders live in `telehealth.md` prose, not frontmatter. **Most still dangle** (Curexa, Tailor Made, Olympia, Empower, Precision, Valiant, Casa Pharma — no store entry); only **Strive** resolves to a `profile.md`. **New finding — the join fails from BOTH directions:** `hallandalerx-com` is a captured 503A compounder *with* a `profile.md` that **no** brand cites in `telehealth.md` (supplier-in-store, edge-absent), the inverse of the named-but-uncaptured danglers. So a populated `pharmacy_partner:` field would still mostly point at nothing today, AND captured suppliers can sit unreferenced. Reinforces the run-014 order-of-operations (capture target first, then add field). **Contract sharpening surfaced by the Loop-2 verifier:** "joinable" must mean a `profile.md` exists, not merely that a `store/<domain>/` directory exists — `belmarpharmasolutions-com` has a `captures/` folder but no `profile.md`, and was briefly overclaimed as joinable before correction. Still a grain/prerequisite sighting; no schema change.

- **2026-06-20 · Third relation flavor confirms the same root cause — clean frontmatter dangles too (run 026):** The first ownership/consolidation read aggregated the **`parent`/`owns` frontmatter axis** — the *cleanest* relation in the schema (structured, often explicit attestation), and the exact axis MRL-006 named as "the clean joinable relations" vs prose partners. Result: it dangles **18 of 21 referenced targets** — only `lifemd.com`, `qualtrics.com`, `rexmd.com` of ~21 distinct parent/owns targets resolve to a captured `profile.md`, and **`lifemd ↔ rexmd` is the ONLY fully-captured, bidirectionally-reconciled edge in the entire store** (run-notes O2/O3). This **generalizes the MRL-006 finding across a third relation flavor** — pharmacy-prose (run 016), clinical-prose (run 014), now ownership-frontmatter (run 026) all fail to join for the **same root cause: the counterpart entity isn't captured**. So the bottleneck is **counterpart capture coverage**, not relation representation or grain — even a perfectly structured field dangles when its target is uncaptured. New wrinkle: a captured-both-ends edge can still be **one-directional** (`delighted → qualtrics`: child names parent, but qualtrics `owns` omits delighted) — a join-integrity caveat distinct from the dangling case. Reinforces the run-014 order-of-ops (capture target first, the clean edge already exists). Loop-2 evidence verifier independently re-derived all counts (13 parent / 15 owns / 3-of-21 captured / 109-6-103 absence split), correcting only the captured-target tally 2→3 (a child is also an `owns` target). Still grain/prerequisite-level; **no field, no edge table, no new primitive** (the field already exists). Pairs with the MRL-005 + MRL-008 run-026 entries.

### MRL-007 - Category-scoped / non-company exogenous-signal anchor

```yaml
id: MRL-007
title: Category-scoped / non-company exogenous-signal anchor - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: run-notes; Loop 2 developer review (Steward + Founder)
area: signals-grain
evidence_summary: Run 002 surfaced category-level exogenous events - FDA compounding legality and NovoCare/LillyDirect reference pricing - that govern a cohort but have no per-domain signal home. Later Signals runs did not strengthen the case; Trustpilot, Wayback, and SEC-EDGAR all attached cleanly to per-domain paths.
proposed_next_step: Hold. If another read surfaces a homeless category-level signal, decide whether it belongs in a market/topic-scoped path or as a project-side monitor. Explicitly do not create a graph, entity-resolution layer, non-company entity type, or served monitor from one sighting.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
  - MRL-008
```

**Evidence Log**

- **2026-06-19 · Negative recurrence check:** Runs 005/006/007 all consumed per-domain Signals cleanly. No new evidence for a category-grain signal home beyond the original Run 002 sighting.

### MRL-010 - Reviews/forums body content as a source ingredient

```yaml
id: MRL-010
title: Reviews/forums body content as a source ingredient - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/009-2026-06-19-longevity-positioning-whitespace
created_from_review: Loop 2 developer review (adversarial workflow)
area: source-panel
evidence_summary: Two reads in the same sprint hit the same wall - strategist trust/whitespace and customer-pain questions need review/forum BODY content (objection mining, distrust of compounded NAD, churn complaints), not just ratings. Run 008 fired source-panel for customer-pain/trust; run 009 fired it again for longevity trust/whitespace. The store already captures Trustpilot/review *scores* in profile.md Credibility blocks, but not the review *bodies*, so the trust dimension of a positioning read is unanswerable store-only. Two sightings across two different read questions on adjacent runs is enough to name the gap; not enough to prescribe a schema change.
proposed_next_step: Hold for a third sighting. If it recurs, decide whether review/forum body content earns a place in profile.md (qualitative pull-quotes) or a signals/<source_type> capture grain. Do not build a scraper, monitor, or non-company entity from two sightings; keep ratings-vs-bodies as the concrete delta.
linked_items:
  - runs/008-2026-06-19-trt-mens-health-price-visibility/run-notes.md
  - runs/009-2026-06-19-longevity-positioning-whitespace/developer-review.md
  - MRL-008
```

**Evidence Log**

- **2026-06-19 · Second sighting (run 009):** The longevity/NAD positioning read's load-bearing whitespace ("do buyers trust this / what do they regret") and trust-gap claims need review/forum bodies the store doesn't hold as State. Ratings appear in some profile.md Credibility blocks; review content does not. Same underlying need as run 008's customer-pain read, fired by a different question.
- **2026-06-19 · Third sighting + FIRST ACTUAL USE (run 011):** The GLP-1 trust-gap read was the lab's first `bounded-live` run, and it *used* the missing surface instead of just naming it — captured Trustpilot 1-2★ review **bodies** for 3 brands (hims/remedymeds/henrymeds) + 1 Reddit triangulation search, 5 Firecrawl credits total. The bodies carried the entire load-bearing answer: a dominant **billing-after-cancel** objection cluster invisible in the headline scores the store *does* hold (remedymeds 4.6 "Excellent" → bodies full of "$2,400 charged for no meds, no refund"). Confirms the ratings-vs-bodies delta concretely and proves the surface is operable unattended at ~3-5 credits without sprawl. Crosses the item's stated "hold for a third sighting" bar. Recommend the human steward decide graduation and the grain question (profile.md qualitative pull-quotes vs a `signals/<source_type>` capture grain vs bounded-live recipe only). Loop 2 verifier + consumer + developer all flagged this as graduation-decision-ready; graduation remains human-gated.

### MRL-011 - Competitive/substitute relation surface as a Judgment

```yaml
id: MRL-011
title: Competitive/substitute relation surface as a Judgment - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/017-2026-06-20-hone-substitute-adjacent-map
created_from_review: Loop 2 developer + consumer review (3-pass adversarial)
area: relations
evidence_summary: First competitive/substitute relation read in the lab - every prior relation run (MRL-005/006) was backend supplier/clinical. Finding: a substitute neighbor set is cheaply enumerable from an anchor_category grep, but the substitute-vs-adjacent line is a positioning judgment that frontmatter enums underdetermine - anchor_category alone lumps vitalityrx (adjacent, single-mechanism enclomiphene) with defymedical (substitute, broad hormone clinic) and misclassifies functionhealth (anchor_category labs, but adjacent because it tests-and-reviews without prescribing). Crucially, "substitute" is buyer-relative: the same Tier-2 TRT brand is a substitute for the male-T buyer and adjacent for the both-sex/longevity buyer. A competitors:/similar_to: field or edge table cannot capture this as a durable fact - it would need re-derivation per buyer-job permutation. This is distinct from MRL-005/006 backend edges (pharmacy_partner/clinical_provider), which are joinable facts independent of any buyer's job. One anchor (Hone), one buyer-job, 16 brands - a single sighting.
proposed_next_step: Hold as a passive condition. If a second single-anchor competitive read recurs (different anchor or buyer-job), decide whether the engine should serve a documented query-time substitute recipe (neighbor enumeration + job-criterion labeling) in QUERYING.md. Explicitly do not build a competitors: field, similar_to: field, or edge table - the relation is a buyer-relative judgment, not a fact. Graduation remains human-gated.
linked_items:
  - runs/017-2026-06-20-hone-substitute-adjacent-map/read.md
  - runs/017-2026-06-20-hone-substitute-adjacent-map/developer-review.md
  - MRL-002
  - MRL-005
```

**Evidence Log**

- **2026-06-20 · First sighting (run 017):** Hone Health substitute/adjacent map. Three tiers across 16 captured neighbors: Tier-1 broad lab-led optimization substitutes (mylifeforce/gogeviti/gethealthspan/defymedical), Tier-2 TRT-optimization brands that substitute only for the male-T buyer, Tier-3 adjacent unbundled components (functionhealth diagnostics-only, vitalityrx enclomiphene-only, agelessrx longevity-Rx, NAD+ supplement sellers). Loop-2 evidence verifier reproduced the grep (16 brands) and 6 tier placements clean, with two precision fixes folded into read.md (functionhealth "no Rx prescribing" wording; Hone 40+/50+ panel A/B caveat). Consumer verdict valuable; developer verdict submit-candidate. Hold for a second sighting before any QUERYING recipe; no field/edge.

### MRL-012 - Change-pulse readiness: capture-cadence + subject-identity + a sec_edgar branch, not a primitive

```yaml
id: MRL-012
title: Change-pulse readiness is a capture-cadence + subject-identity + tooling gap, not a new primitive
priority: P2
status: Submitted
created_from_run: runs/018-2026-06-20-signal-change-pulse-readiness
created_from_review: Loop 2 developer + consumer review (3-pass adversarial)
area: freshness/signals-cadence
evidence_summary: First temporal/diff read in the lab (all 18 prior runs were point-in-time). Diffing every store signal dir with >=2 captures via tools/signal_delta.py shows the append-only signals layer + the comparator are the RIGHT shape - no new change/diff primitive is needed - but a real "trust the cache over time" read is blocked by THREE separable gaps the schema does not distinguish. (1) Cadence-vs-refresh-rate - Trustpilot counts move daily (6 brands gave clean per-day velocity over a ~6.5d gap), but Wayback re-crawls ~monthly so weekly re-captures read delta=0 on 13/15 page-subjects, and SEC pairs are intra-day. (2) Subject-identity is not pinned at capture - SERP "pairs" are unpaired because the second capture was a DIFFERENT query under the same domain/serpapi/ dir; "same domain + same source_type" does not guarantee a diffable pair (this is a capture-contract gap, not cadence). (3) One narrow tooling gap - signal_delta.py has no sec_edgar delta branch (~one function), so SEC funding-pulse vetoes today. Separately, every readable delta is a noisy PROXY for the change a consumer wants (Trustpilot review_count = solicitation cadence on paid_profile, not sentiment; Wayback = archiver re-crawl state, not page-content change). Denominator: 13 distinct domains with a second capture; only 6 yield a usable Trustpilot velocity, 1 a real Wayback archive-presence change.
proposed_next_step: Human-gated decision, sequenced as TWO separable sub-fixes with different owners/costs - (a) ops: stand up a light, per-source-tuned re-capture cadence for a small fixed subject set (start with the 6 clean-velocity Trustpilot brands: honehealth, hims, joinamble, agelessrx, joinfridays, maximustribe); (b) ~30-min code: add a sec_edgar delta branch to signal_delta.py. Plus a capture-contract note: pin a canonical subject (query string for SERP, issuer for SEC) when re-capture targeting matters. Explicitly do NOT build a monitor service, a stored diff/change object, or a non-company signal entity from one run.
linked_items:
  - runs/018-2026-06-20-signal-change-pulse-readiness/read.md
  - runs/018-2026-06-20-signal-change-pulse-readiness/receipts/signal-delta-sweep-2026-06-20.md
  - MRL-008
  - MRL-001
  - MRL-007
```

**Evidence Log**

- **2026-06-20 · First sighting (run 018):** First temporal/diff read. signal_delta.py over all >=2-capture dirs: Trustpilot 6 clean velocities (honehealth +66/10.0d, hims +54/8.7d, joinamble +51/7.8d, agelessrx +17/2.6d, joinfridays +13/2.0d, maximustribe +7/1.1d), 3 vetoes; Wayback 15 page-subjects, 13 delta=0 + honehealth mens/sermorelin archive_presence 0->1 + onemedical snapshot_count -1 confound; SEC 4/4 veto (no branch + intra-day); SERP unpaired (different queries). Adversarial evidence verifier caught a page-grain enumeration miss (Wayback skipped by a company-grain glob) - folded in, distinct-domain count confirmed at 13. Hold for a second temporal read before any QUERYING signals-read recipe graduates; no monitor, no stored diff object.

### MRL-013 - `menopause/HRT` as a first-class anchor_category - hold for capture confirmation

```yaml
id: MRL-013
title: menopause/HRT as a first-class anchor_category value - hold for capture confirmation
priority: P3
status: Submitted
created_from_run: runs/022-2026-06-20-womens-telehealth-whitespace-corroboration
created_from_review: Loop 2 developer review (3-pass adversarial)
area: taxonomy/coverage
evidence_summary: Run 020's audience×category grid had womens-HRT = 1 (innerbalance alone). Run 022's bounded-live panel implies that single cell is hiding a 10+-operator dedicated women's-menopause/HRT segment (Midi, Winona, Evernow, Gennev, Stella, HerMD, Allara, Alloy, Elektra, Pandia) the store has not captured. This is one sighting of a possible under-resolved category, surfaced from an external panel rather than captured State.
proposed_next_step: Hold. Do NOT graduate a taxonomy value from one external-panel sighting. Revisit only if a human-gated tier-1 capture run (MRL-009 worklist) confirms the segment's density and that these brands actually front-door as menopause/HRT. If confirmed, the question is whether menopause/HRT deserves its own anchor_category value vs staying under womens-HRT - a TAXONOMIES decision, human-gated.
linked_items:
  - runs/022-2026-06-20-womens-telehealth-whitespace-corroboration/read.md
  - MRL-001
  - MRL-009
  - MRL-003
```

**Evidence Log**

- **2026-06-20 · First sighting (run 022):** External-panel implication only; no captured State yet. The store under-resolves dedicated women's menopause/HRT (1 anchored brand vs a 10+-named market segment). Held as a watch behind the MRL-009 capture worklist; no taxonomy change from one sighting.

### MRL-014 - Geographic / state availability is a per-line, point-in-time property, not a brand field

```yaml
id: MRL-014
title: Geographic / state availability is a per-line, point-in-time property - hold, do NOT add a brand field
priority: P3
status: Submitted
created_from_run: runs/025-2026-06-20-telehealth-geographic-availability-gap
created_from_review: Loop 2 developer + consumer review (3-pass adversarial)
area: structure/coverage
evidence_summary: First geographic/availability read in the lab - no prior run touched place. The store cannot answer "can I get this in my state?" as a query for any of the 54 telehealth-cohort brands, and the reason is grain mismatch, not thin coverage. Availability is not one of the 8 telehealth cuts and survives only as scattered prose. Of 54 brands: 9 carry decision-grade disclosure (a named exclusion or enumerated state-count limit), 2 carry an un-enumerated limit, 8 carry brand-level "all 50 states" boilerplate, 6 use "nationwide" for a sub-component (labs/pharmacy/clinician), 29 are silent. The load-bearing finding: the splits are WITHIN a brand - joiandblokes restricts testosterone to a 16-state exclusion while its other lines are unrestricted; vitalityrx is all-50 for its kit but 25-states for its Rx; henrymeds flags KYZATREX not-in-CA only; hevahealth is 45/30/50 states by program+audience; marek splits diagnostics from program. So availability is a product x state (sometimes audience x state) fact, and a brand-level available_states field would be false-precise. The hard exclusions cluster on controlled-substance / compounded lines, tracking shifting state pharmacy law - so any captured list is intrinsically point-in-time (struthealth dated "as of Sept 2024"). The store already handles this honestly (henrymeds unverified_fields records that the site won't enumerate its states).
proposed_next_step: Hold as a passive condition. Do NOT add an available_states brand field or a stored service-area object - it would force one answer onto a multi-answer entity and rot as state law shifts. If a second cohort independently shows the same product x state split (controlled-substance lines state-limited, everything else national), decide whether a per-offering-line verbatim availability note (quote the state list/exclusion on the offering line, dated) earns a depth-backfill at the offerings.md grain. Even then, never a brand scalar. Graduation remains human-gated.
linked_items:
  - runs/025-2026-06-20-telehealth-geographic-availability-gap/read.md
  - runs/025-2026-06-20-telehealth-geographic-availability-gap/developer-review.md
  - MRL-008
  - MRL-003
  - MRL-002
```

**Evidence Log**

- **2026-06-20 · First sighting (run 025):** Store-only gap-probe across 54 telehealth-cohort brands. Decision-grade disclosure in 9 (joiandblokes 16-state testosterone exclusion / vitalityrx 25-state Rx vs all-50 kit / henrymeds KYZATREX-not-CA / hevahealth 45-30-50 per-program / marek diagnostics-not-NY-NJ-RI / trtnation 5-state excl / struthealth excl-AR / bluechew excl-ND / niagenplus 7-state at-home-kit excl), 2 un-enumerated (defymedical "most states", kingsbergmedical "where physicians licensed"), 8 brand-level "50 states" boilerplate, 6 sub-component "nationwide", 29 silent. Loop-2 evidence verifier (PASS_WITH_FIXES) reproduced C1–C8/C10 verbatim and caught 2 brands (hevahealth, niagenplus) initially misfiled as sub-component when the store records per-program exclusions — corrected in read.md (7→9). Developer pressure-tested the product×state claim and confirmed it is the dominant pattern among disclosing brands, not an overreach. Hold for a second-cohort sighting before any per-line depth-backfill recipe; explicitly do NOT add an available_states field. Pairs with the MRL-008 run-025 confound entry.

### MRL-001 / MRL-008 cross-links

See the dated Evidence Log entries appended to MRL-001 (temporal-denominator + subject-identity flavor) and MRL-008 (two temporal confound flavors) below, both from run 018.

---

## Resolved

### MRL-004 - Market Read Lab scaffold skill

```yaml
id: MRL-004
title: Market Read Lab scaffold skill
priority: P2
status: Resolved
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: operator-observation
area: operator-ergonomics
evidence_summary: Creating Run 001 required manual folder creation, template copying, path references, and prompt assembly. This setup work will recur across many lab runs and is independent of the market analysis itself.
proposed_next_step: Graduated by explicit approval. Added local Claude skill `.claude/skills/market-read-lab/` with a small scaffold script that creates numbered run folders from repo templates and prints the Loop 1 prompt. No analysis, review, triage graduation, or scheduling is automated.
linked_items:
  - .claude/skills/market-read-lab/SKILL.md
  - .claude/skills/market-read-lab/scripts/new_run.py
```
