"""Shared cohort matcher for raw tool outputs — the judgment step that stays outside captures.

Capture tools in `tools/` deliberately emit raw signal: SERP rows, AIO ranked-brand snippets, Exa
neighbors. This helper is the composable next step callers share: take a tool output plus a plain
cohort list, then answer which cohort members appear, where they appeared, and whether the hit is
their own page or a third-party mention.

The important invariant is the two-channel match:

  - Domain channel: URL host vs. cohort `domain` (and domain-shaped aliases), `www.` stripped,
    subdomains accepted. High precision; a hit means `kind="own_page"` and wins ties.
  - Text channel: word-boundary matching over brand aliases / names, with optional
    `disambiguate_regex` for FP-prone open text. A text-only hit means `kind="mention"`.

The cohort shape is intentionally generic:

    {"slug": "ro", "domain": "ro.co", "aliases": ["Ro"], "disambiguate_regex": r"..."}

`aliases` are the caller-controlled brand-name surface. `name` is also accepted when a caller has
it, but it is not required. No Notion, no vertical taxonomy, no project-specific brands.

Store canonicalization is a hook, not an import. Pass `resolver=store.resolve` (or any compatible
callable) if the caller wants Web Research's alias/rebrand folding; without it this module is
stdlib-only and works anywhere the `tools/` library is copied.
"""

from __future__ import annotations

import re
import urllib.parse
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Callable, Literal

TextMode = Literal["cohort_context", "open_text"]
MatchKind = Literal["own_page", "mention"]
MatchMethod = Literal["domain", "text", "both"]
MatchChannel = Literal["domain", "text"]
Resolver = Callable[[str], str | None]

_COMMON_TLD_SLUG_SUFFIXES = (
    "-com",
    "-co",
    "-io",
    "-ai",
    "-net",
    "-org",
    "-health",
)
_TEXT_BOUNDARY_LEFT = r"(?<![A-Za-z0-9])"
_TEXT_BOUNDARY_RIGHT = r"(?![A-Za-z0-9])"


@dataclass(frozen=True)
class _CompiledMember:
    slug: str
    domains: tuple[str, ...]
    resolved_keys: tuple[str, ...]
    cohort_pattern: re.Pattern[str] | None
    open_text_pattern: re.Pattern[str] | None
    open_text_source: str


def normalize_domain(value: str | None) -> str | None:
    """A comparable host token from a domain-ish value, with scheme/userinfo/port/`www.` noise removed.

    This is deliberately lighter than public-suffix apex folding: `aws.amazon.com` stays
    `aws.amazon.com`. Own-page classification uses exact-or-subdomain comparison against the cohort
    member's configured domain, which is the safer rule when the cohort intentionally tracks a
    sub-brand or product domain.
    """
    if value is None:
        return None
    raw = str(value).strip()
    if not raw:
        return None
    if "://" in raw or "/" in raw:
        return domain_from_url(raw)
    return _normalize_host(raw)


def domain_from_url(url: str | None) -> str | None:
    """Host from a URL or bare `domain/path`, lowercased with `www.` stripped.

    Exa emits both `url` and a convenience `domain`; SerpAPI organic rows emit `link`. This accepts
    either shape so callers do not need separate URL-vs-domain branches before matching.
    """
    if url is None:
        return None
    raw = str(url).strip()
    if not raw:
        return None
    candidate = raw if "://" in raw else f"//{raw}"
    parsed = urllib.parse.urlsplit(candidate)
    host = parsed.hostname
    if not host:
        return None
    return _normalize_host(host)


def same_site(observed_domain: str | None, cohort_domain: str | None) -> bool:
    """Whether `observed_domain` is the configured cohort site or one of its subdomains."""
    observed = normalize_domain(observed_domain)
    cohort = normalize_domain(cohort_domain)
    if not observed or not cohort:
        return False
    return observed == cohort or observed.endswith(f".{cohort}")


