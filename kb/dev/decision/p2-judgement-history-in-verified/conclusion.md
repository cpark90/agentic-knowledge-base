---
id: https://agentic-knowledge-base.dev/id/chunk/4ec4de00-ea81-4ed0-abf7-40beedc25e38
type: decision
level: concrete
title_ko: 판정 이력은 OKF verified 목록에 누적된다
title: Judgement history accumulates in the OKF verified list
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d]
part_of: https://agentic-knowledge-base.dev/id/composite/eec68e02-3a0a-459a-9357-0c6cb85e8267
composite: {id: https://agentic-knowledge-base.dev/id/composite/eec68e02-3a0a-459a-9357-0c6cb85e8267, title_ko: 판정 이력의 누적, title: Accumulating judgement history}
---
**결론** — 검사 게이트·학습된 판정자·유저 승인의 결과를 **일회 필터로 버리지 않고 단위 지식 head에 남긴다.** 판정자 출력을 수명주기 메타데이터로 붙여 검색·충돌 해소·요약·보관에 재사용한다.

**판정 이력은 OKF `verified` 목록에 누적된다.** 노트가 `trust` 필드라고 부른 것은 OKF의 `verified` 목록과 같은 것이므로, 그것을 위한 필드를 새로 만들지 않는다 — 판정 하나가 `verified` 목록의 항목 하나로 붙는다.

같은 단위 지식이 재검증될 때 이전 판정과의 차이가 드러나고, 이것이 **판정자 자체의 드리프트**(7.14절 캘리브레이션)를 측정하는 재료가 된다.

**게이트** `writer`(실행 계층 human, 노트 5.4절·2.5절·8.14절 승인) — 사람의 승인이 판정하는 것은 `requirement`·`decision`의 `stable` 전이, 온톨로지 확장, 학습 판정자의 결과다. 승인은 `verified` 목록과 질문지의 `status: answered`로 기록된다. 2026-09-11의 라벨 재검증에서 사람 검토 10건을 측정했다. 해소는 쓰기 권한 역할(orchestrator·vnv)이 검토를 마친 뒤 `endorse`로 `verified`를 붙이는 것이다.
