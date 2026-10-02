---
id: https://agentic-knowledge-base.dev/id/chunk/86872920-200f-4ccb-b934-238d1c64bab3
type: artifact
level: executable
title_ko: 절 load-profile (tools/judge.py)
title: section load-profile in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
composite: {id: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436, title_ko: 절 복합체 load-profile (tools/judge.py), title: section composite load-profile in tools/judge.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/86872920-200f-4ccb-b934-238d1c64bab3, https://agentic-knowledge-base.dev/id/chunk/473ab4af-5806-45ea-a923-d7f635544fdb, https://agentic-knowledge-base.dev/id/chunk/8a58cf85-fc7e-418d-91fc-ce025cf2cff9, https://agentic-knowledge-base.dev/id/chunk/568c9c47-0d5f-4372-a395-b07605eaeedd, https://agentic-knowledge-base.dev/id/chunk/25dbde8d-3165-4a6e-bda8-313cc2ef674b, https://agentic-knowledge-base.dev/id/chunk/8d5e7694-cb0b-42c7-a734-a6f0e8782caf], part_of: https://agentic-knowledge-base.dev/id/composite/85cd0960-2c5b-4a4c-b5be-bcf71f036c54}
---
**절** — `tools/judge.py` 의 절 `load-profile` 다. 프로파일에서 질문·척도·임계를 읽는다 (도구는 상수를 갖지 않는다)

**정의** — `load_profile` · `questions` · `thresholds` · `route` · `check_question` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 프로파일에서 질문·척도·임계를 읽는다 (도구는 상수를 갖지 않는다) ────────────────────────────────────────
# 원본은 kb_lib(judge_load_profile·judge_questions) 하나다(2026-09-30 vnv 결함 보고 ⑥) — label_sample.py 의
# `--judge-sheet` 가 같은 척도 문장을 그대로 옮기려면 두 도구가 같은 질의를 쓴다. 여기서는 얇게 감싸 JudgeError로만 바꾼다.
```
<!-- 인용 끝 -->