def match_text(text: str | None, cohort: Sequence[Mapping[str, Any]], mode: TextMode = "cohort_context") -> list[dict[str, Any]]:
    """All cohort text matches, sorted by first span.

    Use `cohort_context` for already-brand-shaped text like AIO ranked-brand snippets and organic
    SERP title/snippet text. Use `open_text` for noisy prose; when `disambiguate_regex` is present,
    that strict regex replaces alias matching for the member.
    """
    matcher = CohortMatcher(cohort)
    return matcher.match_text(text, mode=mode)


def match_domain(value: str | None, cohort: Sequence[Mapping[str, Any]], resolver: Resolver | None = None) -> list[dict[str, Any]]:
    """Cohort members whose own domain is the URL/domain `value`, using direct match plus an optional resolver."""
    matcher = CohortMatcher(cohort, resolver=resolver)
    return matcher.match_domain(value)


def match_record(
    *,
    cohort: Sequence[Mapping[str, Any]],
    url: str | None = None,
    text: str | None = None,
    where: Mapping[str, Any] | None = None,
    text_mode: TextMode = "cohort_context",
    resolver: Resolver | None = None,
) -> list[dict[str, Any]]:
    """Match one observed row that may have a URL, text, or both.

    Domain and text hits for the same slug are collapsed into one row with `match_method="both"`;
    the first text span is kept as provenance. Domain hits take priority because they identify the
    cohort member's own page even when title/snippet text is ambiguous.
    """
    matcher = CohortMatcher(cohort, resolver=resolver)
    return matcher.match_record(url=url, text=text, where=where, text_mode=text_mode)


def match_output(
    output: Mapping[str, Any],
    cohort: Sequence[Mapping[str, Any]],
    *,
    text_mode: TextMode = "cohort_context",
    resolver: Resolver | None = None,
) -> list[dict[str, Any]]:
    """Match the supported `tools/` output envelopes (`serpapi`, `exa_similar`) against a cohort.

    Current payload routing:
      - `ranked_brands`: text from `raw_snippet` / `after_colon`
      - `organic_results`: domain from `link`, text from `title` + `snippet`
      - `neighbors`: domain from `url` / `domain`

    Unsupported payloads simply contribute no matches; this keeps the helper safe to call on mixed
    tool outputs while each new source earns an explicit routing branch.
    """
    matcher = CohortMatcher(cohort, resolver=resolver)
    return matcher.match_output(output, text_mode=text_mode)


