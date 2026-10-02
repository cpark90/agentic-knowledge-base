---
id: https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9
type: artifact
level: executable
title_ko: 함수 local (tools/assume_check.py)
title: function local in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `local(iri)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def local(iri) -> str:
    return str(iri)[len(str(ID)):] if str(iri).startswith(str(ID)) else str(iri)
```
<!-- 인용 끝 -->
