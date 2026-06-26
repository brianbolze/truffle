# Proposal: Source Page Tool

Date: 2026-06-26
Status: accepted — approved for implementation by Brian; built + merged (build/graduation status lives in [`implementation-notes.md`](implementation-notes.md), per the note below)
Source request: Brian asked for a plan-only Agentic Build proposal to extract the generic page/listicle reduction layer from the cohort-discovery packet into `tools/source_page.py`.

<!-- Status tracks the PROPOSAL lifecycle only: proposed -> reviewed -> accepted | revise | park | cut.
     Never flip it to a build status. `implemented`, the implementation receipt, and the gate log
     belong in implementation-notes.md -- keep this file a plan, so proposal-review can gate it before code. -->

## Required Fields

risk: medium
write_scope: `tools/source_page.py`, `tools/source_page.md`, `tools/README.md`, plus focused parser fixtures/checks such as `tests/test_source_page.py` and `tests/fixtures/source_page/*.html` if implementation needs them. No `store/`, `cohorts/`, experiment-run, scheduled, or project write paths.
spend_stop: Proposal writing spends none. Future implementation defaults to direct HTTP only with zero paid credits. An explicit Firecrawl fallback acceptance check may spend at most one base scrape credit on one prior known blocked source page, with `markdown` and `links` only, no `json`/LLM extraction, no enhanced proxy, no batch scrape, and no retry loop. Stop before any second paid page, any write destination, or any source family beyond direct HTTP and explicit Firecrawl scrape fallback.
acceptance_checks: Implementation must produce an `implementation-notes.md` receipt showing: (1) unit tests or fixture checks prove the stdlib HTML reducer extracts title, normalized text, absolute links, `text_chars`, and `link_count`; (2) `python3 tools/source_page.py <url>` prints exactly one JSON object with the shared envelope keys from `tools/README.md`, exits 0 on useful direct captures, and writes nothing except stdout; (3) direct-HTTP smoke checks on prior packet pages such as Flow Space menopause and Tana Otter alternatives return `ok:true`, non-empty `title`, `text_chars` above 5,000, and evidence-bearing page text/links; (4) `ok` is explicitly defined and guarded: `ok:true` means the fetch completed and produced useful reduced evidence, not merely non-empty bytes; thin shells, binary/non-text content, undecodable or garbled compressed bodies, and pages below a documented usefulness floor such as 500 normalized chars return `ok:false` with `error` populated; (5) a known prior direct-fetch-blocked page such as the Forbes GLP-1 list returns a loud failure without `--firecrawl-fallback`, then returns `ok:true`, `source:"firecrawl.dev/scrape"` or equivalent, `cost.firecrawl_credits_estimate:1`, useful `text`, and `links` only when the flag is set; (6) fallback spend is negatively checked: one invocation makes at most one Firecrawl scrape call, does not retry automatically, and does not make a second paid call after a malformed or unusable Firecrawl response; (7) JSON shape includes `tool`, `source`, `captured_at`, `ok`, `input`, `schema_drift`, `status`, `content_type`, `error`, `title`, `text`, `text_chars`, `links`, `link_count`, and `cost` when relevant; (8) `schema_drift` is always `[]` and there is no exit-3 validator, because generic HTML has no pinned upstream schema; (9) negative checks confirm no `page_role`, cohort route, candidate route, capture-worthiness, page classification, raw-output path, or store/cohort write appears in the tool output or docs.
escalate_if: Implementation wants multiple URLs per invocation, caller-provided output paths, raw HTML persistence, `page_role`, candidate/entity extraction, cohort or source-panel logic, shared `_http.py`/`_firecrawl.py` helpers, LLM extraction, enhanced proxy, retries that can multiply spend, schema/lint/writer machinery, or any write under `store/`, `cohorts/`, or experiment folders.

## Problem

The cohort-discovery worklist packet proved one reusable thing: opening source/listicle pages and reducing them to text plus links materially improves later evidence reuse. The page extraction probe moved telehealth P@10 from 0.100 to 0.600 and conversation-intelligence P@10 from 0.500 to 0.600 because the source pages contained company names and links hidden behind SERP result rows.

But the probe is packet-local and bundled with cohort evaluation, qrels, ranking, candidate construction, and run writes. Truffle needs the smaller durable primitive first: capture one source page, reduce it, and emit a reusable envelope. Everything downstream can decide whether that page matters.

## Short Answer

Add `tools/source_page.py` as a print-only capture tool for one URL per invocation. It should do direct HTTP first with a real user agent, bounded body read, and stdlib HTML reduction; Firecrawl scrape is available only behind an explicit fallback flag.

Do not add page classification, raw-output paths, candidate routing, cohort storage, or helper abstractions yet. This is the smallest real system change that preserves the useful part of the prior packet without graduating `/cohort-discovery`.

## Constraints / Non-Goals

