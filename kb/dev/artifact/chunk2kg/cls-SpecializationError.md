---
id: https://agentic-knowledge-base.dev/id/chunk/9081dacd-219d-4944-b3c6-d5d9a6955f49
type: artifact
level: executable
title_ko: 클래스 SpecializationError (tools/chunk2kg.py)
title: class SpecializationError in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24
---
**클래스** — `class SpecializationError` 다. specializationOf 규칙 위반 — 자기 참조·사슬 순환.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class SpecializationError(ValueError):
    """specializationOf 규칙 위반 — 자기 참조·사슬 순환. 게이트 id 는 SPECIALIZATION_GATE 다."""
```
<!-- 인용 끝 -->
