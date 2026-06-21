# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [source-rigor, query-time-grouping-enough, confidence-grain, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes. First cross-store audit of the engine's self-uncertainty
  layer. Clean calibration result: strong honesty *discipline*, no queryable confidence
  *surface*. No primitive proposed.
- **What was awkward?** The load-bearing taxonomy is a hand-rolled keyword classifier (my
  own Judgment), so bucket shares are approximate — flagged everywhere as derived, not a
  captured field. Loop 2 should pressure-test the inferred/conflict counts, not the headline.
- **What should the next agent know?** The high-value confidence kinds (inferred ~11%,
  internal-inconsistency ~12%) exist and are honest but live only in prose; only
  point-in-time is greppable (SCHEMA literal). This generalizes MRL-008 run-026
  ("bare field isn't self-describing") to the whole uncertainty layer, and confirms run-027
  (STRAIN ~73% branding). Coined pressure tag: `confidence-grain`.

## What happened

Parsed `unverified_fields` across all 130 profiles (424 items), taxonomized into six kinds
via a keyword classifier + sample-validation, characterized the `# STRAIN` layer (80 lines /
58 profiles), and read the SCHEMA contract for what `unverified_fields` / STRAIN / Enriched /
point-in-time are *meant* to carry. Concluded the layer is a heterogeneous prose catch-all:
the answer to "can a reader grep verified-vs-inferred?" is no (except point-in-time), and
the lightest fix — if any — is a greppable prefix-token convention, not a new field.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | The store's self-uncertainty layer is a strong *discipline* but not a *surface*: `unverified_fields` is non-empty in **130/130** profiles (424 items, mean 3.26) yet is one free-text bucket doing ≥6 jobs. | read.md Result/`C1`,`C2`; receipt | The discipline (never guess; flag what's unsupported) is excellent; the gap is composability, not honesty. | ready-for-triage |
| O2 | observation | ~48% of `unverified_fields` items are **completeness** notes (a field is *absent*: "not on the marketing site," gated price, unnamed pharmacy), not confidence flags on *present* values. A naive reader conflates the two. | read.md `C2`,`C4` | The dominant use answers "what's missing," not "how confident is field X" — the question the safe-to-delegate reader actually asks. | ready-for-triage |
| O3 | observation | The two **high-reader-value** kinds — inferred/claim-not-verified (~11%) and internal-inconsistency (~12%) — exist, are honest, well-written (alange parent inferred; blueowl AUM self-reported; gogeviti $399/$349; beta 188k/188.5k) but live **only in prose**, ~23% of the list, interleaved with completeness notes + branding noise. | read.md `C4` | These are exactly the per-fact confidence signals a delegating agent wants, and they are not separable by query. | ready-for-triage |
| O4 | observation | **Point-in-time/volatile (~11%) is the ONLY greppable kind**, and only because SCHEMA contracts a literal string ("point-in-time snapshot, not fixed", SCHEMA.md:112). | read.md `C3` | The one working precedent for a queryable confidence token — the template for any fix. | ready-for-triage |
| O5 | observation | `# STRAIN` markers: 80 lines / 58 profiles, **~70% branding/visual** (brand_colors/logo/font; corrected from a first-pass 73% per Loop-2 verifier), ~18% classification-field, ~12% other. | read.md `C7`; receipt | Confirms + quantifies run-027: STRAIN is mostly Firecrawl-branding-payload correction, NOT a classification-confidence signal — it doesn't rescue the confidence-grain gap. | ready-for-triage |
| S1 | surprise | Confidence/provenance is **scattered across five partially-overlapping destinations** — `unverified_fields`, the `Enriched (model knowledge)` Provenance line, inline `# STRAIN`, free-prose discrepancy reports, and the point-in-time literal — none a unified "how confident is this fact" surface. | read.md `C6`; SCHEMA.md:22,23,58,112,152 | The trust metadata isn't just unstructured, it's *fragmented* by contract; a consumer would have to read all five. | ready-for-triage |
| G1 | gap | `query-time-grouping-enough` is **FALSE** for "retrieve all low-confidence facts" (no greppable token for inferred/conflict) — the first clean FALSE for that tag on a *trust-metadata* axis, distinct from the content reads where it fires TRUE. | read.md Result/Market Pattern | A real frontier the store can't see at query grain — but the fix is a convention, not a primitive (W1). | ready-for-triage |
| W1 | wish | If anything graduates, the lightest fix is a **greppable prefix-token convention** on the two high-value kinds (e.g. `inferred:` / `conflict:` lead-token, mirroring the existing point-in-time literal) + routing scope-omissions to Provenance — **not** a per-fact `confidence:` field (false-precise across 424 heterogeneous caveats, would rot). "No new primitive needed" is a live outcome. | read.md Market Pattern | Names the anti-sprawl fix consistent with "spend on conventions, not infra"; zero migration blast-radius. | recur-watch |
| F1 | friction | The load-bearing taxonomy required a hand-rolled keyword classifier over 424 free-text prose items; there is no structured field to group on, so every confidence read must re-parse prose. One sighting. | run-notes friction log; receipt Method | Mirrors the recurring MRL-002 prose-read friction, now on the *trust-metadata* grain; recur-watch only. | recur-watch |

