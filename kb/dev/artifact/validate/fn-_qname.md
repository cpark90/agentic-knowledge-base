---
id: https://agentic-knowledge-base.dev/id/chunk/7253cc54-4d5c-47ee-b402-6574573c23ef
type: artifact
level: executable
title_ko: 함수 _qname (tools/validate.py)
title: function _qname in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7624f877-e0d3-45fd-b51d-91d72c7cf025
---
**함수** — `_qname(merged, term)` 다. agt:·id: 용어는 접두사로 적는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _qname(merged: Graph, term) -> str:
    """agt:·id: 용어는 접두사로 적는다 — 병합 그래프의 qname 은 ns2: 처럼 나온다."""
    for prefix, ns in (("agt", AGT), ("id", kb_lib.ID)):
        if str(term).startswith(str(ns)):
            return f"{prefix}:{str(term)[len(str(ns)):]}"
    return merged.qname(term) if isinstance(term, URIRef) else str(term)
```
<!-- 인용 끝 -->
