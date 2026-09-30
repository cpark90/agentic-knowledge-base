---
id: https://agentic-knowledge-base.dev/id/chunk/884c28fc-a47e-4e4b-ac96-a98f560a3d07
type: artifact
level: executable
title_ko: 함수 gather (tools/link.py)
title: function gather in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `gather(u, min_shared)` 다. 증거 수집 → (쌍 → 증거 목록 [(강도, 종류, 값, 정렬용 공유 수)], 쌍 → 인용 방향, 탈락 분포, 쌍 → 승계 종류).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gather(u: Units, min_shared: int):
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
    # (b) 테스트 공동 커버 — 같은 V&V 청크가 verifies 하는 두 개발 단위
    covers = defaultdict(set)
    for s, o in g.subject_objects(AGT.verifies):
        if s in u.live and o in u.unit_of:
            covers[s].add(u.unit_of[o])
    for s in sorted(covers, key=str):
        targets = sorted(covers[s], key=str)
        for i, a in enumerate(targets):
            for b in targets[i + 1:]:
                pair(a, b, "testCoverage", u.stem(s), 0, False)
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
    return evidence, prefer, dropped, hint
```
<!-- 인용 끝 -->
