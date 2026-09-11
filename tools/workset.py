#!/usr/bin/env python3
"""작업 집합 뷰 — 스코프 × 수준 창으로 거른 라벨 목록과 앵커 이웃을 예산 안에 담는다 (노트 0.5절, 5.6절, 11.3절).

작업 집합은 질의 결과이며 저장하지 않는다. 읽기 응답의 기본은 라벨 목록이고 본문은 앵커 이웃만 펼친다.
사용: workset.py --role developer [--levels logical,concrete] [--anchor <IRI|라벨 부분>] [--budget 200] --out workset.md <TTL...>
"""
import argparse
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
ID = Namespace("https://agentic-knowledge-base.dev/id/")
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
NEIGHBOUR = [AGT.refines, AGT.serves, AGT.satisfies, AGT.cites, AGT.supersedes, AGT.hasDirectPart]


def body_lines(path: str) -> list[str]:
    t = Path(path).read_text(encoding="utf-8").split("\n")
    end = t[1:].index("---") + 1
    b = "\n".join(t[end + 1:]).strip("\n")
    return b.split("\n") if b else []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True, help="카탈로그 역할 id 접미 (developer, orchestrator, vnv, inspection, hci)")
    ap.add_argument("--levels", default="", help="수준 창, 쉼표 구분. 비면 전부")
    ap.add_argument("--anchor", default="", help="펼칠 앵커 — 청크 IRI 또는 한글 라벨 부분 문자열")
    ap.add_argument("--hops", type=int, default=1)
    ap.add_argument("--budget", type=int, default=200, help="컨텍스트 예산(줄). 라벨 목록 + 펼친 본문")
    ap.add_argument("--root", default=".", help="assertionLocation 의 기준 디렉토리")
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    g = Graph()
    for f in a.files:
        g.parse(f, format="turtle")
    role = ID[f"role-{a.role}"]
    if (role, RDF.type, AGT.Role) not in g:
        raise SystemExit(f"workset: 카탈로그에 역할 {role} 이 없다")
    reads = set(g.objects(role, AGT.reads)); writes = set(g.objects(role, AGT.writes))
    scope = ID[f"scope-{a.role}"]
    conds = [g.qname(c) for c in g.objects(scope, AGT.includesCondition)]
    window = set(a.levels.split(",")) if a.levels else set(LEVELS)

    chunks = {}
    for c in g.subjects(AGT.lineCount, None):
        cls = next(g.objects(c, RDF.type)); lvl = str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1]
        st = str(next(g.objects(c, AGT.status), ""))
        if cls in reads | writes and lvl in window and st != "deprecated":
            ko = next((str(o) for o in g.objects(c, RDFS.label) if o.language == "ko"), "")
            chunks[c] = (str(cls).split("/")[-1].replace("Chunk", "").lower(), lvl, st, ko, "write" if cls in writes else "read",
                         str(next(g.objects(c, AGT.assertionLocation), "")))
    # 앵커와 이웃
    expanded, anchor = [], None
    if a.anchor:
        anchor = URIRef(a.anchor) if a.anchor.startswith("http") else next((c for c, v in chunks.items() if a.anchor in v[3]), None)
        if anchor is None:
            raise SystemExit(f"workset: 앵커 {a.anchor!r} 를 작업 집합 안에서 찾지 못했다")
        frontier, seen = {anchor}, {anchor}
        for _ in range(a.hops):
            nxt = set()
            for x in frontier:
                for p in NEIGHBOUR:
                    nxt |= set(g.objects(x, p)) | set(g.subjects(p, x))
            # 복합체 노드(청크 아님)는 통과해 부분까지 — 같은 복합체의 형제는 한 홉이다 (4.5절)
            for n in list(nxt):
                if n not in chunks:
                    nxt |= set(g.objects(n, AGT.hasDirectPart))
            nxt = {n for n in nxt if n in chunks and n not in seen}; seen |= nxt; frontier = nxt
        # 우선순위: 앵커 > 같은 복합체 부분 > refines 양방향 > 나머지 (LEDGER 3.2절과 같은 순서 원칙)
        comp = next(g.subjects(AGT.hasDirectPart, anchor), None)
        sib = set(g.objects(comp, AGT.hasDirectPart)) if comp else set()
        def rank(n): return 0 if n == anchor else 1 if n in sib else 2 if (n, AGT.refines, anchor) in g or (anchor, AGT.refines, n) in g else 3
        expanded = sorted(seen, key=rank)

    label_lines = [f"scope: {a.role}   conditions: {', '.join(conds) or '-'}   window: {','.join(l for l in LEVELS if l in window)}", ""]
    by_plane = defaultdict(list)
    for c, v in chunks.items(): by_plane[(v[4], v[0])].append((c, v))
    shown = set(expanded) if expanded else None  # 앵커가 있으면 이웃만 보이고 나머지는 접는다 (5.6절 "N more")
    for (rw, plane), items in sorted(by_plane.items()):
        vis = [t for t in items if shown is None or t[0] in shown]
        label_lines.append(f"{plane}/  ({rw})  {len(items)}" + (f"  ({len(vis)} shown, {len(items)-len(vis)} collapsed)" if shown is not None else ""))
        for c, v in sorted(vis, key=lambda t: (LEVELS.index(t[1][1]), t[1][3])):
            label_lines.append(f"  [{str(c).split('/')[-1][:8]}] {v[3]}  {v[1]}  {v[2]}")
        if shown is not None and len(items) > len(vis):
            label_lines.append(f"  … {len(items)-len(vis)} more (expand?)")
    body, used = [], len(label_lines)
    for n in expanded:
        lines = body_lines(str(Path(a.root) / chunks[n][5]))
        if used + len(lines) + 2 > a.budget:
            body.append(f"… {chunks[n][3]} (펼치지 않음 — 예산 {a.budget}줄 초과)"); continue
        body += ["", f"### {chunks[n][3]}  ({chunks[n][0]}/{chunks[n][1]})", f"<!-- iri: {n} -->"] + lines; used += len(lines) + 3
    head = [f"# workset — {a.role}: 라벨 {len(chunks)}개({len(label_lines)-2}줄), 펼침 {len([b for b in body if b.startswith('### ')])}개, 합계 {used}줄 / 예산 {a.budget}줄 → {'예산 안' if used <= a.budget else '예산 초과'}", ""]
    Path(a.out).write_text("\n".join(head + label_lines + body) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
