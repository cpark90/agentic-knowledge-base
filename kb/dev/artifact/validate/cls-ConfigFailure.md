---
id: https://agentic-knowledge-base.dev/id/chunk/386f974f-846c-47c9-99dc-ee866783f5c5
type: artifact
level: executable
title_ko: 클래스 ConfigFailure (tools/validate.py)
title: class ConfigFailure in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0025c8a9-2659-465c-b2f2-517884f7bcdb
---
**클래스** — `class ConfigFailure` 다. 게이트가 판정을 내릴 수 없는 설정·입력 상태(EXIT_CONFIG) — 메시지가 `FAIL [<검사명>] …` 한 줄이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class ConfigFailure(Exception):
    """게이트가 판정을 내릴 수 없는 설정·입력 상태(EXIT_CONFIG) — 메시지가 `FAIL [<검사명>] …` 한 줄이다."""
```
<!-- 인용 끝 -->
