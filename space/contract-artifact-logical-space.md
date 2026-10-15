---
id: https://agentic-knowledge-base.dev/id/chunk/6a2c53a6-5833-4a8c-a773-f1d0bee785cc
type: agt:Space
level: logical
title_ko: contract·schema의 logical 칸에 독립 내용이 있는가
title: Whether the logical cells of contract and schema hold content of their own
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-15T15:50:59+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 시그니처(`contract`)와 구현(`artifact`)은 관행상 후보 공간 없이 곧바로 확정된다. 그 logical 칸에 무엇이 들어가는가. `decision` logical의 뷰인가, 시그니처 후보 집합 같은 독립 내용인가. 수준 허용표가 `artifact`를 concrete·executable 전용으로 정해 열린 칸은 `contract`·`schema`의 logical이다(`p6-plane-level-occupancy`). 요구 `r-018`에서 이 칸의 지위를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — `contract`는 abstract·logical(타입 범위·계약 조건·판정식), `schema`는 logical·concrete, `artifact`는 concrete·executable에 거주하고 그 근거 청크는 `contract`·`schema`의 logical 칸을 이 표의 시험대로 둔다(`p6-plane-level-occupancy`). logical은 근거의 보존소이고(`p9-candidate-storage`) 파일 형식은 설계 공간 파일이다(`p9-design-space-file`). 계약 logical(사전·사후조건)이 V&V 합격 기준의 직접 재료다(`p7-contract-first`). 인터페이스가 추적성의 기준축이다(Q3, 2026-09-03).

현재 상태(2026-10-05 실측, 해소 전) — 개발 KB의 `contract`·`schema` 청크는 0개였다. `contract` 43개는 전부 V&V KB의 합격 기준이었고 TIM의 빈 칸 둘은 개발 KB 항목이 생겨야 찼다.

답이 가르는 것 — 설계 공간 파일을 plane마다 두는지 `decision`에만 두는지가 갈린다. 설계 논증의 형식화(`https://agentic-knowledge-base.dev/id/chunk/882a087b-9a35-42e5-9017-84b6f417a235`)와도 맞물린다.

선택지 — A는 뷰로 두고 파일을 만들지 않는 안이다(`p6-contract-logical-is-view`). B는 독립 내용으로 두는 안이다(`p6-contract-logical-is-content`). 시그니처 후보·형식 후보를 `contract`·`schema`의 logical 청크로 두고 `decision`을 `satisfies`로 가리킨다. C는 함수 하나의 시그니처 후보 공간을 두 방식으로 써 보고 정하는 안이다(`p6-contract-logical-by-experiment`).

해소 — 유저는 C를 확정 경로로 골랐고(Q78-a) 실험 결과로 B를 확정했다(Q79-a). `parse_chunk` 하나로 쓴 실험에서 질의 조립은 근거를 조립하지 못했고 contract 청크는 결정 logical과 근사 중복이 0쌍이었다. 수치는 관측 `https://agentic-knowledge-base.dev/id/chunk/d8371b0d-8f5d-425c-bf90-7ca89dcad611`에 있다. A는 그 두 수치로 배제하고, C는 실험을 마쳐 배제한다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4
  kind: refines
status: resolved
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/1ac89243-1c3f-4814-8e13-79a5e507ab0b
    state: eliminated
    eliminated_by: {kind: runResult, ref: https://agentic-knowledge-base.dev/id/chunk/d8371b0d-8f5d-425c-bf90-7ca89dcad611}
  - to: https://agentic-knowledge-base.dev/id/chunk/c8069fb9-f2fe-4df9-b34f-c4b8e571b14e
    state: confirmed
    evidence: [{kind: runResult, ref: https://agentic-knowledge-base.dev/id/chunk/d8371b0d-8f5d-425c-bf90-7ca89dcad611}]
  - to: https://agentic-knowledge-base.dev/id/chunk/5b404a5b-f164-4fda-b7a6-9d43bea03825
    state: eliminated
    eliminated_by: {kind: runResult, ref: https://agentic-knowledge-base.dev/id/chunk/d8371b0d-8f5d-425c-bf90-7ca89dcad611}
```
