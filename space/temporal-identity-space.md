---
id: https://agentic-knowledge-base.dev/id/chunk/dda51e76-7054-460b-ba4d-3bd4c14d4e6f
type: agt:Space
level: logical
title_ko: 리팩터링 시 개체가 새로 생기는 것을 무엇이 막는가
title: What prevents a refactoring from minting a new entity
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 설계는 "IRI가 지속하고 변화는 `wasRevisionOf`"라고 하지만 그것을 강제할 장치가 없다. 본문만 고쳤는데 새 항목으로 취급되는 과잉 신생과, 같은 지식인데 새 파일을 만드는 중복 신생을 무엇이 막는가, 그리고 버전 IRI를 쓸 것인가가 변수다. 결정 `p0-iri-design`(불투명 지속 IRI와 해시 버전 IRI)의 결론에서 이 강제 규칙으로 가는 `refines`가 열려 있다. 같은 미결의 다른 변수인 분할·병합의 IRI 기준은 공간 `https://agentic-knowledge-base.dev/id/chunk/6fec9aaa-ca14-42fe-98d4-64bc8d15dbe8`에서 해소됐다.

이미 정해진 것 — 개체는 endurant이고 정체성은 IRI이며 변화는 `prov:wasRevisionOf` 연쇄다(`p2-temporal-identity`). 불투명한 지속 IRI와 내용 해시인 버전 IRI를 함께 쓰고 본문이 같으면 해시가 같다(`p0-iri-design`). 삭제하지 않고 폐기한다. 폐기는 `owl:deprecated`와 대체 지정으로 한다(`p0-deprecate-not-delete`). 분할은 조각 하나가 uuid를 승계하고 병합은 한 uuid를 승계하며 개정은 uuid를 유지한다(`p10-split-keeps-work-identity`).

현재 상태(2026-10-06 실측) — 내용 해시는 head 그래프의 `agt:contentHash`로 있다. 버전 IRI(`<uuid>/<content-hash>`)는 쓰지 않고 `prov:wasRevisionOf` 트리플은 0이다. 중복 신생은 검색 우선 규약(`d-0160-search-before-authoring`)과 `consistency` 보고(라벨 중복·근사 중복 후보)가 다루고 둘 다 게이트가 아니다.

답이 가르는 것 — 두 위험이 갈린다. 첫째, 과잉 신생은 해시 버전 IRI가 막는다. 둘째, 중복 신생은 검색 우선 규약과 라벨 중복 검사가 막는다. 어느 쪽이 더 큰 위험인지 실측이 없다.

선택지 — A는 편집 프로토콜을 게이트로 두는 안이다(`p0-identity-edit-protocol-gate`). 새 파일은 `derived_from`이 필수이고 라벨 유사도가 높은 기존 항목이 있으면 경고하며 본문 변경은 같은 IRI와 해시 버전으로 표현한다. 개정의 uuid 유지는 `p10-split-keeps-work-identity`와 겹치지만 게이트와 해시 버전은 없다. B는 해시 유사도가 임계 이상이면 같은 개체로 자동 판정하는 안이고 산문에는 부정확하다(`p0-identity-hash-similarity-threshold`). C는 연결 단계 전까지 `STYLEGUIDE.md`의 `[지킴]`으로만 강제하는 안이다(`p0-identity-review-convention-only`). 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/d0f3d2b1-9533-40a4-acfb-12f318382f7d
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/b47be6bb-f489-45a3-b584-3449f91ac0a2
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/03e18b53-0aac-486d-8abc-9cfd0d563451
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/ffb0216d-8746-43bf-8da6-8df0f0a3e843
    state: open
```
