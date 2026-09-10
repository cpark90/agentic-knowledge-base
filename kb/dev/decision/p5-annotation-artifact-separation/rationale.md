---
id: https://agentic-knowledge-base.dev/id/chunk/739b97cd-add4-472e-a7b1-98950800b545
type: decision
level: logical
title_ko: 인라인 주석은 저장 수준에서 plane 분리를 불가능하게 만든다
title: Inline annotation makes plane separation impossible at the storage level
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/67157f22-93ba-4abe-a303-d058de25ef7f
---
**근거** (노트 5.1절, 4.6절)

- plane 분리의 목적은 판정 방식이 다른 지식을 한 컨텍스트에 섞지 않는 것인데,
  **인라인 주석은 저장 수준에서 그것을 불가능하게 만든다** — 산출물을 읽으면
  주석이 따라온다. 규약으로는 막히지 않으므로 도구가 필요하다.
- 변경률이 가장 다른 두 plane이 같은 파일에 있으면(주석 매우 높음, 산출물
  빠름) 5.2절 단방향 영향 규칙도 확인할 수 없다.
- 분리해 두면 합치는 일은 4.6절 weave 질의가 한다 — 분리의 비용이 없다.
