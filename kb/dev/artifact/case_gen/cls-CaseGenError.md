---
id: https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a
type: artifact
level: executable
title_ko: 클래스 CaseGenError (tools/case_gen.py)
title: class CaseGenError in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1a0a0d9e-abcb-46ca-bf5b-d530a350816e
---
**클래스** — `class CaseGenError` 다. 생성 시점 거부 — 메시지가 `<경로>: <근거>` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class CaseGenError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다. 여러 줄이면 줄마다 하나다."""
```
<!-- 인용 끝 -->
