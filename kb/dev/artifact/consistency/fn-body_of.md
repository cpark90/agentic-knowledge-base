---
id: https://agentic-knowledge-base.dev/id/chunk/24dc9c0c-05f9-414a-b183-f9974cd57c05
type: artifact
level: executable
title_ko: 함수 body_of (tools/consistency.py)
title: function body_of in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d9f90265-3bbb-4012-993c-a471cd52933e
---
**함수** — `body_of(path)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_of(path: str) -> str:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = lines[1:].index("---") + 1
    return "\n".join(l for l in lines[end + 1:]).strip()
```
<!-- 인용 끝 -->
