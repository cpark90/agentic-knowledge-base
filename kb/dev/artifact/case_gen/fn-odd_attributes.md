---
id: https://agentic-knowledge-base.dev/id/chunk/54c8835d-68d1-43d6-85ab-2a0371c2a67e
type: artifact
level: executable
title_ko: 함수 odd_attributes (tools/case_gen.py)
title: function odd_attributes in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/10ce940e-ae6b-4b2e-8d0e-3bb5448ae88e
---
**함수** — `odd_attributes(path)` 다. ODD 문서의 속성 IRI 집합(`ATTRIBUTES.*.iri` — `id:cond-…` 꼴).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def odd_attributes(path: Path) -> set[str]:
    """ODD 문서의 속성 IRI 집합(`ATTRIBUTES.*.iri` — `id:cond-…` 꼴). 변수의 `odd` 가 이 안이어야 한다 (3.3절 ODD 참조)."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    attrs = data.get("ATTRIBUTES") or {}
    return {str(v.get("iri")) for v in attrs.values() if isinstance(v, dict) and v.get("iri")}
```
<!-- 인용 끝 -->
