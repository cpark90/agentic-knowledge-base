---
id: https://agentic-knowledge-base.dev/id/chunk/95affdef-9253-4022-a9ec-ea650d4b30ed
type: artifact
level: executable
title_ko: 함수 item_plane_resolver (tools/kb_lib.py)
title: function item_plane_resolver in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `item_plane_resolver(g)` 다. 항목 → 지식 종류의 함수.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def item_plane_resolver(g: Graph):
    """항목 → 지식 종류의 함수. 단위 지식은 제 지식 종류고, 복합체는 부분(agt:hasDirectPart)을 따라 내려가 첫 단위 지식의 지식 종류다.

    **중첩 복합체는 깊이만큼 따라간다**(p4-composite-as-part-of) — 코드의 추출은 파일 → 절 → 정의 두 단이다
    (p7-code-links-on-file-composite). 순환은 방문 집합으로 막고 판정은 verify 질의 `composite-cycle` 이 한다. 없으면 None 이다.
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
    return plane_of
```
<!-- 인용 끝 -->
