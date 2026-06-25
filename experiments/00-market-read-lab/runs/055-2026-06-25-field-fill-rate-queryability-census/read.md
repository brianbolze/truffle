# Market Read

## Question

Across all captured `store/<domain>/profile.md` files (N=136), what is the population
rate of each SCHEMA frontmatter field, and which fields are populated reliably enough that
a downstream system can *filter/group* on them — versus which are so sparse, or so
default-/comment-masked, that grouping on them silently drops companies?

**Frame:** a fill-rate is a *capture-coverage* fact about the corpus, never a market fact.
This is a calibration/system-test read; the deliverable is a dependability map for the
"build on top without re-capturing" consumer, not a market claim.

## Result

**Headline: the required scalar contract is 100% present, but "present" splits into four
dependability tiers — and two of them are traps a naive consumer walks into.** (C1 census,
store-only, N=136.)

### Tier 1 — Dependable, discriminating cuts (filter/group safely)
Every profile carries these and the values are real:

| Field | True-fill | Modal value share (concentration) |
|---|---|---|
| `domain` / `name` / `schema_version` | 136/136 (100%) | identity keys — unique |
| `captured_at` / `capture_method` | 136/136 (100%) | clock present on every profile |
| `entity_type` | 136/136 | **90% `Company`** — 13 non-Company are the meaningful minority |
| `primary_industry` | 136/136 | **52% Healthcare** (single-vertical pile) |
| `target_market` | 136/136 | 43% `[B2C]` |
| `offering_category` | 133/136 (97%) | 32% telehealth `[Services/Consulting, Biotech/Pharma]` |
| `business_model` | 130/136 (95%) | 48% `Subscription` |
| `portfolio_shape` | 129/136 (94%) | 40% `Multi-product` |
| `description` | 136/136 | free text — always present |
| `unverified_fields` | **136/136 (100%)** | every profile carries an honesty block (C4) |
| `color_scheme` | 136/136 | 84% `light` |

