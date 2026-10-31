---
id: https://agentic-knowledge-base.dev/id/chunk/884c28fc-a47e-4e4b-ac96-a98f560a3d07
type: artifact
level: executable
title_ko: 함수 gather (tools/link.py)
title: function gather in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/12124054-d49f-44e2-be10-6fbdb102b578, https://agentic-knowledge-base.dev/id/chunk/67eb756b-e7f0-4da2-af55-90f4bc3058e9, https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `gather(u, min_shared, coedit_paths)` 다. 증거 수집 → (쌍 → 증거 목록 [(강도, 종류, 값, 정렬용 공유 수)], 쌍 → 인용 방향, 탈락 분포, 쌍 → 승계 종류).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gather(u: Units, min_shared: int, coedit_paths=()):
    """증거 수집 → (쌍 → 증거 목록 [(강도, 종류, 값, 정렬용 공유 수)], 쌍 → 인용 방향, 탈락 분포, 쌍 → 승계 종류)."""
    g = u.g
    dropped: Counter = Counter()
    evidence: dict = defaultdict(list)
    prefer: dict = {}
    hint: dict = {}

    def pair(s, o, kind: str, value: str, shared: int, directed: bool):
        us, uo = u.unit_of.get(s), u.unit_of.get(o)
        if us is None or uo is None:
            return
        if not (u.alive(us) and u.alive(uo)):
            dropped[R_DEPRECATED] += 1
            return
        if us == uo:
            dropped[R_SELF] += 1
            return
        if u.sibling(us, uo):
            dropped[R_SIBLING] += 1
            return
        key = frozenset((us, uo))
        evidence[key].append((EVIDENCE_RANK[kind], kind, value, shared))
        if directed:
            prefer.setdefault(key, (us, uo))

    # (a) 본문 식별자 — extract_refs 의 agt:cites (인용한 쪽이 앵커 후보)
    for s, o in sorted(g.subject_objects(AGT.cites), key=lambda so: (str(so[0]), str(so[1]))):
        pair(s, o, "constructionRecord", u.stem(o), 0, True)
    # (b) 테스트 공동 커버 — verifies W→A 의 근거 (단일 정의 위치 kb_lib.co_cover). 원 링크 종류처럼 verifies 를 힌트로 준다
    refines, verifies = defaultdict(list), defaultdict(list)
    for p, m in ((AGT.refines, refines), (AGT.verifies, verifies)):
        for s, o in g.subject_objects(p):
            m[s].append(o)
    in_dir = lambda c, d: u.loc.get(c, "").startswith(f"{kb_lib.KB_VV}/{d}/")  # noqa: E731
    cover = kb_lib.co_cover(refines, verifies, [c for c in u.live if in_dir(c, "case")], [c for c in u.live if in_dir(c, "verifier")],
                            [c for c in u.live if u.kb(c) == kb_lib.KB_DEV])
    for (w, x), cases in sorted(cover.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
        before = len(evidence.get(frozenset((u.unit_of.get(w), u.unit_of.get(x))), []))
        pair(w, x, "testCoverage", " · ".join(u.stem(c) for c in sorted(cases, key=str)), 0, True)
        key = frozenset((u.unit_of.get(w), u.unit_of.get(x)))
        if len(evidence.get(key, [])) > before:
            hint.setdefault(key, "verifies")
    # (c) 개념 공유 — 단위별 agt:usesConcept 합집합의 교집합
    concepts = defaultdict(set)
    for s, o in g.subject_objects(AGT.usesConcept):
        if s in u.live:
            concepts[u.unit_of[s]].add(str(o).split("/")[-1])
    units = sorted(concepts, key=str)
    for i, a in enumerate(units):
        for b in units[i + 1:]:
            shared = sorted(concepts[a] & concepts[b])
            if len(shared) >= min_shared:
                pair(a, b, "proposal", f"{len(shared)} ({', '.join('agt:' + t for t in shared[:3])}{', …' if len(shared) > 3 else ''})", len(shared), False)
    # (d) 승계 — 조각 F 가 O 를 특수화하면 O 를 가리키던 확정 링크 X→O 마다 X→F (원 링크의 종류를 힌트로)
    for frag, orig in sorted(g.subject_objects(PROV.specializationOf), key=lambda so: (str(so[0]), str(so[1]))):
        if frag not in u.chunks or orig not in u.chunks:
            continue
        for link in sorted(g.subjects(AGT.linkTo, orig), key=str):
            if str(next(g.objects(link, AGT.linkState), "")) != kb_lib.LINK_STATE_CONFIRMED:
                continue
            kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
            if kind not in LINK_KEYS or kind == "supersedes":
                continue
            for x in sorted(g.objects(link, AGT.linkFrom), key=str):
                before = len(evidence.get(frozenset((u.unit_of.get(x), u.unit_of.get(frag))), []))
                pair(x, frag, "constructionRecord", f"승계: {u.stem(orig)}", 0, True)
                key = frozenset((u.unit_of.get(x), u.unit_of.get(frag)))
                if len(evidence.get(key, [])) > before:
                    hint.setdefault(key, kind)
    # (e) 동시 편집 — 관측이 고정한 쌍 (단일 정의 위치 kb_lib.coedit_pairs). 관측이 없으면 0건이다
    iri = {str(c): c for c in u.chunks}
    obs, coedit, _ = kb_lib.coedit_pairs(coedit_paths, set(iri))
    for a, b in sorted(tuple(sorted(p)) for p in coedit):
        pair(iri[a], iri[b], "coEditHistory", Path(obs).stem, 0, False)
    return evidence, prefer, dropped, hint
```
<!-- 인용 끝 -->
