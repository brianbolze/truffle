#!/usr/bin/env python3
"""Resolve V2 boundary candidates with a small, attributable live-evidence ladder.

V2 correctly refused to promote ambiguous source/listicle-shaped candidates, but
left too much in `boundary_review`. This packet-local pass tests the next slice:
use store baseline, owned-domain homepages, and a few focused SerpAPI lookups to
shrink boundary without making source/listicle publishers into false companies.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path(__file__).resolve().parent
CANDIDATE_FILTERING = OUTPUT_DIR.parents[0]
PACKET = CANDIDATE_FILTERING.parent
ROOT = PACKET.parents[3]
TOOLS = ROOT / "tools"
for path in (OUTPUT_DIR, CANDIDATE_FILTERING, PACKET, TOOLS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from codex_candidate_qualification_prototype import (  # noqa: E402
    INFRA_OR_UTILITY_DOMAINS,
    SOCIAL_OR_FORUM_DOMAINS,
    SOURCE_HINT_DOMAINS,
    domain_matches,
    has_non_profile_domain_shape,
    normalized,
)
from search_harness import Qrel, build_qrels  # noqa: E402

try:
    import serpapi  # type: ignore  # noqa: E402
except Exception:  # pragma: no cover - only used when live SerpAPI is enabled.
    serpapi = None

try:
    from _env import load_key  # type: ignore  # noqa: E402
except Exception:  # pragma: no cover - only used when Firecrawl fallback is enabled.
    load_key = None

CARDS_PATH = OUTPUT_DIR / "codex_v2_candidate_cards.json"
RESULTS_PATH = OUTPUT_DIR / "codex_boundary_resolution_results.json"
SUMMARY_PATH = OUTPUT_DIR / "codex_boundary_resolution_summary.md"
CACHE_DIR = OUTPUT_DIR / "boundary-resolution-cache"
HOMEPAGE_DIR = CACHE_DIR / "homepages"
SERPAPI_DIR = CACHE_DIR / "serpapi"
FIRECRAWL_DIR = CACHE_DIR / "firecrawl"

USER_AGENT = "web-research-boundary-resolution/0.1"
MAX_BYTES = 1_500_000
FIRECRAWL_SCRAPE = "https://api.firecrawl.dev/v2/scrape"
LIVE_METHODS = {"homepage_direct", "homepage_firecrawl", "serpapi_organic"}
RELEVANT_TELEHEALTH_LABELS = {"must_hit", "should_hit", "worth_capture"}
BOUNDARY_OR_BAD_TELEHEALTH_LABELS = {"tier_c_only", "exclude", "unsure"}
RELEVANT_CI_LABELS = {"top_10_core"}
BOUNDARY_CI_LABELS = {"core_boundary_product_workflow"}

GENERIC_NAME_RE = re.compile(
    r"\b("
    r"online trt|local trt clinic|traditional testosterone clinics|online testosterone therapy|"
    r"lifespan|healthspan|linkedin|fact|myth|newsletter"
    r")\b",
    re.IGNORECASE,
)

COMPANY_SIGNAL_RE = re.compile(
    r"\b("
    r"company|platform|clinic|care|health|ai|software|customers|pricing|about|"
    r"telehealth|providers?|clinicians?|sales|revenue|meeting|notetaker|assistant"
    r")\b",
    re.IGNORECASE,
)

PUBLISHER_TLDS = {".edu", ".gov"}
PUBLISHER_DOMAINS = {
    *SOURCE_HINT_DOMAINS,
    "academic.oup.com",
    "capterra.com",
    "cloudtalk.io",
    "doi.org",
    "everydayhealth.com",
    "futuremarketinsights.com",
    "health.amazon.com",
    "health.harvard.edu",
    "jioinstitute.edu.in",
    "tandfonline.com",
    "track.revoffers.com",
    "yourhealthmagazine.net",
}
TLD_BY_SLUG_TOKEN = {
    "ai",
    "app",
    "ca",
    "cc",
    "co",
    "com",
    "fi",
    "fyi",
    "health",
    "io",
    "net",
    "org",
    "us",
}


@dataclass(frozen=True)
class StoreProfile:
    """Minimal store baseline identity for no-spend resolution."""

    slug: str
    domain: str
    name: str
    aliases: tuple[str, ...] = ()


@dataclass
class Budget:
    """Mutable live-call caps for one boundary-resolution run."""

    max_homepages: int
    max_serpapi: int
    max_firecrawl: int
    homepages: int = 0
    serpapi: int = 0
    firecrawl: int = 0


@dataclass
class Resolution:
    """An updated qualification result for one boundary card."""

    kind: str
    route: str
    confidence_band: str
    method: str
    resolved_domain: str | None = None
    canonical_name: str | None = None
    evidence_added: list[dict[str, Any]] = field(default_factory=list)
    spend: dict[str, Any] = field(default_factory=dict)
    alternatives: list[dict[str, Any]] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)
    caveats: list[str] = field(default_factory=list)


class HomepageParser(HTMLParser):
    """Tiny homepage reducer for title, meta description, and visible text."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.title_depth = 0
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.meta_description: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_by_name = {key.lower(): value for key, value in attrs if key}
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.title_depth += 1
        if tag == "meta":
            name = (attrs_by_name.get("name") or attrs_by_name.get("property") or "").lower()
            if name in {"description", "og:description"} and attrs_by_name.get("content"):
                self.meta_description = clean_text(attrs_by_name["content"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        cleaned = clean_text(data)
        if not cleaned:
            return
        if self.title_depth:
            self.title_parts.append(cleaned)
        self.text_parts.append(cleaned)

    def result(self) -> dict[str, Any]:
        """Return compact parsed homepage fields."""
        text = clean_text(" ".join(self.text_parts))
        return {
            "title": clean_text(" ".join(self.title_parts)) or None,
            "description": self.meta_description,
            "text_excerpt": text[:2500],
        }


def utc_now() -> str:
    """Return a stable UTC capture timestamp for this run."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clean_text(value: str) -> str:
    """Normalize whitespace in fetched text."""
    return re.sub(r"\s+", " ", value).strip()


def slug(value: str) -> str:
    """Return a stable filesystem-safe fragment."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def canonical_domain(value: str | None) -> str | None:
    """Normalize URLs/domains into the store's bare-host shape."""
    if not value:
        return None
    parsed = urllib.parse.urlparse(value if "://" in value else f"https://{value}")
    host = (parsed.netloc or parsed.path.split("/")[0]).lower()
    host = host.split("@")[-1].split(":")[0]
    return host.removeprefix("www.") or None


def domain_stem(domain: str | None) -> str:
    """Return a simple domain stem for rough brand matching."""
    if not domain:
        return ""
    labels = domain.split(".")
    if len(labels) > 2 and labels[0] in {"www", "app", "go", "help", "docs"}:
        labels = labels[1:]
    return labels[0].replace("-", " ")


def compact_norm(value: str) -> str:
    """Normalize to alphanumeric only for rough stem/name comparisons."""
    return re.sub(r"[^a-z0-9]+", "", normalized(value))


def strip_company_suffix(value: str) -> str:
    """Remove common company suffix words before exact-ish name matching."""
    stripped = re.sub(r"\b(inc|llc|ltd|limited|corp|corporation|company)\b\.?", "", value, flags=re.IGNORECASE)
    return clean_text(stripped)


def parse_aliases(raw: str) -> tuple[str, ...]:
    """Parse the simple inline alias arrays used in store frontmatter."""
    without_comment = raw.split("#", 1)[0].strip().strip("[]")
    aliases: list[str] = []
    for part in re.split(r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", without_comment):
        value = part.strip().strip("'\"")
        if value:
            aliases.append(value)
    return tuple(aliases)


def read_store_profiles() -> list[StoreProfile]:
    """Read just enough store identity to detect already-captured companies."""
    profiles: list[StoreProfile] = []
    for path in sorted((ROOT / "store").glob("*/profile.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        frontmatter = text.split("---", 2)[1] if text.startswith("---") and "---" in text[3:] else text[:2500]
        domain_match = re.search(r"^domain:\s*([^\s#]+)", frontmatter, flags=re.MULTILINE)
        name_match = re.search(r"^name:\s*(.+)$", frontmatter, flags=re.MULTILINE)
        aliases_match = re.search(r"^aliases:\s*(.+)$", frontmatter, flags=re.MULTILINE)
        inferred_domain = domain_from_slug(path.parent.name)
        domain = canonical_domain(domain_match.group(1) if domain_match else inferred_domain)
        if not domain:
            continue
        name = clean_text((name_match.group(1).split("#", 1)[0] if name_match else path.parent.name).strip().strip("'\""))
        aliases = parse_aliases(aliases_match.group(1)) if aliases_match else ()
        profiles.append(StoreProfile(slug=path.parent.name, domain=domain, name=name, aliases=aliases))
    return profiles


def domain_from_slug(value: str) -> str | None:
    """Infer a domain from the store slug convention when frontmatter is absent."""
    parts = value.split("-")
    if len(parts) < 2 or parts[-1] not in TLD_BY_SLUG_TOKEN:
        return None
    return ".".join(["-".join(parts[:-1]), parts[-1]])


def store_match_for(card: dict[str, Any], profiles: list[StoreProfile], domain: str | None = None) -> StoreProfile | None:
    """Find an existing store profile by exact domain or conservative name match."""
    candidate_domain = canonical_domain(domain or card.get("domain"))
    if candidate_domain:
        for profile in profiles:
            if candidate_domain == profile.domain:
                return profile
        return None

    name_norm = compact_norm(strip_company_suffix(str(card.get("name") or "")))
    if not name_norm or len(name_norm) < 4 or GENERIC_NAME_RE.search(str(card.get("name") or "")):
        return None
    for profile in profiles:
        values = [profile.name, profile.domain, domain_stem(profile.domain), *profile.aliases]
        for value in values:
            value_norm = compact_norm(strip_company_suffix(value))
            if value_norm and (name_norm == value_norm or name_norm == compact_norm(domain_stem(profile.domain))):
                return profile
    return None


def load_cards() -> list[dict[str, Any]]:
    """Load V2 cards and return only boundary-review candidates."""
    with CARDS_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return [card for card in data["cards"] if card["qualification"]["route"] == "boundary_review"]


def is_publisher_domain(domain: str | None) -> bool:
    """Return whether a domain should default to source preservation."""
    host = canonical_domain(domain)
    if not host:
        return False
    if any(host.endswith(tld) for tld in PUBLISHER_TLDS):
        return True
    return any(domain_matches(host, source_domain) for source_domain in PUBLISHER_DOMAINS)


def is_infra_domain(domain: str | None) -> bool:
    """Return whether a domain is not a company-profile target."""
    host = canonical_domain(domain)
    if not host:
        return False
    first_label = host.split(".", maxsplit=1)[0]
    return (
        has_non_profile_domain_shape(host)
        or first_label in {"apps", "chatgpt", "login", "track"}
        or any(domain_matches(host, item) for item in INFRA_OR_UTILITY_DOMAINS)
        or any(domain_matches(host, item) for item in SOCIAL_OR_FORUM_DOMAINS)
    )


def evidence_domains(card: dict[str, Any]) -> list[str]:
    """Collect candidate-adjacent domains from evidence and alternatives."""
    domains: list[str] = []
    for evidence in card.get("evidence", []):
        for key in ("domain", "source_domain"):
            domain = canonical_domain(evidence.get(key))
            if domain and domain not in domains:
                domains.append(domain)
    for alt in card.get("qualification", {}).get("alternatives", []):
        domain = canonical_domain(alt.get("domain"))
        if domain and domain not in domains:
            domains.append(domain)
    return domains


def source_title_names_candidate(card: dict[str, Any], domain: str) -> bool:
    """Detect a source page that names the candidate in title, usually as owned SEO."""
    name_norm = compact_norm(str(card.get("name") or ""))
    if not name_norm:
        return False
    for evidence in card.get("evidence", []):
        if canonical_domain(evidence.get("source_domain") or evidence.get("domain")) != domain:
            continue
        title_norm = compact_norm(str(evidence.get("title") or ""))
        if name_norm in title_norm:
            return True
    return False


def infer_domain(card: dict[str, Any], profiles: list[StoreProfile]) -> tuple[str | None, str]:
    """Infer a likely official domain before spending search credits."""
    if card.get("domain"):
        return canonical_domain(card["domain"]), "observed_domain"

    store_match = store_match_for(card, profiles)
    if store_match:
        return store_match.domain, "store_name_match"

    name_norm = compact_norm(str(card.get("name") or ""))
    if not name_norm or GENERIC_NAME_RE.search(str(card.get("name") or "")):
        return None, "generic_name"

    for domain in evidence_domains(card):
        stem_norm = compact_norm(domain_stem(domain))
        if len(stem_norm) >= 3 and (stem_norm == name_norm or stem_norm in name_norm or name_norm in stem_norm):
            return domain, "source_domain_stem_match"
        if source_title_names_candidate(card, domain) and stem_norm in name_norm:
            return domain, "source_title_domain_match"
    return None, "none"


def parse_homepage(body: bytes) -> dict[str, Any]:
    """Parse fetched homepage HTML into compact text evidence."""
    parser = HomepageParser()
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.result()


def homepage_cache_path(domain: str) -> Path:
    """Path for a direct homepage cache record."""
    return HOMEPAGE_DIR / f"{slug(domain)}.json"


def fetch_homepage(domain: str, budget: Budget, use_cache: bool) -> dict[str, Any] | None:
    """Fetch a domain homepage if direct-HTTP budget remains."""
    path = homepage_cache_path(domain)
    if use_cache and path.exists():
        with path.open(encoding="utf-8") as handle:
            record = json.load(handle)
        record["_cache_hit"] = True
        return record
    if budget.homepages >= budget.max_homepages:
        return None

    HOMEPAGE_DIR.mkdir(parents=True, exist_ok=True)
    budget.homepages += 1
    urls = [f"https://{domain}/"]
    if not domain.startswith("www."):
        urls.append(f"https://www.{domain}/")
    last_error: str | None = None
    for url in urls:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=20, context=ssl.create_default_context()) as response:
                body = response.read(MAX_BYTES)
                parsed = parse_homepage(body)
                record = {
                    "tool": "direct_http",
                    "_cache_hit": False,
                    "captured_at": utc_now(),
                    "ok": True,
                    "input": {"domain": domain, "url": url},
                    "status": response.status,
                    "final_url": response.geturl(),
                    "content_type": response.headers.get("content-type"),
                    **parsed,
                }
                path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
                return record
        except urllib.error.HTTPError as exc:
            last_error = f"HTTP {exc.code}: {exc.reason}"
        except (urllib.error.URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = str(exc)

    record = {
        "tool": "direct_http",
        "_cache_hit": False,
        "captured_at": utc_now(),
        "ok": False,
        "input": {"domain": domain, "url": urls[0]},
        "error": last_error or "unknown fetch error",
    }
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def firecrawl_cache_path(domain: str) -> Path:
    """Path for a Firecrawl homepage fallback cache record."""
    return FIRECRAWL_DIR / f"{slug(domain)}.json"


def fetch_firecrawl_homepage(domain: str, budget: Budget, use_cache: bool) -> dict[str, Any] | None:
    """Use one Firecrawl scrape credit only when direct HTTP cannot resolve a target."""
    path = firecrawl_cache_path(domain)
    if use_cache and path.exists():
        with path.open(encoding="utf-8") as handle:
            record = json.load(handle)
        record["_cache_hit"] = True
        return record
    if budget.firecrawl >= budget.max_firecrawl or load_key is None:
        return None

    FIRECRAWL_DIR.mkdir(parents=True, exist_ok=True)
    budget.firecrawl += 1
    api_key = load_key("FIRECRAWL_API_KEY")
    body = {
        "url": f"https://{domain}/",
        "formats": ["markdown", "html"],
        "maxAge": 0,
        "location": {"country": "US", "languages": ["en-US"]},
        "onlyMainContent": True,
    }
    request = urllib.request.Request(
        FIRECRAWL_SCRAPE,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            raw = json.loads(response.read())
    except Exception as exc:
        raw = {"ok": False, "error": str(exc)}
    data = raw.get("data") if isinstance(raw, dict) else {}
    metadata = data.get("metadata", {}) if isinstance(data, dict) else {}
    markdown = data.get("markdown") or "" if isinstance(data, dict) else ""
    html = data.get("html") or "" if isinstance(data, dict) else ""
    parsed = parse_homepage(html.encode("utf-8")) if html else {}
    record = {
        "tool": "firecrawl",
        "_cache_hit": False,
        "captured_at": utc_now(),
        "ok": bool(raw.get("success", raw.get("ok", bool(data)))) if isinstance(raw, dict) else False,
        "input": {"domain": domain, "url": f"https://{domain}/"},
        "credits": metadata.get("creditsUsed"),
        "status": metadata.get("statusCode"),
        "final_url": metadata.get("sourceURL") or metadata.get("url"),
        "title": metadata.get("title") or parsed.get("title"),
        "description": metadata.get("description") or parsed.get("description"),
        "text_excerpt": clean_text(markdown)[:2500] if markdown else parsed.get("text_excerpt"),
        "raw_error": raw.get("error") if isinstance(raw, dict) else None,
    }
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def homepage_confirms_company(card: dict[str, Any], domain: str, homepage: dict[str, Any] | None) -> tuple[bool, list[str]]:
    """Return whether homepage evidence confirms an official company surface."""
    if not homepage or not homepage.get("ok"):
        return False, ["homepage_unavailable"]
    haystack = " ".join(
        str(homepage.get(key) or "")
        for key in ("title", "description", "text_excerpt", "final_url")
    )
    hay_norm = compact_norm(haystack)
    name_norm = compact_norm(str(card.get("name") or ""))
    stem_norm = compact_norm(domain_stem(domain))
    reasons: list[str] = []
    if stem_norm and stem_norm in hay_norm:
        reasons.append("homepage_contains_domain_stem")
    if name_norm and len(name_norm) >= 4 and name_norm in hay_norm:
        reasons.append("homepage_contains_candidate_name")
    if COMPANY_SIGNAL_RE.search(haystack):
        reasons.append("homepage_company_language")
    if homepage.get("status") and int(homepage["status"]) < 400:
        reasons.append("homepage_http_ok")
    return bool({"homepage_contains_domain_stem", "homepage_contains_candidate_name"} & set(reasons)) and "homepage_http_ok" in reasons, reasons


def serpapi_cache_path(card: dict[str, Any]) -> Path:
    """Cache path for a focused candidate query."""
    return SERPAPI_DIR / f"{card['cohort']}-{card['rank']:03d}-{slug(card['name'])}.json"


def focused_query(card: dict[str, Any]) -> str:
    """Build one candidate-specific official-domain query."""
    name = str(card["name"])
    if card["cohort"] == "conversation_intelligence":
        return f'"{name}" official site AI meeting notes revenue intelligence'
    return f'"{name}" official site telehealth clinic'


def fetch_serpapi(card: dict[str, Any], budget: Budget, use_cache: bool) -> dict[str, Any] | None:
    """Run a focused organic-only SerpAPI query if budget remains."""
    path = serpapi_cache_path(card)
    if use_cache and path.exists():
        with path.open(encoding="utf-8") as handle:
            record = json.load(handle)
        record["_cache_hit"] = True
        return record
    if budget.serpapi >= budget.max_serpapi or serpapi is None:
        return None

    SERPAPI_DIR.mkdir(parents=True, exist_ok=True)
    budget.serpapi += 1
    query = focused_query(card)
    try:
        record = serpapi.fetch_and_parse(query, organic_only=True)
        record["_cache_hit"] = False
    except Exception as exc:
        record = {"tool": "serpapi", "_cache_hit": False, "captured_at": utc_now(), "ok": False, "input": {"query": query}, "error": str(exc)}
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def serpapi_domain(card: dict[str, Any], record: dict[str, Any] | None) -> tuple[str | None, dict[str, Any] | None]:
    """Pick the best official-looking domain from focused organic results."""
    if not record or not record.get("ok"):
        return None, None
    name_norm = compact_norm(str(card.get("name") or ""))
    if not name_norm:
        return None, None
    for result in record.get("organic_results", [])[:5]:
        domain = canonical_domain(result.get("link"))
        if not domain or is_infra_domain(domain) or is_publisher_domain(domain):
            continue
        haystack = " ".join(str(result.get(key) or "") for key in ("title", "link", "snippet", "displayed_link"))
        result_norm = compact_norm(haystack)
        stem_norm = compact_norm(domain_stem(domain))
        if name_norm in result_norm or stem_norm in name_norm or name_norm in stem_norm:
            return domain, {
                "method": "serpapi_organic",
                "query": record.get("input", {}).get("query"),
                "rank": result.get("position"),
                "title": result.get("title"),
                "link": result.get("link"),
                "snippet": result.get("snippet"),
            }
    return None, None


def should_live_resolve(card: dict[str, Any], domain: str | None, method: str) -> bool:
    """Keep live resolution focused on plausible company/brand boundary cases."""
    if card["qualification"]["kind"] not in {"company_or_brand", "uncertain"}:
        return False
    if GENERIC_NAME_RE.search(str(card.get("name") or "")) and not domain:
        return False
    if method == "generic_name":
        return False
    if domain and (is_infra_domain(domain) or is_publisher_domain(domain)):
        return False
    if card["ranker"]["evidence_count"] >= 2:
        return True
    return card["rank"] <= 60


def no_spend_resolution(card: dict[str, Any], profiles: list[StoreProfile]) -> Resolution | None:
    """Resolve obvious boundary cases without live source calls."""
    domain = canonical_domain(card.get("domain"))
    if domain and is_infra_domain(domain):
        return Resolution(
            kind="nav_or_artifact",
            route="reject_or_defer",
            confidence_band="high",
            method="local_domain_filter",
            resolved_domain=domain,
            reasons=["non_profile_domain_shape_or_social_utility_domain"],
        )
    if domain and is_publisher_domain(domain):
        return Resolution(
            kind="source_or_publisher",
            route="preserve_source_evidence",
            confidence_band="high",
            method="local_source_domain_filter",
            resolved_domain=domain,
            reasons=["known_source_or_publisher_domain"],
            caveats=["preserve as market evidence; do not promote publisher as cohort company"],
        )
    if GENERIC_NAME_RE.search(str(card.get("name") or "")) and not domain:
        return Resolution(
            kind="uncertain",
            route="reject_or_defer",
            confidence_band="medium",
            method="local_generic_name_filter",
            reasons=["generic_service_or_article_fragment"],
        )
    store_match = store_match_for(card, profiles, domain=domain)
    if store_match:
        caveats = []
        if card.get("domain") and card["qualification"]["caveats"]:
            caveats.append("owned SEO/listicle evidence is biased; keep it separate from third-party market evidence")
        return Resolution(
            kind="company_or_brand",
            route="existing_profile",
            confidence_band="high",
            method="store_baseline",
            resolved_domain=store_match.domain,
            canonical_name=store_match.name,
            evidence_added=[{"type": "store_profile", "slug": store_match.slug, "domain": store_match.domain, "name": store_match.name}],
            reasons=["already_captured_in_store"],
            caveats=caveats,
        )
    return None


def resolve_card(
    card: dict[str, Any],
    profiles: list[StoreProfile],
    budget: Budget,
    use_cache: bool,
    enable_firecrawl: bool,
) -> Resolution:
    """Resolve one V2 boundary candidate through the escalation ladder."""
    local = no_spend_resolution(card, profiles)
    if local:
        return local

    inferred_domain, infer_method = infer_domain(card, profiles)
    if inferred_domain:
        store_match = store_match_for(card, profiles, domain=inferred_domain)
        if store_match:
            return Resolution(
                kind="company_or_brand",
                route="existing_profile",
                confidence_band="high",
                method=f"local_{infer_method}",
                resolved_domain=store_match.domain,
                canonical_name=store_match.name,
                evidence_added=[{"type": "store_profile", "slug": store_match.slug, "domain": store_match.domain, "name": store_match.name}],
                reasons=["inferred_domain_already_captured"],
                caveats=["source/listicle mentions can be biased; use store profile as company truth"],
            )

    domain = inferred_domain
    evidence_added: list[dict[str, Any]] = []
    spend: dict[str, Any] = {}
    reasons: list[str] = []
    caveats: list[str] = []
    method = infer_method

    if not domain and should_live_resolve(card, None, infer_method):
        serp_before = budget.serpapi
        serp_record = fetch_serpapi(card, budget, use_cache)
        if serp_record:
            spend["serpapi_queries"] = budget.serpapi - serp_before
            serp_domain, serp_evidence = serpapi_domain(card, serp_record)
            if serp_evidence:
                evidence_added.append({"type": "serpapi_result", **serp_evidence})
                domain = serp_domain
                method = "serpapi_organic"
                reasons.append("focused_serpapi_found_candidate_domain")
        elif budget.serpapi >= budget.max_serpapi:
            caveats.append("focused_serpapi_not_run_budget_cap")

    if domain and should_live_resolve(card, domain, method):
        homepage_before = budget.homepages
        homepage = fetch_homepage(domain, budget, use_cache)
        if homepage:
            spend["direct_http_homepage"] = budget.homepages - homepage_before
            evidence_added.append(
                {
                    "type": "homepage_direct",
                    "domain": domain,
                    "ok": homepage.get("ok"),
                    "status": homepage.get("status"),
                    "title": homepage.get("title"),
                    "description": homepage.get("description"),
                    "final_url": homepage.get("final_url"),
                    "cache_hit": homepage.get("_cache_hit", False),
                }
            )
            confirmed, homepage_reasons = homepage_confirms_company(card, domain, homepage)
            reasons.extend(homepage_reasons)
        else:
            confirmed = False
            homepage_reasons = []
            if budget.homepages >= budget.max_homepages:
                caveats.append("direct_homepage_not_run_budget_cap")

        if not confirmed and enable_firecrawl:
            firecrawl_before = budget.firecrawl
            fc_homepage = fetch_firecrawl_homepage(domain, budget, use_cache)
            if fc_homepage:
                spend["firecrawl_scrapes"] = fc_homepage.get("credits") or (budget.firecrawl - firecrawl_before)
                evidence_added.append(
                    {
                        "type": "homepage_firecrawl",
                        "domain": domain,
                        "ok": fc_homepage.get("ok"),
                        "status": fc_homepage.get("status"),
                        "title": fc_homepage.get("title"),
                        "description": fc_homepage.get("description"),
                        "final_url": fc_homepage.get("final_url"),
                        "credits": fc_homepage.get("credits"),
                        "cache_hit": fc_homepage.get("_cache_hit", False),
                    }
                )
                confirmed, fc_reasons = homepage_confirms_company(card, domain, fc_homepage)
                reasons.extend(fc_reasons)
                if confirmed:
                    method = "homepage_firecrawl"

        store_match = store_match_for(card, profiles, domain=domain)
        if store_match:
            return Resolution(
                kind="company_or_brand",
                route="existing_profile",
                confidence_band="high",
                method=method,
                resolved_domain=store_match.domain,
                canonical_name=store_match.name,
                evidence_added=evidence_added + [{"type": "store_profile", "slug": store_match.slug, "domain": store_match.domain, "name": store_match.name}],
                spend=spend,
                reasons=sorted(set(reasons + ["already_captured_in_store"])),
                caveats=["owned SEO/listicle evidence is biased; use store profile as company truth"] if card.get("domain") else [],
            )
        if confirmed:
            if card.get("domain") and card["qualification"]["caveats"]:
                caveats.append("owned SEO/listicle evidence is biased; use homepage as company evidence, not the article as neutral ranking evidence")
            return Resolution(
                kind="company_or_brand",
                route="capture_candidate",
                confidence_band="medium",
                method=method if method in LIVE_METHODS else "homepage_direct",
                resolved_domain=domain,
                canonical_name=domain_stem(domain).title(),
                evidence_added=evidence_added,
                spend=spend,
                reasons=sorted(set(reasons + ["homepage_confirms_company_surface"])),
                caveats=caveats,
            )
        caveats.append("candidate domain found but homepage did not confidently confirm official company surface")

    return Resolution(
        kind=card["qualification"]["kind"],
        route="boundary_review",
        confidence_band="low" if not domain else "medium",
        method=method or "local_unresolved",
        resolved_domain=domain,
        evidence_added=evidence_added,
        spend=spend,
        alternatives=card["qualification"].get("alternatives", [])[:5],
        reasons=sorted(set(reasons or ["insufficient_evidence_after_budgeted_resolution"])),
        caveats=sorted(set(caveats + card["qualification"].get("caveats", [])[:2])),
    )


def qrel_aliases(qrel: Qrel) -> list[str]:
    """Return eval-only aliases for a qrel."""
    aliases = [qrel.name, *qrel.aliases]
    if qrel.domain:
        aliases.append(qrel.domain.split(".")[0])
    return [alias for alias in aliases if alias]


def eval_match(row: dict[str, Any], qrel: Qrel) -> bool:
    """Match boundary rows to qrels only after resolution."""
    domain = row["resolution"].get("resolved_domain") or row.get("domain")
    if qrel.domain and domain == qrel.domain:
        return True
    if row["resolution"]["route"] in {"capture_candidate", "existing_profile"}:
        names_to_check = [str(row["resolution"].get("canonical_name") or ""), domain_stem(domain)]
    else:
        names_to_check = [str(row.get("name") or ""), str(row["resolution"].get("canonical_name") or "")]
    names_norm = [normalized(value) for value in names_to_check if value]
    canonical = normalized(str(row["resolution"].get("canonical_name") or ""))
    domain_norm = normalized((domain or "").replace(".", " "))
    for alias in qrel_aliases(qrel):
        alias_norm = normalized(alias)
        if not alias_norm or len(alias_norm) < 3:
            continue
        if alias_norm in names_norm:
            return True
        if row["resolution"]["route"] not in {"capture_candidate", "existing_profile"}:
            if any(alias_norm in name_norm for name_norm in names_norm):
                return True
        if alias_norm in canonical or alias_norm in domain_norm:
            return True
    return False


def best_qrel(row: dict[str, Any], qrels: list[Qrel]) -> Qrel | None:
    """Find the strongest eval-only qrel match for a resolved row."""
    matches = [qrel for qrel in qrels if qrel.cohort == row["cohort"] and eval_match(row, qrel)]
    if not matches:
        return None
    return sorted(matches, key=lambda item: item.grade, reverse=True)[0]


def is_relevant_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to evaluate recall preservation."""
    if qrel is None:
        return False
    if qrel.cohort == "telehealth":
        return qrel.label in RELEVANT_TELEHEALTH_LABELS
    if qrel.cohort == "conversation_intelligence":
        return qrel.label in RELEVANT_CI_LABELS
    return False


def is_bad_or_boundary_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to detect bad capture promotions."""
    if qrel is None:
        return False
    if qrel.cohort == "telehealth":
        return qrel.label in BOUNDARY_OR_BAD_TELEHEALTH_LABELS
    if qrel.cohort == "conversation_intelligence":
        return qrel.label in BOUNDARY_CI_LABELS
    return False


def serialize_resolution(resolution: Resolution) -> dict[str, Any]:
    """Serialize a resolution dataclass."""
    return {
        "kind": resolution.kind,
        "route": resolution.route,
        "confidence_band": resolution.confidence_band,
        "method": resolution.method,
        "resolved_domain": resolution.resolved_domain,
        "canonical_name": resolution.canonical_name,
        "evidence_added": resolution.evidence_added,
        "spend": resolution.spend,
        "alternatives": resolution.alternatives,
        "reasons": resolution.reasons,
        "caveats": resolution.caveats,
    }


def result_row(card: dict[str, Any], resolution: Resolution) -> dict[str, Any]:
    """Join original V2 card fields with the updated boundary resolution."""
    return {
        "candidate_id": card["candidate_id"],
        "cohort": card["cohort"],
        "rank": card["rank"],
        "name": card["name"],
        "domain": card["domain"],
        "candidate_source": card["candidate_source"],
        "ranker": card["ranker"],
        "original_qualification": card["qualification"],
        "resolution": serialize_resolution(resolution),
        "evidence": card.get("evidence", [])[:8],
    }


def summarize(rows: list[dict[str, Any]], budget: Budget) -> dict[str, Any]:
    """Build evaluation metrics over resolved boundary rows."""
    qrels = list(build_qrels().values())
    qrel_by_id = {row["candidate_id"]: best_qrel(row, qrels) for row in rows}
    by_cohort: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_cohort[row["cohort"]].append(row)

    cohorts: dict[str, Any] = {}
    for cohort, cohort_rows in sorted(by_cohort.items()):
        route_counts = Counter(row["resolution"]["route"] for row in cohort_rows)
        kind_counts = Counter(row["resolution"]["kind"] for row in cohort_rows)
        capture_rows = [row for row in cohort_rows if row["resolution"]["route"] == "capture_candidate"]
        existing_rows = [row for row in cohort_rows if row["resolution"]["route"] == "existing_profile"]
        unresolved_rows = [row for row in cohort_rows if row["resolution"]["route"] == "boundary_review"]
        relevant_rows = [row for row in cohort_rows if is_relevant_eval(qrel_by_id[row["candidate_id"]])]
        bad_promoted = [row for row in capture_rows if is_bad_or_boundary_eval(qrel_by_id[row["candidate_id"]])]
        source_like_capture = [
            row
            for row in capture_rows
            if row["resolution"]["kind"] in {"source_or_publisher", "directory_or_listicle", "nav_or_artifact"}
            or is_publisher_domain(row["resolution"].get("resolved_domain"))
        ]
        cohorts[cohort] = {
            "boundary_input_count": len(cohort_rows),
            "route_counts": dict(sorted(route_counts.items())),
            "kind_counts": dict(sorted(kind_counts.items())),
            "resolved_count": len(cohort_rows) - len(unresolved_rows),
            "unresolved_count": len(unresolved_rows),
            "boundary_shrink_pct": round((len(cohort_rows) - len(unresolved_rows)) / len(cohort_rows), 3) if cohort_rows else 0,
            "source_like_capture_count": len(source_like_capture),
            "known_bad_or_boundary_promoted_count": len(bad_promoted),
            "known_relevant_seen": len(relevant_rows),
            "known_relevant_resolved_or_preserved": len(
                [
                    row
                    for row in relevant_rows
                    if row["resolution"]["route"]
                    in {"capture_candidate", "existing_profile", "boundary_review", "preserve_source_evidence"}
                ]
            ),
            "known_relevant_capture": len([row for row in relevant_rows if row["resolution"]["route"] == "capture_candidate"]),
            "known_relevant_existing_profile": len([row for row in relevant_rows if row["resolution"]["route"] == "existing_profile"]),
            "known_relevant_boundary_review": len([row for row in relevant_rows if row["resolution"]["route"] == "boundary_review"]),
            "top_capture_candidates": [eval_row(row, qrel_by_id[row["candidate_id"]]) for row in capture_rows[:12]],
            "top_existing_profiles": [eval_row(row, qrel_by_id[row["candidate_id"]]) for row in existing_rows[:12]],
            "top_unresolved": [eval_row(row, qrel_by_id[row["candidate_id"]]) for row in unresolved_rows[:12]],
            "source_like_capture_candidates": [eval_row(row, qrel_by_id[row["candidate_id"]]) for row in source_like_capture[:12]],
            "bad_or_boundary_promoted_candidates": [eval_row(row, qrel_by_id[row["candidate_id"]]) for row in bad_promoted[:12]],
        }

    evidence_counts = Counter(
        evidence.get("type")
        for row in rows
        for evidence in row["resolution"].get("evidence_added", [])
        if evidence.get("type")
    )
    cache_hit_counts = Counter(
        evidence.get("type")
        for row in rows
        for evidence in row["resolution"].get("evidence_added", [])
        if evidence.get("cache_hit")
    )
    return {
        "schema": "codex-boundary-resolution-eval-v0",
        "boundary": {
            "input": str(CARDS_PATH.relative_to(PACKET)),
            "routing_uses_qrels": False,
            "qrels_used_for": "evaluation-only matching after resolution",
            "live_spend_caps": {
                "direct_http_homepages": budget.max_homepages,
                "serpapi_queries": budget.max_serpapi,
                "firecrawl_homepage_scrapes": budget.max_firecrawl,
            },
            "live_spend_used": {
                "direct_http_homepages": budget.homepages,
                "serpapi_queries": budget.serpapi,
                "firecrawl_homepage_scrapes": budget.firecrawl,
            },
            "evidence_records_used": dict(sorted(evidence_counts.items())),
            "cache_records_used": dict(sorted(cache_hit_counts.items())),
            "owned_listicle_guardrail": "Listicle/alternatives titles lower confidence but do not disqualify the domain; homepage/store evidence decides whether the publisher is also a company target.",
        },
        "cohorts": cohorts,
    }


def eval_row(row: dict[str, Any], qrel: Qrel | None) -> dict[str, Any]:
    """Compact row for summary/eval tables."""
    return {
        "rank": row["rank"],
        "name": row["name"],
        "domain": row["domain"],
        "resolved_domain": row["resolution"].get("resolved_domain"),
        "canonical_name": row["resolution"].get("canonical_name"),
        "route": row["resolution"]["route"],
        "method": row["resolution"]["method"],
        "qrel_label": qrel.label if qrel else None,
        "qrel_name": qrel.name if qrel else None,
        "reasons": row["resolution"]["reasons"][:4],
        "caveats": row["resolution"]["caveats"][:3],
    }


def markdown_table(rows: list[list[str]]) -> list[str]:
    """Render a compact Markdown table."""
    if not rows:
        return []
    output = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join("---" for _ in rows[0]) + " |",
    ]
    for row in rows[1:]:
        output.append("| " + " | ".join(row) + " |")
    return output


def write_json(path: Path, data: Any) -> None:
    """Write generated JSON with stable indentation."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def write_summary(evaluation: dict[str, Any]) -> None:
    """Write the human-facing boundary-resolution readout."""
    boundary = evaluation["boundary"]
    lines = [
        "# Codex Boundary Resolution",
        "",
        "Date: 2026-06-26",
        "Status: packet-local live-evidence pass over V2 boundary candidates; no engine changes",
        "",
        "## Read",
        "",
        "- V2's `boundary_review` queue can be shrunk with store baseline plus bounded homepage/search checks.",
        "- Owned `best X` / `alternatives` pages are treated as biased source evidence, not as automatic publisher disqualification.",
        "- Qrels remain evaluation-only after routing.",
        "",
        "## Spend / Evidence",
        "",
        f"- Fresh live calls in latest invocation: direct HTTP homepages {boundary['live_spend_used']['direct_http_homepages']} / {boundary['live_spend_caps']['direct_http_homepages']}; SerpAPI focused queries {boundary['live_spend_used']['serpapi_queries']} / {boundary['live_spend_caps']['serpapi_queries']}; Firecrawl homepage scrapes {boundary['live_spend_used']['firecrawl_homepage_scrapes']} / {boundary['live_spend_caps']['firecrawl_homepage_scrapes']}.",
        f"- Evidence records used: {boundary['evidence_records_used']}",
        f"- Cache records reused: {boundary['cache_records_used']}",
        "",
        "## Cohort Summary",
        "",
    ]
    rows = [["Cohort", "Input boundary", "Resolved", "Still boundary", "Capture", "Existing", "Preserve", "Reject", "Source-like capture", "Bad promoted"]]
    for cohort, stats in evaluation["cohorts"].items():
        counts = stats["route_counts"]
        rows.append(
            [
                cohort,
                str(stats["boundary_input_count"]),
                str(stats["resolved_count"]),
                str(stats["unresolved_count"]),
                str(counts.get("capture_candidate", 0)),
                str(counts.get("existing_profile", 0)),
                str(counts.get("preserve_source_evidence", 0)),
                str(counts.get("reject_or_defer", 0)),
                str(stats["source_like_capture_count"]),
                str(stats["known_bad_or_boundary_promoted_count"]),
            ]
        )
    lines.extend(markdown_table(rows))
    lines.append("")

    for cohort, stats in evaluation["cohorts"].items():
        lines.extend(
            [
                f"## {cohort}",
                "",
                f"- Boundary shrink: {stats['resolved_count']} / {stats['boundary_input_count']} ({stats['boundary_shrink_pct']:.1%}).",
                f"- Known relevant: capture {stats['known_relevant_capture']}, existing profile {stats['known_relevant_existing_profile']}, still boundary {stats['known_relevant_boundary_review']}.",
                "",
                "Top capture candidates:",
                "",
            ]
        )
        capture_rows = [["Rank", "Name", "Resolved domain", "Method", "Eval"]]
        for row in stats["top_capture_candidates"][:8]:
            capture_rows.append([str(row["rank"]), str(row["name"]), str(row["resolved_domain"] or ""), str(row["method"]), str(row["qrel_label"] or "unjudged")])
        lines.extend(markdown_table(capture_rows) if len(capture_rows) > 1 else ["_None._"])
        lines.extend(["", "Top existing profiles:", ""])
        existing_rows = [["Rank", "Name", "Store name", "Domain", "Eval"]]
        for row in stats["top_existing_profiles"][:8]:
            existing_rows.append([str(row["rank"]), str(row["name"]), str(row["canonical_name"] or ""), str(row["resolved_domain"] or ""), str(row["qrel_label"] or "unjudged")])
        lines.extend(markdown_table(existing_rows) if len(existing_rows) > 1 else ["_None._"])
        lines.extend(["", "Top unresolved:", ""])
        unresolved_rows = [["Rank", "Name", "Domain", "Reason", "Eval"]]
        for row in stats["top_unresolved"][:8]:
            unresolved_rows.append([str(row["rank"]), str(row["name"]), str(row["resolved_domain"] or row["domain"] or ""), "; ".join(row["reasons"][:2]), str(row["qrel_label"] or "unjudged")])
        lines.extend(markdown_table(unresolved_rows) if len(unresolved_rows) > 1 else ["_None._"])
        lines.append("")

    lines.extend(
        [
            "## Files",
            "",
            f"- Results JSON: `{RESULTS_PATH.name}`",
            f"- Summary: `{SUMMARY_PATH.name}`",
            f"- Live evidence cache: `{CACHE_DIR.name}/`",
            "",
            "## Readout",
            "",
            "This pass should be treated as prototype evidence, not an engine contract. The useful rule is the owned-listicle split: preserve the article as biased source evidence, but resolve the domain through homepage/store evidence before deciding whether the company belongs in a capture queue.",
            "",
        ]
    )
    SUMMARY_PATH.write_text("\n".join(lines), encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    """Run the full boundary-resolution pass."""
    profiles = read_store_profiles()
    budget = Budget(
        max_homepages=args.max_homepages,
        max_serpapi=args.max_serpapi,
        max_firecrawl=args.max_firecrawl,
    )
    rows: list[dict[str, Any]] = []
    for card in load_cards():
        resolution = resolve_card(
            card=card,
            profiles=profiles,
            budget=budget,
            use_cache=not args.refresh,
            enable_firecrawl=args.max_firecrawl > 0,
        )
        rows.append(result_row(card, resolution))

    evaluation = summarize(rows, budget)
    output = {
        "schema": "codex-boundary-resolution-results-v0",
        "generated_at": utc_now(),
        "boundary": evaluation["boundary"],
        "results": rows,
        "evaluation": evaluation,
    }
    write_json(RESULTS_PATH, output)
    write_summary(evaluation)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve V2 boundary candidates with bounded live source checks.")
    parser.add_argument("--max-homepages", type=int, default=40, help="Direct HTTP homepage cap.")
    parser.add_argument("--max-serpapi", type=int, default=10, help="Focused SerpAPI query cap.")
    parser.add_argument("--max-firecrawl", type=int, default=0, help="Firecrawl homepage fallback cap.")
    parser.add_argument("--refresh", action="store_true", help="Ignore packet-local live-evidence caches.")
    args = parser.parse_args()

    output = run(args)
    print(
        json.dumps(
            {
                "results": len(output["results"]),
                "spend_used": output["boundary"]["live_spend_used"],
                "outputs": {
                    "results": str(RESULTS_PATH),
                    "summary": str(SUMMARY_PATH),
                    "cache": str(CACHE_DIR),
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
