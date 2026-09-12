---
id: https://agentic-knowledge-base.dev/id/chunk/3f1efd1b-f49d-4907-8f3f-849d1ffca59d
type: decision
level: concrete
title_ko: 외연은 ODD가 정하고 값은 범위를 벗어날 수 있다
title: The ODD fixes which properties exist; values may fall outside
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
part_of: https://agentic-knowledge-base.dev/id/composite/3d748edf-6a6d-49be-b2e5-8ec9c342d615
composite: {id: https://agentic-knowledge-base.dev/id/composite/3d748edf-6a6d-49be-b2e5-8ec9c342d615, title_ko: ODD가 관측의 외연을 정한다, title: The ODD fixes the extension of observation}
---
**결론** — ODD의 **선별 연산이 곧 이 프로젝트의 대상 영역**을 정하는 일이고, 그것이 지식 베이스와 관측의 외연이 된다 (0.5절).

- **ODD** — 대상 영역의 경계. 어떤 속성을 다루는가 + 설계된 값 범위
- **지식 베이스** — 그 영역의 현재 상태(리비전). 값은 ODD 범위 밖일 수 있다
- **작업 집합** — 지식 베이스를 스코프 × level 창으로 거른 질의 결과
- **실행 기록** — 검증·운영의 관측. append-only

**값이 범위 밖일 수 있다는 것이 핵심이다.** 관측되는 속성의 외연은 ODD가 정하되, 값은 ODD를 벗어날 수 있어야 3.5절 ODD 이탈이 감지된다.

**외연 자체를 벗어난 것 — ODD가 언급조차 하지 않는 조건 — 은 관측되지 않으므로 이탈해도 모른다.**
