---
id: https://agentic-knowledge-base.dev/id/chunk/a8451195-7601-4dd9-aab3-f74defed5506
type: artifact
level: executable
title_ko: 함수 region_qname (tools/extract.py)
title: function region_qname in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9]
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**함수** — `region_qname(r)` 다. 구역의 한정 이름 — 깊이가 종류를 정한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def region_qname(r: Region) -> str:
    """구역의 한정 이름 — 깊이가 종류를 정한다. 장과 그 첫 절이 같은 이름을 키로 가져도 갈린다."""
    return "head" if r.is_head else (f"ch:{r.key}" if r.depth == 1 else f"sec:{r.key}")
```
<!-- 인용 끝 -->
