---
id: https://agentic-knowledge-base.dev/id/chunk/583a95ea-746e-4243-a6d9-108c18a3c9d8
type: artifact
level: executable
title_ko: 함수 link_targets (tools/chunk2kg.py)
title: function link_targets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `link_targets(meta)` 다. 청크가 링크 키(LINK_KEYS)로 가리키는 대상 IRI 전부 — restored: 의 IRI 는 이 안에 있어야 한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_targets(meta: dict) -> set:
    """청크가 링크 키(LINK_KEYS)로 가리키는 대상 IRI 전부 — restored: 의 IRI 는 이 안에 있어야 한다."""
    return {to for key in LINK_KEYS for to in (meta.get(key, []) or [])}
```
<!-- 인용 끝 -->
