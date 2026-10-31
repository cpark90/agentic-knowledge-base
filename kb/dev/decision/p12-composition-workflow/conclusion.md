---
id: https://agentic-knowledge-base.dev/id/chunk/00e1e7b4-42b3-40a3-8ac5-c0483a50ee05
type: decision
level: concrete
title_ko: 조립 워크플로는 뷰에서 검증까지 여섯 단계를 고정한다
title: The composition workflow fixes six steps from view to validation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0015-composition-workflow.md, id: https://agentic-knowledge-base.dev/id/chunk-d0015, title_ko: "조립 워크플로는 뷰에서 검증까지 여섯 단계를 고정한다", title: "The composition workflow fixes six steps from view to validation"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0015]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/16438f48-86f5-4fd8-a6b6-f971064cf38e
composite: {id: https://agentic-knowledge-base.dev/id/composite/16438f48-86f5-4fd8-a6b6-f971064cf38e, title_ko: 구성물 조립 워크플로, title: Composition workflow}
---
**결론** — 새 구성물(하네스)의 조립은 다음 고정된 절차를 따른다.

1. 요청으로 컨텍스트 팩을 뷰로 받는다.
1. 최상위 후보를 템플릿으로 삼는다.
1. 요구 capability마다 제공 컴포넌트를 바인딩해 결핍을 메운다.
1. 조립한다.
1. 출처(derivedFrom)와 성숙도(draft)를 함께 그래프에 기록한다.
1. 검증 게이트를 다시 돌린다.

새 노드도 고아와 drift를 막는 같은 불변식에 잡히므로, 그래프는 부패하는 대신 복리로 쌓인다.

다만 검증 통과가 곧 반영 완료는 아니다. 그래서 coverage-audit 게이트를 둔다. 원천의 구조 요소를 하나도 빠짐없이 열거해 각각을 표현에 매핑하는 감사가 통과해야 완료다. 모든 요소는 표현으로 매핑되거나, 모델 밖에 두는 명시적이고 수용 가능한 사유를 가져야 한다. 담을 어휘 범주 자체가 없으면 조용히 건너뛰지 않고 스키마 확장을 먼저 일으킨다. 그래프 정합성 게이트는 원천 충실도(source-fidelity)를 보지 않으므로 이 감사가 그 축을 맡는다.
