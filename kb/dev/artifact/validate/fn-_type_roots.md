---
id: https://agentic-knowledge-base.dev/id/chunk/cd63cbde-c24e-46c6-892a-a26c39ddaa31
type: artifact
level: executable
title_ko: 함수 _type_roots (tools/validate.py)
title: function _type_roots in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a]
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `_type_roots(asserted, closed, x, cls)` 다. 개체 x 의 cls 소속을 낳은 단언 rdf:type — cls 자신이거나 그 하위 클래스.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _type_roots(asserted: Graph, closed: Graph, x, cls) -> str:
    """개체 x 의 cls 소속을 낳은 단언 rdf:type — cls 자신이거나 그 하위 클래스. 없으면 정의역·치역·동치가 낳은 소속이다."""
    roots = sorted(_term(closed, t) for t in asserted.objects(x, RDF.type)
                   if t == cls or (t, RDFS.subClassOf, cls) in closed)
    return " · ".join(roots) if roots else "단언 유형 없음(추론된 소속)"
```
<!-- 인용 끝 -->
