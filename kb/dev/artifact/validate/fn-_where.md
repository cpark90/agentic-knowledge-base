---
id: https://agentic-knowledge-base.dev/id/chunk/6900e30a-aaf6-462a-b290-9877e3439e9b
type: artifact
level: executable
title_ko: 함수 _where (tools/validate.py)
title: function _where in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0025c8a9-2659-465c-b2f2-517884f7bcdb
---
**함수** — `_where(files, node)` 다. 노드를 주어로 가진 파일 — FAIL 메시지의 <경로> 자리.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _where(files: dict[str, Graph], node) -> str:
    """노드를 주어로 가진 파일 — FAIL 메시지의 <경로> 자리. 어느 파일에도 없으면 IRI 그대로."""
    for path, g in files.items():
        if (node, None, None) in g:
            return path
    return str(node)
```
<!-- 인용 끝 -->
