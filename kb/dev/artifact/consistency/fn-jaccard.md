---
id: https://agentic-knowledge-base.dev/id/chunk/52698279-f1ad-4285-b6a1-161a8d5a2c4c
type: artifact
level: executable
title_ko: 함수 jaccard (tools/consistency.py)
title: function jaccard in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d9f90265-3bbb-4012-993c-a471cd52933e
---
**함수** — `jaccard(a, b)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def jaccard(a: set, b: set) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 1.0
```
<!-- 인용 끝 -->
