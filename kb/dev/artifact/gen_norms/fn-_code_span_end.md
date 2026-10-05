---
id: https://agentic-knowledge-base.dev/id/chunk/61aa2e8e-5b73-49c6-91cb-987c5ffe5aeb
type: artifact
level: executable
title_ko: 함수 _code_span_end (tools/gen_norms.py)
title: function _code_span_end in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T17:30:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0a2c0068-9fd2-4400-9712-7f00184c9800]
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `_code_span_end(s, i)` 다. `s[i]` 에서 시작하는 백틱 열이 여는 코드 스팬의 끝(닫는 열 다음 위치) — 같은 길이의 닫는 열이 없으면 -1 (CommonMark 6.1).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _code_span_end(s: str, i: int) -> int:
    """`s[i]` 에서 시작하는 백틱 열이 여는 코드 스팬의 끝(닫는 열 다음 위치) — 같은 길이의 닫는 열이 없으면 -1 (CommonMark 6.1)."""
    j = _tick_run_end(s, i)
    n = j - i
    while True:
        k = s.find("`" * n, j)
        if k < 0:
            return -1
        m = _tick_run_end(s, k)
        if m - k == n:
            return m
        j = m
```
<!-- 인용 끝 -->
