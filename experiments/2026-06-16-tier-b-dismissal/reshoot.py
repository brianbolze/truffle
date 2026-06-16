#!/usr/bin/env python3
"""Throwaway: re-render any Healthspan page with newsletter modal + custom cookie
banner dismissed/hidden, then tile in shoot.py's shape. Experiment-grade, not committed.

Usage: python3 /tmp/reshoot.py <url> <out-dir>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "scripts")
from shoot import CONSENT_MOUNTS, FINAL_STATE_CSS, tile_offsets  # noqa: E402

from playwright.sync_api import TimeoutError as PWTimeout  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H, OVERLAP, SETTLE = 1920, 1400, 180, 1600
DISMISS_LABELS = ["No, thanks", "No thanks", "No Thanks", "Close", "Decline", "Accept", "Got it"]
EXTRA_HIDE = CONSENT_MOUNTS + (
    "[class*='cookie' i],[id*='cookie' i],[class*='consent' i],[id*='consent' i]"
    "{display:none!important}"
)


def main() -> None:
    url, out = sys.argv[1], Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME, headless=True,
                                    args=["--autoplay-policy=no-user-gesture-required"])
        ctx = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=1,
                                  locale="en-US", reduced_motion="reduce")
        page = ctx.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except PWTimeout:
            pass
        page.wait_for_timeout(3000)
        for _ in range(2):
            page.keyboard.press("Escape")
            page.wait_for_timeout(250)
        for label in DISMISS_LABELS:
            try:
                page.get_by_text(label, exact=True).first.click(timeout=800)
                page.wait_for_timeout(250)
            except PWTimeout:
                continue
        page.keyboard.press("Escape")
        page.wait_for_timeout(250)
        page.add_style_tag(content="[class*='intercom'],iframe[src*='intercom'],[aria-label*='chat' i]{display:none!important}")
        page.add_style_tag(content=EXTRA_HIDE)

        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        for y in range(0, scroll_height, 600):
            page.evaluate("(y) => window.scrollTo(0, y)", y)
            page.wait_for_timeout(120)
        page.evaluate("() => window.scrollTo(0, document.documentElement.scrollHeight)")
        page.wait_for_timeout(SETTLE)
        page.add_style_tag(content=FINAL_STATE_CSS)
        page.wait_for_timeout(400)
        # belt-and-suspenders: re-hide after late-mounting consent widget
        page.add_style_tag(content=EXTRA_HIDE)

        info = page.evaluate("""() => ({url:location.href,title:document.title,
            scrollHeight:document.documentElement.scrollHeight,imageCount:document.images.length,
            loadedImages:Array.from(document.images).filter(i=>i.complete&&i.naturalWidth>0).length})""")
        for old in out.glob("tile-*.png"):
            old.unlink()
        tiles = []
        for index, y in enumerate(tile_offsets(info["scrollHeight"], H, OVERLAP)):
            actual_y = page.evaluate("(y)=>{window.scrollTo(0,y);return window.scrollY;}", y)
            page.wait_for_timeout(SETTLE)
            name = f"tile-{index:02d}-y{round(actual_y):05d}.png"
            page.screenshot(path=str(out / name), full_page=False, type="png")
            tiles.append({"index": index, "y": round(actual_y), "file": name})
        browser.close()
    with open(out / "manifest.json", "w", encoding="utf-8") as fh:
        json.dump({"url": url, "source": "shoot+dismiss", "viewport": {"width": W, "height": H},
                   "overlap": OVERLAP, "page": info, "tiles": tiles}, fh, indent=2)
    print(json.dumps({"page": str(out.name), "loaded": f"{info['loadedImages']}/{info['imageCount']}",
                      "tiles": len(tiles)}))


if __name__ == "__main__":
    main()
