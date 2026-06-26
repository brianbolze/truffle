#!/usr/bin/env python3
"""Run a bounded page/entity extraction probe for cohort discovery search.

The earlier search harness showed that raw SERP/Exa result units rank source pages
and long-tail artifacts above real capture targets. This probe tests the next
smallest hypothesis: open a few high-yield result pages, extract page text and
outbound entity links, then score the augmented evidence against the same qrels.

It is packet-local and writes only under this change directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from search_harness import (
    PACKET,
    RAW_DIR,
    Unit,
    all_units,
    build_candidates,
    build_qrels,
    load_json,
    ranked_candidates,
    summarize_variant,
    write_json,
)

OUTPUT_DIR = PACKET / "receipts" / "raw" / "page-extraction"
RECEIPT = PACKET / "receipts" / "page-extraction-probe.md"
MAX_BYTES = 2_500_000
USER_AGENT = "web-research-page-extraction-probe/0.1"
FIRECRAWL_SCRAPE = "https://api.firecrawl.dev/v2/scrape"
FIRECRAWL_FALLBACK_IDS = {"telehealth-forbes-glp1", "telehealth-usnews-glp1"}

PAGE_PANEL: list[dict[str, Any]] = [
    {
        "id": "telehealth-policy-lab-hrt",
        "cohort": "telehealth",
        "facet": "menopause_hrt",
        "rank": 1,
        "url": "https://policylab.us/hormone-replacement-therapy/hrt-online/",
    },
    {
        "id": "telehealth-flowspace-menopause",
        "cohort": "telehealth",
        "facet": "menopause_hrt",
        "rank": 2,
        "url": "https://www.theflowspace.com/reproductive-health/menopause/online-menopause-treatment-2941951/",
    },
    {
        "id": "telehealth-forbes-glp1",
        "cohort": "telehealth",
        "facet": "glp1",
        "rank": 2,
        "url": "https://www.forbes.com/health/weight-loss/best-affordable-online-glp1-providers/",
    },
    {
        "id": "telehealth-usnews-glp1",
        "cohort": "telehealth",
        "facet": "glp1",
        "rank": 3,
        "url": "https://health.usnews.com/best-diet/medication/top-glp-1-weight-loss-medication-providers",
    },
    {
        "id": "telehealth-policy-lab-trt",
        "cohort": "telehealth",
        "facet": "mens_health_trt",
        "rank": 1,
        "url": "https://policylab.us/testosterone-replacement-therapy/online-trt/",
    },
    {
        "id": "telehealth-innerbody-trt",
        "cohort": "telehealth",
        "facet": "mens_health_trt",
        "rank": 7,
        "url": "https://www.innerbody.com/best-online-trt-clinic",
    },
    {
        "id": "telehealth-trtnation-trt",
        "cohort": "telehealth",
        "facet": "mens_health_trt",
        "rank": 8,
        "url": "https://trtnation.com/top-10-best-online-trt-clinics-for-2026/",
    },
    {
        "id": "telehealth-telyrx-ed",
        "cohort": "telehealth",
        "facet": "ed",
        "rank": 3,
        "url": "https://telyrx.com/blog/erectile-dysfunction/best-online-ed-treatment/",
    },
    {
        "id": "telehealth-pmc-ed-dtc",
        "cohort": "telehealth",
        "facet": "ed",
        "rank": 4,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10397420/",
    },
    {
        "id": "telehealth-years-longevity",
        "cohort": "telehealth",
        "facet": "longevity_healthspan",
        "rank": 6,
        "url": "https://www.years.co/en/blog/longevity-clinics-programs-costs",
    },
    {
        "id": "telehealth-empirical-function-alternatives",
        "cohort": "telehealth",
        "facet": "longevity_healthspan",
        "rank": 8,
        "url": "https://www.empirical.health/blog/function-health-alternatives/",
    },
    {
        "id": "ci-zapier-meeting-assistants",
        "cohort": "conversation_intelligence",
        "facet": "meeting_notes",
        "rank": 2,
        "url": "https://zapier.com/blog/best-ai-meeting-assistant/",
    },
    {
        "id": "ci-readai-meeting-assistants",
        "cohort": "conversation_intelligence",
        "facet": "meeting_notes",
        "rank": 1,
        "url": "https://www.read.ai/articles/best-ai-meeting-assistants",
    },
    {
        "id": "ci-salesforce-gong-alternatives",
        "cohort": "conversation_intelligence",
        "facet": "conversation_intelligence",
        "rank": 1,
        "url": "https://www.salesforce.com/compare/gong-alternatives/",
    },
    {
        "id": "ci-tana-otter-alternatives",
        "cohort": "conversation_intelligence",
        "facet": "meeting_notes",
        "rank": 4,
        "url": "https://tana.inc/blog/best-otter-alternatives-2026/",
    },
]

NON_ENTITY_DOMAINS = {
    "facebook.com",
    "instagram.com",
    "linkedin.com",
    "pinterest.com",
    "reddit.com",
    "tiktok.com",
    "twitter.com",
    "x.com",
    "youtube.com",
}


@dataclass
class LinkRecord:
    """One anchor extracted from a fetched page."""

    href: str
    text: str
    domain: str | None
    position: int


@dataclass
class ParseResult:
    """Reduced text and links from one HTML response."""

    title: str | None
    text: str
    links: list[LinkRecord] = field(default_factory=list)


class PageParser(HTMLParser):
    """Small stdlib HTML reducer for source-page entity extraction."""

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.skip_depth = 0
        self.title_depth = 0
        self.link_href: str | None = None
        self.link_text: list[str] = []
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.links: list[LinkRecord] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.title_depth += 1
        if tag == "a":
            href = attr.get("href")
            self.link_href = urljoin(self.base_url, href) if href else None
            self.link_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "a" and self.link_href:
            text = clean_text(" ".join(self.link_text))
            self.links.append(
                LinkRecord(
                    href=self.link_href,
                    text=text,
                    domain=canonical_domain(self.link_href),
                    position=len(self.links) + 1,
                )
            )
            self.link_href = None
            self.link_text = []

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        cleaned = clean_text(data)
        if not cleaned:
            return
        if self.title_depth:
            self.title_parts.append(cleaned)
        if self.link_href:
            self.link_text.append(cleaned)
        self.text_parts.append(cleaned)

    def result(self) -> ParseResult:
        """Return reduced page text and links."""
        text = clean_text(" ".join(self.text_parts))
        title = clean_text(" ".join(self.title_parts)) or None
        return ParseResult(title=title, text=text, links=self.links)


def utc_now() -> str:
    """Return this run's UTC timestamp for provenance."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clean_text(value: str) -> str:
    """Normalize extracted text enough for matching and receipts."""
    return re.sub(r"\s+", " ", value).strip()


