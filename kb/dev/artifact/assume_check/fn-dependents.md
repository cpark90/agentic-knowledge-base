---
id: https://agentic-knowledge-base.dev/id/chunk/b9bfc5e7-9b9e-4472-bad1-4d151d9fe1c9
type: artifact
level: executable
title_ko: 함수 dependents (tools/assume_check.py)
title: function dependents in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `dependents(g)` 다. 청크 → 그 청크를 가리키는 링크의 주어들 (하류 의존자).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def dependents(g: Graph) -> dict:
    """청크 → 그 청크를 가리키는 링크의 주어들 (하류 의존자). 직접 트리플과 agt:Link 개체(linkFrom·linkTo·linkKind) 둘 다."""
    rdep = defaultdict(set)
    kinds = set(PROPAGATE)
    for p in PROPAGATE:
        for s, o in g.subject_objects(p):
            rdep[o].add(s)
            if p in (AGT.coUpdatesWith, AGT.overlapsWith):  # 대칭 — 함께 갱신되는 쌍은 양쪽이 서로의 하류다
                rdep[s].add(o)
    for link in g.subjects(RDF.type, AGT.Link):
        k = next(g.objects(link, AGT.linkKind), None)
        if k not in kinds:
            continue
        f, t = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        if f is not None and t is not None:
            rdep[t].add(f)
    return rdep
```
<!-- 인용 끝 -->
