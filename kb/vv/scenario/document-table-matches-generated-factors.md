---
id: https://agentic-knowledge-base.dev/id/chunk/c4972f95-7e4e-43f6-b1fa-45426d0ca688
type: decision
level: abstract
title_ko: 시나리오 요인 — 생성물의 수치가 바뀌고 문서의 표가 그대로인 편집이 노출하는 현상
title: Scenario factors — the phenomena exposed by an edit that changes the generated numbers and leaves the document table
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/documentLag, https://agentic-knowledge-base.dev/agt/metricVariesByLoadingOption]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/d71fb313-ed12-47c0-87f8-3c79d7531adf
specializationOf: https://agentic-knowledge-base.dev/id/chunk/31b9d3b9-577d-486a-8792-1146783508ae
---
**요인** — 노출하려는 현상은 `agt:documentLag`(P18)가 주이고 `agt:metricVariesByLoadingOption`(P21)이 부다. 문서가 어느 도구의 수치를 적었는지 쓰지 않으면 두 현상이 구분되지 않으므로 같은 자극이 둘을 함께 드러낸다.

주입하는 한정자는 `agt:incorrectQualifier` 하나다. 표가 빠진 것이 아니라 값이 낡은 것이 이 부류의 결함 형태다. 부류가 주입하는 것은 낡은 수치이고, 문서와 생성물의 어긋남이 검사로 드러나는가를 묻는다.

기여하는 검증 목표는 `kb/vv/goal/document-table-matches-generated.md`(`https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0`)다. 문서의 표가 생성물의 수치와 어긋나면 그 어긋남이 드러나는가를 이 부류가 자극한다.

미확정: 문서의 수치와 생성물의 수치를 대조하는 단위가 표 셀인지 줄인지 정해지지 않았다.
