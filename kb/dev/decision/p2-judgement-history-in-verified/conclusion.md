---
id: https://agentic-knowledge-base.dev/id/chunk/4ec4de00-ea81-4ed0-abf7-40beedc25e38
type: decision
level: concrete
title_ko: 판정 이력은 OKF verified 목록에 누적된다
title: Judgement history accumulates in the OKF verified list
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d]
part_of: https://agentic-knowledge-base.dev/id/composite/eec68e02-3a0a-459a-9357-0c6cb85e8267
composite: {id: https://agentic-knowledge-base.dev/id/composite/eec68e02-3a0a-459a-9357-0c6cb85e8267, title_ko: 판정 이력의 누적, title: Accumulating judgement history}
---
**결론** — 검사 게이트·학습된 판정자·유저 승인의 결과를 **일회 필터로 버리지 않고 청크 head에 남긴다.** 판정자 출력을 수명주기 메타데이터로 붙여 검색·충돌 해소·요약·보관에 재사용한다.

**판정 이력은 OKF `verified` 목록에 누적된다.** 노트가 `trust` 필드라고 부른 것은 OKF의 `verified` 목록과 같은 것이므로, 그것을 위한 필드를 새로 만들지 않는다 — 판정 하나가 `verified` 목록의 항목 하나로 붙는다.

같은 청크가 재판정될 때 이전 판정과의 차이가 드러나고, 이것이 **판정자 자체의 드리프트**(7.14절 캘리브레이션)를 측정하는 재료가 된다.
