---
id: https://agentic-knowledge-base.dev/id/chunk/8d5e7694-cb0b-42c7-a734-a6f0e8782caf
type: artifact
level: executable
title_ko: 함수 check_question (tools/judge.py)
title: function check_question in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `check_question(q, name)` 다. 형이 셋 안이고 선택 집합이 상한 안인가 — 아니면 수정 방향과 함께 거부한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_question(q: dict, name: str) -> None:
    """형이 셋 안이고 선택 집합이 상한 안인가 — 아니면 수정 방향과 함께 거부한다 (규칙 ③)."""
    if q["form"] not in kb_lib.JUDGE_FORMS:
        raise JudgeError(f"질문 {name}: 형 {q['form']!r} 이 {' · '.join(kb_lib.JUDGE_FORMS)} 밖이다 — 자유 서술은 판정이 아니다")
    if q["form"] == "choice" and len(q["options"]) > kb_lib.JUDGE_CHOICE_MAX:
        raise JudgeError(f"질문 {name}: 선택 집합 {len(q['options'])} 개가 상한 {kb_lib.JUDGE_CHOICE_MAX} 를 넘는다 — "
                         f"질문을 2단계로 나눈다: 후보마다 독립 점수(score)를 묻고 상위 {kb_lib.JUDGE_CHOICE_MAX} 이하로 좁힌 뒤 "
                         "명시 선택(choice)을 묻는다 (p8-judge-calibration-binding 규칙 ③)")
```
<!-- 인용 끝 -->
