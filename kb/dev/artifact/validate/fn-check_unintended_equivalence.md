---
id: https://agentic-knowledge-base.dev/id/chunk/ff39b4c5-f9a7-40e5-bda5-e1cab86106d8
type: artifact
level: executable
title_ko: 함수 check_unintended_equivalence (tools/validate.py)
title: function check_unintended_equivalence in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/03af6d80-e46c-44f7-acd5-12d186d9bb75, https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe]
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `check_unintended_equivalence(asserted, closed, classes, unsat, files)` 다. 의도치 않은 동치 (게이트 `unintended-equivalence`, 유저 결정 Q179-a) — 폐포에서 서로 하위이나 선언되지 않은 이름 클래스 쌍.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_unintended_equivalence(asserted: Graph, closed: Graph, classes: set, unsat: set,
                                 files: dict[str, Graph]) -> list[str]:
    """의도치 않은 동치 (게이트 `unintended-equivalence`, 유저 결정 Q179-a) — 폐포에서 서로 하위이나 선언되지 않은 이름 클래스 쌍.

    owlrl 은 폐포에서 모든 클래스에 반사적 owl:equivalentClass 를 더하고 상호 하위에서 동치를 낳으므로, 선언은 단언 그래프에서
    읽는다. 단언된 owl:equivalentClass 간선(빈 노드 포함)의 연결 요소 안의 쌍은 선언된 동치의 사슬이라 보고하지 않는다. 단언된
    rdfs:subClassOf 순환 위의 쌍은 `cyclic-hierarchy` 가, 불만족 클래스의 쌍(owl:Nothing 을 거쳐 서로 하위다)은
    `unsatisfiable-class` 가 보고하므로 여기서 다시 보고하지 않는다. 쌍마다 한 줄이고 순서는 IRI 순이다.
    """
    gate = UNINTENDED_EQUIVALENCE
    declared: dict = {}  # 단언된 동치의 연결 요소 — 합집합 찾기

    def root(n):
        while declared.get(n, n) != n:
            n = declared[n]
        return n

    for s, o in asserted.subject_objects(OWL.equivalentClass):
        declared.setdefault(s, s)
        declared.setdefault(o, o)
        declared[root(s)] = root(o)
    cycle = {c: i for i, comp in enumerate(subclass_components(asserted)) for c in comp}
    errors = []
    pool = sorted(classes - unsat, key=str)
    for i, a in enumerate(pool):
        for b in pool[i + 1:]:
            if (a, RDFS.subClassOf, b) not in closed or (b, RDFS.subClassOf, a) not in closed:
                continue
            if root(a) == root(b) or (a in cycle and cycle.get(b) == cycle[a]):
                continue
            errors.append(f"[{gate}] {_axiom_file(files, (a, RDF.type, OWL.Class))}: 클래스 {_term(closed, a)} 와 "
                          f"{_term(closed, b)}({_axiom_file(files, (b, RDF.type, OWL.Class))}) 가 OWL 2 RL 폐포에서 서로의 하위 "
                          f"클래스다 — owl:equivalentClass 선언이 없다")
    return errors
```
<!-- 인용 끝 -->
