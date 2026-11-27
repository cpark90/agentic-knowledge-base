---
id: https://agentic-knowledge-base.dev/id/chunk/2e3ab692-4155-443c-bf19-1d0a95085056
type: artifact
level: executable
title_ko: 함수 _node_location (tools/validate.py)
title: function _node_location in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a]
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `_node_location(closed, node)` 다. 개체의 파일(`agt:assertionLocation`) — 없으면 개체 표기 그대로다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _node_location(closed: Graph, node) -> str:
    """개체의 파일(`agt:assertionLocation`) — 없으면 개체 표기 그대로다. FAIL 줄의 <경로> 자리."""
    return next((str(l) for l in closed.objects(node, AGT.assertionLocation)), _term(closed, node))
```
<!-- 인용 끝 -->
