---
id: https://agentic-knowledge-base.dev/id/chunk/e09e5796-4a28-4f39-a886-2eb95c957f8a
type: decision
level: concrete
title_ko: 제약의 출처 셋과 공리·제약·가정의 구분
title: Three constraint sources; axiom, constraint and assumption are distinct
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249, https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0099]
part_of: https://agentic-knowledge-base.dev/id/composite/82fb12dd-6188-4e06-bae7-e86e699ac5fe
composite: {id: https://agentic-knowledge-base.dev/id/composite/82fb12dd-6188-4e06-bae7-e86e699ac5fe, title_ko: 제약의 출처 셋과 공리·제약·가정의 구분, title: Three constraint sources; axiom, constraint and assumption are distinct}
---
**결론** — 후보 링크를 깎는 **제약의 출처는 셋**이고, 각각 사는 곳이 정해져 있다.

| 출처 | 예 | 위치 |
|---|---|---|
| 온톨로지 공리 | `satisfies`의 정의역은 `contract`·`artifact`뿐 | `*-ontology`, `related/trace` |
| ODD | 외부 클라이언트가 있으므로 APIKey 링크 불가 | `project-odd` |
| 설계 공간의 국소 제약 | 이 모듈에서는 동기 방식만 | `*-space` |

**공리·제약·가정은 다르다.** 공리는 온톨로지 수준에서 항상 성립하는 논리(`*-ontology`·`*-rules`), 제약은 특정 설계 공간에서 후보 링크를 깎는 양립 조건(`*-space`·ODD), 가정은 **그 제약 자체가 성립하기 위한 전제**이고 `assumes` 링크로 적는다.
