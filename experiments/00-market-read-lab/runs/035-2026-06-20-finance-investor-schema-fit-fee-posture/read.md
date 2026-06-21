# Market Read

## Question

Across the captured Finance & Fintech + Investor/Holding slice, what business model and
fee/pricing posture does each disclose, and does the store's telehealth-shaped universal
schema actually capture what a finance/investor firm *is* — or do the load-bearing facts
(AUM/fund focus, fee/rate structure, who they serve, capital-allocator role) fall
outside the captured fields?

## Result

**Verdict (gap-probe):** The schema does **not** break on finance — it carries a
*contracted subtractive gate* for capital allocators that works cleanly. What it lacks
is a *positive* capital-allocator field set, so the load-bearing finance facts a
"compare these investors" reader wants are **prose-only or undisclosed**, not greppable.
`query-time-grouping-enough` fires **FALSE** for the finance reader — the first clean
FALSE on a *content* axis (every prior content read fired TRUE; only the trust-metadata
reads 031/032 fired FALSE).

The slice splits into two subtypes with opposite schema-fit stories. Reported by subtype
to avoid crowning a single "finance pattern" across n=9 (the contracted failure mode):

**Subtype A — Fintech products (2/9: stripe, runway). Schema fits cleanly, same as SaaS.**

| Co | entity_type | offering_category | portfolio_shape | business_model | price posture |
|---|---|---|---|---|---|
| stripe | Company | Financial/Fintech + Software/SaaS | Catalog | Usage-based / Consumption | **published** (per-txn %/fee) |
| runway | Company | Software / SaaS | Single | Subscription | **gated** — all 3 tiers "Unlock pricing" (enterprise-quote) |

These two behave exactly like the SaaS slice (run 028): every structured field populates,
and the price-visibility axis applies — stripe publishes usage-based pricing, runway
quote-gates all tiers. **Nothing new here**; confirms the run-028 generalization.

**Subtype B — Capital allocators (7/9: blueowl, firstround, lsvp, sequoiacap, standishspring, spero-vc, thrivecap). The schema gates them out, correctly, but offers no positive shape.**

| Co | entity_type | offering_category | portfolio_shape | business_model | stage (prose) | fund/AUM disclosed on-site? |
|---|---|---|---|---|---|---|
| blueowl | Investor / Holding | Financial / Fintech Products | *empty (STRAIN)* | **Other** (mgmt+perf fees on AUM) | private-markets asset mgr | yes — ~$315B AUM (own marketing stat, C5) |
| sequoiacap | Investor / Holding | *empty (implied)* | empty | **empty** | seed→IPO, endowment-LP | no — "not on the marketing site" (C3) |
| lsvp | Investor / Holding | Services / Consulting | empty | **empty** | Seed→Series F, multi-stage | no — AUM/fund sizes not stated (C3) |
| firstround | Investor / Holding | Financial/Fintech + Services/Consulting | empty | **empty** | seed-stage | no — fund size/carry not stated (C3) |
| thrivecap | Investor / Holding | *empty (STRAIN)* | empty | **empty** | incubation→growth | no — none disclosed "by design" (C3) |
| spero-vc | Investor / Holding | *empty (STRAIN)* | empty | **empty** | seed→Series A | **partial** — Fund II $125M, 2024 vintage (C4) |
| standishspring | Investor / Holding | empty | empty | **empty** | early-stage hard-tech | no — fund size/vintage/AUM not stated (C3) |

For 6 of 7, `business_model` is **empty** and every profile says why in identical terms:
*"VC economics (mgmt fees + carry) aren't in the closed set and aren't stated on the
site."* blueowl is the lone `Other` (it's a public asset manager that *does* publish AUM).
`portfolio_shape` is empty-by-rule for all 7 (TAXONOMIES: an Investor/Holding's
"portfolio" is its investments, never `Other`). `offering_category` is empty or STRAIN'd
for 5 of 7.

**The two halves of MRL-015, made concrete:**

1. **Subtractive gate — works.** The schema *has* a real accommodation: a closed-set
   `entity_type: Investor / Holding` value (TAXONOMIES.md:19) plus a documented gating
   rule that empties `portfolio_shape` (TAXONOMIES.md:72) and the convention to leave
   `offering_category`/`business_model` empty. This *prevents wrong product-shaped data* —
   no VC gets a fake "Subscription" model or a forced portfolio_shape. The gate fired
   correctly and consistently across all 7 (with blueowl's `Other` the one principled
   exception). This is the schema generalizing *well* on the negative.

