---
id: https://agentic-knowledge-base.dev/id/chunk/25dbde8d-3165-4a6e-bda8-313cc2ef674b
type: artifact
level: executable
title_ko: 함수 route (tools/judge.py)
title: function route in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `route(confidence, th)` 다. 확신도 → 처리.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def route(confidence: float, th: dict) -> str:
    """확신도 → 처리. 구간별 정확도(정확도·판별력)를 재기 전에는 자동 적용 구간이 없다 (규칙 ②) —
    확신도가 세션 판정자의 자기 보고인 지금은 이 경계가 항상 사람 확인 큐로 떨어진다."""
    if not th["measured"]:
        return kb_lib.JUDGE_QUEUE
    if confidence >= th["auto"]:
        return kb_lib.JUDGE_ROUTES[0]
    return kb_lib.JUDGE_ROUTES[1] if confidence >= th["human"] else kb_lib.JUDGE_ROUTES[2]
```
<!-- 인용 끝 -->
