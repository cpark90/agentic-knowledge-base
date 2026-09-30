---
id: https://agentic-knowledge-base.dev/id/chunk/2c101d4c-b9a7-473c-8c02-5f4de0bbec74
type: artifact
level: executable
title_ko: 함수 _writes_in (tools/validate.py)
title: function _writes_in in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7624f877-e0d3-45fd-b51d-91d72c7cf025
---
**함수** — `_writes_in(merged, role)` 다. 역할이 쓰는 KB 들 — agt:writesIn 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _writes_in(merged: Graph, role: URIRef) -> set[str]:
    """역할이 쓰는 KB 들 — agt:writesIn 값. 없으면 개발 KB(kb_lib.KB_DEV) 하나다 (role-ontology agt:writesIn 정의)."""
    return {str(v) for v in merged.objects(role, kb_lib.AGT.writesIn)} or {kb_lib.KB_DEV}
```
<!-- 인용 끝 -->
