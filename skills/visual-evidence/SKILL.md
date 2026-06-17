---
name: visual-evidence
description: >
  Mine an already-captured company's screenshots into a blind, cited visual-evidence layer at
  store/<domain>/visual.md — falsifiable cards across typography / layout / color-brand-imagery /
  iconography, plus a ~5-second Visual & brand impression. Use when the user wants a visual-quality
  read, a brand/design impression, or "how good does X's site look" from captured screenshots:
  "/visual-evidence acme.com", "visual evidence for X", "mine X's design", "what's my read on X's
  site". Reads cached captures (Tier-A) and re-renders contaminated pages in a real browser (Tier-B);
  zero Firecrawl spend. It emits observable visual STATE — evidence + impression — and never a score,
  quality field, or ranking (that layer is parked). Runs on a company already in the store; if there's
  no capture yet, capture it first with /research-company.
---

# /visual-evidence — mine a company's visual evidence (blind)

Turn `visual-evidence X` into `store/<domain>/visual.md`: cited, blind, falsifiable evidence cards + a prose impression a creative director reads in ~5 seconds. **The contract is [`modules/VISUAL.md`](../../modules/VISUAL.md)** — read it first (the card schema, the closed sets, and the boundary). This skill is the recipe half; the lint is [`scripts/visualcheck.py`](../../scripts/visualcheck.py).

**What this does NOT do:** no score, no quality field, no ranking. If you catch yourself wanting a number, stop — that's the parked layer ([BACKLOG](../../BACKLOG.md)). `visualcheck.py` fails the file if a `score:` field appears.

**The whole game is blinding.** The miners must judge only what's visible — never the company's reputation, dossier, or live site. So: **do not read `profile.md`, Notion, or the live web during this run**, and synthesize the impression only from the returned cards. The capturing agent saw the dossier; that's why visual evidence is a *separate, blind* pass, never folded into `/research-company`.

## Resolve the engine root + the capture

```bash
ENGINE="$(cd "$(dirname "$(realpath "$0")")/../.." 2>/dev/null && pwd)"   # the repo holding this skill
# canonical fallback: "/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research"
cd "$ENGINE"   # run every `python3 scripts/…` command below from here — the paths are engine-root-relative
```

The company must already be captured. `store/<slug>/captures/<date>/.payloads/<page>.png` is the input. No capture → tell the user to run `/research-company <domain>` first (this skill never scrapes).

After resolving the slug and confirming the capture exists, stamp the run clock:
```bash
RUN_STARTED_AT="$(python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" now)"
```

## The loop

**1. Tile the cached screenshots (Tier-A, free).**
```bash
python3 scripts/tile.py --slug <slug> --pages homepage pricing <…>   # curate to real page screenshots
```
Pick the pages that carry the visual system (homepage + 2–4 signal pages); skip capture-experiment variants (`homepage_enhanced_lazyload.png`, etc.). Tiles + `overview-480w.png` land in `captures/<date>/tiles/`.

