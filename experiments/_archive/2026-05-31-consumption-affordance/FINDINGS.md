# Findings — consumption affordance, the *cold* control

> **Verdict: the bet holds. A genuinely cold agent — no `CLAUDE.md`, no memory, no method hint —
> discovered the store and its contract unaided and answered correctly, cited, in one pass on all
> five consumption paths, including the flagship cross-brand price aggregation.** The predecessor's
> "agents start from scratch, never reach for the structure that's already there" failure **did not
> reproduce**. The walls that remain are narrower than expected, and each names one next decision:
> the binding one is a **structured price field** (`offerings.md`) — earned not by a failure but by
> watching exactly how much un-reusable manual labor its absence forces.

*5 probes, one per path/limit. Each = a fresh headless `claude -p` (Opus) in a sandbox copy of the
store that **excludes `CLAUDE.md` + `experiments/`** (introspection-verified cold). Prompt = question
+ store location only. `stream-json` captured the ground-truth tool trace. Method: [`README.md`](README.md);
raw answers: [`_out/`](_out/).*

## TL;DR

- **Discoverability is not the gap (anymore).** 5/5 cold agents self-found `README → QUERYING.md`
  and picked the right recipe (parse-YAML vs grep vs route-to-web) with zero hand-holding. QUERYING.md is load-bearing **and effective** — it carried the negative-distinction, the cross-shape reframe, the "parse YAML, don't `grep|uniq`," and the out-of-scope routing. The rung-2 doc *works*.
- **The flagship aggregation passed** — and that reframes the wall. The cold agent found the cohort
  from frontmatter, located prices via the bold `**name:**` lead-in + captures, **correctly reconciled** four incompatible price structures (membership-stacked, à-la-carte, quarterly, tiered) with *zero* errors on spot-check, cited, flagged the not-priceable cases, and gave a defensible bottom-line. No re-scrape.
- **So the real flagship wall is precise: the numeric answer is non-reusable hand-derivation, not a
  query.** It held *this* time (Opus, one cohort, ~12 tool calls) but it isn't auditable, isn't
  repeatable, can't answer "GLP-1 under $200/mo," doesn't scale to N offerings × 50 brands, and is
  one model-downgrade away from a wrong table. → **graduate `offerings.md` with a structured price.**
- **Two free capture-side findings.** `mylifeforce` carries an off-taxonomy `offering_category:
  Health & Wellness` (1/26) — and `querycheck.py` can't catch it (it validates field *presence*, not
  enum *values*). Both cheap to fix.

---

## Lead with the walls — the decisions this test earned

### Wall 1 — Structured price is the one binding gap. `offerings.md`, now. *(flagship)*
The cold agent **did** answer "how does the cohort price GLP-1." But watch *how*: parse 26 frontmatters
→ filter `primary_industry` → grep 9 profiles for GLP terms → dig into 2 capture sets to close gaps →
hand-normalize four structures into an invented "est. all-in/mo" column → hedge a verdict. ~12 tool
calls and a long reasoning chain, for **one offering in one cohort**. The output is a *narrative*, not
a *query*, and that's the wall:

- **Not auditable / not repeatable.** "AgelessRx ~$99–139 is cheapest" is the agent's own arithmetic
  over prose; there is no field a second agent — or a rung-3 index — could `ORDER BY`. Two runs need
  not agree.
- **Range queries stay impossible.** "GLP-1 under $200/mo," "cheapest TRT" — unanswerable without
  re-doing the whole manual pass. QUERYING.md already declares this ("can't answer yet"); the cold
  run confirms the declaration is real, not conservative.
- **It doesn't scale and isn't model-robust.** This was Opus on one cohort. The two-part Eden
  ($99 med + mandatory $99/mo membership) and quarterly PeterMD structures are exactly where a weaker
  consumer model mis-reads — and the store's queryability shouldn't be contingent on the caller being
  Opus.

