# VISUAL.md — the `visual.md` module contract

> **What this is.** The living contract for the opt-in **`visual.md`** module — a per-company
> **visual-evidence layer**: cited, blind, falsifiable cards across four families (typography,
> layout, color/brand/imagery, iconography) plus a ~5-second prose **Visual & brand impression**,
> mined from screenshots of the company's own site. This is the spec you **obey** when authoring a
> `store/<domain>/visual.md`; the *why* (destination, scope, the score that stays parked) is the
> [frame](../experiments/2026-06-13-visual-quality-graduation-frame/FRAME.md) and its
> [success criteria](../experiments/2026-06-13-visual-quality-graduation-frame/SUCCESS_CRITERIA.md).

> **CAPS vs lowercase.** `VISUAL.md` (this file) = the **contract**. `store/<domain>/visual.md` =
> the **instances** that obey it. Same word, two roles — the case tells them apart.

> **Module convention.** Module contracts are CAPS files under `modules/`. [`OFFERINGS.md`](OFFERINGS.md)
> was the first; this is the second. A **module** = a gathering recipe + a schema + a destination;
> this doc is the schema half. The recipe + blind protocols ship with the [`/visual-evidence`](../skills/visual-evidence/SKILL.md)
> skill; the lint is [`scripts/visualcheck.py`](../scripts/visualcheck.py); instances live at `store/<domain>/visual.md`.

## The boundary — what this does NOT do (read this first)

This module emits **observable visual State** — *what is visibly on the page* — and stops there. It is the engine-ownable half of the [State/Judgment line](../_design/2026-05-29-frame.md). Specifically it does **not**:

- **Emit a quality score.** No `1-5`, no PQR-lite scale, no "overall visual quality" number, no frontmatter quality field. Scoring failed calibration through v5 (raters sit 1–2 buckets above Brian; `weak` never fires) and stays an experiment track against frozen ground truth ([BACKLOG "Visual-quality SCORE — parked"](../BACKLOG.md)). **`visualcheck.py` fails the file if a `score:`/`rating:` field appears anywhere** — the parked line is mechanical, not a promise.
- **Gate a downstream decision.** The cards inform a human (the brief) or a *consumer-owned* judgment (execution-quality, capture-depth). The engine never treats a card as a decision.
- **Judge business, clinical, or copy quality**, SEO/traction (Signals), or anything off the visual axis. Not a live-web audit — judgment runs on captured tiles, after QA.

If you find yourself wanting to rank sites or attach a number, stop: that's the parked layer, not this one.

## When to write it

**Opt-in — enablement = the file exists** (no config). Write `visual.md` for a company **only** when a consumer needs a visual read: the human-facing **brief** (its creative-director consumer values a cited visual/brand impression; [presentation layer](../_design/2026-06-12-presentation-layer.md)), or a consumer-side **execution-quality** signal. Default everywhere else: **don't write the file.**

Run it through the [`/visual-evidence`](../skills/visual-evidence/SKILL.md) skill — a **blind pass over already-captured screenshots**, never inside `/research-company` capture (the capturing agent has read the dossier; it can't be the blind miner). Own freshness: `visual.md` carries its **own `captured_at`** (a re-tile / re-mine), independent of `profile.md`.

**Hard floor — decline over fabricate.** If a site's pages are all capture-contaminated and Tier-B browser re-render can't recover a clean tile (rare), there's nothing to mine — **record the decline** in `## Provenance` (`Skipped: no clean tiles — <reason>`) rather than mine defects out of broken captures. A page with a modal or a grey hero is *unusable evidence*, not a poor-design example (the frame's capture-hygiene principle).

## Frontmatter — doc-meta + capture-scope

```yaml
---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: functionhealth.com        # company key (matches profile.md)
captured_at: 2026-06-14           # own freshness — when these tiles were mined
source_capture: 2026-06-01        # the captures/<date>/ the tiles were derived from
qa_status: clean | exclusions-noted | recapture-used   # closed set (below)
---
```

