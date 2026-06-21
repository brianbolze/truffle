# Market Read

## Question

Across the captured store, how does each profile mark its own uncertainty
(`unverified_fields`, `# STRAIN` markers, hedged `site_notes` prose, absence-as-not-found),
and can a downstream reader distinguish a high-confidence captured fact from an
inferred / point-in-time / scope-omitted one **at query grain** — or is the store's
"honesty layer" a heterogeneous catch-all that does not compose into a usable trust signal?

## Result

**The store has a strong honesty *discipline* but not a queryable confidence *surface*.**
The self-uncertainty layer is real and dense — `unverified_fields` is present and
**non-empty in 130/130 profiles** (424 items total, mean 3.26/profile, range 1–6; `C1`) —
but it is a **free-text prose catch-all that mixes at least six kinds of caveat with very
different reader meaning**, so a reader *cannot* mechanically answer "is the specific value
I'm about to use verified?" The discipline answers "what did the capture *not* nail down,"
not "how confident is field X."

Derived breakdown of the 424 `unverified_fields` items (`C2` — heuristic keyword
classifier + sample-validation; **the taxonomy is my own Judgment, the bucket shares are
approximate ±a few points**, not a captured field):

| Caveat kind | ~Share | Reader meaning | Greppable? |
|---|---|---|---|
| **Not-public / not-captured** ("not on the marketing site," "deep-research job," gated price, unnamed pharmacy) | **~48%** | A field is **absent** — says nothing about confidence in *present* values | No (prose) |
| **Internal-inconsistency / conflict** (store honestly holds two captured values) | **~12%** | High-value: do **not** trust either value blindly | No (prose) |
| **Inferred / claim-not-verified** ("parent inferred from footer," "firm's own stat, not verified," "JSON-LD only") | **~11%** | High-value: the genuine per-fact **confidence** signal | No (prose) |
| **Point-in-time / volatile** (the contract's "point-in-time snapshot, not fixed" line) | **~11%** | Value is real but unstable run-to-run | **Yes** — literal string (`C3`) |
| **Scope-omission / partial-capture** ("not written this run," "not individually scraped") | **~7%** | Capture-scope decision, not data uncertainty | No (prose) |
| **Branding / visual-asset capture-fail** (fonts/logo/og:image/brand-color) | **~6%** | Capture-fidelity noise, **not** data confidence | No (prose) |
| capture-method/tooling artifact (JS-wall, 404, funnel) | ~4% | Why a field is missing | No (prose) |

The two high-reader-value kinds — **inferred** (~11%) and **internal-inconsistency**
(~12%) — together are only **~23%** of the list, and they are interleaved in the same
unlabeled free-text bullets as the dominant ~48% completeness-notes and the ~6% branding
noise. The one kind that **is** mechanically greppable is *point-in-time* — and only
because SCHEMA contracts a literal string for it (`C3`).

**Direct answer:** a reader can grep "is this capture volatile?" (point-in-time literal),
but **cannot** grep "is this present value inferred / conflicted / verified?" — those
signals exist, are honest, and are well-written, but live only as prose and do not compose
into a trust signal at query grain. `query-time-grouping-enough` is **FALSE** for "retrieve
all low-confidence facts," yet the fix is **not** a new field (see Market Pattern).

## Gap Map

**Where Truffle answered cleanly:**
- **The discipline is genuinely present and honest.** 130/130 profiles carry non-empty
  `unverified_fields`; the contract rule ("fill only what captured pages support; else
  `unverified_fields`, never a guess" — SCHEMA.md:23) is visibly lived. Strong examples of
  the high-value kinds: `alange-soehne-com` "parent: richemont.com is **inferred** from
  footer corporate-governance links, not an explicit ownership statement"; `blueowl-com`
  "Headcount/AUM figures are the **firm's own marketing stats** … not independently
  verified"; `hormonemd-com` "Founding year (2023) + founder … from homepage **JSON-LD
  only**; no on-page corroboration"; `gogeviti-com` "free-tier panel listed as both '$399'
  and 'full panel from $349' on the **same card**"; `beta-team` "facility size — homepage
  says 188,000 sq ft; timeline says **188,500**" (`C4`). The store reports discrepancies
  rather than silently reconciling them — exactly the contract's instruction.
- **Absence discipline holds.** Caveats consistently say "not enumerated / not on the site /
  unnamed," i.e. *not-found-on-captured-pages*, never "the company has none" (`C4`). The
  read inherits and respects this: a profile with no caveat on field X means **no caveat
  recorded**, NOT "X is verified" (`C5`).

**Where it fell short (the composability gap):**
- **`unverified_fields` is one prose bucket doing six jobs.** The dominant ~48% is a
  *completeness* note (field absent), which a naive reader could mistake for a *confidence*
  flag on a present value. The ~23% that are real confidence signals (inferred/conflict)
  are not separable by query.
- **The caveat names its field in prose, not as a joinable key.** "parent: richemont.com is
  inferred" is human-readable but does not bind to the `parent:` frontmatter field as a
  confidence attribute — you cannot ask "show me every frontmatter value flagged inferred."
- **Confidence/provenance is scattered across five partially-overlapping destinations**
  (`C6`): `unverified_fields` ("couldn't get it"), the `Enriched (model knowledge)`
  Provenance line ("got it — from the model"), inline `# STRAIN` notes, free-prose
  discrepancy reports, and the point-in-time literal. None is a unified "how confident is
  this fact" surface; each captures a slice.
- **Drift into the bucket.** ~7% scope-omissions ("roster intentionally not written this
  run" — `henrymeds`-style) arguably belong in Provenance `Couldn't get` / `Run profile`,
  not `unverified_fields`; ~6% are branding-payload capture failures (fonts/logo/og) that
  are capture-fidelity, not data-confidence.

**`# STRAIN` markers (the other self-uncertainty surface):** 80 lines across 58 profiles;
**~70% (56) are branding/visual** (brand_colors/logo/font corrections), 14 (~18%) touch a
classification field, ~10 other (inferred/owns/target-market notes) (`C7`). This
**confirms and quantifies run-027's finding**
that STRAIN is mostly a Firecrawl-branding-payload correction layer, **not** a
classification-confidence signal — so STRAIN does not rescue the confidence-grain gap
either.

## Evidence Used

Store-only; all derived counts reproducible from local files. No external/current claims.

- `C1` — `unverified_fields` non-empty in 130/130 profiles; 424 items, mean 3.26, range
  1–6. Method: parse the YAML list block under `unverified_fields:` in each
  `store/*/profile.md` frontmatter. (`receipts/unverified-fields-taxonomy-2026-06-20.md`)
- `C2` — six-kind taxonomy + approximate shares (not-public ~48% / inconsistency ~12% /
  inferred ~11% / point-in-time ~11% / scope ~7% / branding ~6% / tooling ~4%). Heuristic
  keyword classifier over the 424 items, sample-validated; **shares are derived Judgment,
  not a captured field**. (receipt)
- `C3` — point-in-time is the only greppable kind, via the SCHEMA-contracted literal
  "point-in-time snapshot, not fixed" (SCHEMA.md:112). ~11% of items carry the volatility
  flavor.
- `C4` — verbatim high-value exemplars (alange inferred parent; blueowl self-reported AUM;
  hormonemd JSON-LD-only founding; gogeviti $399/$349 conflict; beta 188,000/188,500 sq ft;
  henrymeds "does not enumerate" states). Quoted from each profile's `unverified_fields`.
- `C5` — absence-discipline: no run-wide instance of "company has none"; caveats are
  "not-found-on-captured-pages." (sampled across the 424 items)
- `C6` — five confidence/provenance destinations named in SCHEMA.md (`unverified_fields`
  ln 58/23; `Enriched (model knowledge)` ln 152; inline `# STRAIN` ln 22; discrepancy-
  reporting ln 23; point-in-time literal ln 112).
- `C7` — STRAIN: 80 lines / 58 profiles; ~70% (56) branding/visual, ~18% (14)
  classification-field, ~12% (10) other. Method: grep `STRAIN` across `store/*/profile.md`,
  keyword-bucket each line (heuristic; corrected from a first-pass 73% over-attribution per
  Loop-2 verifier).

## Companies Seen

All 130 profiled companies (the `unverified_fields` census) across telehealth, SaaS/Tech,
watches/luxury, consumer goods, energy, automotive/aero, and investor/holding slices.
High-value exemplars cited verbatim: alange-soehne, blueowl, hormonemd, gogeviti, beta-team,
henrymeds, sequoiacap, qualtrics, rolex, swatch, uber, waldo-fyi.

## Missing / Stale Coverage

Corpus is uniformly recent (`captured_at` spans 2026-05-30 → 2026-06-20; 33 May / 97 June),
so capture-*recency* is not a limiter here — the gap is structural (prose vs queryable),
not stale. No write-back or capture worklist is produced (this is a meta/calibration read,
not a coverage read).

## Source Gaps

None external. The read is fully answerable store-only; the only "missing source" is a
*structured* confidence attribute, whose absence **is** the finding, not a coverage gap.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger IDs **O1–O5, S1, G1, W1, F1** for Loop 2 to append to
`discovery-ledger.md`.

## External Completeness Check

Not load-bearing (no membership/denominator claim). The 130-profile `unverified_fields`
population is a census of the discipline, not a market set.

## Market Pattern

**The engine's honesty is a *capture discipline*, not a *consumption surface*.** Everything
traces to the capture and nothing is guessed (the discipline is excellent), but the trust
metadata that proves it is **write-optimized prose for a human auditor**, not
**read-optimized structure for a delegating agent**. The single counterexample —
point-in-time volatility — is greppable *precisely because* SCHEMA gave it a literal token;
that is the template for any fix.

This generalizes **MRL-008's run-026 finding** ("a bare State field isn't self-describing":
`parent:[]` can't distinguish independent vs not-stated) from one field to the **whole
uncertainty layer**: the layer can't self-describe *as confidence* because it is an
unlabeled prose bucket. It also **confirms run-027** (STRAIN is ~73% branding-payload, not
field-strain).

**Anti-sprawl verdict (builder lens):** the lightest fix, *if anything ever graduates*, is a
**convention, not a new field** — give the two high-value kinds a greppable prefix token the
way point-in-time already has one (e.g. an `inferred:` / `conflict:` lead-token on those
`unverified_fields` lines), and route scope-omissions to Provenance where the contract
already wants them. Zero new schema, zero migration blast-radius, no `confidence:` field
per fact (which would be false-precise across 424 heterogeneous caveats and would rot). The
honest answer may also be **"no new primitive needed"**: a human auditor reading one profile
is served fine today; only a *cross-store agent query* is blocked, and there is no live
consumer for that yet.

## What Would Change This Answer

- A real downstream consumer that needs to **filter facts by confidence at scale** (not
  per-profile) — that would turn the composability gap from latent to binding and justify
  the prefix-token convention.
- Evidence that the inferred/conflict prose **is** reliably machine-parseable as-is (a
  stricter NLP pass than my keyword heuristic) — would weaken the "not queryable" claim.
  My classifier left ~5% genuinely ambiguous and the shares are approximate; a different
  rater would move bucket edges but not the headline (no greppable confidence token exists
  for inferred/conflict).
- A SCHEMA change that consolidated the five confidence destinations — would directly
  resolve `C6`.
