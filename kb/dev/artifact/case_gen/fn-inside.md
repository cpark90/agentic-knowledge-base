---
id: https://agentic-knowledge-base.dev/id/chunk/b055ea3f-2020-43a8-8cc6-942e7df8e99f
type: artifact
level: executable
title_ko: 함수 inside (tools/case_gen.py)
title: function inside in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `inside(var, val)` 다. 값이 keep 안인가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def inside(var: dict, val) -> bool:
    """값이 keep 안인가."""
    if "range" in var:
        return isinstance(val, int) and var["range"][0] <= val <= var["range"][1]
    return str(val) in map(str, var["values"])
```
<!-- 인용 끝 -->
