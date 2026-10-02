---
id: https://agentic-knowledge-base.dev/id/chunk/fedf25c3-0ff9-483f-b5e0-afd61a05c16f
type: artifact
level: executable
title_ko: 함수 short (tools/community.py)
title: function short in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5
---
**함수** — `short(iri)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def short(iri) -> str:
    return str(iri).split("/")[-1][:8]
```
<!-- 인용 끝 -->
