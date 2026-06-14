#!/usr/bin/env python3
"""Build frozen evidence packets for the /research-company model bakeoff."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urljoin


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = EXPERIMENT / "sample.json"
OUT = EXPERIMENT / "_out" / "packets"
CONTRACTS = ["SCHEMA.md", "TAXONOMIES.md", "OFFERINGS.md", "TELEHEALTH.md"]
SVG_SNIFF = re.compile(br"<svg[\s>]", re.I)


def clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def symlink_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    try:
        rel = os.path.relpath(src, dst.parent)
        dst.symlink_to(rel)
    except OSError:
        shutil.copy2(src, dst)


def run_signals(slug: str, date: str, out_path: Path) -> str:
    cmd = [
        "python3",
        "skills/research-company/scripts/fc.py",
        "signals",
        "--slug",
        slug,
        "--date",
        date,
    ]
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(proc.stdout, encoding="utf-8")
    return "ok" if proc.returncode == 0 else f"nonzero:{proc.returncode}"


def svg_dims(text: str) -> tuple[int, int] | None:
    viewbox = re.search(r'viewBox=["\']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)', text)
    if viewbox:
        return (round(float(viewbox.group(1))), round(float(viewbox.group(2))))
    width = re.search(r'width=["\']([\d.]+)', text)
    height = re.search(r'height=["\']([\d.]+)', text)
    if width and height:
        return (round(float(width.group(1))), round(float(height.group(1))))
    return None


def raster_dims(path: Path) -> tuple[int, int] | None:
    proc = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if proc.returncode != 0:
        return None
    width = re.search(r"pixelWidth:\s*(\d+)", proc.stdout)
    height = re.search(r"pixelHeight:\s*(\d+)", proc.stdout)
    if width and height:
        return (int(width.group(1)), int(height.group(1)))
    return None


def data_uri_to_bytes(uri: str) -> tuple[bytes, str] | None:
    if not uri.startswith("data:"):
        return None
    header, _, payload = uri.partition(",")
    if not payload:
        return None
    if ";base64" in header:
        import base64

        blob = base64.b64decode(payload)
    else:
        blob = unquote(payload).encode("utf-8")
    ext = "svg" if "svg" in header or SVG_SNIFF.search(blob[:300]) else "img"
    return blob, ext


def first_homepage_data(capture: Path) -> dict:
    p = capture / ".payloads" / "homepage.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    return data.get("data", data)


def build_logo_evidence(sample: dict, capture: Path, packet: Path) -> dict:
    slug = sample["slug"]
    date = sample["capture_date"]
    data = first_homepage_data(capture)
    meta = data.get("metadata") or {}
    branding = data.get("branding") or {}
    raw = data.get("rawHtml") or ""
    source_url = meta.get("sourceURL") or meta.get("url") or f"https://{sample['domain']}/"
    logo_dir = packet / "logos"
    measured_dir = logo_dir / "measured"
    logo_dir.mkdir(parents=True, exist_ok=True)

    candidates: dict = {
        "source_url": source_url,
        "profile_module": "logos",
        "wordmark_candidates": [],
        "logomark_candidates": [],
        "og_candidates": [],
        "measured_assets": [],
        "branding_summary": {
            "colors": branding.get("colors"),
            "fonts": branding.get("fonts") or (branding.get("typography") or {}).get("fontFamilies"),
            "llm_logo_reasoning": branding.get("__llm_logo_reasoning"),
        },
    }

    logo = ((branding.get("images") or {}).get("logo") or "").strip()
    if logo:
        item = {"source": "branding.images.logo"}
        decoded = data_uri_to_bytes(logo)
        if decoded:
            blob, ext = decoded
            if ext == "svg":
                target = logo_dir / "branding-wordmark.svg"
                target.write_bytes(blob)
                dims = svg_dims(blob.decode("utf-8", "ignore"))
                item.update({"path": str(target.relative_to(packet)), "kind": "decoded-data-uri", "dims": dims})
            else:
                target = logo_dir / f"branding-wordmark.{ext}"
                target.write_bytes(blob)
                item.update({"path": str(target.relative_to(packet)), "kind": "decoded-data-uri", "dims": raster_dims(target)})
        else:
            item.update({"url": logo, "kind": "url"})
        candidates["wordmark_candidates"].append(item)

    jsonld_logo = re.findall(r'"logo"\s*:\s*"([^"]+)"', raw)
    for u in jsonld_logo[:5]:
        candidates["wordmark_candidates"].append({"source": "rawHtml JSON-LD logo", "url": urljoin(source_url, unescape(u)), "kind": "url"})

    favicon = meta.get("favicon")
    if favicon:
        candidates["logomark_candidates"].append({"source": "metadata.favicon", "url": urljoin(source_url, favicon)})
    candidates["logomark_candidates"].append(
        {"source": "google-s2", "url": f"https://www.google.com/s2/favicons?domain={sample['domain']}&sz=256"}
    )
    for lm in re.finditer(r"<link\b[^>]*apple-touch-icon[^>]*>", raw, re.I):
        href = re.search(r'href=["\']([^"\']+)["\']', lm.group(0))
        if href:
            candidates["logomark_candidates"].append({"source": "apple-touch-icon", "url": urljoin(source_url, href.group(1))})

    og = meta.get("og:image") or meta.get("ogImage")
    if isinstance(og, list):
        for u in og:
            if u:
                candidates["og_candidates"].append({"source": "metadata.og:image", "url": urljoin(source_url, u)})
    elif og:
        candidates["og_candidates"].append({"source": "metadata.og:image", "url": urljoin(source_url, og)})

    source_logo_dir = capture / ".payloads" / "logos"
    if source_logo_dir.exists():
        measured_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(source_logo_dir.iterdir()):
            if not src.is_file():
                continue
            dst = measured_dir / src.name
            copy_file(src, dst)
            dims = svg_dims(dst.read_text(encoding="utf-8", errors="ignore")) if dst.suffix == ".svg" else raster_dims(dst)
            candidates["measured_assets"].append({"path": str(dst.relative_to(packet)), "dims": dims})

    (logo_dir / "logo-candidates.json").write_text(json.dumps(candidates, indent=2) + "\n", encoding="utf-8")
    lines = [
        f"# Logo evidence: {sample['sample_id']}",
        "",
        "Use this file to fill `logo_url` and `logos:{}` in `profile.md`.",
        "",
        "## Wordmark candidates",
        "",
    ]
    if candidates["wordmark_candidates"]:
        for item in candidates["wordmark_candidates"]:
            desc = item.get("path") or item.get("url")
            dims = item.get("dims")
            lines.append(f"- {item.get('source')}: `{desc}`" + (f" ({dims[0]}x{dims[1]})" if dims else ""))
    else:
        lines.append("- none found in homepage payload")
    lines.extend(["", "## Logomark candidates", ""])
    for item in candidates["logomark_candidates"]:
        lines.append(f"- {item.get('source')}: `{item.get('url')}`")
    lines.extend(["", "## OG candidates", ""])
    if candidates["og_candidates"]:
        for item in candidates["og_candidates"]:
            lines.append(f"- {item.get('source')}: `{item.get('url')}`")
    else:
        lines.append("- none declared")
    lines.extend(["", "## Measured assets copied from `fc.py logos`", ""])
    if candidates["measured_assets"]:
        for item in candidates["measured_assets"]:
            dims = item.get("dims")
            lines.append(f"- `{item['path']}`" + (f" ({dims[0]}x{dims[1]})" if dims else ""))
    else:
        lines.append("- none yet; run `python3 skills/research-company/scripts/fc.py logos --slug " + slug + " --date " + date + "` and rebuild packets")
    lines.extend(
        [
            "",
            "## Instructions",
            "",
            "- Prefer the decoded branding wordmark when it is visibly the real header brand mark.",
            "- Copy the chosen wordmark into the candidate output as `assets/wordmark.svg` when it is a local SVG.",
            "- Use measured logomark/OG dimensions when present.",
            "- Judge `transparent` by looking at the measured logomark asset; do not trust alpha alone.",
            "- Omit a slot only on true absence and note the reason in `RUN_NOTES.md`.",
            "",
        ]
    )
    (logo_dir / "LOGO_EVIDENCE.md").write_text("\n".join(lines), encoding="utf-8")
    return candidates


def build_packet(sample: dict) -> None:
    sample_id = sample["sample_id"]
    slug = sample["slug"]
    date = sample["capture_date"]
    capture = ROOT / "store" / slug / "captures" / date
    payloads = capture / ".payloads"
    packet = OUT / sample_id

    if not capture.exists():
        raise FileNotFoundError(f"Missing capture: {capture}")

    clean_dir(packet)

    for contract in CONTRACTS:
        copy_file(ROOT / contract, packet / "contracts" / contract)

    source_files = sorted(capture.glob("*.md"))
    for src in source_files:
        copy_file(src, packet / "sources" / src.name)

    payload_files = []
    if payloads.exists():
        for src in sorted(payloads.glob("*.png")):
            symlink_or_copy(src, packet / "screenshots" / src.name)
        for name in ["manifest.jsonl", "map.json"]:
            src = payloads / name
            if src.exists():
                copy_file(src, packet / "payloads" / name)
                payload_files.append(packet / "payloads" / name)

    signals_status = run_signals(slug, date, packet / "signals" / "homepage.txt")
    logo_evidence = build_logo_evidence(sample, capture, packet)

    screenshot_files = sorted((packet / "screenshots").glob("*.png")) if (packet / "screenshots").exists() else []

    manifest = {
        "sample": sample,
        "capture_path": str(capture.relative_to(ROOT)),
        "source_files": [str(p.relative_to(packet)) for p in sorted((packet / "sources").glob("*.md"))],
        "screenshot_files": [str(p.relative_to(packet)) for p in screenshot_files],
        "payload_files": [str(p.relative_to(packet)) for p in payload_files],
        "signals_status": signals_status,
        "profile_modules": sample.get("profile_modules", []),
        "logo_evidence": {
            "wordmark_candidates": len(logo_evidence["wordmark_candidates"]),
            "measured_assets": len(logo_evidence["measured_assets"]),
        },
    }
    (packet / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    packet_md = [
        f"# Evidence packet: {sample_id}",
        "",
        f"- Domain: `{sample['domain']}`",
        f"- Store slug: `{slug}`",
        f"- Capture date: `{date}`",
        f"- Capture path: `{capture.relative_to(ROOT)}`",
        f"- Requested outputs: {', '.join(sample['requested_outputs'])}",
        f"- Requested profile modules: {', '.join(sample.get('profile_modules', [])) or 'none'}",
        f"- Why included: {sample['why']}",
        "",
        "## Boundaries",
        "",
        "- Use only this packet and copied contracts.",
        "- Do not open canonical `store/<slug>/profile.md`, `offerings.md`, or `telehealth.md`.",
        "- Do not use live web, Firecrawl, Notion, or prior knowledge.",
        "",
        "## Contracts",
        "",
    ]
    packet_md.extend(f"- `contracts/{name}`" for name in CONTRACTS)
    packet_md.extend(["", "## Sources", ""])
    packet_md.extend(f"- `{p}`" for p in manifest["source_files"])
    packet_md.extend(["", "## Screenshots", ""])
    if manifest["screenshot_files"]:
        packet_md.extend(f"- `{p}`" for p in manifest["screenshot_files"])
    else:
        packet_md.append("- none")
    packet_md.extend(["", "## Payload Hints", ""])
    packet_md.append("- `signals/homepage.txt`")
    packet_md.extend(f"- `{p}`" for p in manifest["payload_files"])
    packet_md.extend(["", "## Logo Evidence", ""])
    packet_md.append("- `logos/LOGO_EVIDENCE.md`")
    packet_md.append("- `logos/logo-candidates.json`")
    if logo_evidence["measured_assets"]:
        packet_md.extend(f"- `{item['path']}`" for item in logo_evidence["measured_assets"])
    packet_md.extend(
        [
            "",
            "## Candidate Output Location",
            "",
            f"- GPT-5.5: `{EXPERIMENT.relative_to(ROOT)}/_out/gpt55/{sample_id}/`",
            f"- Claude comparator: `{EXPERIMENT.relative_to(ROOT)}/_out/claude/{sample_id}/`",
            "",
        ]
    )
    (packet / "PACKET.md").write_text("\n".join(packet_md), encoding="utf-8")


def main() -> None:
    samples = json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    for sample in samples:
        build_packet(sample)
    index = [
        "# Packet index",
        "",
        f"Built {len(samples)} packets.",
        "",
    ]
    for sample in samples:
        index.append(f"- `{sample['sample_id']}` - {sample['domain']} ({sample['capture_date']})")
    (OUT / "INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
