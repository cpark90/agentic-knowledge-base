---
id: https://agentic-knowledge-base.dev/id/chunk/75bab730-77dc-4a3d-945e-72e305b4eb8c
type: artifact
level: executable
title_ko: 함수 link_cells (tools/kb_lib.py)
title: function link_cells in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/95affdef-9253-4022-a9ec-ea650d4b30ed]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `link_cells(g)` 다. 링크 개체(agt:Link)가 채운 (종류, 출발 지식 종류, 도착 지식 종류) 칸의 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_cells(g: Graph) -> set:
    """링크 개체(agt:Link)가 채운 (종류, 출발 지식 종류, 도착 지식 종류) 칸의 집합.

    복합체 IRI 는 지식 종류가 없으므로 `item_plane_resolver` 로 부분의 지식 종류를 따라 보정한다 — 결정 기록의 부분은 전부
    decision 이다. 1단만 보면 파일 복합체를 가리키는 링크가 칸을 채우지 못한다.
    """
    plane_of = item_plane_resolver(g)
    cells = set()
    for link in g.subjects(RDF.type, AGT.Link):
        f, t = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
        pf, pt = plane_of(f), plane_of(t)
        if kind and pf and pt:
            cells.add((kind, pf, pt))
    return cells
```
<!-- 인용 끝 -->
