---
id: https://agentic-knowledge-base.dev/id/chunk/b92bd358-40c4-4414-b59c-70676927564b
type: artifact
level: executable
title_ko: 함수 suspect_triggers_on (tools/kb_lib.py)
title: function suspect_triggers_on in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `suspect_triggers_on()` 다. 켜진 트리거만 — (링크 종류, 전파 규칙, 근거).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def suspect_triggers_on() -> tuple:
    """켜진 트리거만 — (링크 종류, 전파 규칙, 근거)."""
    return tuple((k, rule, basis) for k, rule, on, basis in SUSPECT_TRIGGERS if on)
```
<!-- 인용 끝 -->