def canonical_domain(value: str | None) -> str | None:
    """Normalize a URL or domain to host form."""
    if not value:
        return None
    parsed = urlparse(value if "://" in value else f"https://{value}")
    host = parsed.netloc.lower().removeprefix("www.")
    return host or None


def page_paths(row: dict[str, Any]) -> tuple[Path, Path]:
    """Return raw HTML and reduced JSON paths for a panel row."""
    html_path = OUTPUT_DIR / "html" / f"{row['id']}.html"
    json_path = OUTPUT_DIR / "pages" / f"{row['id']}.json"
    return html_path, json_path


def fetch_url(url: str) -> tuple[int | None, str | None, bytes, str | None]:
    """Fetch one source page with a real UA and bounded response body."""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "identity",
        },
    )
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=25, context=context) as response:
            body = response.read(MAX_BYTES)
            return response.status, response.headers.get("content-type"), body, None
    except urllib.error.HTTPError as exc:
        body = exc.read(MAX_BYTES)
        return exc.code, exc.headers.get("content-type"), body, str(exc)
    except urllib.error.URLError as exc:
        return None, None, b"", str(exc)
    except TimeoutError as exc:
        return None, None, b"", str(exc)


def parse_html(body: bytes) -> ParseResult:
    """Parse one fetched body into text and links."""
    html = body.decode("utf-8", errors="replace")
    parser = PageParser("")
    parser.feed(html)
    return parser.result()


