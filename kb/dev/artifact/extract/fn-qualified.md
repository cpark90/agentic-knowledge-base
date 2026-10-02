---
id: https://agentic-knowledge-base.dev/id/chunk/5fef9048-0948-4bfe-ad98-9a6587163b44
type: artifact
level: executable
title_ko: 함수 qualified (tools/extract.py)
title: function qualified in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `qualified(kind, key)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def qualified(kind: str, key: str) -> str:
    return f"{kind}:{key}"
```
<!-- 인용 끝 -->