**Caveat that travels with Tier 1 (C2): 100% filled ≠ evenly discriminating.** A naive
`group-by primary_industry` drops 52% of the store into one Healthcare pile;
`group-by entity_type` is 90% one value; `target_market` is 43% a single token. These are
dependable to *read* but weak as *partition* keys — the cut exists but is lopsided. (This
is the empirical store-wide version of run-039 G1's "SaaS pile is one undifferentiated
bucket.")

### Tier 2 — Subtractive-empty fields: the empties are *meaningful*, not coverage holes (C3)
`business_model` (6 empty), `portfolio_shape` (7 empty), `offering_category` (3 empty) are
NOT randomly missing — **every empty is an `Investor / Holding` entity.** The `business_model`
empties are the 6 VCs (firstround, lsvp, sequoiacap, spero-vc, standishspring, thrivecap);
`portfolio_shape` adds blueowl, an asset manager that carries `business_model: Other` (not
blank) because the closed set has no AUM-fee value. So the union of subtractive empties is 7
investor entities, all `entity_type: Investor / Holding`. The closed set deliberately has
no value for "AUM + carried-interest" economics, so the blank *encodes* entity shape. This
is run-035's empty-business_model finding, now sized store-wide and shown to be perfectly
correlated with `entity_type: Investor / Holding`. A consumer should read these blanks
through `entity_type`, not as missing data.

### Tier 3 — Sparse relation fields: cannot be used as a population key (C5)
| Field | True-fill |
|---|---|
| `aliases` | 80/136 (58%) |
| `parent` | **18/136 (13%)** |
| `owns` | **16/136 (11%)** |

Filtering or grouping on `parent`/`owns` silently drops ~87–89% of the store. Their
sparsity is a genuine mix of true-negative (the company has no parent) and not-captured —
**indistinguishable from the field alone.** This is the L005 corollary ("structured
absence ≠ market absence") sized: the vertical relation axis is structurally first-class
(run-039 S1) but populated too thinly to be a query population key. It answers "does THIS
company name a parent?" reliably; it cannot answer "show me all subsidiaries."

### Tier 4 — Optional module layers are a telehealth-concentrated overlay (C6)
Module presence is **not** store-wide; it tracks the intentional deep-telehealth cohort:

| Vertical (n) | `offerings.md` | `visual.md` | `signals/` | avg body chars |
|---|---|---|---|---|
| Healthcare & Life Sci (71) | **81%** | **49%** | **74%** | 9,372 |
| Technology (27) | 18% | 11% | 3% | 8,905 |
| Finance & Fintech (9) | 11% | 11% | 0% | 8,161 |
| Consumer Goods (6) | 0% | 16% | 0% | 9,577 |
| Energy & Utilities (5) | 0% | 0% | 0% | 7,331 |
| store-wide | 52% (71/136) | 32% (44/136) | 40% (54/136) | — |

Two things at once: **(a)** the profile *body* is roughly uniform depth (~8–9k chars) across
verticals, so the core read is comparably deep everywhere; **(b)** the *module layers*
(offerings/visual/signals) are ~4–25× denser on telehealth. A downstream system that treats
`offerings.md` or `signals/` as a store-wide ingredient is really leaning on a telehealth
overlay — outside Healthcare it is mostly absent.

### Trap A — the fail-loud-by-comment convention defeats naive structured parsing (C7)
The store records subtractive emptiness as `business_model:    # empty — VC economics…`.
A naive parser that splits the line on `:` and takes the remainder reads the **comment text
as the value** — my own first census pass counted `business_model` 100% non-empty until I
stripped inline `#` comments, which revealed the 6 true empties. The fail-loud channel
(human-readable inline comment) is *anti*-machine-readable: the guard that protects a human
reader actively misleads a naive downstream parser. (Cousin of run-037 DR2's
"STRAIN-comment is an unreliable second channel," here on the structured-emptiness channel.)

## Gap Map

- **Clean answer:** Tiers 1–4 are fully recoverable store-only; the dependability map is the
  result. A `gap-probe`/calibration whose payload is the map itself.
- **Where the store is strong:** required-scalar contract is genuinely 100%; `unverified_fields`
  is the one *always-present* guard field (136/136), so every profile self-discloses its
  soft spots. Subtractive emptiness is consistent and `entity_type`-gated.
- **Where it falls short as a query substrate:** (1) relation fields too sparse to partition
  on; (2) high-fill fields are concentration-lopsided, so "group-by" buckets unevenly;
  (3) module layers are telehealth-skewed, not store-wide; (4) the inline-comment empty
  convention is a parsing trap for naive consumers.
- **What would change it:** a parser that strips inline comments before reading values
  (cheap, read-side) flips Trap A from a hazard to a non-issue — no schema change. Nothing
  here argues for a new field.

## Evidence Used

All store-local; no external sources, no spend.

- `C1` — per-field present/non-empty counts over 136 `profile.md` frontmatters (grep/awk;
  values read as text *before* any inline `#` comment).
- `C2` — modal-value share per Tier-1 field (concentration).
- `C3` — the 6 `business_model`-empty / 7 `portfolio_shape`-empty / 3 `offering_category`-empty
  domains are all `entity_type: Investor / Holding` (firstround, lsvp, sequoiacap, spero-vc,
  standishspring, thrivecap, blueowl).
- `C4` — `unverified_fields` non-empty 136/136.
- `C5` — `parent` 18/136, `owns` 16/136, `aliases` 80/136 (comment-stripped).
- `C6` — module presence (`offerings.md` / `visual.md` / `signals/`) bucketed by
  `primary_industry`; body length = chars after first `## ` header.
- `C7` — first census pass counted `business_model` 100% non-empty; comment-stripped pass
  found 6 true empties — the inline-comment masking, reproduced.

## Companies Seen

All 136 captured domains (census). Notable sub-sets: the 7 investor/holding entities (Tier-2
subtractive empties); the 71 Healthcare profiles carrying the dense module overlay.

## Missing / Stale Coverage

Not a coverage read per se, but the census *is* a coverage map: outside Healthcare, the
optional module layers (offerings/visual/signals) are largely uncaptured — a deliberate
cohort choice (deep telehealth), surfaced here as a quantified asymmetry rather than a defect.

## Source Gaps

None external. The only "missing surface" is internal: no single field distinguishes a
true-negative relation (`parent: []` because none exists) from a not-captured one — that
disambiguation lives in prose/`unverified_fields`, not in the structured field.

## Raw Learning to Preserve

See `run-notes.md` Observations: `S1` (four-tier dependability), `G1` (relation sparsity sized),
`S2` (subtractive-empty is entity_type-gated), `G2` (module layers telehealth-concentrated),
`R1` (inline-comment parsing trap / Trap A), `S3` (concentration ≠ discrimination),
`S4` (`unverified_fields` the lone always-present guard).

## External Completeness Check

N/A — store-only census; the denominator IS the captured corpus, stated as such. No outside
denominator is load-bearing because no market-completeness claim is made.

## Market Pattern

No market claim. System pattern: **the store's dependability is tiered, and the tier
boundaries are not visible from "is the field filled?" alone** — a consumer must combine
fill-rate, value concentration, `entity_type` gating, and the inline-comment convention to
know what it can build on. The required scalars + `unverified_fields` are the bedrock;
relations and module layers are not store-wide substrate.

## What Would Change This Answer

- A real downstream consumer that needs to *partition* the store by a relation key would
  promote `parent`/`owns` sparsity from "noted" to "blocking" — but the lightest fix is
  capture worklist, not a field.
- If a naive (non-comment-stripping) parser is ever put in front of the store, Trap A (C7)
  becomes a live correctness bug; the fix is a read-side convention ("strip inline comments
  before reading a frontmatter value"), not a schema change.
- "No new primitive needed" stays live: every finding is a *reading*/parsing convention or a
  capture-coverage fact, not a missing field.