## Inputs and scope

- **Universe:** 130 profiled companies (`store/*/profile.md`; 139 dirs, 9 capture-only
  stubs excluded per MRL-001 run-027 stub caveat — count `profile.md`).
- **Surfaces read:** `unverified_fields:` frontmatter block (all 130), inline `# STRAIN`
  lines, `site_notes` hedges (sampled), SCHEMA.md / TAXONOMIES.md contract for the intended
  meaning of each surface, MRL-008 (run-026 bare-field) + run-027 (STRAIN) as adjacent prior art.
- **Exclusions:** no live re-verification of any caveat (deferred bounded-live follow-up);
  no write-back; no scoring/ranking of profiles by trustworthiness.

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

One sighting (F1): the confidence read had no structured field to group on, so it required
a hand-rolled keyword classifier over 424 free-text `unverified_fields` strings. Mirrors the
recurring MRL-002 prose-read friction on a new (trust-metadata) grain; recur-watch only.

## Evidence limits

- The six-kind taxonomy and its bucket shares are a **derived heuristic Judgment** (keyword
  classifier + sample validation), not a captured field — shares are approximate (±a few
  points); a different rater moves bucket edges but not the headline (no greppable token
  exists for inferred/conflict). Reported as derived everywhere.
- "No caveat recorded" on a field ≠ "field verified" — the census sees only what each
  capturer chose to flag; absence language held to "not flagged," never "verified."
- Read is store-only and meta; no external/current/pricing claims, so no snippet risk.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live web, no mutation, no primitive, no score, no re-verification)
- Required citations / receipts present and source-graded: **pass** (`C1`–`C7`; receipt source_grade derived)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (none made; corpus capture span recorded)
- Absence language says "not found", not "not true": **pass** (held throughout; "no caveat recorded" ≠ "verified")

## Surprises

The high-value confidence signals (inferred, internal-inconsistency) *are* present and
honestly written — the surprise is that they're a minority (~23%) buried in prose with no
token, while the dominant ~48% is completeness-notes. And confidence is fragmented across
**five** contract destinations (S1), not one. See Discovery ledger O1–O5, S1.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

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

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `source-rigor` | The read is *about* source-rigor at the meta level: whether the store exposes its own confidence. Generalizes MRL-008's run-026 "bare field isn't self-describing" to the whole uncertainty layer. | submit Evidence Log entry to MRL-008 (new branch: the layer doesn't compose as confidence) |
| `query-time-grouping-enough` | Fires **FALSE** for "retrieve all low-confidence facts" — first clean FALSE on a trust-metadata axis (content reads fire it TRUE). | watch — the fix is a convention, not a primitive (W1) |
| `confidence-grain` (**coined**) | The store has a confidence *discipline* but no queryable confidence *surface*; the highest-value kinds live only in prose, fragmented across 5 destinations. Existing tags (`source-rigor`/`depth-backfill`) cover *specific* signal confounds or *missing modules*, not the meta "is confidence a queryable surface?" question. | submit triage candidate (new item or MRL-008 branch); hold for 2nd sighting before any convention graduates |
| `coverage-caveat` | Absence-of-caveat ≠ verified; census sees only flagged items. | no-op (handled in-read) |

## Optional triage evidence

Normally none. Add only concrete backlog evidence, with priority/status suggestions,
when the run has more than a raw singleton or when review adds evidence to an existing
item. Keep this to 1-3 backlog-ready bullets plus pointers to the Discovery ledger,
`discovery-ledger.md`, or run artifacts.

**Do not implement, spike, or recommend immediate graduation from inside the run.**
Raw learning belongs in the run Discovery ledger and `discovery-ledger.md`. Submit
triage only when the run adds enough evidence for a stewarded backlog item or Evidence
Log entry.

Loop 2 should decide between: (a) a new MRL item ("confidence layer is a discipline, not a
queryable surface"; tag `confidence-grain`), or (b) an Evidence Log branch on **MRL-008**
(this is the meta-generalization of its run-026 "bare field isn't self-describing" branch).
Single sighting either way — hold, do not graduate. The W1 prefix-token convention is a
*wish*, not a proposal.

## Next-run advice

- A second confidence-grain sighting (e.g. a downstream read that actually needs to filter
  facts by confidence at scale, or one that re-parses `unverified_fields` prose for a
  different question) would move `confidence-grain` from coined-singleton toward a documented
  convention. Until a real consumer needs cross-store confidence filtering, "no new
  primitive needed" stands.
- The deferred bounded-live follow-up (spot-check whether `unverified_fields` caveats
  decayed since capture) is a clean, separate, spend-gated run — not autonomous-safe.
- Re-using this run's classifier: treat its bucket shares as approximate; the headline
  (no greppable token for inferred/conflict) is robust to re-rating.
