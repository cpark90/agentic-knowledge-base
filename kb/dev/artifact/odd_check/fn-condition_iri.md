---
id: https://agentic-knowledge-base.dev/id/chunk/b2d18590-036b-4fda-81e8-a8d9a2e4713d
type: artifact
level: executable
title_ko: 함수 condition_iri (tools/odd_check.py)
title: function condition_iri in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/bdc32d15-06d9-439b-a3b2-0d3dab05225f
---
**함수** — `condition_iri(attr)` 다. ATTRIBUTES.<속성>.iri 의 `id:cond-…` 를 전체 IRI 로 편다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def condition_iri(attr: dict) -> str:
    """ATTRIBUTES.<속성>.iri 의 `id:cond-…` 를 전체 IRI 로 편다 (odd2kg 와 같은 접두사)."""
    iri = str(attr.get("iri", ""))
    return ID_BASE + iri[3:] if iri.startswith("id:") else iri
```
<!-- 인용 끝 -->
