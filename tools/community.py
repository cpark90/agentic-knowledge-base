#!/usr/bin/env python3
"""커뮤니티 탐지 뷰 — 링크 구조의 군집을 복합체 후보와 relatedTo 링크 후보로 보고한다
(p4-community-detection-proposes-composites, dependency-graph-design §7 (h)).

게이트가 아니라 **후보 생성기**다: 채택(복합체 선언)·묶기(relatedTo 링크)·기각은 사람이 후보마다 판정하고,
결과는 저장하지 않는다 (4.6절 뷰 원칙). 판정란은 비워 둔다.

  입력  살아 있는 청크(status ≠ deprecated)와 링크 — refines·serves·cites·usesConcept·coUpdatesWith·conflictsWith
        (직접 트리플과 agt:Link 개체 둘 다) + 구성 관계 hasDirectPart. supersedes 는 시간축이라 제외한다.
  계산  결정론적 Louvain (외부 의존 없음). 노드·이웃·군집 순회를 IRI 정렬로 고정하고 동점은 작은 IRI 가 이기므로
        같은 입력이면 같은 출력이다. 이미 선언된 복합체의 부분은 처음부터 한 단위로 묶어 계산이 선언을 쪼개지 않는다
        — 복합체는 선언이고 커뮤니티는 계산이다 (근거 청크). 복합체의 수준은 결론의 수준이다 (defs/kb.bzl ChunkInfo).
  판정  같은 plane·level 안의 군집(청크 2~9, 아직 복합체가 아닌 것)만 복합체 후보,
        plane 또는 level 을 넘는 군집은 relatedTo 링크 후보 — 쌍이 아니라 군집 단위.

사용: community.py --out communities.md <TTL...>   (bazel build //kg:communities)
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
# 군집 계산에 쓰는 링크 종류 (족: references · semanticallyDependsOn · relatedTo). 시간축 supersedes 는 뺀다
EDGE_KINDS = [AGT.refines, AGT.serves, AGT.cites, AGT.usesConcept, AGT.coUpdatesWith, AGT.conflictsWith]
MAX_PARTS = 9  # 복합체 부분 상한 (7±2, composite-kg 배너)


def label_ko(g: Graph, s) -> str:
    return next((str(o) for o in g.objects(s, RDFS.label) if o.language == "ko"), str(s).split("/")[-1])


def short(iri) -> str:
    return str(iri).split("/")[-1][:8]


def louvain(nodes: list, adj: dict) -> dict:
    """결정론적 Louvain — 노드는 IRI 정렬 순으로, 이웃 군집도 정렬 순으로 보고 이득이 양수일 때만 옮긴다.

    adj[u][v] 는 대칭 가중치, adj[u][u] 는 자기 고리(집약 단계에서 생긴다). 반환은 원래 노드 → 군집 id (군집 id 는 그 안의 최소 IRI 문자열).
    """
    member_of = {u: u for u in nodes}   # 원래 노드 → 현재 층의 노드
    cur_nodes, cur_adj = list(nodes), {u: dict(vs) for u, vs in adj.items()}
    for _ in range(50):
        comm, moved = _one_level(cur_nodes, cur_adj)
        member_of = {u: comm[c] for u, c in member_of.items()}
        if not moved:
            break
        cur_nodes, cur_adj = _aggregate(cur_nodes, cur_adj, comm)
    return member_of


def _one_level(nodes: list, adj: dict) -> tuple:
    deg = {u: sum(w for v, w in adj.get(u, {}).items() if v != u) + 2 * adj.get(u, {}).get(u, 0) for u in nodes}
    m = sum(deg.values()) / 2
    comm = {u: u for u in nodes}
    tot = dict(deg)
    moved_any = False
    if m == 0:
        return comm, False
    for _ in range(100):
        moved = False
        for u in nodes:
            nbr = defaultdict(float)
            for v, w in adj.get(u, {}).items():
                if v != u:
                    nbr[comm[v]] += w
            cu = comm[u]
            tot[cu] -= deg[u]
            remove_cost = -nbr.get(cu, 0) / m + tot[cu] * deg[u] / (2 * m * m)
            best, best_gain = cu, 0.0
            for c in sorted(nbr, key=str):
                gain = remove_cost + nbr[c] / m - tot[c] * deg[u] / (2 * m * m)
                if gain > best_gain + 1e-12:
                    best, best_gain = c, gain
            tot[best] += deg[u]
            if best != cu:
                comm[u] = best
                moved = moved_any = True
        if not moved:
            break
    # 군집 id 를 그 안의 최소 노드로 정규화 — 층을 거듭해도 이름이 결정적이다
    rep = {}
    for u in nodes:
        c = comm[u]
        rep[c] = min(rep.get(c, u), u, key=str)
    return {u: rep[comm[u]] for u in nodes}, moved_any


def _aggregate(nodes: list, adj: dict, comm: dict) -> tuple:
    new_adj = defaultdict(lambda: defaultdict(float))
    for u in nodes:
        cu = comm[u]
        for v, w in adj.get(u, {}).items():
            cv = comm[v]
            if u == v:
                new_adj[cu][cu] += w
            elif str(u) < str(v):
                if cu == cv:
                    new_adj[cu][cu] += w
                else:
                    new_adj[cu][cv] += w
                    new_adj[cv][cu] += w
    new_nodes = sorted({comm[u] for u in nodes}, key=str)
    return new_nodes, {u: dict(new_adj[u]) for u in new_nodes}


def modularity(nodes: list, adj: dict, part: dict) -> float:
    deg = {u: sum(w for v, w in adj.get(u, {}).items() if v != u) + 2 * adj.get(u, {}).get(u, 0) for u in nodes}
    m = sum(deg.values()) / 2
    if m == 0:
        return 0.0
    q = 0.0
    for u in nodes:
        for v, w in adj.get(u, {}).items():
            if part[u] == part[v]:
                q += w - deg[u] * deg[v] / (2 * m)
    return q / (2 * m)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    g = Graph()
    for f in a.files:
        g.parse(f, format="turtle")

    # 살아 있는 청크
    chunks = {}
    for c in g.subjects(AGT.lineCount, None):
        if str(next(g.objects(c, AGT.status), "")) == "deprecated":
            continue
        plane = str(next(g.objects(c, RDF.type), "")).split("/")[-1].replace("Chunk", "").lower()
        level = str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1]
        chunks[c] = {"plane": plane, "level": level, "ko": label_ko(g, c), "loc": str(next(g.objects(c, AGT.assertionLocation), ""))}

    # 선언된 복합체 → 단위 노드. 부분은 살아 있는 청크만, 한 청크가 둘에 속하면 IRI 가 작은 복합체
    unit_of = {}
    units = {}  # 단위 → {"parts": [...], "ko", "plane", "level", "composite": bool}
    for comp in sorted(g.subjects(RDF.type, AGT.Composite), key=str):
        parts = sorted((p for p in g.objects(comp, AGT.hasDirectPart) if p in chunks and p not in unit_of), key=str)
        if not parts:
            continue
        for p in parts:
            unit_of[p] = comp
        lvl = str(next(g.objects(comp, AGT.hasLevel), "")).split("/")[-1]
        if not lvl:  # 결론의 수준 (kb.bzl ChunkInfo) — 없으면 부분들의 수준이 하나일 때 그것
            concl = [p for p in parts if chunks[p]["loc"].endswith("conclusion.md")]
            lvls = {chunks[p]["level"] for p in parts}
            lvl = chunks[concl[0]]["level"] if concl else (lvls.pop() if len(lvls) == 1 else "mixed")
        planes = {chunks[p]["plane"] for p in parts}
        units[comp] = {"parts": parts, "ko": label_ko(g, comp), "plane": planes.pop() if len(planes) == 1 else "mixed", "level": lvl, "composite": True}
    for c in sorted(chunks, key=str):
        if c not in unit_of:
            unit_of[c] = c
            units[c] = {"parts": [c], "ko": chunks[c]["ko"], "plane": chunks[c]["plane"], "level": chunks[c]["level"], "composite": False}

    # 링크 → 단위 사이의 가중 무향 엣지. 직접 트리플과 agt:Link 개체를 합치고 (출발, 종류, 도착) 으로 중복을 없앤다
    triples = set()
    for p in EDGE_KINDS:
        for s, o in g.subject_objects(p):
            if s in chunks and o in chunks:
                triples.add((s, p, o))
    for link in g.subjects(AGT.linkKind, None):
        s, o, p = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None), next(g.objects(link, AGT.linkKind), None)
        if p in EDGE_KINDS and s in chunks and o in chunks:
            triples.add((s, p, o))
    kind_count = Counter(str(p).split("/")[-1] for _, p, _ in triples)
    adj = defaultdict(lambda: defaultdict(float))
    for s, p, o in triples:
        u, v = unit_of[s], unit_of[o]
        if u != v:
            adj[u][v] += 1
            adj[v][u] += 1
    nodes = sorted(units, key=str)
    adj = {u: dict(adj.get(u, {})) for u in nodes}

    part = louvain(nodes, adj)
    q = modularity(nodes, adj, part)
    clusters = defaultdict(list)
    for u in nodes:
        clusters[part[u]].append(u)
    clusters = [sorted(v, key=str) for _, v in sorted(clusters.items(), key=lambda kv: str(kv[0]))]

    # 판정 갈래
    def size(cl):
        return sum(len(units[u]["parts"]) for u in cl)

    dist = Counter("1" if size(cl) == 1 else "2–9" if size(cl) <= MAX_PARTS else "10+" for cl in clusters)
    composite_cands, related_cands, already, oversize = [], [], [], []
    for cl in clusters:
        if len(cl) == 1:
            if units[cl[0]]["composite"]:
                already.append(cl)
            continue
        homogeneous = len({(units[u]["plane"], units[u]["level"]) for u in cl}) == 1
        if not homogeneous:
            related_cands.append(cl)
        elif size(cl) <= MAX_PARTS:
            composite_cands.append(cl)
        else:
            oversize.append(cl)
    composite_cands.sort(key=lambda cl: (size(cl), str(cl[0])))
    related_cands.sort(key=lambda cl: (size(cl), str(cl[0])))
    oversize.sort(key=lambda cl: (size(cl), str(cl[0])))

    def member(u):
        it = units[u]
        return f"복합체 ⟨{it['ko']}⟩ ({len(it['parts'])})" if it["composite"] else f"[{short(u)}] {it['ko']}"

    def membership(cl):
        comps = [units[u]["ko"] for u in cl if units[u]["composite"]]
        return "현재 어느 복합체에도 없음" if not comps else "일부는 복합체 " + " · ".join(f"⟨{k}⟩" for k in comps) + " 소속"

    def dist_of(cl):
        c = Counter(f"{units[u]['plane']}/{units[u]['level']}" for u in cl)
        return " · ".join(f"{k} {v}" for k, v in sorted(c.items()))

    n_comp = sum(1 for u in units.values() if u["composite"])
    lines = ["# communities — 커뮤니티 탐지 뷰 (생성물, 저장하지 않는다)", "",
             f"살아 있는 청크 {len(chunks)} · 단위 노드 {len(units)} (선언된 복합체 {n_comp} + 단독 청크 {len(units) - n_comp}) · "
             f"링크 {len(triples)} ({' · '.join(f'{k} {v}' for k, v in sorted(kind_count.items())) or '없음'}) · 모듈러리티 Q = {q:.3f}", "",
             "방법: 결정론적 Louvain (IRI 정렬, 동점은 작은 IRI). 선언된 복합체의 부분은 한 단위로 묶고 시작하며 복합체의 수준은 결론의 수준이다. "
             "supersedes 는 시간축이라 제외. 판정(병합 / 묶기 / 유지)은 사람이 후보마다 한다 — 채택은 `kg/composite-kg.ttl` 복합체 선언, 기각은 관측 한 줄.", "",
             "## 요약", "", "| 항목 | 값 |", "|---|---|",
             f"| 군집 수 | {len(clusters)} |",
             f"| 크기 분포 (청크 수) | 1: {dist.get('1', 0)} · 2–9: {dist.get('2–9', 0)} · 10+: {dist.get('10+', 0)} |",
             f"| 복합체 후보 (같은 plane·level, 2~{MAX_PARTS}, 아직 복합체 아님) | {len(composite_cands)} |",
             f"| relatedTo 링크 후보 (plane 또는 level 을 넘음) | {len(related_cands)} |",
             f"| 선언된 복합체와 일치하는 군집 (후보 아님) | {len(already)} |",
             f"| 같은 plane·level 이지만 {MAX_PARTS} 초과 (분할 뒤 재검토) | {len(oversize)} |", "",
             "## 복합체 후보", "",
             "| # | 크기 | plane/level | 부분 (라벨) | 현재 소속 | 판정 (병합 / 묶기 / 유지) |", "|---|---|---|---|---|---|"]
    for i, cl in enumerate(composite_cands, 1):
        u0 = units[cl[0]]
        lines.append(f"| {i} | {size(cl)} | {u0['plane']}/{u0['level']} | {'<br>'.join(member(u) for u in cl)} | {membership(cl)} |  |")
    if not composite_cands:
        lines.append("| — | | | 후보 없음 | | |")
    lines += ["", "## relatedTo 링크 후보", "",
              "| # | 크기 | plane·level 분포 | 구성 (라벨) | 판정 (묶기 / 유지) |", "|---|---|---|---|---|"]
    for i, cl in enumerate(related_cands, 1):
        lines.append(f"| {i} | {size(cl)} | {dist_of(cl)} | {'<br>'.join(member(u) for u in cl)} |  |")
    if not related_cands:
        lines.append("| — | | | 후보 없음 | |")
    if oversize:
        lines += ["", f"## 같은 plane·level 이지만 {MAX_PARTS} 초과", ""]
        for cl in oversize:
            lines.append(f"- 크기 {size(cl)} ({dist_of(cl)}): " + " · ".join(member(u) for u in cl))
    Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
