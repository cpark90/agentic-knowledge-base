---
id: https://agentic-knowledge-base.dev/id/chunk/58418c78-77dc-491d-bce6-60d85217ee30
type: artifact
level: executable
title_ko: 함수 worst_grade (tools/assume_check.py)
title: function worst_grade in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `worst_grade(grades)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def worst_grade(grades: list[str]) -> str:
    known = [g for g in grades if g in GRADES]
    if not known or len(known) != len(grades):
        return "?"
    return max(known, key=GRADES.index)
```
<!-- 인용 끝 -->
