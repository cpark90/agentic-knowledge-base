---
id: https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4
type: artifact
level: executable
title_ko: 함수 _chunk_location (tools/validate.py)
title: function _chunk_location in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `_chunk_location(merged, chunk)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _chunk_location(merged: Graph, chunk: URIRef) -> str:
    return next((str(l) for l in merged.objects(chunk, kb_lib.AGT.assertionLocation)), merged.qname(chunk))
```
<!-- 인용 끝 -->