- One URL per invocation; no batching or orchestration.
- Print one JSON envelope to stdout; callers redirect if they want a file.
- No writes to `store/`, `cohorts/`, experiments, `.payloads/`, or scratch paths.
- No cohort logic, candidate routing, capture-worthiness, membership, entity extraction, source-panel building, or page classification.
- No durable `page_role`. Caller context may be echoed under `input`, but the tool must not decide whether a page is a listicle, directory, owned comparison page, or source artifact.
- No shared HTTP/Firecrawl helper until a second durable caller earns it.
- No Firecrawl LLM extraction, `json` format, `/crawl`, `/batch/scrape`, monitoring, or enhanced proxy.

## Options considered

1. **Direct HTTP only.** Lowest complexity and zero spend. This matches most of the probe and keeps the tool obviously generic. It fails the known useful blocked-page case: Forbes and U.S. News needed Firecrawl fallback in the prior run. [could have]
2. **Direct HTTP default with explicit Firecrawl fallback.** Direct HTTP remains the normal path; blocked pages can be captured only when the caller opts into `--firecrawl-fallback`. This preserves the prior probe's practical coverage while keeping spend visible and bounded. [should have] -- recommended
3. **Wider source-page capture utility with raw-output paths and `page_role`.** This would make the next discovery workflow easier to wire, but it crosses the boundary too early. Output paths create writer semantics, and `page_role` is a judgment that belongs to the caller or worklist layer. [cut]

## Recommendation

Build option 2: a narrow capture-and-reduce tool with explicit fallback.

The load-bearing bet is that source-page evidence becomes reusable when it has a standard envelope and compact payload, even before Truffle has any cohort storage convention. The tool should be boring: fetch page, reduce page, print envelope. A future worklist can cite the envelope, store it, classify it, or ignore it.

I would push back on adding caller-provided raw-output paths. Shell redirection already solves persistence without giving the tool write authority. If a later reusable workflow needs raw HTML sidecars, that should be a separate storage proposal, not a hidden feature in the capture primitive.

## Implementation Sketch

1. Start from the generic pieces in `page_extraction_probe.py`: direct `urllib` fetch, bounded read, real user agent, simple HTML parser that skips script/style/noscript/svg, title extraction, text normalization, absolute link extraction, domain normalization, and capped emitted `text`/`links`. Tighten the probe semantics for a durable tool: handle or fail loud on compressed bodies that ignore `Accept-Encoding: identity`, respect charset when available, reject binary/non-text responses, and require a documented minimum reduced-text floor before `ok:true`.
2. Shape the CLI like other single-verb tools:
   - `python3 tools/source_page.py <url>`
   - optional `--firecrawl-fallback`
   - optional bounded knobs only if needed for checks, such as `--timeout`, `--max-bytes`, `--max-text-chars`, and `--max-links`.
3. Emit one envelope matching `tools/README.md` conventions:
   - reserved keys: `tool:"source_page"`, `source`, `captured_at`, `ok`, `input`, `schema_drift`, optional `cost`;
   - payload keys beside the spine: `status`, `content_type`, `error`, `title`, `text`, `text_chars`, `links`, `link_count`;
   - `schema_drift` stays `[]`; this reducer has no fixed upstream schema and should not invent a parser-version gate.
4. Implement Firecrawl fallback inline, not as `_firecrawl.py`: load `FIRECRAWL_API_KEY` via `_env.load_key`, call `/v2/scrape` with `formats:["markdown","links"]`, `maxAge:0`, US location, and no LLM formats. Make it one paid call per invocation with no automatic retry; malformed or thin Firecrawl output should fail loud in the envelope, not trigger a second call.
5. Add `tools/source_page.md` with CLI examples, output shape, exit codes, Firecrawl spend warning, and gotchas carried from the probe.
6. Update `tools/README.md` to list the tool and document that it is page-grain source evidence, not cohort or company state.
7. Add focused tests/fixtures only where they reduce risk: parser behavior, envelope shape, no-write/no-page-role negative checks. Live smoke checks can be documented in `implementation-notes.md` because they require network and optional Firecrawl spend.

## Review Notes

Risk is medium because this adds a durable `tools/` entry and optional paid fallback, not because the code should be large. Lead context treats paid capture posture as a high-risk line; this stays medium only because the paid path is explicit, one-page, one-call, uses the existing Firecrawl key posture, and is guarded by a negative spend check. If implementation wants retries, batching, enhanced proxy, or automatic fallback, reclassify or return to review.

The main review question is whether the fallback belongs in v1. My recommendation is yes, but only as an explicit flag, because the prior packet already found valuable source pages that direct HTTP could not reduce. Direct-HTTP-only is cleaner, but it would knowingly omit a proven source-page class and force agents back into packet-local hacks.

The second review question is `ok` semantics. For this tool, `ok:true` should mean "useful reduced evidence was captured," not "a transport returned some bytes." Thin shells, binary bodies, encoding failures, and junk reductions should be visible failures.

The main cut line is `page_role`. It is tempting because storage and worklist docs discuss source-page roles, but this tool should not know why a caller cares about the page. Echoing caller-provided metadata under `input` is enough; classification belongs later.