2. **No positive shape — the open gap.** The facts a finance reader actually compares —
   **fund stage focus, AUM/fund-size band, fund vintage/number, check size, LP type,
   thesis sectors** — have **no structured home**. They live in `description` + body
   prose (stage, thesis), or are flagged in `unverified_fields` as "not on marketing
   site / deep-research" (AUM, fees, fund sizes for 5 of 7). You can grep
   `entity_type: Investor / Holding` and `primary_industry: Finance & Fintech`; you
   **cannot** grep "all seed-stage funds," "all funds > $1B AUM," or "2024-vintage funds."

**Gate-type (run-033 W1, the 4th-vertical bar):** capital allocators expose a **distinct,
deeper gate-type** than the three prior verticals. The "price" is management fee +
carried interest, which is (a) absent from the `business_model` closed set, and (b)
essentially never on the marketing site — because **the site is a founder/LP-recruiting
surface, not a commerce surface at all.** This isn't telehealth sales-intake gating,
SaaS enterprise-quote gating, or luxury dealer-waitlist gating (all of which *gate* a
price that exists behind a wall); here the marketing site **simply isn't a pricing
surface**. The closest disclosed proxy is fund size/vintage (spero $125M Fund II;
blueowl $315B AUM as a public asset manager). This is a clean **4th distinct gate-type ×
gate-grain** data point for run-033 W1.

## Gap Map

| Reader question | Store answer store-only | Grain |
|---|---|---|
| "What does this finance entity do?" | **Clean** — `description` + prose carry it for all 9 | prose |
| "Is it a capital allocator or a fintech product?" | **Clean** — `entity_type` splits 7 vs 2 greppably | structured |
| "What's its business model / how does it make money?" | **Split** — 2 fintech products: clean (structured). 7 allocators: *empty by contract* — true answer (mgmt fee + carry) has no closed-set value and is off-site | structured (fail for allocators) |
| "What stage / sector does this VC invest in?" | **Prose-only** — readable per-firm, not greppable across the set | prose |
| "What's its AUM / fund size / vintage?" | **Mostly not-found** — disclosed 2/7 (blueowl, spero partial); flagged `unverified_fields` "deep-research" for 5/7 | prose / absent |
| "Compare fee structures across these investors" | **Not answerable** — no fee field; fees off-site for 6/7 | absent |
| "Give me all seed-stage / all >$1B funds" | **Not answerable store-only** — no structured stage/AUM cut | absent |

**The load-bearing distinction (contracted failure mode, avoided):** `business_model:`
empty for the 7 allocators is **two stacked absences** — (a) *schema-can't*: the closed
set has no value for fund economics; (b) *firm-didn't*: 6/7 don't disclose fees/AUM on
their marketing site anyway. Reading the empty field as "no business model" would be
wrong on both counts. This is a *different* flavor from the run-028/033 structured-surface
-absence branch: there, the empty token **masked real, disclosed market data** (a backfill
gap); here, the emptiness is the schema **correctly declining to assert** on an entity
the product taxonomy doesn't fit. The fix in 028/033 was backfill; the "fix" here (if
any) is a positive field set, not backfill.

## Evidence Used

All store-only; capture clocks per profile frontmatter. No external/current claims.

- `C1` — Slice membership: `grep -rl '^primary_industry: Finance & Fintech'` → 9;
  `grep -rl '^entity_type: Investor / Holding'` → 7; the 7 are a **subset** of the 9.
  Union = 9 (not the ~16 the Scout contract estimated). Reconciliation in receipt.
- `C2` — All 7 allocators carry `business_model:` empty (6) or `Other` (blueowl, 1);
  `portfolio_shape:` empty for all 7; verbatim "VC economics (mgmt fees + carry) aren't
  in the closed set" note in firstround/lsvp/spero-vc/thrivecap/standishspring frontmatter.
- `C3` — AUM/fund size/fees flagged "not on the marketing site (deep-research, not
  capture)" in `unverified_fields` of sequoiacap, lsvp, firstround, thrivecap,
  standishspring (5/7).
