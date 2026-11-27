---
id: https://agentic-knowledge-base.dev/id/chunk/2ef143c2-3056-410b-90b7-4bf908e80b8b
type: artifact
level: executable
title_ko: 함수 probe_unsatisfiable (tools/validate.py)
title: function probe_unsatisfiable in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/264d9fd1-b338-48ec-9eb9-9ca20577aecc, https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe, https://agentic-knowledge-base.dev/id/chunk/da2d5667-a0ed-4a3d-bfa8-6a83213f1d3f]
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `probe_unsatisfiable(ontology, classes, onto_files)` 다. 불만족 클래스와 그 근거(클래스 → 근거 문구 목록) — 프로브 개체를 넣은 판정용 사본의 OWL 2 RL 폐포로 근사한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def probe_unsatisfiable(ontology: Graph, classes: set, onto_files: dict[str, Graph]) -> dict:
    """불만족 클래스와 그 근거(클래스 → 근거 문구 목록) — 프로브 개체를 넣은 판정용 사본의 OWL 2 RL 폐포로 근사한다.

    사본은 온톨로지 그래프와 클래스마다 프로브 개체 `urn:probe:<퍼센트 인코딩한 클래스 IRI>` 하나(`rdf:type` 단언 하나)다. 데이터
    그래프와 기존 폐포에는 섞이지 않는다. 데이터 개체는 클래스 수준 불만족에 기여하지 않는다 — 프로브에는 속성 단언이 없다.
    프로브가 owl:Nothing 에 속하거나, 서로소 클래스(owl:disjointWith·owl:AllDisjointClasses)나 owl:complementOf 의 두 클래스에 함께
    속하거나, 그 밖의 추론기 오류가 프로브를 가리키면 그 클래스가 불만족이다. RL 근사다 — RL 규칙이 낳지 않는 불만족(예:
    전칭 제약과 존재 제약의 충돌)은 놓친다. owl:Nothing 의 개체는 모든 클래스에 속하므로 그 프로브의 서로소 메시지는 근거에서 뺀다.
    """
    from urllib.parse import quote

    probes = {URIRef("urn:probe:" + quote(str(c), safe="")): c for c in classes}
    copy = Graph()
    copy += ontology
    for p, c in probes.items():
        copy.add((p, RDF.type, c))
    closed, messages = owl_rl_closure(copy)
    reasons: dict = {}
    for p, c in probes.items():
        if (p, RDF.type, OWL.Nothing) not in closed:
            continue
        axioms = [(s, pr) for s in told_superclasses(ontology, c) for pr in (RDFS.subClassOf, OWL.equivalentClass)
                  if (s, pr, OWL.Nothing) in ontology or (pr == OWL.equivalentClass and (OWL.Nothing, pr, s) in ontology)]
        reasons[c] = [f"owl:Nothing 의 하위다(공리 {_term(closed, s)} {_term(closed, pr)} owl:Nothing, "
                      f"{_axiom_file(onto_files, (s, pr, OWL.Nothing), (OWL.Nothing, pr, s))})" for s, pr in sorted(axioms)] \
            or ["owl:Nothing 에 속한다(단언된 계층에 근거 공리가 없는 추론)"]
    for c1, c2 in sorted(closed.subject_objects(OWL.complementOf)):  # owlrl 의 cls-comm 메시지는 개체를 적지 않는다
        for p in set(closed.subjects(RDF.type, c1)) & set(closed.subjects(RDF.type, c2)) & set(probes):
            if (p, RDF.type, OWL.Nothing) not in closed:
                reasons.setdefault(probes[p], []).append(
                    f"상위 클래스 {_term(closed, c1)} 와 {_term(closed, c2)} 가 여집합이다(공리 {_term(closed, c1)} owl:complementOf "
                    f"{_term(closed, c2)}, {_axiom_file(onto_files, (c1, OWL.complementOf, c2))})")
    for msg in messages:
        if _OWLRL_NOTHING.match(msg):
            continue
        m = _OWLRL_DISJOINT.match(msg)
        if m:
            c1, c2, x = (URIRef(v) for v in m.groups())
            if x not in probes or (x, RDF.type, OWL.Nothing) in closed:
                continue
            if (c1, OWL.disjointWith, c2) not in ontology:  # 공리는 대칭이라 owlrl 이 두 순서로 낸다 — 단언된 방향으로 적는다
                c1, c2 = c2, c1
            text = (f"상위 클래스 {_term(closed, c1)} 와 {_term(closed, c2)} 가 서로소다(공리 {_term(closed, c1)} owl:disjointWith "
                    f"{_term(closed, c2)}, {_axiom_file(onto_files, (c1, OWL.disjointWith, c2), (c2, OWL.disjointWith, c1))})")
            if text not in reasons.get(probes[x], []):
                reasons.setdefault(probes[x], []).append(text)
            continue
        for i in _IRI_IN_TEXT.findall(msg):
            if URIRef(i) in probes and (URIRef(i), RDF.type, OWL.Nothing) not in closed:
                reasons.setdefault(probes[URIRef(i)], []).append(
                    "추론기 오류 — " + _IRI_IN_TEXT.sub(lambda t: _term(closed, URIRef(t.group(0))), msg))
    return {c: sorted(set(why)) for c, why in reasons.items()}
```
<!-- 인용 끝 -->
