---
id: https://agentic-knowledge-base.dev/id/chunk/02c3daad-5974-4be8-80ea-4c6b338b45de
type: artifact
level: executable
title_ko: 클래스 SyntaxFailure (tools/validate.py)
title: class SyntaxFailure in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/0025c8a9-2659-465c-b2f2-517884f7bcdb
---
**클래스** — `class SyntaxFailure` 다. 파일 하나가 파싱되지 않는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class SyntaxFailure(Exception):
    """파일 하나가 파싱되지 않는다 — 어느 파일인지를 메시지에 지닌다."""
```
<!-- 인용 끝 -->
