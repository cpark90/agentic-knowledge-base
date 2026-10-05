---
id: https://agentic-knowledge-base.dev/id/chunk/afe80dd3-6dab-4d6c-bc6c-51c534ca4697
type: artifact
level: executable
title_ko: 함수 in_domain (tools/case_gen.py)
title: function in_domain in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b055ea3f-2020-43a8-8cc6-942e7df8e99f]
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `in_domain(var, val)` 다. 정의역 판정 — True(keep 안) · False(keep 밖 정의역) · None(정의역 밖).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def in_domain(var: dict, val):
    """정의역 판정 — True(keep 안) · False(keep 밖 정의역) · None(정의역 밖)."""
    if inside(var, val):
        return True
    if "range" in var:
        lo, hi = var.get("domain", [None, None])
        if not isinstance(val, int) or isinstance(val, bool):
            return None
        return False if lo is None or lo <= val <= hi else None
    return False if str(val) in map(str, var.get("reject", [])) else None
```
<!-- 인용 끝 -->
