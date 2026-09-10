---
id: https://agentic-knowledge-base.dev/id/chunk-d0054
type: decision
level: concrete
title_ko: 추론은 OWL 2 RL 프로파일로 제한한다
title: Restrict reasoning to the OWL 2 RL profile
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 허용 추론을 OWL 2 RL로 정한다. 규칙 기반이고 다항 시간이며
`part-of` 이행성과 `subPropertyOf` 전파를 얻는다. 검사 게이트(6.7절)와
무효화 전파(6.5절)는 RL 프로파일 안에서 동작해야 하고, 그 밖의 추론은
배치로 돌린다.

**근거** (노트 2.9절)
- 어떤 추론을 허용할지 정해야 검사와 질의의 비용이 예측된다. 비용이
  예측되지 않으면 실시간 게이트를 설계할 수 없다.
- `defect-rules`와 같은 엔진을 쓴다 — 규칙 실행 경로가 하나로 유지된다.

**대안**
- OWL 2 DL 전체 — 표현력이 최대이고 결정 가능하나 느리다. 실시간 검사
  게이트에 부적합해 미채택.
- OWL 2 EL — 큰 분류 계층에 최적이므로 온톨로지 위생 검사(2.5절)에만 쓴다.