- `C4` — spero-vc: "Fund II ($125M, 2024-vintage)" stated on-site; Fund I size unstated.
- `C5` — blueowl: "~$315B AUM" stated, flagged as "the firm's own marketing stats … not
  independently verified"; `business_model: Other` with note "management + performance/
  incentive fees on AUM; no taxonomy value fits asset-management fee economics."
- `C6` — runway: all three tiers "Unlock pricing / quote-only" (`unverified_fields`);
  `business_model: Subscription`. stripe: `business_model: Usage-based / Consumption`,
  "per-transaction / %-of-volume fees."
- `C7` — Contract refs: TAXONOMIES.md:19 (`Investor / Holding` value), :72
  (portfolio_shape empty-by-rule for investors, never `Other`), :108 (`Other` is the
  escape on category fields, not portfolio_shape); business_model closed set = 8 values,
  none covering AUM-fee/carry economics.

## Companies Seen

9 (full union, treated as the complete in-store finance slice as of capture, NOT the
complete market): **Allocators (7):** blueowl-com, firstround-com, lsvp-com,
sequoiacap-com, standishspring-com, spero-vc, thrivecap-com. **Fintech products (2):**
stripe-com, runway-com.

## Missing / Stale Coverage

- The union is only 9 — a thin, mostly-VC cohort (5 of 7 allocators are early/multi-stage
  VC firms; only blueowl is a public asset manager and only stripe is large-scale
  fintech infra). Any "finance market pattern" claim is n-limited and subtype-skewed.
- 5 of 7 allocators do not disclose AUM/fees/fund sizes on-site — this is a **market
  disclosure norm**, not a capture gap (the store correctly flags it not-found).
- `primary_industry: Finance & Fintech` appears as 4 distinct *lines* in a naive `uniq`
  (6 value-only + 3 with inline `# comment` suffixes); the YAML *value* is clean, but an
  exact-line `==` match against the bare string under-counts by 3. Use substring/per-file
  `grep -rl`. Mirrors run-033 G1 cross-field under-count. (Verifier fix: the 3 are
  comment-suffixed lines, not trailing-whitespace values.)

## Source Gaps

- **No external denominator drawn** (store-only by contract). Whether the store's 9 is
  representative of "the finance vertical" is unknowable store-only — but the question is
  a schema-fit probe, not a market-completeness claim, so this is acceptable.
- The decision-grade finance facts (fees, AUM, vintage) are a **deep-research source
  family** the store deliberately doesn't capture from marketing sites — confirmed by 5/7
  `unverified_fields` notes. A finance read that needed them would require a non-marketing
  source (SEC ADV, Form D, PitchBook), out of scope here.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger IDs O1–O5, S1, G1, W1, F1 for Loop 2 to append to
`discovery-ledger.md`.

## External Completeness Check

Not run (store-only; question is schema-fit, not market completeness). Flagged as a Source
Gap rather than performed.

## Market Pattern

1. **The store's "finance vertical" is 7 capital allocators + 2 fintech products** — a
   capital-allocation cohort, not a fee-bearing-services cohort. The product taxonomy
   fits the 2 products and is *correctly gated off* the 7 allocators.
2. **Capital allocators expose a 4th, deeper gate-type:** the marketing site isn't a
   pricing surface at all (founder/LP recruiting), so fee economics are structurally
   off-site — distinct from the gate-a-real-price pattern of telehealth/SaaS/luxury.
3. **MRL-015 is two problems, not one:** the *subtractive* gate (don't force product
   fields on investors) is **solved and working**; the *additive* shape (a positive
   capital-allocator field set: stage / AUM band / vintage / thesis / LP type) is the
   **open gap**, and it's the first vertical where prose-only genuinely fails a
   recognizable cross-entity reader cut.

## What Would Change This Answer

- A **second, larger finance cohort** (more asset managers / PE / banks / fintech infra,
  not 5/7 early-stage VC) — would test whether the "no positive shape" gap recurs or is
  a VC-cohort artifact, and whether `business_model: Other` (blueowl) recurs for
  fee-bearing allocators.
- A **downstream reader actually asking for a structured finance cut** ("all seed funds,"
  "funds > $1B") — would move the additive-field gap from theoretical to load-bearing and
  decide whether it graduates past "leave as prose."
- If allocators commonly disclosed fees/AUM on-site (they don't, 5/7), the gap would be a
  capture-backfill problem (like 028/033) rather than a schema-shape problem.
