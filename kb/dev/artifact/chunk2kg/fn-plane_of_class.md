---
id: https://agentic-knowledge-base.dev/id/chunk/9bfb814f-db8d-42dc-b618-9f691a50596d
type: artifact
level: executable
title_ko: 함수 plane_of_class (tools/chunk2kg.py)
title: function plane_of_class in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/741f8dd1-f282-478e-b9c0-40e1300f6dce
---
**함수** — `plane_of_class(cls)` 다. plane 청크 클래스(IRI·`agt:` 접두 이름·지역명) → plane 이름.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plane_of_class(cls) -> str:
    """plane 청크 클래스(IRI·`agt:` 접두 이름·지역명) → plane 이름. plane 청크 클래스가 아니면 빈 문자열이다."""
    name = str(cls).rsplit("/", 1)[-1].rsplit(":", 1)[-1]
    return CLASS_PLANE.get(name, "")
```
<!-- 인용 끝 -->