class CohortMatcher:
    """Compiled cohort matcher for callers that will match many rows against the same cohort."""

    def __init__(self, cohort: Sequence[Mapping[str, Any]], resolver: Resolver | None = None) -> None:
        self._resolver = resolver
        self._members = tuple(self._compile_member(member) for member in cohort)

    def match_text(self, text: str | None, mode: TextMode = "cohort_context") -> list[dict[str, Any]]:
        """All text-channel matches, sorted by span; row-level callers collapse to first span per slug."""
        if not text:
            return []
        out = []
        for member in self._members:
            pattern = member.cohort_pattern if mode == "cohort_context" else member.open_text_pattern
            if pattern is None:
                continue
            source = "terms" if mode == "cohort_context" else member.open_text_source
            for match in pattern.finditer(text):
                out.append(
                    {
                        "slug": member.slug,
                        "span": (match.start(), match.end()),
                        "text": match.group(0),
                        "mode": mode,
                        "source": source,
                    }
                )
        out.sort(key=lambda item: (item["span"][0], item["span"][1], item["slug"]))
        return out

    def match_domain(self, value: str | None) -> list[dict[str, Any]]:
        """All domain-channel matches for a URL or domain value."""
        observed = domain_from_url(value) or normalize_domain(value)
        if not observed:
            return []

        resolved = self._resolve(observed)
        out = []
        for member in self._members:
            direct_domain = next((domain for domain in member.domains if same_site(observed, domain)), None)
            resolved_match = bool(resolved and resolved in member.resolved_keys)
            if not direct_domain and not resolved_match:
                continue
            out.append(
                {
                    "slug": member.slug,
                    "observed_domain": observed,
                    "matched_domain": direct_domain,
                    "resolved_key": resolved if resolved_match else None,
                    "via_resolver": bool(resolved_match and not direct_domain),
                }
            )
        out.sort(key=lambda item: item["slug"])
        return out

    def match_record(
        self,
        *,
        url: str | None = None,
        text: str | None = None,
        where: Mapping[str, Any] | None = None,
        text_mode: TextMode = "cohort_context",
    ) -> list[dict[str, Any]]:
        """Matches for a single source row, classified as `own_page` or `mention`."""
        where_dict = dict(where or {})
        domain_hits = {hit["slug"]: hit for hit in self.match_domain(url)}
        text_hits = _first_text_hit_by_slug(self.match_text(text, mode=text_mode))
        slugs = sorted(set(domain_hits) | set(text_hits), key=lambda slug: _record_sort_key(slug, domain_hits, text_hits))

        out = []
        observed_domain = domain_from_url(url) or normalize_domain(url)
        for slug in slugs:
            domain_hit = domain_hits.get(slug)
            text_hit = text_hits.get(slug)
            first_channel: MatchChannel = "domain" if domain_hit else "text"
            kind: MatchKind = "own_page" if domain_hit else "mention"
            if domain_hit and text_hit:
                match_method: MatchMethod = "both"
            elif domain_hit:
                match_method = "domain"
            else:
                match_method = "text"

            out.append(
                {
                    "slug": slug,
                    "kind": kind,
                    "match_method": match_method,
                    "first_channel": first_channel,
                    "where": where_dict,
                    "url": url,
                    "domain": observed_domain,
                    "domain_hit": domain_hit,
                    "text_hit": text_hit,
                }
            )
        return out

    def match_output(self, output: Mapping[str, Any], text_mode: TextMode = "cohort_context") -> list[dict[str, Any]]:
        """Matches for the known capture payloads in a tool envelope."""
        out = []
        tool = output.get("tool")

        for index, item in enumerate(_iter_dicts(output.get("ranked_brands"))):
            text = _join_text(item.get("raw_snippet"), item.get("after_colon"))
            where = {
                "tool": tool,
                "payload": "ranked_brands",
                "index": index,
                "position": item.get("position"),
            }
            out.extend(self.match_record(text=text, where=where, text_mode=text_mode))

        for index, item in enumerate(_iter_dicts(output.get("organic_results"))):
            text = _join_text(item.get("title"), item.get("snippet"))
            where = {
                "tool": tool,
                "payload": "organic_results",
                "index": index,
                "position": item.get("position"),
            }
            out.extend(self.match_record(url=_string_or_none(item.get("link")), text=text, where=where, text_mode=text_mode))

        for index, item in enumerate(_iter_dicts(output.get("neighbors"))):
            url = _string_or_none(item.get("url")) or _string_or_none(item.get("domain"))
            where = {
                "tool": tool,
                "payload": "neighbors",
                "index": index,
                "rank": item.get("rank"),
            }
            out.extend(self.match_record(url=url, where=where, text_mode=text_mode))

        return out

    def _compile_member(self, member: Mapping[str, Any]) -> _CompiledMember:
        slug = _required_string(member, "slug")
        domain = _required_string(member, "domain")
        aliases = tuple(_string_values(member.get("aliases") or ()))
        name = _string_or_none(member.get("name"))
        disambiguate_regex = _string_or_none(member.get("disambiguate_regex"))

        domains = _unique(
            normalized for value in (domain, *aliases) if _is_domainish(value) for normalized in (normalize_domain(value),) if normalized
        )
        text_terms = _text_terms(slug=slug, domain=domain, name=name, aliases=aliases)
        cohort_pattern = _word_boundary_pattern(text_terms)
        open_text_pattern = re.compile(disambiguate_regex, re.IGNORECASE) if disambiguate_regex else cohort_pattern
        open_text_source = "disambiguate_regex" if disambiguate_regex else "terms"

        resolved_keys = {slug}
        for value in (slug, domain, *aliases):
            resolved = self._resolve(value)
            if resolved:
                resolved_keys.add(resolved)

        return _CompiledMember(
            slug=slug,
            domains=domains,
            resolved_keys=tuple(sorted(resolved_keys)),
            cohort_pattern=cohort_pattern,
            open_text_pattern=open_text_pattern,
            open_text_source=open_text_source,
        )

    def _resolve(self, value: str | None) -> str | None:
        if not self._resolver or not value:
            return None
        return self._resolver(value)


