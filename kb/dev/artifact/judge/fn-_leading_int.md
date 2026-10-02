---
id: https://agentic-knowledge-base.dev/id/chunk/a2001d9e-7d53-4d25-b643-9825bd271d97
type: artifact
level: executable
title_ko: 함수 _leading_int (tools/judge.py)
title: function _leading_int in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/25ad6efd-997a-44a7-b5c4-dc61c13b63ed
---
**함수** — `_leading_int(scale_situation)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _leading_int(scale_situation: str) -> int:
    m = re.match(r"\s*(-?\d+)", scale_situation)
    return int(m.group(1)) if m else 0
```
<!-- 인용 끝 -->
