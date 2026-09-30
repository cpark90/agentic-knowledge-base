---
id: https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551
type: artifact
level: executable
title_ko: 클래스 GenBuildError (tools/gen_build.py)
title: class GenBuildError in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd
---
**클래스** — `class GenBuildError` 다. 생성 시점 거부 — 메시지가 `<경로>: <근거>` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class GenBuildError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""
```
<!-- 인용 끝 -->
