---
id: https://agentic-knowledge-base.dev/id/chunk/31b9d3b9-577d-486a-8792-1146783508ae
type: decision
level: abstract
title_ko: 시나리오 자극 — 생성물의 수치가 바뀌고 문서의 표가 그대로인 편집
title: Scenario stimulus — an edit that changes the generated numbers and leaves the document table
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0]
part_of: https://agentic-knowledge-base.dev/id/composite/d71fb313-ed12-47c0-87f8-3c79d7531adf
composite: {id: https://agentic-knowledge-base.dev/id/composite/d71fb313-ed12-47c0-87f8-3c79d7531adf, title_ko: 생성물의 수치가 바뀌고 문서의 표가 그대로인 편집, title: An edit that changes the generated numbers and leaves the document table, ordered: [https://agentic-knowledge-base.dev/id/chunk/31b9d3b9-577d-486a-8792-1146783508ae, https://agentic-knowledge-base.dev/id/chunk/c4972f95-7e4e-43f6-b1fa-45426d0ca688, https://agentic-knowledge-base.dev/id/chunk/15d8c8e5-5bd9-44ba-ae32-7580a70fc20c]}
---
**자극** — 부류의 자극은 그래프를 고쳐 생성물의 수치를 바꾸고 그 수치를 인용한 문서의 표는 고치지 않은 채 게이트를 도는 것이다. actor는 그래프를 편집하는 에이전트이고 action은 생성물의 수치만 바꾸고 문서의 표는 그대로 두는 것이다. 순서는 그래프 편집 → 게이트 통과 → 문서 방치이고, `keep()`은 편집 뒤에도 유지되는 문서의 옛 표 값이다.

변수는 ODD 속성 둘이다. `id:cond-repo-layout`(저장소 구조 — `docs/`는 그래프 밖이다)이 검사 대상 여부를 가르고, `id:cond-build-system`(빌드 체계 — 생성물은 `bazel-out`에만 있다)이 대조의 기준이 되는 산출물을 가른다.