**Decision:** a per-offering structured price — `{value, unit, cadence, included/excluded,
molecule, compounded|branded}` — in `offerings.md`. Converts a 12-call manual narrative into a
one-parse query, makes range queries answerable, makes the number auditable, and de-risks it from
model strength. *This is the same conclusion the [prior consumption test](../2026-05-31-consumption/)
reached — now reconfirmed by a cold agent on a 9-brand cohort, and upgraded from "manual & messy" to
"works once, by hand, for Opus, un-reusably."*

> **Refined across three cohorts (Addenda 1–2):** the heavy normalization is **messy-pricing-specific,
> not universal** — clean SaaS tiers *and* published watch MSRPs read straight off the body with zero
> arithmetic. So `offerings.md`'s heavy price model is earned only where sites publish messy prices.
> The *universal* core is **lighter and lives per-offering, not in profile frontmatter**: a
> `price_visibility` enum (published | on-request | partial) — the one axis common to SaaS "sales-
> gated," telehealth quiz-walls, and luxury "price on request." The earlier `pricing_model` framing is
> **retired** (per-seat/usage don't survive watches); and Cartier proves visibility is a property of
> the *offering*, not the company. Net: **light by default, heavy per messy vertical, and the one
> universal field is per-offering `price_visibility` — never a company scalar.**

### Wall 2 — Discoverability holds, but it's entry-point- and model-contingent. Surface QUERYING *at the entry*.
The win (5/5 found the contract) is real but rests on two unprobed supports: every agent **entered at
the store root**, where `README` sits and links `QUERYING.md`; and every agent was **Opus**. A
consumer handed a deeper path (`store/<domain>/`, or a single `profile.md` via `WEB_RESEARCH_HOME`)
never passes the README, and QUERYING was load-bearing for the *correctness* of P3/P4/P5 — so its
discoverability is a single point of dependence.

**Decision:** make the entry point self-document — a one-line header pointer in every `profile.md`
(`> querying this store: ../../QUERYING.md`) and/or have the skill that exposes `WEB_RESEARCH_HOME`
hand the consumer QUERYING.md. Cheap insurance on the rung-2 "wrap it in a skill the agent reaches
for" half of the Frame, which is still unbuilt. *Don't* rewrite QUERYING — it works; just guarantee
it's seen.

### Wall 3 — Frontmatter cohorts over-include; the comparison unit should be the *offering*.
Both price probes showed `primary_industry: Healthcare & Life Sciences` is coarser than "price-
comparable": P2 had to *secondary-grep GLP terms* to drop Function Health (lab-testing) from the
10-company cohort, and P3 crowned a diagnostics brand "best value" against treatment providers. The
axis that governs comparability — diagnostics vs prescriber vs longevity-program vs platform — isn't
in frontmatter, and **shouldn't be** (it's a Tier-2 project vertical the engine deliberately doesn't
own). The clean resolution is architectural: compare **offerings, not companies** ("who sells a GLP-1
offering, at what price") — which `offerings.md` keys directly. **Wall 3 collapses into Wall 1** and
is evidence *for* it: offering-level structure, not a new company-level taxonomy, is the right fix.

### Wall 4 — One capture-side non-conformance + a `querycheck` blind spot.
`store/mylifeforce-com` has `offering_category: [Services / Consulting, Health & Wellness, Biotech /
Pharma Products]` — `Health & Wellness` is **not** in the TAXONOMIES closed set (and isn't `Other`).
It's the only violation in 26 profiles, but it silently fragments any `offering_category` grouping —
and `scripts/querycheck.py` **passed it green**, because querycheck validates field presence + the
multiselect convention, not value membership.

**Decision:** (a) fix the value (drop it, or use a listed category); (b) add a `--strict` enum-
conformance pass to `querycheck.py` (it already parses every frontmatter — checking values against
TAXONOMIES is a few lines). Closes the contract↔corpus drift class the prior test named, at the
*value* level this time.

### Wall 5 (calibration, not a defect) — "describe + price" works; "rank / cheapest" stays soft.
The agent's verdict was honestly mush ("$85 on paper, mid-pack in practice"; "cheapest verifiable but
coupon-soft"). That softness is *correct* — membership-stacking + coupon/A-B volatility make a clean
ranking genuinely impossible, and the store surfaces that rather than faking a leaderboard. Note for
expectation-setting: even `offerings.md` (Wall 1) narrows but won't fully close this. The store's
honest ceiling is a *defensible narrative comparison*, not a *leaderboard* — don't over-build for one.

---

## Per-probe scorecard

Dimensions from the Frame's success criteria. ✓ = clean, ⚠ = partial/contingent, — = n/a.

| Probe (path) | Reach¹ | Tool-fit² | Correct³ | Cited | Honest⁴ | No re-scrape⁵ | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **P1** point read — Hims | ✓ | ✓ point-read | ✓ | ✓✓ | ✓ | ✓ | **exemplary** |
| **P2** intra-cohort GLP-1 price | ✓ | ✓ parse-YAML+grep | ✓ | ✓ | ✓✓ | ✓ | **pass; numeric = manual** |
| **P3** ill-posed "best pricing?" | ✓ | ✓ reframe+cohort | ✓ | ✓ | ✓✓ | ✓ | **pass (reframed)** |
| **P4** negative — Function/GLP-1 | ✓ | ✓ 3-signal+grep | ✓ | ✓ | ✓✓ | ✓ | **exemplary** |
| **P5** deep-research — Maximus | ✓ | ✓ store+web split | ✓ | ✓✓ | ✓✓ | ✓ | **exemplary** |

<sub>¹ found store + contract unaided · ² matched query-shape to the right tool · ³ vs. store ground
truth · ⁴ flags limits / not-captured / out-of-scope, no fabrication · ⁵ warm-serve where the store
suffices (P5's web calls were *only* for out-of-scope funding — correct).</sub>

- **P1 (point read) — exemplary.** 6 calls, no web. `ls → README → QUERYING → profile.md`. Returned a
  briefing with **per-section source attribution**, reasoned that re-scraping "would duplicate work the
  capture already paid for" (it grasped the economic premise), noted freshness ("captured 2026-05-30,
  one day old"), and flagged three gaps from `unverified_fields`/Provenance. The C1/C2 criterion to
  the letter.
- **P2 (aggregation) — pass; the numeric is hand-built.** See Wall 1. The reconciliation was
  *correct* (Eden two-part, Marek à-la-carte, PeterMD quarterly, Hone Basic-tier all verified against
  the store) — the wall is that it's a narrative, not a reusable query.
- **P3 (ill-posed) — pass, correctly reframed.** Refused to rank 26 companies across business shapes
  ("a per-night Airbnb commission, Stripe's take-rate %, Nike's one-time price, and a B2B seat license
  don't share a denominator … fake precision"), cited QUERYING Recipe 4, narrowed to the comparable
  cohort. Its prices were real (Marek $455, Maximus $349.99/146-markers, PeterMD $79/mo+6-mo, Hone
  Basic $25/mo — all verified; **zero fabrication**). Residual: the diagnostics-vs-treatment sub-cohort
  slip → Wall 3.
- **P4 (negative) — exemplary.** Ran QUERYING's "before trusting a negative" three-signal test
  explicitly (key_pages coverage + `unverified_fields` + a verbatim grep of all 7 captures), then
  returned a **confident "not offered, not just not-captured"** at a stated ~95% with the residual
  named. This is the single clearest proof the contract's honesty machinery works when discovered.
- **P5 (deep-research) — exemplary.** Read the profile for *state*, recognized via QUERYING + the Frame
  that funding/size are **out of scope by design** ("the store correctly told me so rather than
  guessing"), routed only those asks to the web, synthesized the *threat judgment* as its own (not the
  store's), cited everything, **did not write back to the store**, and — notably — **caught and
  discarded a cross-company data contamination** ("$2.94B revenue is *Maximus Inc.* NYSE:MMS, a
  different company"), independently validating the store's domain-as-key entity-disambiguation thesis.

## Did the bold `**name:**` lead-in move the needle?
**Yes — it was exercised and it worked.** P2 and P3 both used the exact QUERYING Recipe-4 pattern
(`rg '^- \*\*.*\$[0-9]'`) to enumerate priced lines; P1 read prices straight off the bold-led *What
they offer* bullets. The convention is what made cross-company price *location* a one-grep step. It is
necessary but not sufficient: it solves **locate**, never **normalize** — the leftover normalization
is precisely Wall 1.

## Against the Frame's success criteria
- **C1 (cold flagship, cited, fresh, one pass, no hand-holding):** ✅ met — P2 + P1. The hand-built
  numeric is the asterisk (Wall 1).
- **C2 (warm second look ≈ $0 Firecrawl):** ✅ — 4/5 used **zero** network; P5's web was only for
  out-of-scope events. No agent re-scraped a warm company.
- **C3 (legible enough that deep-research reads it before re-scraping):** ✅ — P5 read priors first,
  went wide only for what the store disclaims, kept its narrative out of the store.
- **C5 (trustworthy for a real strategy call):** ✅ on honesty/citation; the trust ceiling is Wall 1
  (numbers are narrated, not queried) + Wall 2 (correctness leaned on QUERYING + Opus).

## Artifacts
- [`_out/`](_out/) — the cold-agent answers, verbatim (P1–P7), gitignored bulk.
- Method, sandbox, and the cold-control validity check: [`README.md`](README.md).
- Tool traces (`stream-json`) retained at `/tmp/wr-probe-*.jsonl` for this session.

---

# Addendum — the SaaS cohort: does aggregation generalize, and is the price gap universal? *(P6–P7)*

> **Localization verdict: the structured-price gap is MESSY-PRICING-SPECIFIC, not universal.** A cold
> agent reading **clean published tiers** (Typeform, Delighted) got the prices **straight off the
> stored body — verbatim, zero arithmetic** ("exactly as SCHEMA's body rule promises"). The
> telehealth "collapse to a hand-built narrative column" **did not reproduce.** So `offerings.md` does
> *not* need a universal heavy price-normalizer — the bold-lead body convention already makes clean
> per-company pricing auditable. The heavy all-in normalization (the telehealth Wall 1) is earned only
> where sites publish *messy* prices (stacking / quiz-gating / cadence). What *is* universal — and
> cheap — is two **light** structured fields the cold run kept reaching for by hand: a `pricing_model`
> (public-tiers | sales-gated | usage/quote) and a value-metric `unit` (per-seat | per-response |
> per-interaction | flat). That's the input to *how heavy* `offerings.md` must be: **scoped, not full.**

Same cold harness, same root-entry, cohort = the only new variable. Two probes: **P6** — price-
benchmark the research/feedback/intelligence SaaS tools (heterogeneous on purpose); **P7** — resolve
the Qualtrics↔Delighted relation (QUERYING #3).

### 1. Generalization — yes, cleanly.
P6 (10 calls, no web) produced a sub-grouped pricing benchmark for the SaaS cohort with the same
discipline the telehealth probes showed: parse-YAML to scope, QUERYING Recipe 4 to bound the
comparison, `rg '\$[0-9]'` to enumerate every published figure (and discard the non-price `$` hits —
CSR "$5", "$500M ARR", "$5T under management"). Aggregation is **not** a telehealth-only trick.

### 2. The localization test — clean tiers stay queryable; only cross-company needs (light) work.
The deliverable. From P6's own process log:
- **Within a company, clean tiers read straight off the profile, no arithmetic.** Delighted (`Free $0
  · Starter $19 · Growth $39 · Advanced $149 · Premium $249`, each with resp/user counts) and
  Typeform (`$0 / $39 / $79 / $129` + yearly-effective + add-ons) were lifted verbatim from bold-led
  body lines. *The messy-pricing narrative collapse did not happen.*
- **The only reconstruction was the cross-company compare.** Delighted-vs-Typeform tiers don't share
  breakpoints, so the agent picked "common anchor points" (entry / ~100 responses / high-volume) — a
  *light, deterministic alignment*, not telehealth's all-in stacking math. And it landed the right
  read: "not 'one is cheaper'; they're cheapest for different jobs" (Delighted seat-generous/volume-
  capped, Typeform volume-cheap at scale).
- **6 of 9 are sales-gated → there is no price to structure.** The agent correctly reported quote-only
  for Qualtrics/UserTesting/Listen Labs/Gong/Clari/AlphaSense and Free-+-custom for Dovetail — each
  verified as *not-offered-publicly* (not *not-captured*) via the three QUERYING negative signals. This
  is the SaaS reality the telehealth probes never showed: **"sales-gated" is a first-class state**, and
  a `pricing_model` field would turn "who's even priceable?" into a one-field query instead of nine
  `unverified_fields` reads.

→ **Implication for `offerings.md` weight.** Scope the heavy normalizer to messy-DTC verticals. The
universal core is light: `pricing_model` (so sales-gated is queryable, not a gap) + a value-metric
`unit` (so comparability is machine-checkable). The clean-tier *price itself* already lives auditably
in the body — don't rebuild it.

### 3. Sub-grouping — the agent carved it well, but **only because it read prose**; frontmatter can't.
Asked to group a deliberately heterogeneous cohort, the agent produced a sensible **4-way** carve
(survey/VoC · qual-UX-research · revenue-intel · market-intel) on "buyer + value metric + pricing
unit," and excluded BlueOwl (fintech) correctly. **But the carve came from `description` prose** — the
closed-set frontmatter is useless here: all nine are `Technology / B2B / Software / SaaS /
Subscription` and **`tags` is empty on all of them**. This is the SaaS echo of telehealth's Wall 3:
the axis that governs comparability (product sub-type / value-metric) isn't in frontmatter and
shouldn't be a new company taxonomy — but a light offering-level `unit` would make it partly
queryable instead of a prose-reading judgment call.

### 4. Relations (P7) — resolved correctly, and exposed an asymmetry worth indexing around.
The cold agent (6 calls, no web) correctly returned **Qualtrics owns Delighted**, sourced from
`delighted.parent: [qualtrics.com]` + aliases + description + the `/qualtrics` migration page, at
calibrated *high* confidence — and **caught the asymmetry**: `qualtrics.owns` lists only `"Press Ganey
Forsta"`, **not** Delighted. It read that correctly as a capture-coverage gap (Qualtrics's own pages
didn't surface Delighted), not a contradiction, using the same not-captured-vs-not-true discipline as
P4. **Finding for rung-3:** `parent`/`owns` are populated **one-sided** (only the subsidiary carried
the link) — a relational index must **reverse-scan `parent` across the corpus**; trusting `owns` for
symmetry would miss real edges. The QUERYING #3 recipe works; the *corpus* is asymmetric.

### Scorecard (P6–P7)
| Probe | Reach | Tool-fit | Correct | Cited | Honest | No re-scrape | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **P6** SaaS price benchmark | ✓ | ✓ parse-YAML+sub-group+grep | ✓ | ✓ | ✓✓ | ✓ | **pass; clean tiers stay queryable** |
| **P7** Qualtrics↔Delighted relation | ✓ | ✓ Recipe-3 + cross-check | ✓ | ✓✓ | ✓✓ | ✓ | **exemplary (caught asymmetry)** |

### Net effect on the walls
- **Wall 1 (structured price) is now *scoped*, not universal.** Heavy normalization → messy verticals
  only. Universal add is light (`pricing_model` + `unit`). This is the concrete answer to "how heavy
  does `offerings.md` need to be": **light by default, heavy only where sites publish messy prices.**
- **Wall 3 reconfirmed across a second cohort** — frontmatter under-groups heterogeneous industries
  (SaaS sub-types here, telehealth sub-types before); the fix is an offering-level `unit`, not a new
  company taxonomy.
- **New relations note** — `parent`/`owns` asymmetry: index the subsidiary side (`parent`).

---

# Addendum 2 — the watch cohort: does *any* pricing field survive a third shape? *(P8–P10)*

> **Verdict for the design session: NO universal pricing/visibility *company-frontmatter* field
> survives three shapes — but one axis does generalize if you put it in the right place.** Across SaaS,
> telehealth, and physical-luxury watches, the only thing common to all three is **price *visibility***
> (published | on-request/gated | partial) — *not* pricing *model* (the SaaS-shaped `pricing_model`
> values per-seat/usage are meaningless for a watch). The luxury "price on request, see an authorized
> dealer" is the **same state** as SaaS "request a quote." **But the watch cohort breaks the field two
> ways the 2-cohort runs couldn't see:** (1) **Cartier** publishes jewelry/fragrance prices while
> gating its *watches* — so visibility is a property of the **offering, not the company**, and a
> profile-frontmatter scalar is a category error; (2) the price **value never generalizes** (a watch
> list price, a SaaS seat tier, a telehealth all-in share no unit), and `Catalog` shape caps even
> *published* watch prices at a **range**, not per-SKU. **So: don't add a company pricing field. The
> one universal, cheap thing is a per-offering `price_visibility` enum in `offerings.md`; the price
> value stays body/offering-resident, heavy only per messy vertical.** Watches *extend* the SaaS
> conclusion; they don't overturn it — and they retire the SaaS-shaped `pricing_model` idea.

Same harness, sandbox rebuilt to the 40-company store. 7 watch brands spanning the shape on purpose:
affordable published-MSRP (Casio, Swatch), luxury (Cartier, Rolex), grail-tier price-on-request
(Patek, Audemars Piguet, A. Lange & Söhne).

### 1. Visibility is the universal axis — confirmed, and the states fell out clean.
P10 (8 calls, no web) independently produced exactly three states and named the pattern:
- **Publishes exact prices** — Casio (`~$100–$165+` watches), Swatch (`$75–$420`): read **straight off
  the bold-led body**, no arithmetic — the clean-tier result from SaaS, reproduced on physical goods.
- **Price-on-request / gated** — Rolex, Patek, AP, Lange: each "no prices anywhere… sold via
  boutiques/authorized dealers," captured as a **fact** in `unverified_fields`/Provenance (not-offered,
  not not-captured — the P4 discipline again). P10's own framing: *"the real divide isn't a number;
  it's whether the brand will tell you the price at all."* This is **SaaS "sales-gated" on a watch** —
  same state, different mechanism (an open "contact us," not a Marketo form or a telehealth quiz-wall).
- **Partial / per-line** — see Cartier, below.

### 2. The killer: visibility is per-*offering*, not per-company. *(Cartier — caught by both probes)*
**Cartier publishes jewelry (`$2,130–$38,520`) and fragrance (`$49–$355`) prices but gates its
*watches* (appointment-only).** Both P9 and P10 caught it unprompted and drew the right conclusion —
P10: *"the same rule applied per product line."* A `price_visibility:` scalar in `profile.md`
frontmatter would be **wrong for Cartier and every multi-line seller.** → if visibility becomes a
field, it must be **per-offering (in `offerings.md`), not company frontmatter.** This is the constraint
the SaaS/telehealth cohorts (single-pricing-shape per company) could not surface.

### 3. No structured field captures visibility today — and even a derived proxy fails.
P10 was asked whether a single field let it classify quickly. Its answer is the design input:
> *"No. This is the important finding. `business_model` is `Transactional / One-time` for **all
> seven**; `primary_industry` is `Consumer Goods` for six of seven. The closest structured proxy is
> `offering_category` containing `Retail / E-Commerce` … **except it gives a false positive on A. Lange
> & Söhne**" (Retail/E-Commerce for accessories, yet zero watch prices). "The actual answer lived in
> prose … there is no `prices_published: yes/no` field, exactly as QUERYING.md's limits predict."*

(Verified: `alange-soehne-com` does carry `offering_category: [Hardware…, Retail / E-Commerce]`. The
proxy genuinely misclassifies it.) So visibility is recoverable only from `site_notes` + `unverified_
fields` + body prose — i.e. it is **real, consistent, and currently un-queryable**: the precise profile
of something that *earns* a structured field — but a per-offering one.

### 4. The price value never generalizes; `Catalog` caps even published prices at a range.
Watches are `portfolio_shape: Catalog` (hundreds of refs). The store captures price **bands** (Swatch
`~$50–$420`), and **P9 connected it itself**: *"the store captures price bands/ranges, not per-model
prices, by design (per-SKU depth deferred to the unwritten `offerings.md`)."* So "what does
[reference] cost" is out of scope by design for catalogs — and a watch list-price shares no unit with
a SaaS seat-tier or a telehealth all-in. **Only the visibility *state* generalizes; the *value* stays
shape-specific and body/offering-resident.** Watches confirm the SaaS verdict (light-universal +
heavy-per-messy-vertical), they don't extend the heavy normalizer to a third vertical.

### 5. Grouping wall — 3rd and decisive sighting: the cohort isn't frontmatter-definable *at all*.
Telehealth needed a secondary grep to refine its cohort; SaaS needed descriptions to sub-group; the
**watch cohort can't be assembled from frontmatter at any level.** `primary_industry` splits it
(**Casio is `Technology`**, the other six `Consumer Goods`); `offering_category` scatters across
`Hardware` / `Apparel & Footwear` / `Retail`; `tags` is empty on all seven. Both P9 and P10 found the
cohort by **recognizing brand names on the domain slug + confirming via `description`** — world
knowledge, not a query (P10's `grep 'watch|horolog'` over-matched Airbnb/Apple/Datadog "watch a demo"
and was discarded). Across three cohorts the comparability axis is **consistently prose-only** — now a
robust recurring fact, not a one-off. (Live BACKLOG item already debates a `Luxury Goods / Jewelry &
Watches` `offering_category` value; note it would fix *naming*, not *grouping* — Casio would still sit
in `Technology`, and luxury-vs-affordable / mechanical-vs-quartz stay prose.)

### Scorecard (P8–P10)
| Probe | Reach | Tool-fit | Correct | Cited | Honest | No re-scrape | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **P8** point read — Rolex | ✓ | ✓ point-read | ✓ | ✓✓ | ✓✓ | ✓ | **exemplary (no-price handled cleanly)** |
| **P9** watch price aggregation | ✓ | ✓ find+split+ranges | ✓ | ✓ | ✓✓ | ✓ | **pass; "two will, five won't"** |
| **P10** price-visibility classification | ✓ | ✓ tri-signal classify | ✓ | ✓ | ✓✓ | ✓ | **exemplary (proved no field exists)** |

P8 is the cleanest no-price point-read possible: asked "what do their watches cost," it returned
*"Could not be determined… reporting the gap rather than fabricating figures,"* noted `offerings.md`
doesn't exist for Rolex, and did not re-scrape or reach to training knowledge.

### Net effect on the design session
- **Retire `pricing_model`; the universal axis is `price_visibility`** (published | on-request | partial)
  — and it lives **per-offering in `offerings.md`, never in profile frontmatter** (Cartier). It answers
  the question 5/7 watches + 6/9 SaaS actually hit: *"can I even get a price?"*
- **No universal price-*value* field** — shape-specific, body/offering-resident, heavy normalization
  earned only per messy vertical (telehealth). Three shapes now agree.
- **Grouping stays prose/consumer-side** — don't try to make cohort membership a frontmatter query; a
  `Luxury Goods` enum value would tidy naming but not fix grouping (Casio ⊂ `Technology`).
