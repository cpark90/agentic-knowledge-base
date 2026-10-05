---
id: https://agentic-knowledge-base.dev/id/chunk/0a2c0068-9fd2-4400-9712-7f00184c9800
type: artifact
level: executable
title_ko: 함수 _tick_run_end (tools/gen_norms.py)
title: function _tick_run_end in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T17:30:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `_tick_run_end(s, i)` 다. `s[i]` 에서 시작하는 백틱 열의 끝 위치.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _tick_run_end(s: str, i: int) -> int:
    """`s[i]` 에서 시작하는 백틱 열의 끝 위치."""
    return len(s) - len(s[i:].lstrip("`"))
```
<!-- 인용 끝 -->
