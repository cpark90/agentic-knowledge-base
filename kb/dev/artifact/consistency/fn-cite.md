---
id: https://agentic-knowledge-base.dev/id/chunk/fdb7f411-8074-4715-a11f-815131022f96
type: artifact
level: executable
title_ko: 함수 cite (tools/consistency.py)
title: function cite in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/e33ee826-0842-4cdd-8e68-16823604cffa
---
**함수** — `cite(it, ln, expr, quote)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def cite(it, ln, expr, quote):
    return f"- `{expr}`: `{it['path']}:{ln}` — {quote}"
```
<!-- 인용 끝 -->
