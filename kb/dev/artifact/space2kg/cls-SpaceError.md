---
id: https://agentic-knowledge-base.dev/id/chunk/9875f781-35a4-413a-beae-89f20bb6ea33
type: artifact
level: executable
title_ko: 클래스 SpaceError (tools/space2kg.py)
title: class SpaceError in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/fc3f9858-3941-435d-b741-071b871ce613
---
**클래스** — `class SpaceError` 다. 설계 공간의 형식 위반 — 메시지가 `<경로>: <근거>` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class SpaceError(ValueError):
    """설계 공간의 형식 위반 — 메시지가 `<경로>: <근거>` 다. 게이트 id 는 GATE."""
```
<!-- 인용 끝 -->
