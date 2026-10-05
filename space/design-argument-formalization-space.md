---
id: https://agentic-knowledge-base.dev/id/chunk/882a087b-9a35-42e5-9017-84b6f417a235
type: agt:Space
level: logical
title_ko: 설계 논증을 형식화할 수 있는가
title: Whether design arguments can be formalized
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 계층의 functional → abstract 전이는 자연어를 형식 언어로 옮기는 단계이고 abstract는 기계가독의 경계다. `decision`의 내용은 결론·근거·대안으로 이루어진 논증인데, 논증을 형식 언어로 옮길 수 있는가. 옮길 수 없다면 `decision`은 functional에서 곧바로 concrete로 가는 plane이 되어 계층의 예외가 된다. 형식 언어의 어휘는 온톨로지에서 오므로 요구 `r-017`(어휘 밖 지식은 거부한다)에서 이 형식화 여부를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 형식 언어는 abstract 단계의 언어이며 온톨로지 개념을 키워드로 쓰는 표기이고 따로 설계하지 않는다(`p6-formal-language-reproducibility`). `decision`의 판정 방식은 논증의 타당성이고(`p5-plane-by-verification`) 기계가 판정하지 못하므로 유저 승인이 stable 전이의 조건이다(`p5-verification-tools-per-plane`). 설계가 이미 이 plane의 형식화 한계를 인정한다. 결정은 abstract·logical·concrete 세 수준에 걸치고 abstract 변수 청크는 설계 공간이 있는 결정에만 만든다(`p7-decision-spans-three-levels`). 결정은 결론·근거·대안 세 청크의 복합체이고(`p7-alternatives-mandatory`) 결정의 abstract 표기는 변수 선언 YAML과 결론·근거·대안이다(`pe-notation-and-cel`).

현재 상태(2026-10-05 실측) — 개발 KB의 살아 있는 결정 청크는 899개(logical 513 · concrete 386)이고 abstract는 0개다. 본문은 산문이다. abstract `decision` 청크 16개는 전부 V&V KB의 시나리오다. 설계 공간 파일이 변수를 출발 항목과 링크 타입의 쌍으로 YAML에 선언하나 그 파일의 level은 logical이다. 저장소는 사실상 이 질문을 부정한 상태로 운영되고 있으나 그것은 판단이 아니라 미착수의 결과다.

답이 가르는 것 — 긍정이면 결정마다 abstract 형식이 별도 항목으로 생기고 `refines` 연쇄가 functional까지 닿는다. 부정이면 `decision`은 계층의 예외로 명시되고 contract·artifact의 logical(`https://agentic-knowledge-base.dev/id/chunk/6a2c53a6-5833-4a8c-a773-f1d0bee785cc`)이 `decision`의 뷰일 수 없게 된다.

선택지 — A는 구조만 형식화하는 안이다(`p7-argument-structure-formalized`). 내용은 산문으로 두되 결론·근거·대안·기각 사유·대안 간 관계의 구조를 역할 태그와 링크 타입으로 형식화하고 abstract는 이 결정이 고정하는 변수와 값 한 줄로 제한한다. 결정 복합체와 설계 공간의 변수가 이 구조의 일부를 이미 갖추었으나 `p7-decision-spans-three-levels`의 미확정이 바로 이 질문이라 확정으로 들지 않는다. B는 논증 온톨로지 도입이다(`p7-argument-ontology`). 표준 논증 어휘로 근거·반박·전제를 개체화한다. 표준어 원칙에 맞으나 비용이 크고 청크 상한과 충돌할 위험이 있다. C는 부정으로 확정하는 안이다(`p7-decision-is-level-exception`). `decision`은 계층 예외이고 옛 격자 결정(현행 `p6-plane-level-occupancy`가 대체)의 대안절을 결정으로 승격한다. 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/5ab37f16-4f00-4a3d-b770-508facc9ebfd
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/28278772-f8a3-4a4d-ae05-c27c86f23330
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/afd80fc9-16e2-4837-be0e-5646fd427a2e
    state: open
```
