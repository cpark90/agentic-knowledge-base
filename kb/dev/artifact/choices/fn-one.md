---
id: https://agentic-knowledge-base.dev/id/chunk/27565539-2b3a-4beb-b476-f7ac8360c2de
type: artifact
level: executable
title_ko: 함수 one (tools/choices.py)
title: function one in tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6c9da832-fd4f-4fba-a0f6-33561303de46
---
**함수** — `one(g, s, p)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def one(g: Graph, s, p) -> str:
    return str(next(g.objects(s, p), ""))
```
<!-- 인용 끝 -->