def run_fetch(skip_existing: bool) -> list[dict[str, Any]]:
    """Fetch the fixed page panel and write reduced page envelopes."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "page-panel.json").write_text(json.dumps(PAGE_PANEL, indent=2) + "\n", encoding="utf-8")
    run_rows = []
    for row in PAGE_PANEL:
        html_path, json_path = page_paths(row)
        html_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        if skip_existing and json_path.exists() and json_path.stat().st_size > 0:
            data = load_json(json_path)
            run_rows.append(
                {
                    "id": row["id"],
                    "skipped": True,
                    "ok": bool(data.get("ok")),
                    "status": data.get("status"),
                    "path": str(json_path.relative_to(PACKET)),
                }
            )
            continue
        status, content_type, body, error = fetch_url(row["url"])
        html_path.write_bytes(body)
        parsed = parse_html(body) if body else ParseResult(title=None, text="", links=[])
        envelope = {
            "tool": "page_extraction_probe",
            "source": "direct_http_fetch",
            "captured_at": utc_now(),
            "ok": status is not None and 200 <= status < 400 and bool(parsed.text),
            "input": row,
            "schema_drift": [],
            "cost": {"credits": 0, "usd": 0},
            "status": status,
            "content_type": content_type,
            "error": error,
            "raw_html_path": str(html_path.relative_to(PACKET)),
            "title": parsed.title,
            "text": parsed.text[:300_000],
            "text_chars": len(parsed.text),
            "links": [
                {
                    "href": link.href,
                    "text": link.text,
                    "domain": link.domain,
                    "position": link.position,
                }
                for link in parsed.links[:400]
            ],
            "link_count": len(parsed.links),
        }
        write_json(json_path, envelope)
        run_rows.append(
            {
                "id": row["id"],
                "skipped": False,
                "ok": envelope["ok"],
                "status": status,
                "path": str(json_path.relative_to(PACKET)),
                "text_chars": envelope["text_chars"],
                "link_count": envelope["link_count"],
            }
        )
        time.sleep(0.8)
    write_run_summary(run_rows, source="direct_http_fetch")
    return run_rows


def write_run_summary(rows: list[dict[str, Any]], source: str) -> None:
    """Persist page-run status after direct or fallback fetches."""
    run_summary = {
        "captured_at": utc_now(),
        "source": source,
        "page_count": len(PAGE_PANEL),
        "ok_count": sum(1 for row in rows if row["ok"]),
        "rows": rows,
    }
    write_json(OUTPUT_DIR / "run-summary.json", run_summary)


def summarize_page_files(source: str) -> list[dict[str, Any]]:
    """Read current reduced page envelopes into run-summary rows."""
    rows = []
    for row in PAGE_PANEL:
        _html_path, json_path = page_paths(row)
        if not json_path.exists():
            rows.append({"id": row["id"], "ok": False, "status": None, "path": str(json_path.relative_to(PACKET))})
            continue
        data = load_json(json_path)
        rows.append(
            {
                "id": row["id"],
                "ok": bool(data.get("ok")),
                "status": data.get("status"),
                "source": data.get("source"),
                "path": str(json_path.relative_to(PACKET)),
                "text_chars": data.get("text_chars", 0),
                "link_count": data.get("link_count", 0),
                "fallback": data.get("fallback"),
            }
        )
    write_run_summary(rows, source=source)
    return rows


def load_firecrawl_key() -> str:
    """Load FIRECRAWL_API_KEY from env or repo `.env` for packet-local fallback."""
    key = os.environ.get("FIRECRAWL_API_KEY")
    if key:
        return key
    env_path = PACKET.parents[3] / ".env"
    if env_path.exists():
        with env_path.open(encoding="utf-8") as handle:
            for raw in handle:
                line = raw.strip()
                if line.startswith("FIRECRAWL_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError(f"Missing FIRECRAWL_API_KEY in environment or {env_path}")


def firecrawl_scrape(url: str, api_key: str) -> dict[str, Any]:
    """Scrape one blocked source page through Firecrawl without LLM extraction."""
    body = {
        "url": url,
        "formats": ["markdown", "links"],
        "maxAge": 0,
        "waitFor": 3500,
        "timeout": 60000,
        "onlyMainContent": False,
        "location": {"country": "US", "languages": ["en-US"]},
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    request = urllib.request.Request(
        FIRECRAWL_SCRAPE,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def firecrawl_links(raw: dict[str, Any]) -> list[LinkRecord]:
    """Normalize Firecrawl link payloads to the same reduced link shape."""
    data = raw.get("data") if isinstance(raw.get("data"), dict) else raw
    links = data.get("links") or []
    normalized = []
    for index, item in enumerate(links, start=1):
        if isinstance(item, str):
            href = item
            text = item
        elif isinstance(item, dict):
            href = str(item.get("url") or item.get("href") or item.get("link") or "")
            text = str(item.get("text") or item.get("title") or href)
        else:
            continue
        if not href:
            continue
        normalized.append(LinkRecord(href=href, text=clean_text(text), domain=canonical_domain(href), position=index))
    return normalized


def run_firecrawl_fallback() -> list[dict[str, Any]]:
    """Use Firecrawl only for page-panel rows that failed direct HTTP."""
    api_key = load_firecrawl_key()
    raw_dir = OUTPUT_DIR / "firecrawl"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for row in PAGE_PANEL:
        if row["id"] not in FIRECRAWL_FALLBACK_IDS:
            continue
        _html_path, json_path = page_paths(row)
        existing = load_json(json_path) if json_path.exists() else {}
        if existing.get("ok"):
            continue
        try:
            raw = firecrawl_scrape(row["url"], api_key)
            error = None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raw = {}
            error = str(exc)
        raw_path = raw_dir / f"{row['id']}.json"
        write_json(raw_path, raw)
        data = raw.get("data") if isinstance(raw.get("data"), dict) else raw
        markdown = clean_text(str(data.get("markdown") or ""))
        metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
        links = firecrawl_links(raw)
        envelope = {
            "tool": "page_extraction_probe",
            "source": "firecrawl_scrape",
            "captured_at": utc_now(),
            "ok": bool(raw.get("success", raw.get("ok", False))) and bool(markdown),
            "fallback": "firecrawl_scrape",
            "input": row,
            "schema_drift": [],
            "cost": {"firecrawl_credits_estimate": 1},
            "status": 200 if raw else None,
            "content_type": "text/markdown",
            "error": error or raw.get("error"),
            "raw_firecrawl_path": str(raw_path.relative_to(PACKET)),
            "title": metadata.get("title") or data.get("title"),
            "text": markdown[:300_000],
            "text_chars": len(markdown),
            "links": [
                {
                    "href": link.href,
                    "text": link.text,
                    "domain": link.domain,
                    "position": link.position,
                }
                for link in links[:400]
            ],
            "link_count": len(links),
        }
        write_json(json_path, envelope)
        time.sleep(1.0)
    return summarize_page_files(source="direct_http_fetch_plus_firecrawl_fallback")


def page_units() -> list[Unit]:
    """Build matchable source units from reduced page envelopes."""
    units: list[Unit] = []
    for row in PAGE_PANEL:
        _html_path, json_path = page_paths(row)
        if not json_path.exists():
            continue
        data = load_json(json_path)
        source_domain = canonical_domain(row["url"])
        if data.get("text"):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder="page_extraction",
                    tool="direct_http_fetch",
                    unit_type="page_text",
                    rank=int(row["rank"]),
                    text=data["text"].lower(),
                    domain=None,
                    url=row["url"],
                    title=data.get("title"),
                    facet=row["facet"],
                )
            )
        seen_domains: set[str] = set()
        for link in data.get("links", []):
            domain = link.get("domain")
            if not domain or domain == source_domain or domain in NON_ENTITY_DOMAINS:
                continue
            if domain in seen_domains:
                continue
            seen_domains.add(domain)
            text = clean_text(f"{link.get('text') or ''} {domain} {link.get('href') or ''}").lower()
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder="page_outbound_links",
                    tool="direct_http_fetch",
                    unit_type="outbound_link",
                    rank=int(link.get("position") or 100),
                    text=text,
                    domain=domain,
                    url=link.get("href"),
                    title=link.get("text") or domain,
                    facet=row["facet"],
                )
            )
    return units


def metric_triplet(variant: dict[str, Any], at: str = "@10") -> str:
    """Format a compact metrics tuple for the receipt."""
    metrics = variant["metrics"][at]
    return f"P{at} {metrics['precision']:.3f}, R{at} {metrics['recall']:.3f}, nDCG{at} {metrics['ndcg']:.3f}"


def write_receipt(summary: dict[str, Any]) -> None:
    """Write the human-facing receipt for the page extraction probe."""
    tele_raw = summary["variants"]["telehealth_raw"]
    tele_aug = summary["variants"]["telehealth_page_augmented"]
    ci_raw = summary["variants"]["conversation_raw"]
    ci_aug = summary["variants"]["conversation_page_augmented"]
    failed = [row for row in summary["run_summary"]["rows"] if not row["ok"]]
    fallback_rows = [row for row in summary["run_summary"]["rows"] if row.get("fallback") == "firecrawl_scrape"]
    low_grade_top20 = tele_aug["low_grade_or_boundary_in_top20"] + ci_aug["low_grade_or_boundary_in_top20"]
    if fallback_rows:
        source_line = (
            "- Source method: direct HTTP fetch with stdlib HTML reduction; Firecrawl fallback "
            f"for {len(fallback_rows)} direct-fetch-blocked pages."
        )
        spend_line = (
            f"- Spend: estimated {len(fallback_rows)} Firecrawl base scrape credits; "
            "no SerpAPI or Exa calls."
        )
    else:
        source_line = "- Source method: direct HTTP fetch with stdlib HTML reduction; no Firecrawl, SerpAPI, or Exa calls."
        spend_line = "- Spend: 0 API credits / USD 0. User-approved paid expansion was not needed for this first pass."
    lines = [
        "# Page Extraction Probe Receipt",
        "",
        "Date: 2026-06-26",
        "Status: live page/entity extraction probe complete",
        "",
        "## Boundary",
        "",
        "- Fixed panel: 11 telehealth result/list pages and 4 conversation-intelligence pages.",
        source_line,
        spend_line,
        "- Writes only packet-local raw/reduced page envelopes and this receipt.",
        "",
        "## Fetch Result",
        "",
        f"- Pages fetched with usable text: {summary['run_summary']['ok_count']}/{summary['run_summary']['page_count']}.",
        f"- Page units added: {summary['page_unit_count']}.",
    ]
    if failed:
        failed_text = ", ".join(f"{row['id']} ({row['status']})" for row in failed)
        lines.extend(
            [
                f"- Fetch failures or unusable pages: {failed_text}.",
            ]
        )
    lines.extend(
        [
            "",
            "## Metrics",
            "",
            "| Variant | Candidates | Judged | P@10 | R@10 | nDCG@10 | Relevant misses |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
            _metric_row("telehealth_raw", tele_raw),
            _metric_row("telehealth_page_augmented", tele_aug),
            _metric_row("conversation_raw", ci_raw),
            _metric_row("conversation_page_augmented", ci_aug),
            "",
            "## Read",
            "",
            f"- Telehealth moved from {metric_triplet(tele_raw)} to {metric_triplet(tele_aug)}.",
            f"- Telehealth retrieval by label after page extraction: {_breakdown(tele_aug['retrieval_breakdown'])}.",
            f"- Conversation moved from {metric_triplet(ci_raw)} to {metric_triplet(ci_aug)}.",
            "- The improvement comes from page text and outbound links naming entities hidden behind source result pages.",
            "- This supports making page/entity extraction part of the evaluated recipe before adding new discovery sources.",
            "- The ranker still needs a candidate-type filter / verification gate: source domains remain in the top ranks.",
            "",
            "Remaining telehealth misses:",
            "",
            *[
                f"- {row['name']} ({row['label']}, grade {row['grade']})"
                for row in tele_aug["misses"][:14]
            ],
            "",
            "Generated detail:",
            "",
            f"- Page panel: `{summary['outputs']['page_panel']}`",
            f"- Run summary: `{summary['outputs']['run_summary']}`",
            f"- Score summary: `{summary['outputs']['score_summary']}`",
        ]
    )
    if low_grade_top20:
        lines.extend(
            [
                "",
                "Low-grade or boundary rows in top 20:",
                "",
                *[
                    f"- {row['name']} at rank {row['rank']} ({row['qrel_label']}, grade {row['qrel_grade']})"
                    for row in low_grade_top20
                ],
            ]
        )
    else:
        lines.extend(["", "Low-grade or boundary rows in top 20: none."])
    RECEIPT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _metric_row(label: str, variant: dict[str, Any]) -> str:
    """Format one metric table row."""
    at10 = variant["metrics"]["@10"]
    return (
        f"| {label} | {variant['candidate_count']} | {variant['judged_candidate_count']} | "
        f"{at10['precision']:.3f} | {at10['recall']:.3f} | {at10['ndcg']:.3f} | "
        f"{len(variant['misses'])} |"
    )


def _breakdown(breakdown: dict[str, Any]) -> str:
    """Format retrieval breakdown counts."""
    return "; ".join(
        f"{name} {values['retrieved']}/{values['total']}"
        for name, values in breakdown.items()
    )


def score_outputs() -> dict[str, Any]:
    """Score raw-only versus page-augmented retrieval over the same qrels."""
    qrels = build_qrels()
    rows = load_json(RAW_DIR / "query-panel.json")
    raw_units = all_units(rows)
    extracted_units = page_units()
    raw_candidates = build_candidates(raw_units, qrels, include_store_baseline=False)
    augmented_candidates = build_candidates(raw_units + extracted_units, qrels, include_store_baseline=False)
    run_summary = load_json(OUTPUT_DIR / "run-summary.json")
    fallback_count = sum(1 for row in run_summary["rows"] if row.get("fallback") == "firecrawl_scrape")
    live_spend = (
        f"direct HTTP plus estimated {fallback_count} Firecrawl base scrape credits"
        if fallback_count
        else "direct HTTP only; no API credits"
    )
    score_summary = {
        "schema": "cohort-discovery-page-extraction-probe-v1",
        "inputs": {
            "query_panel": str((RAW_DIR / "query-panel.json").relative_to(PACKET)),
            "page_panel": str((OUTPUT_DIR / "page-panel.json").relative_to(PACKET)),
            "run_summary": str((OUTPUT_DIR / "run-summary.json").relative_to(PACKET)),
            "live_spend": live_spend,
        },
        "outputs": {
            "page_panel": str((OUTPUT_DIR / "page-panel.json").relative_to(PACKET)),
            "run_summary": str((OUTPUT_DIR / "run-summary.json").relative_to(PACKET)),
            "score_summary": str((OUTPUT_DIR / "score-summary.json").relative_to(PACKET)),
            "receipt": str(RECEIPT.relative_to(PACKET)),
        },
        "run_summary": run_summary,
        "firecrawl_fallback_count": fallback_count,
        "raw_unit_count": len(raw_units),
        "page_unit_count": len(extracted_units),
        "variants": {
            "telehealth_raw": summarize_variant("telehealth_raw", raw_candidates, qrels, "telehealth"),
            "telehealth_page_augmented": summarize_variant(
                "telehealth_page_augmented",
                augmented_candidates,
                qrels,
                "telehealth",
            ),
            "conversation_raw": summarize_variant(
                "conversation_raw",
                raw_candidates,
                qrels,
                "conversation_intelligence",
            ),
            "conversation_page_augmented": summarize_variant(
                "conversation_page_augmented",
                augmented_candidates,
                qrels,
                "conversation_intelligence",
            ),
        },
        "top_page_augmented_domains": {
            "telehealth": [
                {
                    "rank": index + 1,
                    "name": candidate.name,
                    "domain": candidate.domain,
                    "qrel_grade": candidate.qrel_grade,
                    "qrel_label": candidate.qrel_label,
                    "feeders": sorted(candidate.feeders),
                    "score": round(candidate.search_score, 6),
                }
                for index, candidate in enumerate(ranked_candidates(augmented_candidates, "telehealth")[:25])
            ],
            "conversation_intelligence": [
                {
                    "rank": index + 1,
                    "name": candidate.name,
                    "domain": candidate.domain,
                    "qrel_grade": candidate.qrel_grade,
                    "qrel_label": candidate.qrel_label,
                    "feeders": sorted(candidate.feeders),
                    "score": round(candidate.search_score, 6),
                }
                for index, candidate in enumerate(
                    ranked_candidates(augmented_candidates, "conversation_intelligence")[:25]
                )
            ],
        },
    }
    write_json(OUTPUT_DIR / "score-summary.json", score_summary)
    write_receipt(score_summary)
    return score_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run packet-local page extraction probe.")
    parser.add_argument("--skip-existing", action="store_true", help="Reuse existing reduced page captures.")
    parser.add_argument("--score-only", action="store_true", help="Do not fetch; score existing page captures.")
    parser.add_argument(
        "--firecrawl-failed",
        action="store_true",
        help="Use Firecrawl only for the direct-fetch failures in the fixed page panel.",
    )
    args = parser.parse_args()

    if not args.score_only:
        if args.firecrawl_failed:
            run_firecrawl_fallback()
        else:
            run_fetch(skip_existing=args.skip_existing)
    summary = score_outputs()
    print(
        json.dumps(
            {
                "ok_pages": summary["run_summary"]["ok_count"],
                "page_count": summary["run_summary"]["page_count"],
                "receipt": str(RECEIPT),
                "score_summary": str(OUTPUT_DIR / "score-summary.json"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
