# AIO / SEO mining — how do real companies make themselves discoverable to LLMs?

*2026-06-05. The corpus holds ~88 captured companies across telehealth, B2B SaaS, luxury, and consumer.
This probe mines them for **concrete, stealable discoverability tactics** — biased toward **AIO** (getting
cited/surfaced by ChatGPT, Claude, Perplexity, Google AI Overviews) over classic SEO, since AIO is the
newer, higher-value question. Output is a catalog: each tactic with an example, a citation, and a one-line
"steal this" → [`FINDINGS.md`](FINDINGS.md).*

## The question

> Mine the corpus for how real companies make themselves discoverable — in classic search, and especially
> in LLM / AI answers. Catalog the tactics actually in use, with examples and citations, so we can crib the
> good ideas. Rank by common × clever; flag where verticals diverge.

## The catch — settled first

SEO/AIO signals live in exactly the page furniture Firecrawl **markdown strips**: `<meta>`, JSON-LD,
`robots.txt`, `llms.txt`, sitemaps. So before mining, work out what the store already keeps vs. what's gone:

| Signal | In the store? | Where |
|---|---|---|
| `<meta>` / og / twitter / canonical | **Yes** | `captures/*/.payloads/*.json` → `data.metadata` (+ `rawHtml`). Markdown drops it; the **raw payload keeps it**. |
| **JSON-LD / schema.org** | **Yes** | `.payloads/*.json` → `data.rawHtml`, the `<script type="application/ld+json">` blocks (74% of homepages ship one — confirmed by the [signal-audit](../2026-06-01-signal-audit/)). |
| hreflang, `<header>`/`<nav>` | Yes | `rawHtml` |
| **robots.txt** | **No** (0/88) | never captured — a per-host file, not a page |
| **llms.txt** | **No** (1/88) | never captured |
| **sitemap.xml** | **No** (0/88) | never captured |

So the harvest has two halves: **extract** meta + JSON-LD from the payloads we already paid Firecrawl for,
and **fetch** the three AIO-native files we never grabbed. Those three are tiny static text files — plain
`urllib`, no Firecrawl credits ([per the brief](../../CLAUDE.md)).

## Method

**1. Deterministic harvest** ([`harvest.py`](harvest.py) → [`summarize.py`](summarize.py)) — the
*commonality* backbone, $0, re-runnable:
- Fetches `robots.txt`, `llms.txt`, `llms-full.txt` for all 88 domains in parallel (browser UA; SPA
  catch-alls that 200-serve `index.html` for `/llms.txt` are rejected by a non-HTML guard).
- Parses robots into per-crawler posture, splitting **training** bots (GPTBot, ClaudeBot, Google-Extended,
  CCBot, Bytespider…) from **retrieval/answer-time** bots (OAI-SearchBot, ChatGPT-User, PerplexityBot,
  Claude-User…) — because blocking *retrieval* bots is an AIO own-goal, blocking *training* bots isn't.
  A bot is only counted as a deliberate stance if it's **named** in its own group, not if it inherits a
  normal `User-agent: *` rule.
- Mines JSON-LD `@type` inventory (union across every captured page) + homepage meta from the payloads.
- → `_out/signals/<slug>.json` (per company, with verbatim bodies), `_out/raw/*.{robots,llms}.txt`
  (citable), `_out/matrix.{json,md}` (the corpus table).

**2. Workflow fan-out + synthesis** ([`mine.workflow.js`](mine.workflow.js)) — the *cleverness* layer that
a script can't judge:
- **9 extractor agents**, one per vertical batch (telehealth ×4, B2B SaaS ×2, consumer, luxury, other),
  each reads its companies' harvested signals + raw files and returns concrete tactics with verbatim
  examples + citations + "steal this".
- **1 synthesis agent** (barrier — needs all batches at once) dedupes, ranks by actionability then
  prevalence × cleverness (AIO-first), and writes the vertical-divergence cuts, fed the **exact** rollup
  counts so prevalence isn't eyeballed.

Division of labor: the **script computes how common**, the **agents find the clever examples**, the
**synthesis ranks**. Verticals: telehealth 47 · B2B SaaS 22 · consumer 9 · luxury-watch 7 · other 3.

## Repro

```bash
cd "$WEB_RESEARCH_HOME"
python3 experiments/2026-06-05-aio-seo-mining/harvest.py     # fetch + extract → _out/
python3 experiments/2026-06-05-aio-seo-mining/summarize.py   # rollups + matrix.md
# then the workflow (mine.workflow.js) over _out/, args = _out/wf_args.json
```

## Caveats (read before over-trusting)

- **Live-fetch snapshot, one day (2026-06-05).** robots/llms/sitemap are fetched now; the JSON-LD/meta are
  as-captured (capture dates vary by company). A site can change its `llms.txt` or AI-crawler stance any day.
- **6/88 robots unreachable** — `rolex.com`/`keeps.com` genuinely 404 their robots; `ford.com`/`swatch.com`
  hard-block non-browser UAs (Akamai); `innerbalance` 429'd. Counted as "not observed," not "absent."
- **Absence ≠ proof.** "No FAQPage schema" means none on the *captured* pages (homepage + key pages), not
  none site-wide. JSON-LD on deep article/product pages we didn't capture is invisible here.
- **llms.txt presence ≠ quality.** The script confirms a non-HTML text file exists; whether it's a useful,
  current, well-curated one is the agents' qualitative read.
- **Self-authored signals are seed-to-verify.** JSON-LD `AggregateRating`/`alternateName` are marketing-
  shaped (the signal-audit's caution) — cited verbatim + flagged, never blind-trusted.
</content>
