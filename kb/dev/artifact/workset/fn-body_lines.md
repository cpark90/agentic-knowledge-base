---
id: https://agentic-knowledge-base.dev/id/chunk/1c918cdf-d80a-4d97-be99-915bb8ee7e17
type: artifact
level: executable
title_ko: 함수 body_lines (tools/workset.py)
title: function body_lines in tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/efdb6344-03eb-4727-97ba-fe8aadcc7424
---
**함수** — `body_lines(path)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_lines(path: str) -> list[str]:
    t = Path(path).read_text(encoding="utf-8").split("\n")
    end = t[1:].index("---") + 1
    b = "\n".join(t[end + 1:]).strip("\n")
    return b.split("\n") if b else []
```
<!-- 인용 끝 -->
