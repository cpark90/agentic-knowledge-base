#!/usr/bin/env python3
"""골격 지표 투영 — 그래프에서 metrics.md를 생성한다 (노트 4.13절, 10.14절, 12.3절, 14.1절).

문서에 수치를 적으면 반드시 낡으므로(4.6절 투영 원칙) 지표는 이 생성물을 인용한다.
  청크 수(plane·level·status) · 고아율(구성체 부분도 링크도 없는 청크, 4.13절) · 크기 분포 ·
  링크 밀도 · 가정 · 트러스트(사람 검토) · CQ19 하강 완주율 · CQ20 상향 귀속률 · 도입 1단계 통과 조건.
사용: metrics.py --out metrics.md <TTL...>
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
LINKS = [AGT[p] for p in ("refines", "serves", "satisfies", "verifies", "cites", "targets", "assumes", "supersedes",
                          "derivesFrom", "constrains", "usesConcept", "allocates", "generates", "coUpdatesWith", "conflictsWith")]
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory"]
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    g = Graph()
    for f in a.files:
        g.parse(f, format="turtle")

    chunks = {s for s in g.subjects(AGT.lineCount, None)}
    plane = {c: str(next(g.objects(c, RDF.type))).split("/")[-1].replace("Chunk", "").lower() for c in chunks}
    level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in chunks}
    status = {c: str(next(g.objects(c, AGT.status), "")) for c in chunks}
    lines = {c: int(next(g.objects(c, AGT.lineCount))) for c in chunks}
    live = {c for c in chunks if status[c] != "deprecated"}

    linked = set()
    for p in LINKS:
        for s, o in g.subject_objects(p):
            linked.add(s); linked.add(o)
    parts = {o for o in g.objects(None, AGT.hasDirectPart)}
    orphans = {c for c in chunks if c not in linked and c not in parts}
    link_count = Counter(g.qname(p) for p in LINKS for _ in g.subject_objects(p))

    reqs = {c for c in live if plane[c] == "requirement"}
    # CQ19: 요구에서 refines 역방향으로 내려가 닿는 가장 낮은 level
    down = defaultdict(set)
    for s, o in g.subject_objects(AGT.refines):
        down[o].add(s)
    for s, o in g.subject_objects(AGT.serves):
        down[o].add(s)
    def deepest(r):
        seen, stack, best = set(), [r], -1
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in level and level[x] in LEVELS: best = max(best, LEVELS.index(level[x]))
            stack.extend(down.get(x, ()))
        return best
    reach = Counter(LEVELS[deepest(r)] if deepest(r) >= 0 else "none" for r in reqs)
    # CQ20: 요구가 아닌 살아 있는 청크 중 refines 연쇄로 요구에 닿는 비율 (구성체 부분은 대표 부분을 따라간다)
    up = defaultdict(set)
    for s, o in g.subject_objects(AGT.refines): up[s].add(o)
    for s, o in g.subject_objects(AGT.serves): up[s].add(o)
    comp_of = {}
    for comp, part in g.subject_objects(AGT.hasDirectPart): comp_of[part] = comp
    siblings = defaultdict(set)
    for part, comp in comp_of.items(): siblings[comp].add(part)
    def reaches_req(c):
        seen, stack = set(), [c]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in reqs: return True
            stack.extend(up.get(x, ()))
            if x in comp_of: stack.extend(siblings[comp_of[x]])
        return False
    nonreq = [c for c in live if plane[c] != "requirement"]
    ascribed = sum(1 for c in nonreq if reaches_req(c))

    human = sum(1 for c in chunks for v in g.objects(c, AGT.verifiedBy) if str(v).startswith("human:"))
    gen = Counter(str(next(g.objects(c, AGT.generatedBy), "")) for c in chunks)
    hist = Counter(min((lines[c] - 1) // 10, 4) for c in live)
    assumes = sum(1 for _ in g.subject_objects(AGT.assumes))

    def pct(n, d): return f"{100*n/d:.1f}%" if d else "—"
    o = ["# metrics — 골격 지표 (생성 파일, tools/metrics.py)", "",
         f"청크 {len(chunks)} (살아 있는 것 {len(live)}, deprecated {len(chunks)-len(live)}) · 구성체 {len(siblings)} · 트리플 {len(g)}", "",
         "## plane × level (살아 있는 청크)", "", "| plane | " + " | ".join(LEVELS) + " | 합 |", "|---|" + "---|" * (len(LEVELS) + 1)]
    for p in PLANES:
        row = [sum(1 for c in live if plane[c] == p and level[c] == l) for l in LEVELS]
        o.append(f"| `{p}` | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    o += ["", "## 고아율 (4.13절 — 구성체 부분도 링크도 없는 청크)", "",
          f"- 전체: {len(orphans)}/{len(chunks)} = **{pct(len(orphans), len(chunks))}**",
          f"- 살아 있는 청크: {len(orphans & live)}/{len(live)} = **{pct(len(orphans & live), len(live))}** — 도입 1단계 통과 조건 < 10%: **{'통과' if len(live) and len(orphans & live)/len(live) < 0.10 else '미통과'}**"]
    for p in PLANES:
        n = sum(1 for c in live if plane[c] == p)
        if n: o.append(f"  - `{p}`: {sum(1 for c in orphans & live if plane[c] == p)}/{n}")
    o += ["", "## 링크 밀도", "", f"- 링크 {sum(link_count.values())} / 살아 있는 청크 {len(live)} = **{sum(link_count.values())/max(len(live),1):.2f}**/청크",
          "- 타입별: " + " · ".join(f"`{k}` {v}" for k, v in link_count.most_common()),
          f"- 링크 개체(`agt:Link`): {sum(1 for _ in g.subjects(RDF.type, AGT.Link))} · 증거 항목: {sum(1 for _ in g.subjects(RDF.type, AGT.Evidence))}",
          "", "## 크기 분포 (본문 줄 수, 살아 있는 청크)", "",
          "| 1–10 | 11–20 | 21–30 | 31–40 | 41–42 |", "|---|---|---|---|---|",
          "| " + " | ".join(str(hist[i]) for i in range(5)) + " |",
          f"- 41–42줄 비율 {pct(hist[4], len(live))} — 42줄 근처에 몰리면 억지 분할 의심 (4.13절)",
          "", "## 하강 완주 (CQ19) · 상향 귀속 (CQ20)", "",
          f"- 요구 {len(reqs)}건이 `refines`/`serves` 연쇄로 닿는 가장 낮은 수준: " + " · ".join(f"{k} {v}" for k, v in reach.most_common()),
          f"- executable까지 닿은 요구: {reach.get('executable', 0)}/{len(reqs)} = **{pct(reach.get('executable', 0), len(reqs))}** (하강 완주율, 목표 100%)",
          f"- 요구로 거슬러 오르는 비요구 청크: {ascribed}/{len(nonreq)} = **{pct(ascribed, len(nonreq))}** (상향 귀속률, 목표 100%)",
          "", "## 가정 · 트러스트", "",
          f"- `assumes` 링크 {assumes} · 가정 개체 {sum(1 for _ in g.subjects(RDF.type, AGT.Assumption))}",
          f"- 생성자: " + " · ".join(f"`{k}` {v}" for k, v in gen.most_common()) + f" · **사람 검토(`human:`) {human}건**",
          ""]
    Path(a.out).write_text("\n".join(o), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
