#!/usr/bin/env python3
"""Score the routed candidates AFTER routing. Labels are the oracle only.

Reports (no blended score):
  - route tally per cohort
  - every source-host (listicle host) card and where it routed  [cardinal precision]
  - the full capture list per cohort                            [eyeball precision]
  - holdout / CI-core recall over candidates that were actually present
"""
import json, os, re

HERE = os.path.dirname(__file__)
PACKET = os.path.abspath(os.path.join(HERE, "..", ".."))
VAL = os.path.join(PACKET, "validation-inputs")


def reg(h):
    h = re.sub(r"^https?://", "", (h or "").lower()).split("/")[0]
    h = h[4:] if h.startswith("www.") else h
    p = h.split(".")
    return h if len(p) <= 2 else ".".join(p[-2:])


def load(path):
    return [json.loads(l) for l in open(path)] if os.path.exists(path) else []


def tally(rows):
    t = {}
    for r in rows:
        t[r["route"]] = t.get(r["route"], 0) + 1
    return {k: t[k] for k in sorted(t)}


def main():
    th = load(os.path.join(HERE, "routed-telehealth.jsonl"))
    ci = load(os.path.join(HERE, "routed-conversation-intelligence.jsonl"))

    for name, rows in [("TELEHEALTH", th), ("CONVERSATION-INTELLIGENCE", ci)]:
        print(f"\n================ {name} ({len(rows)} cards) ================")
        print("route tally:", tally(rows))

        srcs = [r for r in rows if r.get("is_source_domain")]
        print(f"\nsource-host cards ({len(srcs)}) -> route  [cardinal: a pure publisher in 'capture' is the error]")
        for r in sorted(srcs, key=lambda r: r["route"]):
            print(f"  {r['route']:9s} {r['domain']:24s} {r.get('reason','')[:70]}")

        caps = [r for r in rows if r["route"] == "capture"]
        print(f"\ncapture list ({len(caps)}):")
        for r in sorted(caps, key=lambda r: r["domain"]):
            flag = " [SOURCE-HOST]" if r.get("is_source_domain") else ""
            print(f"  {r['domain']:26s} {r.get('confidence','?'):5s}{flag}  {r.get('reason','')[:60]}")

    # recall: telehealth holdouts present in routed set
    print("\n================ RECALL (present candidates only) ================")
    holд = json.load(open(os.path.join(VAL, "telehealth-holdouts.json")))["holdouts"]
    routed_dom = {reg(r["domain"]): r for r in th}
    present = [(h, routed_dom[reg(h["website"])]) for h in holд if reg(h["website"]) in routed_dom]
    good = [p for p in present if p[1]["route"] in ("capture", "review")]
    print(f"telehealth holdouts present in cards: {len(present)}/{len(holд)}; routed to capture/review: {len(good)}")
    for h, r in present:
        print(f"  {h['name']:16s} {h['gate']:10s} -> {r['route']}")

    core = json.load(open(os.path.join(VAL, "conversation-intelligence-targets.json")))["core_ranked"]
    names = {(r.get("name") or "").lower(): r for r in ci}
    anchors = {(r.get("name") or "").lower(): r for r in ci}
    def find(nm):
        nm = nm.lower()
        for k, r in names.items():
            if k and (k in nm or nm.split()[0] == k or nm.split()[0] in k):
                return r
        return None
    hits = [(c, find(c["name"])) for c in core]
    present_ci = [(c, r) for c, r in hits if r]
    good_ci = [(c, r) for c, r in present_ci if r["route"] in ("capture", "review", "product")]
    print(f"\nCI core present in cards: {len(present_ci)}/{len(core)}; routed to capture/review/product: {len(good_ci)}")
    for c, r in present_ci:
        print(f"  {c['name']:28s} -> {r['route']}")


if __name__ == "__main__":
    main()
