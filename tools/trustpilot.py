#!/usr/bin/env python3
"""Trustpilot profile fetcher + parser — one company profile at one point in time, captured not judged.

Scope is deliberately narrow: scrape `trustpilot.com/review/<slug>` through Firecrawl-stealth and
parse the durable State of the profile — review count, TrustScore, rating distribution, a sample of
the most-recent reviews, and the raw integrity *flags* (paid profile, merged, asks-for-reviews,
AI-assisted replies, people-also-looked-at neighbors, profile-state). That's the whole job.

What this tool does NOT do — on purpose, so it stays reusable beyond the traction lens:
  - No velocity. A delta across captures is the caller's arithmetic (it owns the prior snapshot).
  - No trust verdict. "paid + merged + AI-replies → not apples-to-apples" is a judgment; we surface
    the raw flags and let the caller's integrity gate decide. We report `paid_profile: true`, never
    `trustworthy: false`.
  - No SKU/category attribution. Trustpilot is brand-grain; the tool emits the brand snapshot only.

Generic on purpose: emits parsed JSON to stdout, no cohort / Notion / vertical baked in.

CLI:
  python3 tools/trustpilot.py honehealth.com
  python3 tools/trustpilot.py hims.com --wait-ms 15000        # bump the Cloudflare wait if it doesn't clear

Exit codes:
  0  clean capture (INCLUDING a factual not_found / removed / empty profile — that's data, not failure)
  2  fetch error (network, auth, Firecrawl error, OR a returned Cloudflare challenge page — stealth/wait
     didn't clear; re-runnable)
  3  schema drift detected (a real profile page whose pinned anchors are gone — parser is version-pinned;
     stop the run, never silently parse-on)

Auth: FIRECRAWL_API_KEY from env, falling back to a `.env` at the repo root (gitignored).

Pinned parser version: v1 — bump only on an intentional schema migration, never to paper over drift.

Firecrawl recipe (load-bearing — see trustpilot.md): `/v2/scrape` with `proxy:"stealth"` AND an
explicit `actions:[{type:"wait",milliseconds:12000}]` to clear the Cloudflare JS challenge. Stealth
alone lands on the challenge page (charged 5 credits); the wait drops it to ~1 credit, ~30s/page.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import time
import urllib.request
from typing import Any

from _env import load_key

PARSER_VERSION = "v1"
API_KEY_VAR = "FIRECRAWL_API_KEY"
FIRECRAWL_SCRAPE = "https://api.firecrawl.dev/v2/scrape"
DEFAULT_WAIT_MS = 12000  # the Cloudflare-clearing wait action — 12s is the proven floor (INVARIANTS)
RECENT_REVIEWS_CAP = 30  # the markdown carries one page (~20); cap defensively

# A scrape that "succeeds" (HTTP 200) but returns the Cloudflare interstitial instead of the profile.
# This is a transport block (re-runnable), NOT upstream schema drift — keep the two exit paths distinct.
_CHALLENGE_SIGNS = (
    "Verifying you are human",
    "Verifying your connection",
    "Just a moment",
    "Enable JavaScript and cookies to continue",
    "needs to review the security of your connection",
    "cf-challenge",
)
# A profile Trustpilot pulled for guideline breaches (getpetermd live-observed 2026-06-07). Factual page
# state, surfaced as such — the "is this an integrity red flag" read is the caller's, not the tool's.
_REMOVED_SIGNS = re.compile(
    r"goes against our guidelines|profile (?:has been |was )?removed|we removed this profile|"
    r"this profile is no longer",
    re.IGNORECASE,
)
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"


def _now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _firecrawl_scrape(url: str, api_key: str, wait_ms: int) -> dict[str, Any]:
    """The stealth scrape, inlined (trustpilot is Firecrawl's only caller here — lift a shared
    `_firecrawl.py` on the SECOND Firecrawl tool, the way `_env.py` earned its place). Returns the
    raw Firecrawl response. Network/HTTP errors bubble to main()'s exit-2 handler."""
    body = {
        "url": url,
        "formats": ["markdown"],
        "proxy": "stealth",
        "waitFor": max(wait_ms + 3000, 15000),  # let the page settle a beat past the challenge wait
        "timeout": 60000,
        "onlyMainContent": False,  # the integrity flags + neighbors live in chrome, not main content
        "actions": [{"type": "wait", "milliseconds": wait_ms}],
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    req = urllib.request.Request(FIRECRAWL_SCRAPE, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def _parse_int(raw: str | None) -> int | None:
    """'11,573' -> 11573. None-safe; None on anything non-numeric."""
    if not raw:
        return None
    digits = re.sub(r"[^\d]", "", raw)
    return int(digits) if digits else None


def _strip_md(text: str) -> str:
    """Markdown -> plain text for a review body: drop images, unwrap links, kill the `\\` soft-breaks,
    collapse whitespace. Faithful capture — no truncation, no editorializing."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)  # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> their text
    text = text.replace("\\", " ")
    return re.sub(r"\s+", " ", text).strip()


# --- top-line metrics -------------------------------------------------------
# Anchored on the header line `# <Name>Reviews<count>` and the bare TrustScore decimal that follows
# the FIRST `![TrustScore N out of 5]` image (the header score; the related-company cards lower down
# carry their own TrustScore images, so first-match is what pins us to the subject profile).
def parse_review_count(md: str) -> int | None:
    m = re.search(r"^#\s+.+?Reviews([\d,]+)\s*$", md, re.MULTILINE)
    if m:
        return _parse_int(m.group(1))
    m = re.search(r"See all ([\d,]+) reviews", md)  # fallback anchor
    return _parse_int(m.group(1)) if m else None


def parse_trust_score(md: str) -> float | None:
    m = re.search(r"!\[TrustScore [\d.]+ out of 5\][^\n]*\n+\s*([0-5](?:\.\d{1,2})?)\b", md)
    return float(m.group(1)) if m else None


def parse_rating_label(md: str) -> str | None:
    """Trustpilot's word grade (Excellent/Great/Average/Poor/Bad) — the `### <Word>` near the score."""
    m = re.search(r"^###\s+(Excellent|Great|Average|Poor|Bad)\b", md, re.MULTILINE)
    return m.group(1) if m else None


def parse_reviews_last_12m(md: str) -> int | None:
    m = re.search(r"([\d,]+)\s*reviews?\s*\*{0,2}\s*\n*\s*in the last 12 months", md, re.IGNORECASE)
    return _parse_int(m.group(1)) if m else None


def parse_rating_distribution(md: str) -> dict[str, str] | None:
    """The lifetime star distribution from the `## All reviews` block: `5-star\\n93%`, `1-star\\n3%`.

    NOTE (2026-06-08): these percentages are NOW in the scraped markdown — directly contradicting the
    2026-05-06 INVARIANT that said they aren't (Trustpilot reshaped). We parse them verbatim ('<1%'
    kept as-is, never invented into a number). If Trustpilot drops them again, the caller still has
    `recent_reviews[].rating` to compute a recent-sample distribution — the old fallback. See trustpilot.md.
    """
    section = md[md.index("## All reviews") :] if "## All reviews" in md else md
    pairs = re.findall(r"([1-5])-star\s*\n+\s*(<?\s*\d+(?:\.\d+)?\s*%)", section)
    if not pairs:
        return None
    return {star: pct.replace(" ", "") for star, pct in pairs}


# --- raw integrity flags (surfaced, never judged) ---------------------------
def parse_profile_flags(md: str) -> dict[str, Any]:
    """The raw integrity signals the caller's gate reads — presence/absence facts off the page, plus
    the negative-reply rate when stated. We report what Trustpilot shows; we do not weigh it."""
    asks: bool | None
    if re.search(r"Asks customers to review|invites their customers to review", md, re.IGNORECASE):
        asks = True
    elif re.search(r"No history of asking", md, re.IGNORECASE):
        asks = False
    else:
        asks = None
    reply_m = re.search(r"Replied to (\d+)% of negative reviews", md, re.IGNORECASE)
    return {
        "claimed": bool(re.search(r"Claimed profile", md, re.IGNORECASE)),
        "paid_profile": bool(re.search(r"Paid Trustpilot subscription", md, re.IGNORECASE)),
        "asks_for_reviews": asks,
        "ai_assisted_replies": bool(re.search(r"AI-assist(?:ed)? (?:with )?repl|AI-assisted response", md, re.IGNORECASE)),
        "merged_profile": bool(re.search(r"merged with one or more other Trustpilot|profile was merged", md, re.IGNORECASE)),
        "negative_reply_rate_pct": int(reply_m.group(1)) if reply_m else None,
    }


def parse_people_also_looked_at(md: str) -> list[dict[str, Any]]:
    """The 'People also looked at' neighbor cards — name + domain (required), score + count (best-effort).
    Off-vertical neighbors are a veto signal for the caller; the tool just hands over the raw set."""
    if "## People also looked at" not in md:
        return []
    section = md[md.index("## People also looked at") :]
    section = section.split("## All reviews", 1)[0]  # don't bleed into the review feed
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    # Each card ends in `](https://www.trustpilot.com/review/<domain>)`; the bold name, score and
    # (count) sit in the card body just before it. Bound each card between consecutive closers (NOT a
    # fixed lookback — that bleeds the previous card's score into this one).
    prev_end = 0
    for m in re.finditer(r"\]\(https://www\.trustpilot\.com/review/([^)]+)\)", section):
        domain = m.group(1)
        card = section[prev_end : m.start()]
        prev_end = m.end()
        if domain in seen:
            continue
        name_m = re.search(r"\*\*([^*]+?)\*\*", card)
        # the bare TrustScore decimal sits just before the `(count)` (`2.2\\ \\ (14)`); the `\\` soft-
        # breaks are noise, so allow backslashes/whitespace between the score and the count.
        score_m = re.search(r"([0-5](?:\.\d)?)[\\\s]+\([\d.,KM]+\)", card)
        count_m = re.search(r"\(([\d.,]+[KM]?)\)\s*$", card.rstrip())
        seen.add(domain)
        out.append(
            {
                "name": name_m.group(1).strip() if name_m else None,
                "domain": domain,
                "trust_score": float(score_m.group(1)) if score_m else None,
                "review_count_label": count_m.group(1) if count_m else None,  # verbatim '14' / '5K' / '1.4K'
            }
        )
    return out


# --- recent-review sample ---------------------------------------------------
# Each review in the `## All reviews` feed opens with a reviewer token
# `[Name\\ <COUNTRY>•<N> reviews](…/users/<id>)`; the review body follows it up to the next reviewer
# token. We slice on that token, then pull rating / title / id / body / date / labels per slice.
# The name/loc separator is the `\\` soft-break (or a bare newline), NOT a space — so the name keeps
# its internal spaces ('ashly fox') instead of truncating at the first one. Name excludes `]\\` and
# newline; the separator requires a backslash-run or a newline.
_REVIEWER_RE = re.compile(
    r"\[(?P<name>[^\]\\\n]+?)\s*(?:\\+|\n)\s*(?P<loc>[^\]]*?)\]\(https://www\.trustpilot\.com/users/[0-9a-f]+\)",
)
_DATE_RE = re.compile(rf"\b((?:{_MONTHS})\s+\d{{1,2}},\s+\d{{4}})\b")
_RELTIME_RE = re.compile(
    r"\b(\d+\s+(?:minute|hour|day|week|month|year)s?\s+ago|A(?:n)?\s+(?:day|month|year|hour)\s+ago|Updated[^\n]*ago)\b",
    re.IGNORECASE,
)


def _parse_one_review(block: str, name: str, loc: str) -> dict[str, Any] | None:
    """One review slice -> structured fields. Returns None when the slice carries no star rating
    (i.e. it isn't a review). Missing title/body/date degrade to None — never crash the block."""
    rating_m = re.search(r"!\[Rated ([1-5]) out of 5 stars\]", block)
    if not rating_m:
        return None
    rating = int(rating_m.group(1))
    title_m = re.search(r"\[\*\*(?P<title>.+?)\*\*\]\(https://www\.trustpilot\.com/reviews/(?P<rid>[0-9a-f]+)\)", block, re.DOTALL)
    if title_m:
        title: str | None = _strip_md(title_m.group("title"))
        review_id: str | None = title_m.group("rid")
        body_start = title_m.end()
    else:
        title, body_start = None, rating_m.end()
        rid_m = re.search(r"https://www\.trustpilot\.com/reviews/([0-9a-f]+)", block)
        review_id = rid_m.group(1) if rid_m else None
    date_m = _DATE_RE.search(block)
    body_end = date_m.start() if date_m else len(block)
    body = _strip_md(block[body_start:body_end]) or None
    reltime_m = _RELTIME_RE.search(block[: rating_m.start()])
    country_m = re.match(r"\s*([A-Za-z]{2})\b", loc)
    nrev_m = re.search(r"(\d[\d,]*)\s+reviews?", loc)
    return {
        "review_id": review_id,
        "rating": rating,
        "title": title,
        "body": body,
        "date_of_experience": date_m.group(1) if date_m else None,
        "posted": reltime_m.group(1) if reltime_m else None,
        "verified": bool(re.search(r"(?m)^Verified\s*$", block)),
        "unprompted": bool(re.search(r"Unprompted review", block)),
        "reviewer_name": name.strip() or None,
        "reviewer_country": country_m.group(1) if country_m else None,
        "reviewer_review_count": _parse_int(nrev_m.group(1)) if nrev_m else None,
    }


def parse_recent_reviews(md: str) -> list[dict[str, Any]]:
    """The most-recent feed under `## All reviews` (NOT the cherry-picked 'Reviews shaping this
    summary' block above it — those skew positive). Caller does the dedup/template/sentiment work."""
    if "## All reviews" not in md:
        return []
    section = md[md.index("## All reviews") :]
    tokens = list(_REVIEWER_RE.finditer(section))
    out: list[dict[str, Any]] = []
    for i, tok in enumerate(tokens):
        block = section[tok.end() : tokens[i + 1].start() if i + 1 < len(tokens) else len(section)]
        review = _parse_one_review(block, tok.group("name"), tok.group("loc"))
        if review:
            out.append(review)
        if len(out) >= RECENT_REVIEWS_CAP:
            break
    return out


# --- profile state + drift --------------------------------------------------
def classify_state(md: str, status_code: int | None, review_count: int | None) -> str:
    """Factual page state, not a trust read: not_found | removed | empty | active. A missing or pulled
    profile is DATA (like AIO-absent), captured as such — never an error and never a verdict."""
    if _REMOVED_SIGNS.search(md):
        return "removed"
    if status_code == 404:
        return "not_found"
    if review_count == 0 or re.search(r"Be the first to review", md, re.IGNORECASE):
        return "empty"
    if review_count is None and "## All reviews" not in md:
        return "not_found"  # no header count and no review feed — not a real profile page
    return "active"


def is_challenge_page(md: str) -> bool:
    """The scrape returned the Cloudflare interstitial, not the profile (stealth/wait didn't clear)."""
    head = md[:4000]
    return any(sign.lower() in head.lower() for sign in _CHALLENGE_SIGNS)


def validate_shape_v1(result: dict[str, Any]) -> list[str]:
    """Drift complaints against the pinned v1 markdown shape — empty list means OK. Only runs for an
    `active` profile: an active page that yields no count AND no score AND no reviews means Trustpilot
    reshaped the markup we anchor on. Fail loud (exit 3) rather than emit plausible-but-wrong State."""
    issues: list[str] = []
    if result["profile_state"] != "active":
        return issues
    if result["review_count"] is None:
        issues.append("active profile but review_count not found (header `# <Name>Reviews<count>` anchor missing)")
    if result["trust_score"] is None:
        issues.append("active profile but trust_score not found (TrustScore-decimal anchor missing)")
    if not result["recent_reviews"]:
        issues.append("active profile but zero recent reviews parsed (`![Rated N out of 5 stars]` blocks missing)")
    return issues


def fetch_and_parse(slug: str, api_key: str | None = None, wait_ms: int = DEFAULT_WAIT_MS) -> dict[str, Any]:
    """Full pipeline: scrape `trustpilot.com/review/<slug>` -> parsed snapshot dict.

    Raises on transport failure / a returned challenge page (main() maps to exit 2). Sets
    `schema_drift` (non-empty -> exit 3) when an active profile's pinned anchors are gone.
    """
    slug = _normalize_slug(slug)
    url = f"https://www.trustpilot.com/review/{slug}"
    api_key = api_key or load_key(API_KEY_VAR)

    t0 = time.time()
    resp = _firecrawl_scrape(url, api_key=api_key, wait_ms=wait_ms)
    elapsed = time.time() - t0
    if not resp.get("success", True):
        raise RuntimeError(f"Firecrawl error: {resp.get('error', resp)}")
    data = resp.get("data") or {}
    md = data.get("markdown") or ""
    meta = data.get("metadata") or {}
    status_code = meta.get("statusCode")

    if not md or is_challenge_page(md):
        raise RuntimeError(
            f"Cloudflare challenge page returned (no profile markdown) for {url} — stealth/wait did not "
            f"clear. Re-run, or raise --wait-ms. (status={status_code}, mdlen={len(md)})"
        )

    review_count = parse_review_count(md)
    state = classify_state(md, status_code, review_count)

    result: dict[str, Any] = {
        # --- the reserved envelope spine (tools/README.md), identical across the library ---
        "tool": "trustpilot",
        "source": "trustpilot.com",  # the signal's origin; fetched VIA Firecrawl-stealth (see capture.via)
        "parser_version": PARSER_VERSION,  # optional spine key: this upstream is drift-prone
        "captured_at": _now_utc(),  # THIS invocation's wall-clock — the caller diffs counts ACROSS these
        "ok": True,  # flipped False below on schema drift; transport failures never reach here (exit 2)
        "input": {"slug": slug, "wait_ms": wait_ms},
        "schema_drift": [],
        "cost": {"firecrawl_credits": meta.get("creditsUsed")},  # optional spine key: the source meters credits
        # --- payload, beside the spine (never nested under a generic `data`) ---
        "trustpilot_url": url,
        "profile_state": state,  # active | empty | removed | not_found
        "review_count": review_count if state == "active" else (0 if state == "empty" else None),
        "reviews_last_12m": parse_reviews_last_12m(md) if state == "active" else None,
        "trust_score": parse_trust_score(md) if state == "active" else None,
        "rating_label": parse_rating_label(md) if state == "active" else None,
        "rating_distribution": parse_rating_distribution(md) if state == "active" else None,
        "rating_distribution_source": None,
        "profile_flags": parse_profile_flags(md),
        "people_also_looked_at": parse_people_also_looked_at(md),
        "recent_reviews": parse_recent_reviews(md) if state == "active" else [],
        "capture": {  # fetch provenance (named field — not the metered cost, which is `cost`)
            "via": "firecrawl-stealth",
            "status_code": status_code,
            "proxy_used": meta.get("proxyUsed"),
            "fetch_seconds": round(elapsed, 1),
            "source_url": meta.get("sourceURL") or meta.get("url"),
            "markdown_chars": len(md),
        },
    }
    if result["rating_distribution"]:
        result["rating_distribution_source"] = "trustpilot_all_reviews"
    result["recent_reviews_sample_size"] = len(result["recent_reviews"])

    drift = validate_shape_v1(result)
    if drift:
        # Fail loud, don't parse-on. An active page missing its anchors yields plausible-but-wrong
        # State — let `schema_drift` carry the truth and suppress the trust-bearing parsed fields, so
        # an importing caller (not just the CLI) sees the failure. Bump PARSER_VERSION only on an
        # intended migration, never to silence a real change.
        result["ok"] = False
        result["schema_drift"] = drift
        for k in ("review_count", "trust_score", "rating_distribution", "reviews_last_12m"):
            result[k] = None
        result["recent_reviews"] = []
        result["recent_reviews_sample_size"] = 0
        sys.stderr.write(
            f"WARNING: trustpilot schema drift for slug={slug!r}: {drift}\n"
            f"Parser pinned to {PARSER_VERSION} — parsed fields suppressed; review the shape before bumping (exit 3).\n"
        )
    return result


def _normalize_slug(arg: str) -> str:
    """Accept a bare slug/domain ('honehealth.com'), or a full Trustpilot review URL, -> the slug."""
    arg = arg.strip()
    m = re.search(r"trustpilot\.com/review/([^/?#]+)", arg)
    if m:
        return m.group(1)
    return re.sub(r"^https?://", "", arg).rstrip("/")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", help="Trustpilot slug/domain (e.g. 'honehealth.com') or a full review URL")
    p.add_argument(
        "--wait-ms",
        type=int,
        default=DEFAULT_WAIT_MS,
        help=f"Cloudflare-clearing wait action in ms (default: {DEFAULT_WAIT_MS}; raise if the challenge doesn't clear)",
    )
    args = p.parse_args()

    try:
        result = fetch_and_parse(args.slug, wait_ms=args.wait_ms)
    except Exception as e:
        sys.stderr.write(f"Error capturing {args.slug!r}: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))
    if result.get("schema_drift"):
        sys.exit(3)


if __name__ == "__main__":
    main()
