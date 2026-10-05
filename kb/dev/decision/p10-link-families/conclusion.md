---
id: https://agentic-knowledge-base.dev/id/chunk/05a91d58-53ec-4f3f-92e3-4587bded13f7
type: decision
level: concrete
title_ko: 링크 타입은 참조·의미 의존·관련성 세 족과 구성 관계로 정렬하고 전파는 족 단위로 정한다
title: Link types are arranged into three families, references, semantic dependence and relatedness, plus composition, and propagation is set per family
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3
composite: {id: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3, title_ko: 링크의 세 족과 구성 관계, title: Three link families and composition}
---
**결론** — 링크 타입은 세 족과 구성 관계로 정렬한다(`kb/ontology/related/trace/`). 세 족은 추상 상위 `agt:dependsOn` 아래의 상위 속성이고, 잎은 `rdfs:subPropertyOf`로 족에 속한다. 구성 관계는 링크 족이 아니다.

| 족 | 뜻 | 잎 | 전파 |
|---|---|---|---|
| `agt:references` | 본문이 식별자로 가리킴 | `cites` · `targets` · `usesDefinition` | 대상 변경 → 출발점 `suspect` |
| `agt:semanticallyDependsOn` | 빼면 의미상 불완전 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 같음. plane 단방향 안에서만 |
| `agt:relatedTo` | 앞의 두 족에 들지 않는 관련성 | `coUpdatesWith` · `conflictsWith` · `overlapsWith` | 대칭. 양쪽 `suspect` |
| (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체 `suspect` |

- `agt:dependsOn`은 직접 쓰지 않는다.
- `supersedes`·`prov:wasRevisionOf`는 시간축이라 족 밖이다.
- 표준 정렬은 `agt:references ⊑ dcterms:references`와 `agt:relatedTo ⊑ skos:related`다.
- 새 관계는 세 족 가운데 하나의 잎으로만 더하고 족을 새로 만들지 않는다(유저 승인 2026-09-23).
