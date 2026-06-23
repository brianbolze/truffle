#!/usr/bin/env python3
"""Light mechanical checks for model-bakeoff candidate outputs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


EXPERIMENT = Path(__file__).resolve().parents[1]
SAMPLES = json.loads((EXPERIMENT / "sample.json").read_text(encoding="utf-8"))
LEAK_TOKENS = ["</invoke>", "</content>", "<invoke", "<content"]
OFFERINGS_ENUMERATION = {"indexed-complete", "lines-omitted", "unknown"}

# Profile classification closed sets (from contracts/TAXONOMIES.md). Mechanizing
# the -15 "value outside closed set" penalty keeps it off the LLM judge's plate —
# a deterministic pass/fail the judge can't bias or overlook. Empty is allowed
# everywhere; `Other` is allowed only on the four category fields, never on the
# ordinal portfolio_shape.
PROFILE_SINGLE = {
    "entity_type": {"Company", "Brand", "Investor / Holding", "Nonprofit",
                    "Government", "Education", "Individual / Creator", "Other"},
    "portfolio_shape": {"Single", "Flagship + companions", "Multi-product", "Catalog"},
    "business_model": {"Subscription", "Transactional / One-time", "Usage-based / Consumption",
                       "Marketplace / Commission", "Freemium", "Advertising",
                       "Services / Project-based", "Licensing", "Other"},
    "primary_industry": {"Technology", "Energy & Utilities", "Finance & Fintech",
                         "Healthcare & Life Sciences", "Retail & E-Commerce", "Media & Entertainment",
                         "Manufacturing & Industrial", "Automotive & Mobility", "Logistics & Supply Chain",
                         "Agriculture & Food", "Real Estate & Construction", "Education & Training",
                         "Consulting & Professional Services", "Consumer Goods", "Telecommunications",
                         "Environmental & Sustainability", "Defense & Security", "Hospitality & Tourism",
                         "Cryptocurrency & Blockchain", "Sports & Recreation", "Other"},
}
PROFILE_MULTI = {
    "target_market": {"B2B", "B2C", "B2B2C", "B2G", "Other"},
    "offering_category": {"Software / SaaS", "Physical Products / Hardware", "Services / Consulting",
                          "Marketplace / Platform", "Media / Content", "Financial / Fintech Products",
                          "Biotech / Pharma Products", "Consumer Packaged Goods (CPG)",
                          "Retail / E-Commerce", "Industrial / Manufacturing", "Energy / Utilities",
                          "Non-Profit / NGO", "Other"},
}
REQUIRED_PROFILE_SECTIONS = ["## Overview", "## Provenance"]
TELEHEALTH_FIELDS = {
    "value_chain_role": {"DTC brand", "compounding pharmacy", "platform/infra", "diagnostics/labs", "wholesale/supply", "unclear"},
    "pharmacy_model": {"integrated", "third-party", "is-a-pharmacy", "none/diagnostics-only", "unclear"},
    "audience": {"men-only", "men-first", "all-genders", "women-first", "women-only", "unclear"},
    "compounding_posture": {"compounded-only", "both", "FDA-brand-only", "OTC/supplement", "unclear"},
    "anchor_category": {"TRT", "GLP-1", "sexual-health", "hair", "skin", "longevity/NAD", "peptides", "womens-HRT", "labs", "mental-health", "primary-care", "multi/none", "unclear"},
    "modality": {"async", "hybrid", "sync", "N/A", "unclear"},
    "access_model": {"membership-required", "all-in", "per-visit", "à-la-carte/both", "unclear"},
    "pay_model": {"cash-pay only", "HSA/FSA eligible", "bills insurance", "N/A", "unclear"},
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    raw = text.split("---", 2)[1]
    values: dict[str, str] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if " #" in value:
            value = value.split(" #", 1)[0].rstrip()
        values[key.strip()] = value.strip('"').strip("'")
    return values


def list_values(raw: str) -> list[str]:
    """Split a YAML inline-list frontmatter value (`[A, B]`) into members.

    Offering/market values never contain commas, so a naive comma split is safe.
    """
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [v.strip().strip('"').strip("'") for v in raw.split(",") if v.strip()]


def closed_set_errors(sample_id: str, fm: dict[str, str]) -> list[str]:
    """Validate profile classification fields against the contract closed sets."""
    errors: list[str] = []
    for field, allowed in PROFILE_SINGLE.items():
        value = (fm.get(field) or "").strip()
        if value and value not in allowed:
            errors.append(f"{sample_id}: profile.md {field} {value!r} outside closed set")
    for field, allowed in PROFILE_MULTI.items():
        for value in list_values(fm.get(field) or ""):
            if value not in allowed:
                errors.append(f"{sample_id}: profile.md {field} value {value!r} outside closed set")
    return errors


# Mirrors fc.py's logo_issues / SCHEMA §Logos-lint: a recorded slot must carry its measurement
# (wordmark/og: w+h; logomark: px+transparent) — the bar FINDINGS flagged as too loose here.
LOGO_SLOT_KEYS = {"wordmark": ("w", "h"), "logomark": ("px", "transparent"), "og": ("w", "h")}


def logo_slot_issues(path: Path) -> list[str]:
    """Slots in a logos:{} block must carry measurements. Returns issue strings: an empty/absent
    block (logos was a requested module), plus any recorded slot missing its measurement."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if "logos: {}" in text or not text.startswith("---\n"):
        return ["has empty logos block for requested logos module"]
    raw = text.split("---", 2)[1]
    found = False
    issues: list[str] = []
    for slot, required in LOGO_SLOT_KEYS.items():
        m = re.search(rf"^\s{{2,}}{slot}:\s*\{{([^}}]*)\}}", raw, re.M)
        if not m:
            continue
        found = True
        missing = [k for k in required if not re.search(rf"\b{k}:", m.group(1))]
        if missing:
            issues.append(f"logos.{slot} recorded without {', '.join(missing)} (the measurement is the fact)")
    if not found:
        issues.append("has empty logos block for requested logos module")
    return issues


