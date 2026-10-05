---
id: https://agentic-knowledge-base.dev/id/chunk/288a1409-ff72-4aa4-b505-661af74bce3e
type: artifact
level: executable
title_ko: 함수 _spans_closed (tools/gen_norms.py)
title: function _spans_closed in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T17:30:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/61aa2e8e-5b73-49c6-91cb-987c5ffe5aeb]
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `_spans_closed(s)` 다. `s` 안의 코드 스팬이 전부 `s` 안에서 닫히는가 — 링크 텍스트가 코드 스팬의 중간에서 끝나면 링크가 아니다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _spans_closed(s: str) -> bool:
    """`s` 안의 코드 스팬이 전부 `s` 안에서 닫히는가 — 링크 텍스트가 코드 스팬의 중간에서 끝나면 링크가 아니다."""
    i = 0
    while (i := s.find("`", i)) >= 0:
        end = _code_span_end(s, i)
        if end < 0:
            return False
        i = end
    return True
```
<!-- 인용 끝 -->
