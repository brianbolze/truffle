# serpapi.py — Google organic + AI Overview capture

Fetches one Google query through [SerpAPI](https://serpapi.com) and parses **two signals**: the
**AI Overview** block and the **top-10 organic results**. Emits parsed JSON to stdout — no store
write, no brand-matching, no vertical baked in. A caller decides where it lands and what to match.

```bash
python3 tools/serpapi.py "best NAD provider 2026"                 # 2 calls: organic + AIO
python3 tools/serpapi.py "compounded tirzepatide online" --organic-only   # 1 call: organic only
python3 tools/serpapi.py "best online TRT clinic 2026" --gl us --hl en --device desktop
```

Auth: `SERP_API_KEY` from the environment, falling back to a `.env` at the repo root (gitignored).

## What it does now vs. what it could grow into

**Now — `engine=google` only.** Organic web results + the AI Overview. That's the whole scope.

**Could grow into** — SerpAPI exposes many more engines behind the same key and HTTP shape. Each
is a *scoped* addition (a new `engine=`, its own result-shape parser, a pinned version), not a
rediscovery:

| Engine | Signal it would add |
|---|---|
| `google_news` | dated news mentions (an *event* signal — belongs to a traction consumer, not State) |
| `google_shopping` | product listings, price, merchant |
| `google_maps` / `google_local` | local pack, "near me" intent, review counts |
| `google_scholar` | citations / research footprint |
| `google_trends` | search-interest over time (today served by `trends.py`) |

Keep the boundary deliberate: extend by adding an engine + its parser, **not** by widening this
file into a general SerpAPI client. One source-shape per parser, one version pin per shape.

## The gotchas (most of the value)

These cost a probe or a real bug to learn. Carry them forward; don't relitigate them live.

- **Parser is version-pinned (`v2`); drift fails loud.** Google has reshaped the AI surface ~3×
  in a year — surface drift is the highest-impact failure mode. `validate_aio_shape_v2` checks the
  AIO shape; on a mismatch the tool **warns to stderr, emits `schema_drift`, suppresses the parsed
  AIO fields (no parse-on into plausible-but-wrong output), and exits 3**. Bump the version only on
  an *intentional* migration — never to silence a real change.
- **AI Overview is non-deterministic; organic is the stable channel.** AIO is LLM-synthesized and
  rotates within hours (a NAD capture had AgelessRx + Jinfiniti one day, neither the next). Organic
  is SEO-mediated and moves on a far slower clock. **Capture both, diff independently** — when AIO
  names a brand organic doesn't, that disagreement is the instability tell, not a parse error.
- **AIO-absent is data.** When Google renders no AIO, the tool sets `ai_overview_present: false`
  and lets organic carry the rank signal. It never falls back to treating organic *as* the AIO.
  `ai_overview_skipped` distinguishes "we chose `--organic-only`" from "Google rendered none."
- **AIO arrives two ways.** Usually behind a `page_token` (the second call). Sometimes Google
  returns the body **inline** in the first response (`text_blocks` populated, no token) — same
  shape, parsed unchanged (live-observed 2026-05-07).
- **A `page_token` can still yield nothing.** Google sometimes declines the async body even after
  handing back a token; SerpAPI returns `{"error": "Google hasn't returned any results…"}` on call
  2. That's semantically "no AIO" → `ai_overview_present: false`, **not** schema drift (live-observed
  2026-W21 on 6/7 categories).
- **Two AIO list-item formats.** `labeled` — `"Best Value: PartiQlar …"` (prefix ∈ Best/Other/
  Recommended/Top); `bare` — just a brand name, short and capitalized, no colon. Anything else
  (e.g. a `"Lab Fees: …"` considerations row) is rejected as noise. The parser captures the raw
  snippet and tags the format; *splitting and matching individual brands is the caller's job.*

## Output shape

The shared **envelope** keys (`tool` … `cost`) lead; serpapi's own payload sits beside them. The
envelope is uniform across every tool in `tools/` — see the library README's Conventions.

```jsonc
{
  // --- shared envelope ---
  "tool": "serpapi",                   // which tool produced this blob
  "source": "serpapi.com",             // the external system actually hit
  "captured_at": "2026-06-08T19:42:00Z", // this invocation's wall-clock (UTC) — NOT a source date
  "ok": true,                          // capture completed cleanly; false -> see schema_drift
  "input": { "query": "best NAD provider 2026", "gl": "us", "hl": "en", "device": "desktop" },
  "schema_drift": [],                  // non-empty -> parsed fields suppressed, exit 3
  "parser_version": "v2",              // AIO shape is drift-prone -> version-pinned
  "cost": { "credits": 2 },            // 2 for a full capture, 1 with --organic-only or no AIO
  // --- payload ---
  "ai_overview_present": true,
  "ai_overview_skipped": false,        // true under --organic-only OR a declined async body
  "ai_overview_unavailable_reason": "…", // present only when a page_token yielded an error body
  "ranked_brands": [                   // [] when no brand-list block (a signal, not a bug)
    { "position": 1, "label": "Best Value", "after_colon": "PartiQlar …",
      "raw_snippet": "Best Value: PartiQlar …", "format": "labeled", "reference_indexes": [3] }
  ],
  "narrative_paragraphs": ["Based on 2026 data, …"],
  "headings": [],
  "references": [ { "index": 0, "source": "…", "title": "…", "link": "…" } ],
  "organic_results": [                 // always top-10 from call 1
    { "position": 1, "title": "…", "link": "…", "snippet": "…", "displayed_link": "…" }
  ]
}
```
