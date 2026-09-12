#!/usr/bin/env python3
"""작업 집합 뷰 — 스코프 × 수준 창으로 거른 라벨 목록과 앵커 이웃을 예산 안에 담는다 (노트 0.5절, 5.6절, 11.3절).

작업 집합은 질의 결과이며 저장하지 않는다. 읽기 응답의 기본은 라벨 목록이고 본문은 앵커 이웃만 펼친다.
이웃은 앵커에서 k홉 안의 청크(upstream ∪ downstream, 직접 트리플과 agt:Link 개체 둘 다)이며, 펼치는 순서는
링크 족의 우선순위다 — 앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo
(dependency-graph-design §4, p0-workset-anchor-neighbourhood). 예산을 넘는 이웃은 라벨만 남는다.
사용: workset.py --role developer [--levels logical,concrete] [--anchor <IRI|라벨 부분>] [--budget 200] --out workset.md <TTL...>
"""
import argparse
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
ID = Namespace("https://agentic-knowledge-base.dev/id/")
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
# 이웃 링크의 족 — 표의 순서가 곧 펼침 우선순위. supersedes 는 족 밖의 시간축이라 맨 뒤 (kb/ontology/related/trace)
FAMILIES = [
    ("refs", [AGT.cites, AGT.targets]),
    ("dep", [AGT.refines, AGT.serves, AGT.satisfies, AGT.constrains, AGT.verifies, AGT.usesConcept, AGT.derivesFrom, AGT.allocates]),
    ("part", [AGT.hasDirectPart]),
    ("rel", [AGT.coUpdatesWith, AGT.conflictsWith]),
    ("time", [AGT.supersedes]),
]
FAMILY_OF = {p: (i + 1, tag) for i, (tag, ps) in enumerate(FAMILIES) for p in ps}
PART = FAMILY_OF[AGT.hasDirectPart]


def body_lines(path: str) -> list[str]:
    t = Path(path).read_text(encoding="utf-8").split("\n")
    end = t[1:].index("---") + 1
    b = "\n".join(t[end + 1:]).strip("\n")
    return b.split("\n") if b else []


def neighbours(g: Graph, x):
    """x 의 이웃 (노드, 족 순위, 족 표시) — 양방향. 직접 트리플과 agt:Link 개체(linkFrom·linkTo·linkKind)를 모두 본다."""
    for p, fam in FAMILY_OF.items():
        for o in g.objects(x, p):
            yield o, fam
        for s in g.subjects(p, x):
            yield s, fam
    for link in g.subjects(AGT.linkFrom, x):
        fam = FAMILY_OF.get(next(g.objects(link, AGT.linkKind), None))
        if fam:
            for o in g.objects(link, AGT.linkTo):
                yield o, fam
    for link in g.subjects(AGT.linkTo, x):
        fam = FAMILY_OF.get(next(g.objects(link, AGT.linkKind), None))
        if fam:
            for s in g.objects(link, AGT.linkFrom):
                yield s, fam


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
    # 앵커와 이웃 — K홉 확장(upstream ∪ downstream), 스코프 필터(chunks 밖은 버림), 족별 우선순위, 예산 패킹 (§4 네 단계)
    expanded, anchor, fam = [], None, {}
    if a.anchor:
        anchor = URIRef(a.anchor) if a.anchor.startswith("http") else next((c for c, v in sorted(chunks.items(), key=lambda t: str(t[0])) if a.anchor in v[3]), None)
        if anchor is None:
            raise SystemExit(f"workset: 앵커 {a.anchor!r} 를 작업 집합 안에서 찾지 못했다")
        fam, hop, frontier = {anchor: (0, "anchor")}, {anchor: 0}, [anchor]
        for h in range(1, a.hops + 1):
            found = {}
            def take(n, f):
                if n in chunks and n not in fam and (n not in found or f[0] < found[n][0]):
                    found[n] = f
            for x in sorted(frontier, key=str):
                for n, f in neighbours(g, x):
                    if n in chunks:
                        take(n, f)
                    elif (n, AGT.hasDirectPart, None) in g:
                        # 복합체 노드(청크 아님)는 통과해 부분까지 — 같은 복합체의 형제는 한 홉이다 (4.5절)
                        for p in g.objects(n, AGT.hasDirectPart):
                            take(p, PART)
            fam.update(found); hop.update({n: h for n in found}); frontier = list(found)
        # 족 순서 ≫ 홉 ≫ 같은 족 안에서는 이전 순서(같은 복합체 부분 > refines 양방향 > 나머지) ≫ IRI — 결정적이다
        comp = next(g.subjects(AGT.hasDirectPart, anchor), None)
        sib = set(g.objects(comp, AGT.hasDirectPart)) if comp else set()
        def rank(n): return 0 if n == anchor else 1 if n in sib else 2 if (n, AGT.refines, anchor) in g or (anchor, AGT.refines, n) in g else 3
        expanded = sorted(fam, key=lambda n: (fam[n][0], hop[n], rank(n), str(n)))

    tag = lambda n: f"  [{fam[n][1]}]" if n in fam else ""
    label_lines = [f"scope: {a.role}   conditions: {', '.join(conds) or '-'}   window: {','.join(l for l in LEVELS if l in window)}"
                   + ("   order: anchor ≫ refs ≫ dep ≫ part ≫ rel ≫ time" if anchor else ""), ""]
    by_plane = defaultdict(list)
    for c, v in chunks.items(): by_plane[(v[4], v[0])].append((c, v))
    shown = set(expanded) if expanded else None  # 앵커가 있으면 이웃만 보이고 나머지는 접는다 (5.6절 "N more")
    for (rw, plane), items in sorted(by_plane.items()):
        vis = [t for t in items if shown is None or t[0] in shown]
        label_lines.append(f"{plane}/  ({rw})  {len(items)}" + (f"  ({len(vis)} shown, {len(items)-len(vis)} collapsed)" if shown is not None else ""))
        for c, v in sorted(vis, key=lambda t: (LEVELS.index(t[1][1]), t[1][3])):
            label_lines.append(f"  [{str(c).split('/')[-1][:8]}] {v[3]}  {v[1]}  {v[2]}{tag(c)}")
        if shown is not None and len(items) > len(vis):
            label_lines.append(f"  … {len(items)-len(vis)} more (expand?)")
    body, used = [], len(label_lines)
    for n in expanded:
        lines = body_lines(str(Path(a.root) / chunks[n][5]))
        if used + len(lines) + 2 > a.budget:
            body.append(f"… {chunks[n][3]}{tag(n)} (펼치지 않음 — 예산 {a.budget}줄 초과)"); continue
        body += ["", f"### {chunks[n][3]}  ({chunks[n][0]}/{chunks[n][1]}){tag(n)}", f"<!-- iri: {n} -->"] + lines; used += len(lines) + 3
    head = [f"# workset — {a.role}: 라벨 {len(chunks)}개({len(label_lines)-2}줄), 펼침 {len([b for b in body if b.startswith('### ')])}개, 합계 {used}줄 / 예산 {a.budget}줄 → {'예산 안' if used <= a.budget else '예산 초과'}", ""]
    Path(a.out).write_text("\n".join(head + label_lines + body) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
