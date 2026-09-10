---
id: https://agentic-knowledge-base.dev/id/chunk/e0c54da4-5d6f-43cf-b6c9-094548333c74
type: decision
level: concrete
title_ko: 시나리오는 부류에서 시작하는 V&V decision 복합체이고 concrete는 사람이 쓰지 않는다
title: A scenario is a V&V decision composite that starts from a class; concrete cases are never hand-written
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/791e4e4c-db54-45f9-a03b-8922cd7cc3af, title_ko: 시나리오 저작, title: Scenario authoring}
part_of: https://agentic-knowledge-base.dev/id/composite/791e4e4c-db54-45f9-a03b-8922cd7cc3af
---
**결론** — 시나리오는 `decision`(vv) 복합체다. 결론·근거·대안이 각각 **자극**(actor·action·순서·`keep()`)·**요인**(노출하려는 결함 요인, 기여하는 검증 목표)·**배제 자극**(다루지 않기로 한 자극과 이유 — ODD 밖, 다른 시나리오가 덮음)이다 (노트 8.22절).

**시나리오 부류에서 시작한다.** 위험 분석 G5의 abstract 라이브러리에서 부류를 고르고, 프로젝트의 ODD 속성으로 변수를 채우고, 계약의 사후조건으로 기준을 만든다. 저작 순서는 abstract → logical → concrete이되 **concrete는 사람이 쓰지 않는다** — 논리 시나리오의 `keep(범위)`와 `cover()`에서 생성기가 만든다.
