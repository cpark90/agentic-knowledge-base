---
id: https://agentic-knowledge-base.dev/id/chunk/7f478037-6677-43f4-8b6e-5c7795f7f571
type: artifact
level: executable
title_ko: 함수 main (tools/workset.py)
title: function main in tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/efdb6344-03eb-4727-97ba-fe8aadcc7424
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True, help="카탈로그 역할 id 접미 (developer, orchestrator, vnv, hci)")
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

    tag = lambda n: f"  [{fam[n][1]}]" if n in fam else ""  # noqa: E731
    label_lines = [f"scope: {a.role}   conditions: {', '.join(conds) or kb_lib.NONE_MARK}   window: {','.join(l for l in LEVELS if l in window)}"
                   + ("   order: anchor ≫ refs ≫ dep ≫ part ≫ rel ≫ time" if anchor else ""), ""]
    by_plane = defaultdict(list)
    for c, v in chunks.items():
        by_plane[(v[4], v[0])].append((c, v))
    shown = set(expanded) if expanded else None  # 앵커가 있으면 이웃만 보이고 나머지는 접는다 (5.6절 "N more")
    for (rw, plane), items in sorted(by_plane.items()):
        vis = [t for t in items if shown is None or t[0] in shown]
        label_lines.append(f"{plane}/  ({rw})  {len(items)}" + (f"  ({len(vis)} shown, {len(items)-len(vis)} collapsed)" if shown is not None else ""))
        for c, v in sorted(vis, key=lambda t: (LEVELS.index(t[1][1]), t[1][3])):
            label_lines.append(f"  [{str(c).split('/')[-1][:8]}] {v[3]}  {v[1]}  {v[2]}{tag(c)}")
        if shown is not None and len(items) > len(vis):
            label_lines.append(f"  … {len(items)-len(vis)} more (expand?)")
    body, used, read_paths = [], len(label_lines), []
    for n in expanded:
        src = str(Path(a.root) / chunks[n][5])
        read_paths.append(src)
        lines_ = body_lines(src)
        if used + len(lines_) + ENTRY_OVERHEAD > a.budget:
            body.append(f"… {chunks[n][3]}{tag(n)} (펼치지 않음 — 예산 {a.budget}줄 초과)")
            continue
        # 청크 본문을 그대로 옮긴 자리다 — 원본이 자기 게이트를 통과했으므로 서식 규칙은 이 구역을 판정하지 않는다
        body += ["", f"### {chunks[n][3]}  ({chunks[n][0]}/{chunks[n][1]}){tag(n)}", f"<!-- iri: {n} -->"] \
            + kb_lib.gendoc_quote("\n".join(lines_))
        used += len(lines_) + ENTRY_OVERHEAD
    verdict = "예산 안" if used <= a.budget else "예산 초과"
    inputs = list(a.files) + sorted(set(read_paths))
    head = kb_lib.gendoc_header(
        f"workset-{a.role}", f"{a.role} 역할의 작업 집합 뷰", "tools/workset.py",
        f"카탈로그 역할 `id:role-{a.role}` 이 읽고 쓰는 plane 과 수준 창 `{','.join(l for l in LEVELS if l in window)}` 으로 살아 있는 청크를 거른 라벨 목록, "
        + (f"앵커 `{a.anchor}` 에서 {a.hops}홉 이웃의 본문을 족 우선순위(anchor ≫ refs ≫ dep ≫ part ≫ rel ≫ time)로 펼쳐 예산 안에 담는다"
           if anchor else "앵커를 주지 않았으므로 본문은 펼치지 않는다 — 앵커는 `--//kb:anchor` 로 준다"),
        f"bazel build //kg:workset --//kb:role={a.role}", inputs,
        f"라벨 {len(chunks)}개 · 펼침 {len([b for b in body if b.startswith('### ')])}개",
        kb_lib.gendoc_view_notice("청크의 frontmatter 와 본문"), input_kind="입력 파일",
        extra=[f"- 예산 판정: 이 문서 전체(라벨 목록 {len(label_lines)-2}줄 + 펼친 본문)의 합계 **{used}줄 / 예산 {a.budget}줄 → {verdict}**",
               f"- 정의: 여기의 예산 판정은 **문서 전체**를 잰다. `bazel build //kg:metrics` 의 역할별 예산 준수율은 "
               f"**앵커마다** 1홉 이웃을 펼친 줄 수를 재므로 두 수치는 같은 이름이되 다른 것을 센다"])
    # 라벨은 청크에서 그대로 옮긴 값이다 — 서식 규칙은 이 구역을 판정하지 않는다
    out = ["## 라벨 목록", "", kb_lib.GENDOC_QUOTE_OPEN] + label_lines + [kb_lib.GENDOC_QUOTE_CLOSE, "", "## 펼친 본문", ""] \
        + (body or [f"{kb_lib.NONE_MARK} — 앵커가 없어 본문을 펼치지 않았다", ""])
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, out, inputs), encoding="utf-8")
    if anchor is not None and used > a.budget:
        print(f"FAIL [{kb_lib.WORKSET_BUDGET_GATE}] 앵커 {a.anchor!r}: 문서 전체 {used}줄 > 예산 {a.budget}줄 "
              f"— 앵커 없는 뷰는 판정 밖이다", file=sys.stderr)
        return kb_lib.EXIT_FAIL
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
