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
- **Re-render (Tier-B)** when the page's evidence depends on a region the cached shot rendered *statically* wrong — a grey/WebGL hero, black media, lazy-load gaps, unsettled animation:
  ```bash
  python3 "$ENGINE/scripts/shoot.py" "https://<the page url>" --out-dir "$ENGINE/store/<slug>/captures/<today>/tiles/<page>"
  ```
  `shoot.py` drives system Chrome (real WebGL), warm-scrolls to load lazy media, settles motion, hides known consent vendors (OneTrust/Transcend/Cookiebot/Didomi), then tiles. Replace that page's tiles with the re-rendered set; `qa_status: recapture-used`. (No Firecrawl; needs `playwright` — `pip install playwright` once.)
  - **Don't Tier-B a timed/marketing modal** (newsletter, "10% off") — a fresh load just re-arms it, often over different content; exclude or caveat the tile instead.
  - **Pass `--out-dir` absolute** (as above), and **never disable the sandbox** to dodge a path-permission / `getcwd` error — that once left a sticky lockdown that killed a run. The fix is the absolute path, not a bigger hammer.
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

**6. Report.** One line: company → `store/<slug>/visual.md`, N cards across the four families, `qa_status`, any pages that needed Tier-B re-render.

## Why a workflow (not hand-rolled sub-agents)

The fan-out is 4 blind miners + a judge with schema-validated card output. The workflow buys three things a loose `Agent` fan-out doesn't: **structural blinding** (each miner is a fresh context with only tile paths — it can't reach the dossier), **schema validation** (vision agents emit messy YAML; StructuredOutput retries until each card is well-formed), and **determinism + reuse** (the same script, re-runnable, validate-many in parallel). The miner and judge prompts live in [`mine.workflow.js`](mine.workflow.js) — that's their single source of truth, so there's no protocol doc to drift from it.
