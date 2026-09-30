---
id: https://agentic-knowledge-base.dev/id/chunk/9e72d875-7a97-411f-a264-49bd2a07e2d5
type: artifact
level: executable
title_ko: 함수 normalize (tools/judge.py)
title: function normalize in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/97e93b30-be59-4c26-b322-176b8e0f350e
---
**함수** — `normalize(payload, default_judge)` 다. 응답 항목 → {value, confidence, judge}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def normalize(payload: dict, default_judge: str) -> dict:
    """응답 항목 → {value, confidence, judge}. 키 이름은 `value`·`confidence`·`judge`이고 옛 이름(`decision`·
    `probability`·`model`)도 받는다 — 세션 판정자가 기록 형식을 조금씩 다르게 낼 수 있어서다."""
    value = payload.get("value", payload.get("decision"))
    conf = payload.get("confidence", payload.get("probability"))
    if value is None or conf is None:
        raise JudgeError(f"응답에 값 또는 확신도가 없다 — 받은 키 {sorted(payload)}. 필요한 것은 `value`·`confidence` 다")
    judge_id = str(payload.get("judge", payload.get("model", default_judge)))
    return {"value": str(value), "confidence": float(conf), "judge": judge_id}
```
<!-- 인용 끝 -->
