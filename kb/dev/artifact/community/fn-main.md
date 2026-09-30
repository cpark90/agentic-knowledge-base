---
id: https://agentic-knowledge-base.dev/id/chunk/dd9af6e3-0248-4ddf-893c-a10669c406cc
type: artifact
level: executable
title_ko: 함수 main (tools/community.py)
title: function main in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/09eb4947-176f-41ad-92ee-7632b5240022
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
    head = kb_lib.gendoc_header(
        "communities", "커뮤니티 탐지 뷰", "tools/community.py",
        "살아 있는 청크와 그 링크(`refines`·`serves`·`cites`·`usesConcept`·`coUpdatesWith`·`conflictsWith` + 구성 관계)에 "
        "결정론적 Louvain 을 돌려 — 같은 plane·level 안의 군집은 복합체 후보, plane·level 을 넘는 군집은 relatedTo 링크 후보. "
        "후보 생성기이고 판정(병합 / 묶기 / 유지)은 사람이 후보마다 한다",
        "bazel build //kg:communities", a.files,
        f"링크 {len(triples)} · 단위 노드 {len(units)}", kb_lib.gendoc_view_notice("청크의 frontmatter 와 `kg/composite-kg.ttl`"),
        input_kind="그래프 파일",
        extra=[f"- 살아 있는 청크 {len(chunks)} · 단위 노드 {len(units)} (선언된 복합체 {n_comp} + 단독 청크 {len(units) - n_comp}) · "
               f"링크 {len(triples)} ({' · '.join(f'{k} {v}' for k, v in sorted(kind_count.items())) or kb_lib.NONE_MARK}) · "
               f"모듈러리티 Q = {kb_lib.num(q)}",
               "- 방법: 결정론적 Louvain (IRI 정렬, 동점은 작은 IRI). 선언된 복합체의 부분은 한 단위로 묶고 시작하며 복합체의 수준은 결론의 수준이다. "
               "supersedes 는 시간축이라 제외. 채택은 `kg/composite-kg.ttl` 복합체 선언, 기각은 관측 한 줄"])
    lines = ["## 요약", "", "| 항목 | 값 |", "|---|---|",
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
        lines.append(f"| {i} | {size(cl)} | {u0['plane']}/{u0['level']} | {'<br>'.join(member(u) for u in cl)} | {membership(cl)} | {kb_lib.NONE_MARK} |")
    if not composite_cands:
        lines.append(f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 후보 {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} |")
    lines += ["", "## relatedTo 링크 후보", "",
              "| # | 크기 | plane·level 분포 | 구성 (라벨) | 판정 (묶기 / 유지) |", "|---|---|---|---|---|"]
    for i, cl in enumerate(related_cands, 1):
        lines.append(f"| {i} | {size(cl)} | {dist_of(cl)} | {'<br>'.join(member(u) for u in cl)} | {kb_lib.NONE_MARK} |")
    if not related_cands:
        lines.append(f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 후보 {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} |")
    lines += ["", f"## 같은 plane·level 이지만 {MAX_PARTS} 초과", ""]
    if oversize:
        for cl in oversize:
            lines.append(f"- 크기 {size(cl)} ({dist_of(cl)}): " + " · ".join(member(u) for u in cl))
    else:
        lines.append(f"- {kb_lib.NONE_MARK}")
    lines.append("")
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.files, input_kind="그래프 파일"), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
