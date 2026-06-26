# source_page.py — one-page capture + reduce

Fetches **one** web page and reduces it to source-page evidence — title, normalized visible text,
and absolute outbound links — then prints **one** JSON envelope to stdout. Direct HTTP by default
(zero spend); an explicit `--firecrawl-fallback` spends at most one Firecrawl credit when direct
HTTP can't get the page. No store write, no classification, no `page_role`.

```bash
python3 tools/source_page.py https://example.com/best-things-2026/
python3 tools/source_page.py https://www.forbes.com/health/...  --firecrawl-fallback   # spend 1 credit only if direct fails
python3 tools/source_page.py <url> --timeout 30 --max-bytes 4000000 --max-text-chars 200000 --max-links 300
```

Auth: only the fallback needs `FIRECRAWL_API_KEY` (env first, repo-root `.env` fallback, via `_env.load_key`).
The direct-HTTP path needs no key.

## What it is (and what it deliberately is not)

This lifts the one durable primitive from the cohort-discovery page-extraction probe — *opening a
source/listicle page and reducing it to text + links materially improves later evidence reuse* (it
moved that packet's telehealth P@10 0.100→0.600) — and leaves every packet-local concern behind. It
captures **page-grain source evidence**, not company State and not a judgment.

| The tool does (capture) | The caller does (judgment) |
|---|---|
| fetch one URL, reduce to `title` / `text` / `links` | decide whether the page is a listicle, directory, owned comparison, or noise |
| emit absolute links with `domain` + `position` | extract entities / brands / candidates from those links |
| report `ok` = useful evidence vs. not | decide whether the page is *worth capturing* into a cohort or the store |
| print one envelope to stdout | route it to a cohort, a source panel, or `store/` (with shell redirection) |

There is **no** `page_role`, cohort, candidate, capture-worthiness, membership, entity-extraction, or
page-classification field — those are caller judgments. Caller context can ride under `input` (it's
echoed verbatim), but the tool never decides *why* the page matters. It writes nothing: persistence
is the caller's `> file.json`.

## The `ok` contract (load-bearing — read this)

`ok:true` means **"captured useful reduced evidence"**, not "a transport returned some bytes". The
probe's permissive `ok` (any non-empty text) would pass JS shells, gzip-garbage, and mojibake; this
tool refuses all three. `ok:true` requires **all** of:

1. a **2xx/3xx** status,
2. a **text/HTML** body (declared content-type contains html/xml/text; or, when the header is
   absent, no NUL bytes in the head),
3. a **clean decode** (≤5% U+FFFD replacement chars — see the gzip gotcha below),
4. a reduction at or above the **usefulness floor** (`MIN_TEXT_CHARS = 500` normalized chars).

Otherwise `ok:false` with the first failing reason in `error`. For binary/garbled bodies the parsed
fields are suppressed (parsing them yields junk); for HTTP errors and thin shells the parsed text is
**kept** — a 403 block page's text is real evidence of the block.

## The gotchas (most of the value)

- **A real browser UA is load-bearing.** The prior probe used a bot UA (`…page-extraction-probe/0.1`)
  and got 403'd by Forbes / U.S. News. This tool sends a plausible desktop Chrome UA, which clears
  most polite anti-bot gates — Flow Space and Tana reduce cleanly over direct HTTP, no spend. Hard
  bot-walls (Forbes) still 403; that's what `--firecrawl-fallback` is for.
- **gzip-despite-identity → garbled, not silent mojibake.** We ask for `Accept-Encoding: identity`,
  but some servers gzip anyway. If they set `Content-Encoding: gzip`/`deflate` we decompress (stdlib).
  If they gzip *without* the header, the bytes are undecodable — the U+FFFD replacement-ratio check
  catches it and returns `ok:false` ("garbled body") instead of emitting binary-as-text. `br`
  (brotli) is not in the stdlib, so a br-encoded body also fails loud rather than parsing to junk.
- **`text_chars` is the full reduced length; `text` may be capped.** `text` is truncated to
  `--max-text-chars` (default 300k) for a sane envelope; `text_chars` always reports the full reduced
  length, and the usefulness floor is judged against the full length. Same split for `links`
  (capped to `--max-links`, default 400) vs. `link_count` (full count).
- **Links are absolutized against the page's *final* URL** (after redirects), with `domain`
  www-stripped. A `<base href>` tag is **not** honored (rare; documented limitation) — relative links
  on a `<base>`-using page resolve against the final URL, which is correct for the vast majority.
- **The fallback is a fallback, not a mode.** Firecrawl fires **only** when direct HTTP returned
  `ok:false` **and** `--firecrawl-fallback` is set. A successful direct capture never spends, even
  with the flag on. The call goes through the shared [`_firecrawl.py`](_firecrawl.py) caller. One
  scrape call, no retry: **every** failure — missing key, transport/HTTP error, unparseable JSON,
  `success:false`, or thin markdown — fails loud as an `ok:false` envelope (never a crash) and does
  **not** trigger a second paid call.
- **No schema-drift validator.** Open-ended HTML has no pinned upstream schema, so `schema_drift` is
  always `[]` and there is no exit-3 path. Don't cargo-cult a `validate_*_shape()` onto this reducer
  (unlike serpapi/trustpilot, whose upstreams *are* drift-prone).

## Output shape

Conforms to the library's reserved envelope spine (`tool · source · captured_at · ok · input ·
schema_drift`, plus `cost` on the metered fallback path); the source-page payload sits beside it.

```jsonc
{
  // --- reserved envelope spine (tools/README.md) ---
  "tool": "source_page",
  "source": "direct_http",                  // direct_http | firecrawl.dev/scrape — the mechanism used
  "captured_at": "2026-06-26T18:42:11Z",    // THIS invocation's wall-clock, UTC — not a source date
  "ok": true,                               // useful reduced evidence captured (see the ok contract)
  "input": { "url": "https://tana.inc/blog/best-otter-alternatives-2026/",
             "firecrawl_fallback": false, "timeout": 25, "max_bytes": 2500000,
             "max_text_chars": 300000, "max_links": 400 },
  "schema_drift": [],                        // ALWAYS [] — no pinned upstream schema, no exit-3 path
  // --- payload, beside the spine ---
  "status": 200,                             // HTTP status (null on a transport failure)
  "content_type": "text/html; charset=utf-8",
  "final_url": "https://tana.inc/blog/best-otter-alternatives-2026/",  // after redirects (the link base)
  "error": null,                             // populated string when ok:false
  "title": "Best Otter alternatives for AI meeting notes in 2026 - Tana",
  "text": "Best Otter alternatives … ",      // normalized visible text, capped to --max-text-chars
  "text_chars": 14514,                       // FULL reduced length (text above may be truncated)
  "links": [                                 // absolute links, capped to --max-links
    { "href": "https://tana.inc/pricing", "text": "Pricing", "domain": "tana.inc", "position": 2 }
  ],
  "link_count": 33                           // FULL link count (links above may be truncated)
}
```

On the Firecrawl fallback path, `source` becomes `firecrawl.dev/scrape`, `cost` appears, and `input`
carries the direct-HTTP error that triggered the fallback:

```jsonc
{ "tool": "source_page", "source": "firecrawl.dev/scrape", "ok": true,
  "input": { "url": "https://www.forbes.com/health/...", "firecrawl_fallback": true,
             "direct_http_error": "HTTP 403: Forbidden", "...": "..." },
  "schema_drift": [], "cost": { "firecrawl_credits_estimate": 1 },
  "status": 200, "content_type": "text/markdown",
  "title": "Study Finds The Most Affordable GLP-1 Providers in 2026 – Forbes Health",
  "text": "…", "text_chars": 105611, "links": [ … ], "link_count": 496 }
```

## Exit codes

- `0` — useful reduced evidence captured (`ok:true`).
- `2` — capture did **not** yield useful evidence (`ok:false`): transport/HTTP block, non-text/binary
  body, undecodable/garbled body, or a reduction below the usefulness floor. **One envelope is still
  printed to stdout** — the failure is loud (non-zero exit + a stderr line) but the evidence (status,
  error, any parsed block-page text) stays inspectable.
- There is no `3`: this reducer has no upstream schema to validate.

## Credits

Direct HTTP spends nothing. `--firecrawl-fallback` spends **at most one** base Firecrawl scrape credit
(`formats: ["markdown","links"]`, no LLM/json format, no enhanced proxy), and only when direct HTTP
already failed. One call per invocation, no retry — a failed/thin Firecrawl response does not re-spend.
`cost.firecrawl_credits_estimate` reports Firecrawl's own per-call `metadata.creditsUsed` when present
(the attribution-grade billed number — a multi-page PDF bills >1), else a 1-if-the-call-was-made estimate.

## See also

[`skills/research-company/firecrawl-capture.md`](../skills/research-company/firecrawl-capture.md) — the
canonical Firecrawl capture playbook: the hazard knobs (`maxAge:0` + `location:US` + `waitFor` vs. the
silent geo-misroute/cache collision), the cost add-ons, and the avoid-list (`json` LLM extract,
enhanced proxy, `/crawl`, monitoring). Read it before changing the fallback's request recipe. The call
itself goes through the shared [`_firecrawl.py`](_firecrawl.py) caller.
