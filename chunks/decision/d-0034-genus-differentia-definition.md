---
id: https://agentic-knowledge-base.dev/id/chunk-d0034
type: decision
level: concrete
title_ko: 정의는 속 더하기 종차로 쓴다
title: Definitions use genus plus differentia
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 온톨로지의 모든 개념은 텍스트 정의를 갖는다(2.5절 위생). 형식은
상위 온톨로지 커뮤니티의 관행을 따라 **속(genus) + 종차(differentia)**로
쓴다 — "A는 [상위 개념] 중 [구별 조건]인 것이다."

```
agt:DecisionChunk = agt:Chunk 중 판정 방식이 논증의 타당성인 것
agt:Assumption    = 명제 중 어떤 지식 항목이 유효하기 위해 참이어야 하는 것
```

**근거** (노트 0.9절)
- 이 형식이면 **상위 개념이 정의 안에 명시되어 분류 오류가 드러난다.**
  정의를 읽는 것만으로 그 개념이 잘못된 부모 아래 놓였는지 알 수 있다.
- 종차가 판정 조건의 형태를 띠므로 정의가 곧 검사 기준이 된다 — 위 예에서
  `agt:DecisionChunk`의 종차는 plane의 판정 방식(5.1절)과 그대로 이어진다.
- 상위 온톨로지 커뮤니티의 관행이므로 지어낸 규칙이 아니다(0.0절).
