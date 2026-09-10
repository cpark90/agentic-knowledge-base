---
id: https://agentic-knowledge-base.dev/id/chunk/40abcad5-6a9c-4233-99d3-0b7ceeafb06b
type: decision
level: concrete
title_ko: ODD에 없는 속성을 참조하는 파생물은 게이트가 거부한다
title: The gate rejects derivations that reference properties absent from the ODD
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0008]
part_of: https://agentic-knowledge-base.dev/id/composite/87eb4cc9-8cf0-4461-a9af-24945dccda21
composite: {id: https://agentic-knowledge-base.dev/id/composite/87eb4cc9-8cf0-4461-a9af-24945dccda21, title_ko: ODD에서 파생되는 것, title: What derives from the ODD}
---
**결론** — ODD가 기반인 이유는 아래 전부가 ODD를 참조하기 때문이다.

| 파생물 | 관계 |
|---|---|
| 스코프 | ODD 속성의 부분집합 + plane 권한 |
| 가정 | 각 가정은 ODD 속성 위의 명제 |
| 시나리오 (V&V KB) | 시나리오 변수는 ODD 속성, 케이스 값은 그 범위의 표본 |
| 설계 공간 | 도메인 전개(6.2절)는 ODD 값 범위 안에서 |
| 커버리지 | 분모가 ODD다 (Part VIII) |
| 하네스 | 하네스가 부여하는 스코프는 ODD의 부분집합 |

**파생물이 ODD에 없는 속성을 참조하면 검사 게이트가 거부한다.** 대응은 둘 중 하나 — **ODD를 확장하거나(3.6절), 파생물을 기각한다. 세 번째 선택지(그냥 통과)는 없다.**
