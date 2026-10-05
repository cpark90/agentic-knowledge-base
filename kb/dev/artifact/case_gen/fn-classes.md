---
id: https://agentic-knowledge-base.dev/id/chunk/6807ef1c-074c-48b5-a2e8-31e44223ab17
type: artifact
level: executable
title_ko: 함수 classes (tools/case_gen.py)
title: function classes in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `classes(var)` 다. 등가 부류 — 범위 변수는 keep 구간과 `domain` 이 남기는 아래·위 구간, 열거 변수는 keep 값 묶음과 reject 묶음.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def classes(var: dict) -> list[list]:
    """등가 부류 — 범위 변수는 keep 구간과 `domain` 이 남기는 아래·위 구간, 열거 변수는 keep 값 묶음과 reject 묶음."""
    if "values" in var:
        return [c for c in (list(var["values"]), list(var.get("reject", []))) if c]
    lo, hi = var["range"]
    dlo, dhi = var.get("domain", [lo, hi])
    return [iv for iv in ([dlo, lo - 1], [lo, hi], [hi + 1, dhi]) if iv[0] <= iv[1]]
```
<!-- 인용 끝 -->
