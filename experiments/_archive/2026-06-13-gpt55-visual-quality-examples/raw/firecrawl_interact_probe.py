#!/usr/bin/env python3
"""Small Firecrawl /interact probe for Function screenshot rendering."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
API = "https://api.firecrawl.dev/v2"


def api_key() -> str:
    key = os.environ.get("FIRECRAWL_API_KEY")
    if key:
        return key
    settings = Path.home() / ".claude" / "settings.json"
    if settings.exists():
        data = json.loads(settings.read_text())
        key = data.get("env", {}).get("FIRECRAWL_API_KEY")
        if key:
            return key
    raise SystemExit("FIRECRAWL_API_KEY missing")


def request_json(method: str, path: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        f"{API}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=360) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        payload = e.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {payload}") from e


CODE = r"""
const desktop = 'https://pm3i9nzo0jeqag2m.public.blob.vercel-storage.com/lucid/hero/desktop/images/3vid_1920x1080.webp';
const mobile = 'https://pm3i9nzo0jeqag2m.public.blob.vercel-storage.com/lucid/hero/mobile/images/3vid_1080x1920.webp';
const info = await page.evaluate(async ({ desktop, mobile }) => {
  const hero = document.querySelector('#canvasContainer');
  const canvas = hero && hero.querySelector('.flute-canvas');
  const glProbe = document.createElement('canvas');
  const webgl =
    Boolean(glProbe.getContext('webgl')) ||
    Boolean(glProbe.getContext('experimental-webgl')) ||
    Boolean(glProbe.getContext('webgl2'));
  const before = canvas ? {
    className: canvas.className,
    style: canvas.getAttribute('style'),
    width: canvas.width,
    height: canvas.height,
    opacity: getComputedStyle(canvas).opacity,
    visibility: getComputedStyle(canvas).visibility
  } : null;
  const src = window.innerWidth < 768 ? mobile : desktop;
  if (hero) {
    const old = hero.querySelector('.fc-hero-poster');
    if (old) old.remove();
    const img = new Image();
    img.className = 'fc-hero-poster';
    img.alt = 'Abstract glass helix in motion';
    Object.assign(img.style, {
      position: 'absolute',
      inset: '0',
      width: '100%',
      height: '100%',
      objectFit: 'cover',
      zIndex: '0',
      pointerEvents: 'none'
    });
    if (canvas && (canvas.classList.contains('is-hidden') || getComputedStyle(canvas).visibility === 'hidden' || getComputedStyle(canvas).opacity === '0')) {
      canvas.style.display = 'none';
    }
    const content = hero.querySelector('.flute-hero');
    if (content) Object.assign(content.style, { position: 'relative', zIndex: '2' });
    hero.prepend(img);
    await new Promise((resolve) => {
      img.onload = resolve;
      img.onerror = resolve;
      img.src = src;
      if (img.complete) resolve();
    });
  }
  const poster = hero && hero.querySelector('.fc-hero-poster');
  return {
    url: location.href,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    webgl,
    before,
    poster: poster ? {
      src: poster.currentSrc || poster.src,
      complete: poster.complete,
      naturalWidth: poster.naturalWidth,
      naturalHeight: poster.naturalHeight
    } : null
  };
}, { desktop, mobile });
const heroShot = await page.locator('#canvasContainer').screenshot({ type: 'png' });
JSON.stringify({ info, heroPngBase64: heroShot.toString('base64') });
"""

INSPECT_CODE = r"""
const info = await page.evaluate(() => {
  const hero = document.querySelector('#canvasContainer');
  const canvas = hero && hero.querySelector('.flute-canvas');
  const glProbe = document.createElement('canvas');
  const webgl =
    Boolean(glProbe.getContext('webgl')) ||
    Boolean(glProbe.getContext('experimental-webgl')) ||
    Boolean(glProbe.getContext('webgl2'));
  return {
    url: location.href,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    webgl,
    heroFound: Boolean(hero),
    canvas: canvas ? {
      className: canvas.className,
      style: canvas.getAttribute('style'),
      width: canvas.width,
      height: canvas.height,
      opacity: getComputedStyle(canvas).opacity,
      visibility: getComputedStyle(canvas).visibility,
      display: getComputedStyle(canvas).display
    } : null,
    videos: Array.from(document.querySelectorAll('video')).slice(0, 8).map(video => ({
      src: video.currentSrc || video.src,
      readyState: video.readyState,
      networkState: video.networkState,
      paused: video.paused,
      currentTime: video.currentTime,
      videoWidth: video.videoWidth,
      videoHeight: video.videoHeight
    })),
    images: Array.from(document.images).slice(0, 12).map(img => ({
      src: img.currentSrc || img.src,
      complete: img.complete,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      loading: img.loading
    }))
  };
});
JSON.stringify(info);
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("scrape_id")
    ap.add_argument("--out", required=True)
    ap.add_argument("--timeout", type=int, default=90)
    ap.add_argument("--inspect-only", action="store_true")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    try:
        resp = request_json(
            "POST",
            f"/scrape/{args.scrape_id}/interact",
            {"code": INSPECT_CODE if args.inspect_only else CODE, "language": "node", "timeout": args.timeout},
        )
    finally:
        try:
            request_json("DELETE", f"/scrape/{args.scrape_id}/interact")
        except Exception as e:  # best-effort cleanup
            print(f"warning: stop interaction failed: {e}", file=sys.stderr)

    raw_path = out.with_suffix(".json")
    raw_path.write_text(json.dumps(resp, indent=2) + "\n")

    result = resp.get("result") or "{}"
    payload = json.loads(result) if result else {}
    image_b64 = payload.pop("heroPngBase64", None)
    if image_b64:
        out.write_bytes(base64.b64decode(image_b64))

    print(json.dumps({"success": resp.get("success"), "out": str(out), "raw": str(raw_path), **payload}, indent=2))


if __name__ == "__main__":
    main()
