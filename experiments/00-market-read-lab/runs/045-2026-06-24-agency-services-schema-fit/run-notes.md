# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [schema-edge-entity-type, denominator-reconciliation, query-time-grouping-enough, source-rigor, depth-backfill]
```

## 30-second operator read

- **Did the run work?** Yes. Clean store-only gap-probe on the most product-hostile entity
  type the schema-edge series hasn't hit: pure project-based creative/strategy **agencies**
  (ideo, redantler, heco, bullish, parlance). Split verdict — a human buyer **can** shortlist
  from prose, but **every** structured field the schema offers either can't assemble the
  cohort or can't differentiate within it.
- **What was awkward?** The cohort has **no isolating structured key** at all:
  `offering_category [Services / Consulting]` matches 80 profiles (carried store-wide as a
  secondary), `business_model Services / Project-based` matches 8 (3 non-agency contaminants).
  A sharper denominator-reconciliation flavor than the n=4 industry-draw.
- **What should the next agent know?** "No new primitive needed" holds, *harder* than usual:
  prose carries the full buyer decision and the price-visibility token is **faithful** on
  services (`[on-request]` = no list price *exists*, not a hidden one). Parlance is the lone
  price-transparent member ($15k Sprints / $225 Office Hours `[published]`) and the token
  captures it. Don't propose a firm-scale field — it would rot.

## What happened

Scout selected a store-only gap-probe (C1). Loop 1 read all 5 agency profiles + the clerky
foil in full, then ran 3 grep tests on the structured layer: the two candidate cohort keys
(`offering_category`, `business_model`) and `portfolio_shape` across the 5. Confirmed the
split verdict (cohort non-isolating + within-cohort degenerate, prose carries the decision,
token faithful), wrote read.md + run-notes, set `read-done`. No external sources, no spend,
no receipts (all evidence is local store file:line).

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | **No structured field isolates the creative-agency cohort.** `offering_category [Services / Consulting]` matches **80** profiles (carried store-wide as a *secondary* clinical-services value across telehealth + VC firms + usertesting/warbyparker); `business_model Services / Project-based` matches **8** — the 5 agencies + 3 non-agency contaminants (euclidpower energy, verdegoaero aerospace mfg, goinfusive healthtech). A buyer who doesn't already know the 5 names cannot draw them from frontmatter. **New, more severe flavor of denominator-reconciliation:** the n=4 industry-draw (036 G3/037 G2/039 DR1/042 G3) was a roughly-right draw *contaminated*; here **no field even approximates the cohort.** | That the fields are mis-tagged — each is individually correct; only that *creative agency* has no isolating structured handle. | read.md Result(1), C1/C2; grep counts 80 vs 8 | denominator-reconciliation, schema-edge-entity-type |
| G2 | gap | **Within-cohort structured degeneracy *for buyer differentiation*.** The 4 *typing* fields are identical across all 5: `entity_type Company` · `offering_category [Services / Consulting]` · `business_model Services / Project-based` · `primary_industry Consulting & Professional Services`. The 2 fields that vary — `target_market` (IDEO `[B2B, B2G]`, rest `[B2B]`) and `portfolio_shape` (3 values) — vary in **buyer-irrelevant** ways (neither separates global from solo). The closed `offering_category` set **bottoms out** at `[Services / Consulting]` — no finer leaf in TAXONOMIES.md. **Taxonomy-bottomed-out**, sharper than run-039's SaaS flattening (where `[Software / SaaS]` sat above ~19 sub-markets *and* finer leaves were conceivable). [Corrected per VR1/DR1: original row said "identical 5-field tuple" — an overreach on target_market + portfolio_shape.] | That a finer enum value should be added — n=5, single cohort; prose differentiates them. Only that the structured layer can't (for the buyer's purpose). | read.md Result(2), C3; 5 profiles' frontmatter | schema-edge-entity-type, query-time-grouping-enough |
| G3 | gap | **The buyer's #1 differentiator — firm scale/shape (solo→boutique→global) — has no structured field.** The cohort spans the whole range (IDEO 5 global studios → Parlance 1 person + EA → Heco 2 partners). `portfolio_shape` is the nearest field and is **degenerate for it**: **3/5** (IDEO global, Heco 2-partner, Parlance solo) all carry `Flagship + companions` — it encodes service-line structure, not firm size. Scale lives only in prose. | That a firm-scale field should be built — it'd be a rotting captor judgment, mostly-blank store-wide (fails engine-dev's fillable-cut bar). Only that the most decision-relevant axis is unstructured. | read.md Result(3); portfolio_shape across 5; ideo:44/heco:39/parlance:38 | depth-backfill, query-time-grouping-enough |
| S1 | surprise | **Prose carries the full buyer decision — richly — for all 5.** Capability (`What they offer`), specialization (`Positioning & audience`), proof/named clients (`Credibility & proof`), and engagement model (`How it works`) are all present and well-organized; a human can shortlist + differentiate cleanly. The **buyer-value inverse** of the schema-fit failure — continues the run-042 S2 / run-043 S1 "store is a genuine strength for the reader" thread on the entity type that most defeats structure. | That the schema succeeds — it fails structurally (G1–G3); only that the *prose layer* serves the buyer well. | read.md Result(4); 5 profiles' body sections | query-time-grouping-enough |
| S2 | surprise | **The price-visibility token is faithful on services — `[on-request]` here means no list price *exists* (custom-scoped), not a hidden/gated one.** Unlike a DTC brand withholding a real price, an agency's bespoke scope has no list price to withhold, so the schema's pricing silence is honest market structure. The token's "can I even get a price?" axis (SCHEMA 2.3) generalizes correctly onto the lowest-price-surface entity type. Cleanest case yet for engine-dev's "evidence, not a score/field." | That the token is the only pricing answer needed — a buyer still wants a budget anchor; only that the token reads *correctly* here. | read.md Result(5); SCHEMA.md:142; parlance:62-66 | source-rigor, query-time-grouping-enough |
| S3 | surprise | **Parlance is the lone price-transparent member and the token captures it — but only at body-line grain.** Sprints "$15k" / Office Hours "$225" / Mentorship "free" are `[published]`; its bespoke fractional/advisory lines are `[on-request]`. The other 4 are uniformly `[on-request]`. The token correctly surfaces the split, but it's a `What they offer` body token with **no frontmatter roll-up** — a buyer filtering frontmatter for "which agency publishes any price" wouldn't see it. **Echo of run-044 G1** (token uneven/invisible as a cross-cohort surface). | That a frontmatter price-visibility scalar should be built — SCHEMA explicitly makes it per-offering, never a company scalar. Only that the transparency split is invisible to a structured filter. | read.md Result(5), C5; parlance:62-66; SCHEMA.md:142 | depth-backfill, query-time-grouping-enough |
| W1 | wish | If anything ever graduated from G1/G2, the lightest path is **not a firm-scale field** but acknowledging the closed `offering_category` set lacks an *agency/specialization* value (it bottoms out at `[Services / Consulting]`) — and even that only *if* a real **filtering/programmatic** consumer needs to select agencies by specialization from frontmatter. A human reader needs neither (S1 is positive evidence). Mirrors run-036/037/039/042/043/044 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* a 2nd pure-services cohort shows the same pattern AND a filtering (not reading) consumer appears. "No new primitive needed" stays live. | read.md What Would Change; .claude/rules/engine-dev.md | query-time-grouping-enough, schema-edge-entity-type |
| S4 | surprise | **The design-agency-specific visual read is already in profile.md, not gated behind visual.md.** `visual.md` exists for only 2/5 (bullish, parlance), but every profile carries a rich `Visual & brand impression` section — and for a *design* agency (where the site IS the portfolio piece), that section is a genuine buyer ingredient. So the uneven `visual.md` coverage (2/5) doesn't block the shortlist. | That visual.md is redundant — it adds depth (blind cards) profile.md compresses; only that the buyer-load-bearing visual read is in profile.md for all 5. | read.md Gap Map; profile `Visual & brand impression` x5; visual.md present 2/5 | coverage-caveat |
| VR1 | risk-miss | (Evidence verifier) G2 originally asserted "All 5 collapse to the identical tuple: target_market [B2B]" but IDEO is `[B2B, B2G]` (ideo:42), and `portfolio_shape` has 3 distinct values (Flagship+companions / Single / Multi-product) — "identical" was false on 2 of 5 fields. Degeneracy-for-buyer survives; framing overstated. **Corrected in read.md Result(2) + G2/G3.** The 3-pass verifier caught a precision slip a single-pass read shipped (as run-042 VR1). | That the finding is wrong — only that "identical tuple" was an overreach. | ideo:42; redantler:37; bullish:44; run-notes G2 | source-rigor, schema-edge-entity-type |
| CR1 | gap | (Consumer review) Prose carries the shortlist, but "rough price" was bundled into the carried-cleanly Gap Map column when **4/5 firms give zero price signal**. A buyer pre-qualifying by *budget* (not capability) can't shortlist from prose for 4/5. Gap Map conflates capability-shortlisting (prose sufficient) with budget-qualification (not). | That prose fails or a price field is needed — `[on-request]` is honest for custom-scoped firms; only the Gap Map conflation. | read.md Gap Map row 3; ideo:66; heco:28 | query-time-grouping-enough, coverage-caveat |
| CR2 | friction | (Consumer review) Firm scale is the *first* buyer screen (IDEO global vs Parlance solo), but lives only in prose — forcing sequential full reads of all 5 before the filter fires. The read's "sufficient for a human shortlist" understates this front-loaded reading cost. | That a scale field should be built — W1 argues it'd rot; only that prose-only scale imposes real friction. | read.md Result(3); ideo:62; parlance:73; heco:111 | depth-backfill, query-time-grouping-enough |
| DR1 | gap | (Developer review) portfolio_shape degeneracy is **3/5 not 2/5** — Heco (2-partner boutique) also carries `Flagship + companions` (heco:39), across global/boutique/solo scales. Evidence was understated; same conclusion. **Corrected in read.md Result(3) + G3.** | That the finding is wrong — only that citing 2 members understated it. | heco:39; ideo:44; parlance:38 | source-rigor, schema-edge-entity-type |
| DR2 | gap | (Developer review) W1's lighter-fix alternative (offering_category lacks an agency/specialization value) is offered without testing whether *that* value would also rot. "Creative agency" vs "consultancy" vs "dev shop" is a captor judgment, not site-derivable — roughly as unstable as the firm-scale field W1 rejects. Anti-sprawl reasoning for the alternative is incomplete against the fillable-cut bar. | That W1's hold is wrong — "no new primitive" is right; only that the lighter-path reasoning has an unnamed gap. | run-notes W1; .claude/rules/engine-dev.md; ideo:32 | schema-edge-entity-type, query-time-grouping-enough |

## Inputs and scope

- **Core set (5):** store/ideo-com, redantler-com, heco-partners, bullish-co, parlance-cc —
  full profile.md read each. All `offering_category [Services / Consulting]` +
  `business_model Services / Project-based` + `primary_industry Consulting & Professional
  Services`, all B2B, none with `offerings.md`.
- **Foil:** store/clerky-com (legaltech hybrid; priced packages, has offerings.md) — read for
  contrast.
- **Structured-layer tests:** 3 greps — `offering_category` draw (80), `business_model` draw
  (8, 3 contaminants), `portfolio_shape` across the 5.
- **Token check:** SCHEMA.md price-visibility definition (line 142) vs parlance offering lines.
- **Exclusions:** no external sources, no Firecrawl/SERP, no spend; cohort is partial by
  construction (captured agencies only; market majors uncaptured).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

No tooling friction — three greps + six file reads answered it. The only "friction" is the
finding itself: assembling the cohort required already knowing the 5 names, because no
structured key isolates them (G1).

## Evidence limits

- Cohort is partial by construction (captured agencies only; market majors uncaptured) — "not
  found in store," not "not there." No "N agencies do X" headline made.
- Firm-scale claims (G3) rest on prose self-description (studio counts, partner counts,
  engagement caps), flagged `unverified_fields` on each profile as deep-research, not
  marketing-site facts. Honest absence, not a capture failure.
- n=5, single cohort — every gap is a single-cohort sighting; W1 holds graduation pending a
  2nd pure-services cohort.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (all evidence local store file:line / grep counts)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (pricing read from dated captures; parlance $15k/$225 from 2026-06-10 capture)
- Absence language says "not found", not "not true": **pass** (cohort "partial by construction"; "not found in store")

## Surprises

The schema-edge series expected another "wrong-grain" failure (like marketplace take-rate);
instead this entity type fails by having **nothing to grab** — non-isolating *and* degenerate
(S1/G1/G2). And the price-visibility token, which has been a soft spot in recent runs (044
G1), is the one convention that reads **correctly and faithfully** here, because its question
survives the absence of a list price (S2).

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

**Fired:** `schema-edge-entity-type` (the run's spine — services entity type vs product
spine), `denominator-reconciliation` (G1 — non-isolating cohort key, a more severe flavor),
`query-time-grouping-enough` (G2/G3/S1/W1 — no new primitive), `source-rigor` (S2 — token
faithfulness), `depth-backfill` (G3/S3 — unstructured firm-scale + body-only token). No new
tag needed; the existing set covered it.

"No new primitive needed" is a valid outcome — and it is this run's outcome, held harder than
usual because the prose serves the buyer and the one structured pricing convention reads
faithfully.

## Next-run advice

- **To promote G1/G2 from singleton toward a lesson:** run a **second pure-services cohort** —
  management/strategy consultancies, law firms, or dev/eng shops — and test the same two
  things (does any field isolate the cohort; do members differentiate structurally). If the
  non-isolating + degenerate pattern repeats, it's a general "services entity type defeats the
  product spine" shape, not an agency quirk.
- **Avoid** re-running the same agency cohort; the schema verdict here is clean.
- A **bounded-live** variant (find the uncaptured agency majors via a listicle/SERP panel)
  would test denominator completeness — but mind run-040's spend block; keep the ceiling tight.