def check_candidate(model: str, sample: dict) -> list[str]:
    sample_id = sample["sample_id"]
    out = EXPERIMENT / "_out" / model / sample_id
    errors: list[str] = []

    if not out.exists():
        return [f"{sample_id}: missing output dir {out}"]

    for name in sample["requested_outputs"]:
        path = out / name
        if not path.exists():
            errors.append(f"{sample_id}: missing {name}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if name == "profile.md":
            if not text.startswith("---\n"):
                errors.append(f"{sample_id}: profile.md missing YAML frontmatter")
            fm = frontmatter(path)
            if not fm.get("schema_version"):
                errors.append(f"{sample_id}: profile.md missing schema_version")
            if "logos" in sample.get("profile_modules", []):
                if not fm.get("logo_url"):
                    errors.append(f"{sample_id}: profile.md missing logo_url for requested logos module")
                for issue in logo_slot_issues(path):
                    errors.append(f"{sample_id}: profile.md {issue}")
            for section in REQUIRED_PROFILE_SECTIONS:
                if section not in text:
                    errors.append(f"{sample_id}: profile.md missing {section} section")
            errors.extend(closed_set_errors(sample_id, fm))
        if name == "offerings.md":
            fm = frontmatter(path)
            enumeration = fm.get("enumeration")
            if enumeration not in OFFERINGS_ENUMERATION:
                errors.append(f"{sample_id}: offerings.md bad enumeration {enumeration!r}")
        if name == "telehealth.md":
            fm = frontmatter(path)
            for field, allowed in TELEHEALTH_FIELDS.items():
                value = fm.get(field)
                if value not in allowed:
                    errors.append(f"{sample_id}: telehealth.md bad {field} {value!r}")
        if any(tok in text for tok in LEAK_TOKENS):
            errors.append(f"{sample_id}: {name} contains leaked tool-call tag")

    if not (out / "RUN_NOTES.md").exists():
        errors.append(f"{sample_id}: missing RUN_NOTES.md")

    return errors


def main() -> int:
    model = sys.argv[1] if len(sys.argv) > 1 else "gpt55"
    all_errors: list[str] = []
    for sample in SAMPLES:
        all_errors.extend(check_candidate(model, sample))

    if all_errors:
        print("\n".join(all_errors))
        return 1
    print(f"{model}: all requested candidate files present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
