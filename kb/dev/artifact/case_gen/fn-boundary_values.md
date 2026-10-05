---
id: https://agentic-knowledge-base.dev/id/chunk/1f54d1f6-5634-49e6-abcf-060e526dcd88
type: artifact
level: executable
title_ko: 함수 boundary_values (tools/case_gen.py)
title: function boundary_values in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/afe80dd3-6dab-4d6c-bc6c-51c534ca4697]
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `boundary_values(var)` 다. 각 범위의 양 끝과 바로 안팎 — `domain` 이 있으면 그 밖은 내지 않는다(정의역 밖 값은 케이스가 아니다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def boundary_values(var: dict) -> list[int]:
    """각 범위의 양 끝과 바로 안팎 — `domain` 이 있으면 그 밖은 내지 않는다(정의역 밖 값은 케이스가 아니다)."""
    lo, hi = var["range"]
    out = []
    for x in (lo - 1, lo, lo + 1, hi - 1, hi, hi + 1):
        if x not in out and in_domain(var, x) is not None:
            out.append(x)
    return out
```
<!-- 인용 끝 -->
