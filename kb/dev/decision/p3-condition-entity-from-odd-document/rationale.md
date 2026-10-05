---
id: https://agentic-knowledge-base.dev/id/chunk/b32f99c3-94f6-4ac0-b812-13189f5919d9
type: decision
level: logical
title_ko: 등록은 스코프·가정의 참조 검사가 기대는 자리이고 제외의 기록은 같은 검토의 반복을 막는다
title: Registration is what the scope and assumption reference checks rely on, and recording exclusions prevents repeating a review
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a42db8cd-3f7e-443f-bb88-61ac79945d82
---
**근거** — 등록이 필요한 까닭은 참조 검사가 ODD의 조건 목록에 기대기 때문이다. ODD에 없는 속성을 참조하는 스코프나 가정은 존재할 수 없다(`p0-odd-scope-assumption`). 게이트 `odd-ref`는 `agt:refersTo`의 대상이 ODD 그래프에 있는지 본다. 게이트 `catalog`는 스코프의 include/exclude 조건이 ODD의 `agt:hasCondition`에 등록돼 있는지 본다(2026-09-26 지표에서 게이트로 승격).

명시 제외의 서식은 노트 3.2절의 예시(`reviewed 2026-08, 이유: …`)를 따른다. 3.2절은 제외를 적는 이유도 적는다. "적지 않은 것"과 "검토한 뒤 제외한 것"은 다르고, 후자를 기록하지 않으면 다음 검토자가 같은 검토를 반복한다(`p3-odd-required-sections`).

손 저작이 TTL에서 OpenODD YAML로 옮겨진 것은 2026-09-10이다(`pe-odd-is-openodd`). 그 뒤 등록과 제외 문자열은 생성기가 낸다. 생성이 곧 검사다. 속성에 `ATTRIBUTES`(IRI·라벨)나 `CHECKS`(방법·등급)가 없으면 `odd2kg`가 FAIL을 낸다.

미확정: 조건 IRI의 `cond-` 접두를 정한 이유의 기록이 없다. 이 접두를 판정하는 검사도 없다. `odd2kg`는 `iri` 값의 꼴을 보지 않는다(2026-10-03 실측).
