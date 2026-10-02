---
id: https://agentic-knowledge-base.dev/id/chunk/040b7a8d-10e8-4e6e-96db-b8495e467218
type: artifact
level: executable
title_ko: 함수 order_errors (tools/chunk2kg.py)
title: function order_errors in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e
---
**함수** — `order_errors(where, order, source)` 다. 순서 목록 자체의 형 검사 — 목록인가·빈 문자열이 없는가·중복이 없는가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def order_errors(where: str, order, source: str) -> list:
    """순서 목록 자체의 형 검사 — 목록인가·빈 문자열이 없는가·중복이 없는가. 부분 집합과의 일치는 묶음 전체를 아는 곳이 본다."""
    if not isinstance(order, list) or not all(isinstance(o, str) and o for o in order):
        return [f"{where}: {source} 는 부분 IRI 목록 [<IRI>, …] 이어야 한다 — 실제 {order!r} (p4-composite-order-is-declared)"]
    dups = sorted({o for o in order if order.count(o) > 1})
    return [f"{where}: {source} 에 같은 부분이 두 번 있다 — 부분마다 색인 하나다: {dups}"] if dups else []
```
<!-- 인용 끝 -->
