---
id: https://agentic-knowledge-base.dev/id/chunk/8a58cf85-fc7e-418d-91fc-ce025cf2cff9
type: artifact
level: executable
title_ko: 함수 questions (tools/judge.py)
title: function questions in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `questions(g)` 다. 등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def questions(g: Graph) -> dict:
    """등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}."""
    return kb_lib.judge_questions(g)
```
<!-- 인용 끝 -->
