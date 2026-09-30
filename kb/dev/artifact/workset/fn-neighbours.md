---
id: https://agentic-knowledge-base.dev/id/chunk/347d7f8b-0fe2-43ee-b702-9dea92fdad9d
type: artifact
level: executable
title_ko: 함수 neighbours (tools/workset.py)
title: function neighbours in tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/efdb6344-03eb-4727-97ba-fe8aadcc7424
---
**함수** — `neighbours(g, x)` 다. x 의 이웃 (노드, 족 순위, 족 표시) — 양방향.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def neighbours(g: Graph, x):
    """x 의 이웃 (노드, 족 순위, 족 표시) — 양방향. 직접 트리플과 agt:Link 개체(linkFrom·linkTo·linkKind)를 모두 본다."""
    for p, fam in FAMILY_OF.items():
        for o in g.objects(x, p):
            yield o, fam
        for s in g.subjects(p, x):
            yield s, fam
    for link in g.subjects(AGT.linkFrom, x):
        fam = FAMILY_OF.get(next(g.objects(link, AGT.linkKind), None))
        if fam:
            for o in g.objects(link, AGT.linkTo):
                yield o, fam
    for link in g.subjects(AGT.linkTo, x):
        fam = FAMILY_OF.get(next(g.objects(link, AGT.linkKind), None))
        if fam:
            for s in g.objects(link, AGT.linkFrom):
                yield s, fam
```
<!-- 인용 끝 -->
