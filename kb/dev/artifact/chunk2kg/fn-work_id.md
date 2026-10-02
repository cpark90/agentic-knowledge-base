---
id: https://agentic-knowledge-base.dev/id/chunk/8a9578b7-a0d9-4b0a-951e-aed33d8b8825
type: artifact
level: executable
title_ko: 함수 work_id (tools/chunk2kg.py)
title: function work_id in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9081dacd-219d-4944-b3c6-d5d9a6955f49]
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `work_id(iri, spec)` 다. 뿌리 uuid(work-id) — specializationOf 사슬(spec: 조각 → 원본)을 따라 올라간 끝.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def work_id(iri: str, spec: dict) -> str:
    """뿌리 uuid(work-id) — specializationOf 사슬(spec: 조각 → 원본)을 따라 올라간 끝. 사슬이 순환하면 SpecializationError.

    대상이 spec 에 없는 IRI(사슬 밖 또는 dangling)면 거기서 멈춘다 — 실재는 validate dangling 이 본다.
    """
    seen = [iri]
    while iri in spec:
        iri = spec[iri]
        if iri in seen:
            raise SpecializationError(f"{SPECIALIZATION_KEY} 사슬이 순환한다: {' → '.join(seen + [iri])} — 조각은 원본을, 원본은 조각을 가리키지 않는다")
        seen.append(iri)
    return iri
```
<!-- 인용 끝 -->
