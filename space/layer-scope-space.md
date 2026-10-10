---
id: https://agentic-knowledge-base.dev/id/chunk/026b98a6-6ef6-443d-934f-93e2bd54cc0f
type: agt:Space
level: logical
title_ko: 서비스 층이 청크 밖의 것에도 값을 주는가
title: Whether the service layer gives a value to things outside chunks
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 층 축(`agt:inLayer`)은 청크에만 값을 준다. ODD 조건, 손 시드의 가정(`kg/base-kg.ttl`), catalog의 역할·스코프, 온톨로지 모듈, 손 문서, 하네스는 층이 없다. 그래서 `p0-service-is-a-three-layer-wiki`의 "모든 것은 한 층의 항목이거나 투영이다"를 이들에 대해 판정할 수 없다. 같은 원인의 사례로 새 가정의 자리가 셋(base-kg · ODD · catalog 스코프)으로 갈린다. 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). 결정 `p0-service-is-a-three-layer-wiki`의 결론에서 층의 범위를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 저장소의 모든 것은 세 층 중 하나의 항목이거나 그 투영이다. 명시한 예외는 빌드 배선 하나다(Q10-a). 뷰·skill은 층을 갖지 않는 투영이다(Q9-a). 층은 plane과 직교하는 선택 키 `layer`이고 기본값은 `knowledge`다(`p0-service-is-a-three-layer-wiki`). "층"은 서비스 층의 단축형이다(Q69-a).

현재 상태(2026-10-09 실측) — `agt:inLayer`를 방출하는 도구는 `chunk2kg`·`gates2kg` 둘이다(`grep -l inLayer tools/*.py`, `kb_lib`는 술어의 정의처). 게이트 개체 57개도 층을 받는다(`gates-kg.ttl`). 층이 없는 것은 ODD 조건 9개, 손 시드 가정 5개, catalog의 역할 4 · 스코프 4 · 채널 3 · 하네스 1, 온톨로지 모듈 63개(`kb/ontology/**/*-ontology.ttl`), 손 문서, `harness/`의 파일이다. 개수는 각 그래프 파일의 `rdf:type` 개체 수다.

답이 가르는 것 — p0의 "모든 것은 한 층의 항목이거나 투영이다"를 청크 밖의 것에 대해 판정할 수 있는지가 갈린다.

선택지 — A는 층을 청크와 게이트 개체에만 두는 현행 유지안이다(`p0-layer-stays-on-chunks`). B는 청크 밖의 것에도 층을 주는 안이다(`p0-layer-extends-beyond-chunks`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/ec094e42-1b17-45ac-805e-064317912ac6
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/a57ebc46-86e6-4111-949a-c3929298390c
    state: open
```
