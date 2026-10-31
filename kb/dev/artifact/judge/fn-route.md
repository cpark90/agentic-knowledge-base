---
id: https://agentic-knowledge-base.dev/id/chunk/25dbde8d-3165-4a6e-bda8-313cc2ef674b
type: artifact
level: executable
title_ko: 함수 route (tools/judge.py)
title: function route in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `route()` 다. 판정 행의 처리.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def route() -> str:
    """판정 행의 처리. 자동 적용은 정확도·판별력을 잰 뒤에만 켜고 단독 응답에는 붙지 않는다 (규칙 ③·④) — 그 측정이
    아직 없으므로 지금은 전부 사람 확인 큐다. 확신도는 자기 보고라 처리를 가르지 않는다 (규칙 ②, Q-0056 Q119-a)."""
    return kb_lib.JUDGE_QUEUE
```
<!-- 인용 끝 -->
