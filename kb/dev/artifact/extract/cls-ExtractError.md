---
id: https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b
type: artifact
level: executable
title_ko: 클래스 ExtractError (tools/extract.py)
title: class ExtractError in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/57a845e1-da27-4d9d-b5b0-b25148ccece7
---
**클래스** — `class ExtractError` 다. 생성 시점 거부 — 메시지가 `<경로>: <근거>` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class ExtractError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""
```
<!-- 인용 끝 -->