**2. QA gate — clean tiles, or remediate (vision, the load-bearing step).** Read each page's `overview-480w.png` and spot-check tiles. Capture hygiene is phase one, not cleanup — a contaminated tile is *unusable evidence*, not a poor-design example. Flag:
- **modal / cookie banner / newsletter overlay** covering content,
- **grey or blank hero** (WebGL/canvas that didn't render), **black media/video cards**, **lazy-load gaps**,
- **mid-animation** capture (faded reveals, count-ups still at 0.0), **full-page compositing artifacts** (repeated hero).

For each flagged page, decide:
- **Exclude** the contaminated *tile(s)* if the rest of the page is clean → note them; `qa_status: exclusions-noted`.
- **Re-render (Tier-B)** when the page's evidence depends on a region the cached shot got *statically* wrong — grey/WebGL hero, black media, lazy-load gaps, unsettled animation — **or** an overlay covers the content. Add `--dismiss` for the overlay case:
  ```bash
  python3 "$ENGINE/scripts/shoot.py" "https://<page url>" --out-dir "$ENGINE/store/<slug>/captures/<source-capture>/tiles/<page>" [--dismiss]
  ```
  `shoot.py` drives system Chrome (real WebGL), warm-scrolls to load lazy media, then reduced-motion + settles, tiles, and emits `overview-480w.png` for the QA gate. `--dismiss` clears overlays through the page's *own* affordances — Escape + clicks on dismiss-buttons scoped to overlay-shaped elements; no vendor denylist, no CSS-hide ([probe](../../experiments/2026-06-16-tier-b-dismissal/FINDINGS.md): structural-hide harmed real nav 4/8 sites; affordance-only cleared 5/5 dismissable overlays, 0/8 harm). Replace the page's tiles with the re-rendered set; `qa_status: recapture-used`. (No Firecrawl; needs `playwright` — if your resolved `python3` lacks it, call the interpreter that has it, e.g. a pyenv binary.)
  - **The page URL comes from the capture's stamp — never grep the body.** Read it from the cleaned `.md`: `grep -m1 '^source_url:' store/<slug>/captures/<date>/<page>.md`. The body opens with nav/CTA links, so grepping it mis-picks (functionhealth → a `my.*/signup` CTA). Pre-stamp captures (predate the `source_url` header) fall back to that page's `sourceURL` in `.payloads/manifest.jsonl` if it survives; otherwise re-capture rather than guess.
  - **Tier-B is a comparison, not an automatic upgrade.** Check the re-render against the cached shot before adopting — sometimes cached wins (alange-soehne, 2026-06-16: live Chrome rendered the hero *black* + scroll-locked while the cached hero was clean). If the re-render is worse, keep cached and ship `exclusions-noted`.
  - **Render into the `source_capture` (dossier) date dir**, the same `captures/<date>/` `tile.py` tiled — not `<today>` — so `visual.md` cites one tiles root and `source_capture` stays the dossier date (VISUAL.md). `captured_at` carries today.
  - **Dual-render only when WebGL/lazy *and* an overlay contaminate one page** — the cached payload can't be the faithful baseline, so render twice into sibling dirs: `tiles/<page>` (faithful, no flag) + `tiles/<page>__dismissed` (`--dismiss`). Cards cite the `__dismissed` set; the faithful tiles are kept on disk as the comparison view. (The WebGL-incompleteness that triggers this can read as intentional dark design — spot the flat-dark hero before classing a page overlay-only.)
  - **Timed/marketing modals** (newsletter, "10% off") — if there's a dismiss control (Escape, "No thanks", "×"), `--dismiss` may clear it in one shot. If the modal re-arms during the warm-scroll loop (gethealthspan, 2026-06-16 — see [BACKLOG](../../BACKLOG.md)) or has no dismiss path, a guard fires (below); exclude or caveat the tile instead.
  - **Pass `--out-dir` absolute** (as above), and **never disable the sandbox** to dodge a path-permission / `getcwd` error — that once left a sticky lockdown that killed a run.
  - **Loud-not-silent.** A `WARNING` on stderr (and the matching manifest field) means a guard fired — don't ignore it: `dismiss_cleared=false` (the overlay didn't clear — closed shadow root / off-list labels; compare to cached, exclude or caveat), `scroll_locked` (still locked after dismiss — fall back to cached or exclude), a **thin/interstitial page** (bot-wall / login-gate / splash captured as the page — exclude or use a non-walled path), or a missing `overview-480w.png` (magick failed — fall back to tile spot-check).
- If a page can't be made clean at all, drop it. If *nothing* is clean, **decline** and record it in `## Provenance` — don't mine defects out of broken captures.

Assemble the **active tile list** (all kept tile paths, repo-relative) and the **exclusions** (path + reason).