def _normalize_host(host: str) -> str | None:
    host = host.strip().lower().split("@")[-1].split(":", 1)[0].rstrip(".")
    while host.startswith("www."):
        host = host[4:]
    return host or None


def _word_boundary_pattern(parts: Sequence[str]) -> re.Pattern[str] | None:
    clean = _unique(part.strip() for part in parts if part and part.strip())
    if not clean:
        return None
    body = "|".join(re.escape(part) for part in sorted(clean, key=len, reverse=True))
    return re.compile(rf"{_TEXT_BOUNDARY_LEFT}(?:{body}){_TEXT_BOUNDARY_RIGHT}", re.IGNORECASE)


def _text_terms(*, slug: str, domain: str, name: str | None, aliases: Sequence[str]) -> tuple[str, ...]:
    explicit = [term for term in (name, *aliases) if term and not _is_domainish(term)]
    if explicit:
        return _unique(explicit)

    slug_term = _slug_to_text_term(slug)
    domain_term = _domain_to_text_term(domain)
    return _unique(term for term in (slug_term, domain_term) if term)


def _slug_to_text_term(slug: str) -> str | None:
    token = slug.strip().lower()
    for suffix in _COMMON_TLD_SLUG_SUFFIXES:
        if token.endswith(suffix):
            token = token[: -len(suffix)]
            break
    token = token.replace("-", " ").strip()
    return token or None


def _domain_to_text_term(domain: str) -> str | None:
    normalized = normalize_domain(domain)
    if not normalized:
        return None
    return normalized.split(".", 1)[0].strip() or None


def _first_text_hit_by_slug(text_hits: Sequence[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    first: dict[str, dict[str, Any]] = {}
    for hit in text_hits:
        first.setdefault(hit["slug"], hit)
    return first


def _record_sort_key(
    slug: str,
    domain_hits: Mapping[str, dict[str, Any]],
    text_hits: Mapping[str, dict[str, Any]],
) -> tuple[int, int, str]:
    if slug in domain_hits:
        return (0, 0, slug)
    span = text_hits[slug]["span"]
    return (1, span[0], slug)


def _iter_dicts(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _join_text(*parts: Any) -> str | None:
    clean = [str(part).strip() for part in parts if part is not None and str(part).strip()]
    return "\n".join(clean) if clean else None


def _string_or_none(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _string_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if not isinstance(value, Sequence):
        return []
    return [str(item).strip() for item in value if item is not None and str(item).strip()]


def _required_string(member: Mapping[str, Any], key: str) -> str:
    value = _string_or_none(member.get(key))
    if value is None:
        raise ValueError(f"cohort member missing required {key!r}: {member!r}")
    return value


def _is_domainish(value: str) -> bool:
    raw = str(value).strip()
    if not raw or re.search(r"\s", raw):
        return False
    normalized = normalize_domain(raw)
    return bool(normalized and "." in normalized)


def _unique(values: Any) -> tuple[str, ...]:
    out = []
    seen = set()
    for value in values:
        text = str(value).strip()
        key = text.lower()
        if not text or key in seen:
            continue
        seen.add(key)
        out.append(text)
    return tuple(out)
