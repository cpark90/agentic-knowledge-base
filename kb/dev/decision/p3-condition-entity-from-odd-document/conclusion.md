---
id: https://agentic-knowledge-base.dev/id/chunk/54bdaa79-5ee8-4d4e-8653-6dc0d05d9a0f
type: decision
level: concrete
title_ko: 조건은 ODD 문서의 속성으로 저작하고 id:cond-<slug>로 ODD에 등록되며 명시 제외는 검토 시점과 이유를 갖는다
title: Conditions are authored as ODD document properties, registered on the ODD as id:cond-<slug>, and explicit exclusions carry a review date and a reason
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a42db8cd-3f7e-443f-bb88-61ac79945d82
composite: {id: https://agentic-knowledge-base.dev/id/composite/a42db8cd-3f7e-443f-bb88-61ac79945d82, title_ko: 조건 개체의 저작, title: Authoring condition entities}
---
**결론** — 조건은 OpenODD 문서 `kb/odd/project-odd.yml`의 속성으로 저작한다. ODD 그래프 `project-odd.ttl`은 `tools/odd2kg.py`가 생성한다(`pe-odd-is-openodd`).

| 규약 | 문서(손) | 그래프(생성) |
|---|---|---|
| 조건 IRI | `ATTRIBUTES`의 `iri`를 `id:cond-<slug>`로 적는다 | 조건 개체 `id:cond-<slug>` |
| 분류 | `TAXONOMY`의 범주 키 셋 중 하나 아래에 둔다 | `agt:StaticElement`·`agt:EnvironmentalCondition`·`agt:DynamicElement` 중 하나 |
| 등록 | `MODULES`의 식에 속성으로 쓴다 | ODD 개체의 `agt:hasCondition` 목록 |
| 명시 제외 | `EXCLUSIONS_REVIEWED`에 `concept`·`reviewed`(YYYY-MM)·`reason`을 적는다 | `agt:excludes` 문자열 `"<대상> — reviewed YYYY-MM, 이유: <근거>"` |

- **등록 없는 조건을 만들지 않는다.** 생성기는 `MODULES`에 쓰인 속성만 조건 개체로 내고 그 전부를 `agt:hasCondition`에 올린다.
- 분류 셋은 `p0-condition-taxonomy-extensible`이 정한다. 판정 방법과 등급은 같은 결정과 `p3-odd-required-sections`가 정한다.