**3. Blind mining + judge (the workflow).** Hand the active tiles to the fan-out — 4 family miners in parallel (each a fresh, tiles-only agent) → judge/prune. The miners are blind by construction; StructuredOutput validates every card:
```
Workflow({ scriptPath: "skills/visual-evidence/mine.workflow.js",
           args: { slug: "<slug>", engineRoot: "$ENGINE", tiles: [<active tile paths, repo-relative>], exclusions: [{path, reason}] } })
```
It returns `accepted_cards` (with ids), `rejected_cards`, and judge `notes`, with **tile paths already repo-relative** — the workflow absolutizes them for the blind reads and relativizes on return, so author them straight into `visual.md` (no hand-rewrite). The four miners default to **Sonnet** — it holds Opus's calibration even on the dark-gradient seduction case at ~⅕ the per-token cost ([experiment](../../experiments/2026-06-14-visual-miner-model-calibration/FINDINGS.md)); override with a `minerModel` arg. The **judge inherits the session model** (Opus on an Opus session) — the cross-family prune/merge is the higher-reasoning step, and it absorbs Sonnet's chattier output.

**4. Synthesize + write `store/<slug>/visual.md`** per [`modules/VISUAL.md`](../../modules/VISUAL.md):
- **First, spot-check every `poor` *structural* card against its native tile.** Miners and judge are both blind — neither can tell a mid-animation/compositing artifact (double-rendered row, cards mid-flight, blank icons) from a genuine layout defect, so a capture artifact can slip through as a `poor` card. This is the one check the workflow can't self-perform; drop any such card before writing.
- Frontmatter: `schema_version: "1.0"`, `domain`, `captured_at` (today — when tiles were mined), `source_capture` (the **dossier** capture date this layer pairs with; stays the dossier date even when Tier-B re-renders fresh tiles today — see VISUAL.md), `qa_status` (from step 2).
- `## Visual & brand impression` — ≤120 words, **only from the accepted cards**, every claim citing a card id (`[typography_01]`). A lens over the cards, never new assertion. This is the brief's deliverable.
- `## Evidence cards` — the accepted cards as a `yaml` block (the schema in VISUAL.md).
- `## Provenance` — tiles read, exclusions named, whether Tier-B was used and for which pages, and a snapshot caveat.

**5. Lint.** `python3 scripts/visualcheck.py --slug <slug>` — must exit 0 (tile paths valid + active, closed sets, ≥1 tell per card, impression cites ids, and **no score anywhere**). Fix anything it flags.

**6. Record the run, then report.**

**Write the run record _before_ you report — the run is not done until it's written** (this is the step agents drop). Record what *actually ran*:
```bash
python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" write \
  --slug <slug> \
  --verb visual-evidence \
  --started-at "$RUN_STARTED_AT" \
  --artifact visual.md \
  --components-json '[{"tool":"claude-code","model":"sonnet","role":"visual-miner:typography_hierarchy"},{"tool":"claude-code","model":"sonnet","role":"visual-miner:layout_composition_components"},{"tool":"claude-code","model":"sonnet","role":"visual-miner:color_brand_imagery"},{"tool":"claude-code","model":"sonnet","role":"visual-miner:iconography_illustration"}]'
```
Tool is env-detected for **both Claude Code and Codex** — no `--tool` needed. Pass `--model <id>` if you know it (a session `export RUNREC_MODEL=…` is authoritative; else `unknown`). **`components` must be the miners that actually ran — never copy the four above as boilerplate.** The four-miner list is correct *only* when you ran the `mine.workflow.js` blind fan-out (use the `minerModel` model if it was overridden). **If the workflow runner was unavailable and you did a degraded manual pass** (no fan-out — e.g. a Codex session without the Workflow tool), drop the four miners, record the single pass you actually did (or omit `--components-json`), **and pass `--status partial`.** A Tier-B Playwright render is deterministic shell work, not an LLM component; mention it in `--note` only if it matters.

Then report. One line: company → `store/<slug>/visual.md`, N cards across the four families, `qa_status`, any pages that needed Tier-B re-render.

## Why a workflow (not hand-rolled sub-agents)

The fan-out is 4 blind miners + a judge with schema-validated card output. The workflow buys three things a loose `Agent` fan-out doesn't: **structural blinding** (each miner is a fresh context with only tile paths — it can't reach the dossier), **schema validation** (vision agents emit messy YAML; StructuredOutput retries until each card is well-formed), and **determinism + reuse** (the same script, re-runnable, validate-many in parallel). The miner and judge prompts live in [`mine.workflow.js`](mine.workflow.js) — that's their single source of truth, so there's no protocol doc to drift from it.
