---
id: https://agentic-knowledge-base.dev/id/chunk/6a2c53a6-5833-4a8c-a773-f1d0bee785cc
type: agt:Space
level: logical
title_ko: contract·schema의 logical 칸에 독립 내용이 있는가
title: Whether the logical cells of contract and schema hold content of their own
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 시그니처(`contract`)와 구현(`artifact`)은 현재 관행에서 후보 공간을 남기지 않고 곧바로 확정된다. 이 plane들의 logical 칸, 즉 도메인과 제약으로 이루어진 선택지 공간에 무엇이 들어가는가. `decision`의 logical을 다른 각도에서 본 것에 불과한가, 아니면 시그니처 후보 집합·알고리즘 후보 집합 같은 독립 내용이 있는가. 수준 허용표가 `artifact`를 concrete·executable 전용으로 정한 뒤 열린 칸은 `contract`·`schema`의 logical이다(`p6-plane-level-occupancy`의 미확정). 후보 셋의 `artifact` 몫은 이 표로 해소됐다. 요구 `r-018`에서 이 칸의 지위를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — `contract`는 abstract·logical(타입 범위·계약 조건·판정식), `schema`는 logical·concrete, `artifact`는 concrete·executable에 거주하고 그 근거 청크는 `contract`·`schema`의 logical 칸을 이 표의 시험대로 둔다(`p6-plane-level-occupancy`). logical은 근거의 보존소다(`p9-candidate-storage`). logical의 파일 형식은 설계 공간 파일이다(`p9-design-space-file`). 뷰는 저장하지 않고 질의로 조립하므로(`p4-projection-as-query`) 이 칸이 뷰라면 파일을 만들지 않는다. 계약 logical(사전·사후조건)이 V&V 합격 기준의 직접 재료다(`p7-contract-first`). 인터페이스가 추적성의 기준축이다(Q3, 2026-09-03). 이는 `contract`가 매트릭스의 행 키가 된다는 뜻이라 독립 내용 쪽에 무게를 싣는다.

현재 상태(2026-10-05 실측) — 개발 KB의 `contract`·`schema` 청크는 0개이고 `artifact` 952개는 전부 소스에서 추출한 executable이다. 살아 있는 `contract` 43개는 전부 V&V KB의 합격 기준이고 `schema` 16개는 V&V KB의 케이스다. 설계 공간 파일의 후보는 전부 `decision` 청크다. TIM 허용 칸 15개 중 빈 둘은 `contract`·`schema`·`artifact` 항목이 생겨야 찬다. 개발 KB의 계약 logical을 실물로 검증할 수는 아직 없다.

답이 가르는 것 — 설계 공간 파일을 plane마다 두는지 `decision`에만 두는지가 갈린다. 설계 논증의 형식화(`https://agentic-knowledge-base.dev/id/chunk/882a087b-9a35-42e5-9017-84b6f417a235`)와도 맞물린다. 그쪽이 부정이면 `decision`의 logical이 얇아져 이 질문이 독립 내용 쪽으로 기운다.

선택지 — A는 뷰로 두고 파일을 만들지 않는 안이다(`p6-contract-logical-is-view`). B는 독립 내용으로 두는 안이다(`p6-contract-logical-is-content`). 시그니처 후보·구현 후보를 각 plane의 설계 공간 파일로 두고 `decision`의 후보와 `refines`로 잇는다. `p6-plane-level-occupancy`·`p7-contract-first`가 계약 logical의 내용을 일부 정했으나 앞 결정의 미확정이 이 질문이라 B의 확정으로 들지 않는다. C는 함수 하나의 시그니처 후보 공간을 두 방식으로 써 보고 정하는 안이다(`p6-contract-logical-by-experiment`). 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/1ac89243-1c3f-4814-8e13-79a5e507ab0b
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/c8069fb9-f2fe-4df9-b34f-c4b8e571b14e
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/5b404a5b-f164-4fda-b7a6-9d43bea03825
    state: open
```
