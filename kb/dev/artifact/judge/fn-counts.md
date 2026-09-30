---
id: https://agentic-knowledge-base.dev/id/chunk/25d46f37-11ee-4e27-92e7-9584f2dcb1a0
type: artifact
level: executable
title_ko: 함수 counts (tools/judge.py)
title: function counts in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/8f3b4eaf-dced-410d-98cc-6771157e17c6
---
**함수** — `counts(rows)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def counts(rows: list[dict]) -> dict:
    return {r: sum(1 for x in rows if x["route"] == r) for r in kb_lib.JUDGE_ROUTES}
```
<!-- 인용 끝 -->
