---
id: https://agentic-knowledge-base.dev/id/chunk/09909df0-d231-4cd6-ae92-f2867a75a9f9
type: artifact
level: executable
title_ko: 함수 _place (tools/extract.py)
title: function _place in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `_place(regions, node)` 다. 정의를 그것을 담는 가장 깊은 구역에 넣는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _place(regions: list[Region], node) -> None:
    """정의를 그것을 담는 가장 깊은 구역에 넣는다."""
    for r in regions:
        if r.start <= node.lineno <= r.end:
            if any(c.start <= node.lineno <= c.end for c in r.children):
                _place(r.children, node)
            else:
                r.defs.append((node.lineno, node))
            return
```
<!-- 인용 끝 -->