- **`qa_status`** (closed set) — the capture-health verdict the QA gate reached: `clean` (all cited tiles came straight from cached payloads, no exclusions) · `exclusions-noted` (≥1 tile excluded for contamination; the `## Provenance` exclusion note names them) · `recapture-used` (Tier-B browser re-render supplied ≥1 page's tiles because the cached Firecrawl screenshot was contaminated — WebGL/lazy/animation; the note names which pages).

## Body — impression first, cards as the audit trail

Order: `## Visual & brand impression` → `## Evidence cards` → `## Provenance`. (Seed exemplar: [`store/goinfusive-com/visual.md`](../store/goinfusive-com/visual.md).)

- **`## Visual & brand impression`** — a short, cited prose read (≤120 words) a creative director judges in ~5 seconds: what the site's visual presentation *is* — its character, where it's controlled, where it falls down. **Every claim points at a card id** (`[typography_01]`) — the impression is a *lens over the cards*, never new assertions. It synthesizes only from **accepted** cards; if the cards don't support a line, it doesn't go in. This is the brief's deliverable.

- **`## Evidence cards`** — the falsifiable core. **One card per distinct visible tell**, in YAML (schema below) — comprehensive, not capped to a number. Spans the four families and a mix of polarities. The impression up top is the tight read; these cards are the full audit trail, so depth here is a feature. (Merge only true duplicates — cards pointing at the *same* tell.)

- **`## Provenance`** — tiles read (the `captures/<date>/tiles/` set), the **QA note** (exclusions named, whether Tier-B re-render was used and for which pages), and a point-in-time caveat (the site changes; this is a snapshot of the captured tiles).

### The card schema

```yaml
- id: typography_01                     # <family-stem>_<NN>
  family: typography_hierarchy          # closed set (4, below)
  polarity: strong | mixed | poor       # NOT a score — a direction
  page_or_region: "homepage hero"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-04-y04880.png"
  claim: "One calibrated sentence a reader can verify in the cited tile."
  visible_tells:
    - "Specific visual evidence (≥1 required)."
  confidence: high | medium | low       # closed set
  contrast_with: "store/.../tiles/.../tile-NN.png"   # OPTIONAL — within-company only
```

**Closed sets:**
- **`family`** — `typography_hierarchy` · `layout_composition_components` · `color_brand_imagery` · `iconography_illustration`. (The four v5 mining families.)
- **`polarity`** — `strong` · `mixed` · `poor`. A **direction, not a magnitude** — it says *which way this tell points*, not how good the site is. Generic competence is `mixed`, not `strong`; broken fundamentals are `poor`.
- **`confidence`** — `high` · `medium` · `low` (how cleanly the tell reads from a static tile).
- **`contrast_with`** *(optional)* — a tile path on the **same domain** for a useful within-company contrast (a strong hero vs. a weak chart on the same site). **Cross-company contrast is out** — the engine is per-domain; comparing sites is a downstream consumer's job.

## The rules (what the lint enforces)

`python3 scripts/visualcheck.py --slug <slug>` is the gate — it must pass. The load-bearing rules:

1. **No score, ever.** No `score:` / `rating:` / `quality:` field, and no `N/5` or `N/10` quality figure, anywhere in the file. This is the parked-line guard — the one rule that makes "evidence, not score" mechanical.
2. **Tile paths valid + active.** Every card's `tile_path` (and `contrast_with`) **exists on disk** under the company's `captures/<date>/tiles/`, and is **not** in the run's exclusion list. A card can't cite a tile that isn't there or was excluded for contamination.
3. **Falsifiable.** Every card has a non-empty `claim` and **≥1 `visible_tell`**. A card with no tell is a vibe, not evidence.
4. **Closed sets.** `family`, `polarity`, `confidence`, and `qa_status` each hold a value from their set above.
5. **Impression is a lens.** `## Visual & brand impression` is present and **cites card ids**; it introduces no claim absent from the cards.
6. **Structural.** Frontmatter keys present (`schema_version`, `domain`, `captured_at`, `source_capture`, `qa_status`); both body sections present; no leaked tool-call tags (shared `storelint` guard).

## Capture & QA — clean tiles, or none

Evidence quality is capped by tile quality — capture hygiene is **phase one, not cleanup**. Two tiers (recipe + protocols ship with the [`/visual-evidence`](../skills/visual-evidence/SKILL.md) skill):

- **Tier A — cached (default, zero-cost).** Slice the full-page screenshot the capture already stored (`captures/<date>/.payloads/<page>.png`) into native-resolution tiles (`scripts/tile.py`, `sips`-cropped). Native tiles surface the defects full-page downsampling hides.
- **Tier B — browser re-render (escalation).** When the QA gate flags a contaminated page the cached screenshot can't fix — a WebGL/grey hero, black media cards, lazy-load gaps, or mid-animation reveals — re-render it in a real browser (`scripts/shoot.py`: Playwright drives system Chrome with real WebGL, warm-scrolls to fire lazy media, then reduced-motion + settle so animations finish before tiling). No Firecrawl spend. Tiles land beside the capture; `qa_status: recapture-used`.

The **QA gate** runs before mining: it inspects each page's tiles, excludes or remediates contamination, and emits the active tile manifest + exclusion list the blind miners are confined to. Capture status is **split from design judgment** — a broken hero is a capture caveat, never a `poor` card.

## Invocation

The [`/visual-evidence`](../skills/visual-evidence/SKILL.md) skill is the only writer. It runs a blind fan-out over already-captured (or Tier-B re-rendered) tiles: QA + tile → four family miners in parallel (each a fresh, tiles-only, no-network agent) → judge/prune → synthesize the impression → write + lint. Blinding is structural — the miners never see `profile.md`, the dossier, Notion, or live web, so reputation can't contaminate the read. The default `/research-company` capture is **untouched**; visual evidence is a separate, opt-in pass.
