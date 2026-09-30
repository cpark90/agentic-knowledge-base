---
id: https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b
type: artifact
level: executable
title_ko: 클래스 JudgeError (tools/judge.py)
title: class JudgeError in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add
---
**클래스** — `class JudgeError` 다. 입력·설정 문제 — 메시지가 곧 수정 안내다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class JudgeError(Exception):
    """입력·설정 문제 — 메시지가 곧 수정 안내다 (EXIT_CONFIG)."""
```
<!-- 인용 끝 -->
