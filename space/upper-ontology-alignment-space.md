---
id: https://agentic-knowledge-base.dev/id/chunk/b2d479b1-790b-44e1-90e7-5f4dff66bff6
type: agt:Space
level: logical
title_ko: 상위 온톨로지의 continuant·occurrent 구분을 어떻게 적용하는가
title: How the continuant and occurrent split of the upper ontology is applied
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 표준 상위 온톨로지인 BFO는 세계를 continuant와 occurrent로 가른다. continuant는 시간을 관통해 존재하는 것으로 물체·정보 내용·역할이 여기 든다. occurrent는 시간 안에서 일어나는 것으로 과정·사건이 여기 든다. 이 체계의 개체들(청크·복합체·결정·링크·가정·scene·실행 기록·역할)이 각각 어느 쪽인지, 그 구분이 어휘·shape·질의에 무엇을 요구하는지가 변수다. 분류가 틀리면 나중에 전부 다시 봐야 한다. `part-of`가 continuant용과 occurrent용으로 갈리므로 링크 타입의 정의역·치역 공리가 그 위에 얹힌다. 요구 `r-001`(분야 지식을 어휘로 축적한다)에서 이 정렬 규칙으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 맨바닥에서 짓지 않고 표준 상위 온톨로지 위에 구축하며 후보는 BFO다(`p2-upper-ontology-foundation`). 개체는 여러 scene을 관통하는 endurant이고 정체성은 IRI, 상태 변화는 `prov:wasRevisionOf`다(`p2-temporal-identity`). 온톨로지는 정제 계층 전체가 쓰는 어휘다(`p2-ontology-as-vocabulary`). 상위 온톨로지 선택이 모든 plane에 걸린다.

현재 상태(2026-10-06 실측) — `upper` 모듈이 없다. 온톨로지 모듈은 `entity`·`profile`·`related` 아래에 있고 continuant·occurrent를 쓰는 온톨로지 파일은 0이다. `agt:KnowledgeItem` 정의문이 "상위 온톨로지 도입 시 `iao:InformationContentEntity` 아래로 정렬한다"고 예고만 하고, `agt:hasDirectPart`도 "표준 part-of의 하위 속성으로 정렬한다"고 예고한다. `tools/kb_lib.py`에 obo 접두어만 등록되어 있다. occurrent 쪽 개체는 이제 있다. `kb/vv/run/`의 실행 기록 9건과 시나리오 58개다.

답이 가르는 것 — traceability 링크 타입의 공리가 이 분류 위에 놓인다. 연결 단계 전에 정하면 한 번, 후에 정하면 링크 전체를 재검토한다.

선택지 — A는 BFO+IAO를 도입하고 있는 것만 정렬하는 안이다(`p2-upper-bfo-iao-align-existing`). BFO 채택은 `p2-upper-ontology-foundation`과 겹치지만 정렬 범위는 정해지지 않았다. B는 자체 최소 구분(`agt:Continuant`/`agt:Occurrent` 두 클래스)이고 표준어 우선 원칙과 충돌한다. `p2-upper-ontology-foundation`의 대안 청크가 상위 온톨로지 없이 프로젝트가 최상위 분류를 직접 정하는 안을 배제해 그 청크를 배제된 후보로 든다(Q64-a). C는 실행 기록이 생길 때까지 미루는 안이다(`p2-upper-alignment-deferred`). A와 C가 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/d4c5ee5f-7ef0-4530-bde4-f202e44565a8
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/531e36a2-1a74-4eed-935f-e8522896fc4d
    state: eliminated
    eliminated_by: {kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/531e36a2-1a74-4eed-935f-e8522896fc4d}
  - to: https://agentic-knowledge-base.dev/id/chunk/f44a431d-0d76-4b37-90f0-bf572ab5b567
    state: open
```
