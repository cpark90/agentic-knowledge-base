---
id: https://agentic-knowledge-base.dev/id/chunk/36ed7d92-b42b-43c6-9325-c9846e77d4fb
type: artifact
level: executable
title_ko: 함수 check_logical_consistency (tools/validate.py)
title: function check_logical_consistency in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2e3ab692-4155-443c-bf19-1d0a95085056, https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe, https://agentic-knowledge-base.dev/id/chunk/cd63cbde-c24e-46c6-892a-a26c39ddaa31]
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `check_logical_consistency(asserted, closed, messages, files)` 다. OWL 2 RL 폐포의 모순 (게이트 `logical-consistency`, 유저 결정 Q174-a) — 오류 노드와 owl:Nothing 소속.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_logical_consistency(asserted: Graph, closed: Graph, messages: list[str],
                              files: dict[str, Graph]) -> list[str]:
    """OWL 2 RL 폐포의 모순 (게이트 `logical-consistency`, 유저 결정 Q174-a) — 오류 노드와 owl:Nothing 소속.

    FAIL 줄은 모순의 근원을 가리킨다 — 개체 IRI 와 그 파일(`agt:assertionLocation`), 모순을 낳은 공리와 그 파일, 개체의
    단언 유형이다. 서로소 클래스의 공통 개체는 owlrl 메시지에서 두 클래스와 개체를 읽어 공리 `owl:disjointWith` 의 자리를
    찾는다. owl:Nothing 소속은 폐포를 직접 질의하고(owlrl 의 같은 메시지는 겹치므로 뺀다) 개체가 속한 불만족 클래스를 적는다.
    그 밖의 owlrl 메시지는 IRI 만 접두사로 줄여 그대로 옮긴다.
    """
    gate = LOGICAL_CONSISTENCY
    errors = []
    nothing = set(closed.subjects(RDF.type, OWL.Nothing))
    for x in sorted(nothing):
        unsat = sorted((c for c in closed.objects(x, RDF.type)
                        if c != OWL.Nothing and (c, RDFS.subClassOf, OWL.Nothing) in closed), key=str)
        why = ", ".join(f"{_term(closed, c)}({_axiom_file(files, (c, RDFS.subClassOf, OWL.Nothing), (c, OWL.equivalentClass, OWL.Nothing))})"
                        for c in unsat) or "없음(owl:Nothing 직접 단언)"
        roots = " / ".join(_type_roots(asserted, closed, x, c) for c in unsat) or _type_roots(asserted, closed, x, OWL.Nothing)
        errors.append(f"[{gate}] {_node_location(closed, x)}: 개체 <{x}> 가 owl:Nothing 에 속한다 — 불만족 클래스 {why}, "
                      f"단언 유형 {roots}")
    seen: set = set()
    for msg in messages:
        if _OWLRL_NOTHING.match(msg):
            continue
        m = _OWLRL_DISJOINT.match(msg)
        if m:
            c1, c2, x = (URIRef(v) for v in m.groups())
            # owl:Nothing 의 개체는 모든 클래스에 속하므로 서로소 공리마다 걸린다 — 근원은 위의 owl:Nothing 줄 하나다.
            # 공리는 대칭이라 owlrl 이 두 순서로 낼 수 있다 — 개체와 클래스 쌍마다 한 줄이다
            if x in nothing or (x, frozenset((c1, c2))) in seen:
                continue
            seen.add((x, frozenset((c1, c2))))
            axiom = _axiom_file(files, (c1, OWL.disjointWith, c2), (c2, OWL.disjointWith, c1))
            errors.append(f"[{gate}] {_node_location(closed, x)}: 개체 <{x}> 가 서로소 클래스 {_term(closed, c1)} 와 "
                          f"{_term(closed, c2)} 에 함께 속한다 — 공리 {_term(closed, c1)} owl:disjointWith {_term(closed, c2)}"
                          f"({axiom}), 단언 유형 {_type_roots(asserted, closed, x, c1)} / {_type_roots(asserted, closed, x, c2)}")
            continue
        iris = _IRI_IN_TEXT.findall(msg)
        where = next((_node_location(closed, URIRef(i)) for i in iris
                      if (URIRef(i), AGT.assertionLocation, None) in closed), "OWL 2 RL 폐포")
        errors.append(f"[{gate}] {where}: 추론기 오류 — " + _IRI_IN_TEXT.sub(lambda i: _term(closed, URIRef(i.group(0))), msg))
    return errors
```
<!-- 인용 끝 -->
