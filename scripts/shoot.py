#!/usr/bin/env python3
"""shoot — Tier-B browser re-render for the visual-evidence module.

Firecrawl's headless browser exposes no WebGL and fires its full-page screenshot before
lazy media and scroll-triggered animations settle — so a WebGL hero renders as a grey
block, count-ups read 0.0, and reveals stay half-faded (proven on Function Health). This
is the escalation the QA gate reaches for when a cached payload can't be trusted: drive
*system Chrome* (real WebGL via ANGLE Metal), warm-scroll to fire lazy media, then ask the
page for reduced motion and settle so animations finish before tiling.

It writes native-resolution viewport tiles + a manifest fragment to --out-dir, the same
tile shape `tile.py` emits for the cached path, so downstream blind mining reads either
uniformly. No Firecrawl spend; the only dependency the module earns (quarantined here).

CLI:  python3 scripts/shoot.py <url> --out-dir store/<slug>/captures/<date>/tiles/<page>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

# System Chrome (not Playwright's bundled Chromium) — it ships real GPU/WebGL, which is the
# whole point: it renders the marketing media Firecrawl's browser can't.
DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Injected only after the warm scroll: forces any lingering opacity/transform reveal to its
# resting state and zeroes transition/animation time, so a tile never catches mid-animation.
FINAL_STATE_CSS = """
*, *::before, *::after {
  animation-duration: 0s !important; animation-delay: 0s !important;
  transition-duration: 0s !important; transition-delay: 0s !important;
}
[class*="fade"], [class*="reveal"], [data-aos], [class*="inview"], [class*="in-view"] {
  opacity: 1 !important; transform: none !important; filter: none !important;
}
"""

CONSENT_LABELS = ["I understand", "Accept", "Accept all", "Got it", "Agree", "I consent"]

# Consent/cookie managers render a fixed overlay pinned to a viewport corner — on a
# viewport-tile re-render it stamps onto every tile, and click-dismissal misses it when the
# widget duplicates itself or mounts a closed shadow root (e.g. Transcend on goodlifemeds).
# Hiding the known vendor mounts is more reliable than clicking through them.
CONSENT_MOUNTS = (
    "#transcend-consent-manager,#onetrust-consent-sdk,#onetrust-banner-sdk,"
    "#CybotCookiebotDialog,#didomi-host,#termly-code-snippet-support,#usercentrics-root,"
    ".osano-cm-window,#cookie-law-info-bar,#cookie-consent-dialog{display:none!important}"
)


def tile_offsets(scroll_height: int, viewport_height: int, overlap: int) -> list[int]:
    """Top y-offset of each viewport tile, overlapping by `overlap` and pinning the last to the floor."""
    step = viewport_height - overlap
    offsets: list[int] = []
    y = 0
    last = max(0, scroll_height - viewport_height)
    while y < last:
        offsets.append(y)
        y += step
    if not offsets or offsets[-1] != last:
        offsets.append(last)
    return offsets


def capture(url: str, out_dir: Path, width: int, height: int, overlap: int,
            settle_ms: int, chrome: str) -> dict:
    """Drive system Chrome to warm-scroll `url`, settle motion, then write viewport tiles to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome,
            headless=True,
            args=["--autoplay-policy=no-user-gesture-required"],
        )
        # reduced_motion=reduce: a well-built site shortcuts its animations to final state for us.
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            locale="en-US",
            reduced_motion="reduce",
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(2500)

        for label in CONSENT_LABELS:
            try:
                page.get_by_text(label, exact=True).first.click(timeout=1200)
                page.wait_for_timeout(400)
                break
            except PlaywrightTimeoutError:
                continue
        page.add_style_tag(
            content="[class*='intercom'],iframe[src*='intercom'],[aria-label*='chat' i]{display:none!important}"
        )
        page.add_style_tag(content=CONSENT_MOUNTS)

        # Finer warm scroll (600px steps) so every intersection-observer fires and lazy media loads.
        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        for y in range(0, scroll_height, 600):
            page.evaluate("(y) => window.scrollTo(0, y)", y)
            page.wait_for_timeout(120)
        page.evaluate("() => window.scrollTo(0, document.documentElement.scrollHeight)")
        page.wait_for_timeout(settle_ms)
        page.add_style_tag(content=FINAL_STATE_CSS)
        page.wait_for_timeout(400)

        info = page.evaluate(
            """() => ({
                url: location.href,
                title: document.title,
                scrollHeight: document.documentElement.scrollHeight,
                imageCount: document.images.length,
                loadedImages: Array.from(document.images)
                  .filter((img) => img.complete && img.naturalWidth > 0).length
              })"""
        )

        tiles: list[dict] = []
        for index, y in enumerate(tile_offsets(info["scrollHeight"], height, overlap)):
            actual_y = page.evaluate("(y) => { window.scrollTo(0, y); return window.scrollY; }", y)
            page.wait_for_timeout(settle_ms)
            name = f"tile-{index:02d}-y{round(actual_y):05d}.png"
            page.screenshot(path=str(out_dir / name), full_page=False, type="png")
            tiles.append({"index": index, "y": round(actual_y), "file": name})

        browser.close()

    manifest = {
        "url": url,
        "source": "shoot",  # Tier-B browser re-render (vs tile.py's cached crop)
        "viewport": {"width": width, "height": height},
        "overlap": overlap,
        "page": info,
        "tiles": tiles,
    }
    with open(out_dir / "manifest.json", "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Tier-B browser re-render → native-resolution tiles.")
    parser.add_argument("url")
    parser.add_argument("--out-dir", required=True, help="tile dir, e.g. store/<slug>/captures/<date>/tiles/<page>")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1400)
    parser.add_argument("--overlap", type=int, default=180)
    parser.add_argument("--settle-ms", type=int, default=1600)
    parser.add_argument("--chrome", default=DEFAULT_CHROME)
    args = parser.parse_args()

    manifest = capture(
        args.url, Path(args.out_dir), args.width, args.height,
        args.overlap, args.settle_ms, args.chrome,
    )
    page = manifest["page"]
    print(json.dumps({
        "outDir": args.out_dir,
        "loaded": f"{page['loadedImages']}/{page['imageCount']}",
        "scrollHeight": page["scrollHeight"],
        "tiles": len(manifest["tiles"]),
        "title": page["title"],
    }, indent=2))


if __name__ == "__main__":
    main()
