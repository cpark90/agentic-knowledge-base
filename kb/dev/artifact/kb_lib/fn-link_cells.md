---
id: https://agentic-knowledge-base.dev/id/chunk/75bab730-77dc-4a3d-945e-72e305b4eb8c
type: artifact
level: executable
title_ko: 함수 link_cells (tools/kb_lib.py)
title: function link_cells in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `link_cells(g)` 다. 링크 개체(agt:Link)가 채운 (종류, 출발 plane, 도착 plane) 칸의 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_cells(g: Graph) -> set:
    """링크 개체(agt:Link)가 채운 (종류, 출발 plane, 도착 plane) 칸의 집합.

    복합체 IRI 는 plane 이 없으므로 복합체의 부분(agt:hasDirectPart)을 따라 내려가 첫 청크의 plane 으로 보정한다 —
    결정 복합체의 부분은 전부 decision 이다. **중첩 복합체는 깊이만큼 따라간다**(p4-composite-as-part-of): 코드의
    추출은 파일 → 절 → 정의 두 단이라(p7-code-links-on-file-composite) 1단만 보면 파일 복합체를 가리키는 링크가
    칸을 채우지 못한다. 순환은 방문 집합으로 막는다 — 판정은 verify 질의 `composite-cycle` 이 한다.
    """
    plane = chunk_planes(g)
    part_of_comp = {}
    for comp, part in g.subject_objects(AGT.hasDirectPart):
        part_of_comp.setdefault(comp, part)

    def plane_of(node):
        seen = set()
        while node is not None and node not in seen:
            if plane.get(node):
                return plane[node]
            seen.add(node)
            node = part_of_comp.get(node)
        return None

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
