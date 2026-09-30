---
id: https://agentic-knowledge-base.dev/id/chunk/90abf3f7-3c52-496f-9cb4-a2af556264cb
type: artifact
level: executable
title_ko: 함수 is_well_known (tools/kb_lib.py)
title: function is_well_known in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7aee7ddf-f82b-4788-88ce-b27bd5290481
---
**함수** — `is_well_known(iri)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def is_well_known(iri: str) -> bool:
    return any(iri.startswith(p) for p in WELL_KNOWN_PREFIXES)
```
<!-- 인용 끝 -->
