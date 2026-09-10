#!/usr/bin/env python3
"""코어 지표 뷰 — 그래프에서 metrics.md를 생성한다 (노트 4.13절, 10.14절, 12.3절, 14.1절).

문서에 수치를 적으면 반드시 낡으므로(4.6절 뷰 원칙) 지표는 이 생성물을 인용한다.
  청크 수(plane·level·status) · 고아율(복합체 부분도 링크도 없는 청크, 4.13절) · 크기 분포 ·
  링크 밀도 · 가정 · 신뢰 등급(사람 검토) · CQ19 전방 추적 커버리지 · CQ20 후방 추적 커버리지 · 도입 1단계 통과 조건.
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
    # CQ20: 요구가 아닌 살아 있는 청크 중 refines 연쇄로 요구에 닿는 비율 (복합체 부분은 대표 부분을 따라간다)
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

    # 세 축 대리 (14.1 정정본, p14-stage-pass-conditions): 연결 성분 · 매트릭스 채움률 · level 건너뜀 · 수준 허용표 위반
    parent = {c: c for c in live}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a_, b_):
        if a_ in parent and b_ in parent: parent[find(a_)] = find(b_)
    for p_ in LINKS + [AGT.hasDirectPart]:
        for s_, o_ in g.subject_objects(p_): union(s_, o_)
    for part_, comp_ in comp_of.items():
        for sib in siblings[comp_]: union(part_, sib)
    components = len({find(c) for c in live})
    skips = [(s_, o_) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level and level[s_] in LEVELS and level[o_] in LEVELS
             and LEVELS.index(level[s_]) - LEVELS.index(level[o_]) != 1]
    lvl_pairs = {(level[o_], level[s_]) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level}
    adjacent = [(LEVELS[i], LEVELS[i + 1]) for i in range(4)]
    filled = [p_ for p_ in adjacent if p_ in lvl_pairs]
    RESIDENCY = {"requirement": {"functional"}, "decision": {"abstract", "logical", "concrete"}, "contract": {"abstract", "logical"},
                 "schema": {"logical", "concrete"}, "artifact": {"concrete", "executable"}, "memory": {"concrete"}}
    residency_bad = [c for c in live if plane[c] in RESIDENCY and level[c] not in RESIDENCY[plane[c]]]

    def pct(n, d): return f"{100*n/d:.1f}%" if d else "—"
    o = ["# metrics — 코어 지표 (생성 파일, tools/metrics.py)", "",
         f"청크 {len(chunks)} (살아 있는 것 {len(live)}, deprecated {len(chunks)-len(live)}) · 복합체 {len(siblings)} · 트리플 {len(g)}", "",
         "## plane × level (살아 있는 청크)", "", "| plane | " + " | ".join(LEVELS) + " | 합 |", "|---|" + "---|" * (len(LEVELS) + 1)]
    for p in PLANES:
        row = [sum(1 for c in live if plane[c] == p and level[c] == l) for l in LEVELS]
        o.append(f"| `{p}` | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    o += ["", "## 고아율 (4.13절 — 복합체 부분도 링크도 없는 청크)", "",
          f"- 전체: {len(orphans)}/{len(chunks)} = **{pct(len(orphans), len(chunks))}**",
          f"- 살아 있는 청크: {len(orphans & live)}/{len(live)} = **{pct(len(orphans & live), len(live))}** — 도입 1단계 통과 조건 < 10%: **{'통과' if len(live) and len(orphans & live)/len(live) < 0.10 else '미통과'}**"]
    for p in PLANES:
        n = sum(1 for c in live if plane[c] == p)
        if n: o.append(f"  - `{p}`: {sum(1 for c in orphans & live if plane[c] == p)}/{n}")
    o += ["", "## 세 축 대리 — 1·3·5단계 (14.1 정정본: 의미 보존 · 구체화 · 유기적 연결)", "",
          f"- 연결: 살아 있는 청크의 연결 성분 **{components}**개 (링크·복합체로 이어진 덩어리. 목표 1)",
          f"- 연결: level×level `refines` 매트릭스 채움 {len(filled)}/4 — " + (", ".join(f"{a_}→{b_}" for a_, b_ in filled) or "없음") + " (목표 4/4)",
          f"- 구체화: level을 한 단계씩 내려가지 않는 `refines` **{len(skips)}**건 (목표 0; 지금은 concrete→functional 직행이 구조적으로 허용됨 — abstract·logical 결정이 생기면 0이어야 한다)",
          f"- 구체화: 수준 허용표 위반 **{len(residency_bad)}**건 (목표 0)",
          "- 의미 보존: 확정 문장 커버리지·라벨 대표성은 이 도구 밖 — 감사 §3과 실험",
          "", "## 링크 밀도", "", f"- 링크 {sum(link_count.values())} / 살아 있는 청크 {len(live)} = **{sum(link_count.values())/max(len(live),1):.2f}**/청크",
          "- 타입별: " + " · ".join(f"`{k}` {v}" for k, v in link_count.most_common()),
          f"- 링크 개체(`agt:Link`): {sum(1 for _ in g.subjects(RDF.type, AGT.Link))} · 증거 항목: {sum(1 for _ in g.subjects(RDF.type, AGT.Evidence))}",
          "", "## 크기 분포 (본문 줄 수, 살아 있는 청크)", "",
          "| 1–10 | 11–20 | 21–30 | 31–40 | 41–42 |", "|---|---|---|---|---|",
          "| " + " | ".join(str(hist[i]) for i in range(5)) + " |",
          f"- 41–42줄 비율 {pct(hist[4], len(live))} — 42줄 근처에 몰리면 억지 분할 의심 (4.13절)",
          "", "## 정제 완주 (CQ19) · 후방 추적 귀속 (CQ20)", "",
          f"- 요구 {len(reqs)}건이 `refines`/`serves` 연쇄로 닿는 가장 낮은 수준: " + " · ".join(f"{k} {v}" for k, v in reach.most_common()),
          f"- executable까지 닿은 요구: {reach.get('executable', 0)}/{len(reqs)} = **{pct(reach.get('executable', 0), len(reqs))}** (전방 추적 커버리지, 목표 100%)",
          f"- 요구로 거슬러 오르는 비요구 청크: {ascribed}/{len(nonreq)} = **{pct(ascribed, len(nonreq))}** (후방 추적 커버리지, 목표 100%)",
          "", "## 가정 · 신뢰 등급", "",
          f"- `assumes` 링크 {assumes} · 가정 개체 {sum(1 for _ in g.subjects(RDF.type, AGT.Assumption))}",
          f"- 생성자: " + " · ".join(f"`{k}` {v}" for k, v in gen.most_common()) + f" · **사람 검토(`human:`) {human}건**",
          ""]
    Path(a.out).write_text("\n".join(o), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
