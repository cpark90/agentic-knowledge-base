---
id: https://agentic-knowledge-base.dev/id/chunk/f418fcb4-df9f-496c-9cc7-09f83dc5d1e5
type: artifact
level: executable
title_ko: 함수 is_link_block (tools/chunk2kg.py)
title: function is_link_block in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828
---
**함수** — `is_link_block(iri)` 다. 링크·증거 블록인가 — 청크·복합체와 달리 뿌리 uuid 로 IRI 를 다시 계산하고 같은 IRI 는 합친다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def is_link_block(iri: str) -> bool:
    """링크·증거 블록인가 — 청크·복합체와 달리 뿌리 uuid 로 IRI 를 다시 계산하고 같은 IRI 는 합친다."""
    return iri.startswith(LINK_PREFIX) or iri.startswith(EVIDENCE_PREFIX)
```
<!-- 인용 끝 -->
