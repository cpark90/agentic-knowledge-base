---
id: https://agentic-knowledge-base.dev/id/chunk/cb8f9e96-f81a-4f66-bf73-31c0a8de3be2
type: decision
level: concrete
title_ko: 정책만으로는 후보가 늘면 답이 바뀌므로 선택 결과 자체를 고정해야 한다
title: A policy alone gives a different answer when candidates grow, so the selection itself must be pinned
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0178-lock-snapshot-reproducibility.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:56:58+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:56:58+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/ab3d3668-34d4-43a1-b5d2-220cdbd6ca30
---
**근거** — 출처는 harness-concrete `docs/odr-bind-lock.md`의 "The lock" 절이다.

- 명세와 정책만으로는 재현이 후보 집합의 불변성에 기댄다. 후보가 하나 추가되면 같은 정책이 다른 답을 내므로, 시간이 지나도 같은 산출을 얻으려면 정책이 아니라 **선택 결과 자체**를 고정해야 한다.
- 스냅샷은 명세 정체성인 대상 식별자와 개체 수, 항목별로 선택된 후보와 그 참조, 버전, 태그, 적용된 정책, 복사된 내용의 해시값을 고정한다.
- 스냅샷 자체도 결정론적이어야 한다. 타임스탬프를 넣지 않고 키를 정렬해야 스냅샷을 포함한 산출물 전체가 바이트 동일해진다.
- 소비할 때는 세 검사를 모두 통과해야 한다. 명세 정체성이 일치해야 하고, 고정된 후보가 같은 참조로 여전히 존재해야 하며, 복사 후 다시 계산한 해시값이 일치해야 한다. 그래서 재현은 정확히 되거나 거부되거나 둘 뿐이고 중간이 없다.
- **lock은 검증을 완화하지 않는다.** 사전 검증 게이트는 lock의 유무와 무관하게 돈다. lock은 무엇을 골랐는가만 고정하고 그것이 옳은가를 대신하지 않는다.
- lock으로 재현했다는 사실은 스냅샷 필드에 적지 않고 **빌드 보고**에 적는다. 스냅샷을 고쳐 쓰면 재현된 산출이 원본과 달라져 바이트 동일성이 깨지기 때문이다. 재현 여부는 산출물의 속성이 아니라 실행의 속성이다.

이 결정은 재현 가능한 시나리오에 초기 상태와 자극 열, seed, 환경 버전을 기록하는 규칙(`p8-reproducibility`)의 생성 경로판이다.
