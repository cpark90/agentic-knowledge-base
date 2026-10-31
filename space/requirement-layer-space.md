---
id: https://agentic-knowledge-base.dev/id/chunk/8bce3e5d-1317-4efb-ad64-95caded30c95
type: agt:Space
level: logical
title_ko: 요구에 서비스 층을 표시하는가
title: Whether requirements carry a service-layer mark
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:10:52+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 개발 요구에는 `layer:` 표시가 하나도 없다. `p0-service-is-a-three-layer-wiki`의 근거는 요구에도 방법론 역할이 있다고 적는다. 표시가 없는 요구는 기본값 `knowledge`로 방출된다. 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). abstract 결정 `p0-requirement-layer-variable`에서 요구의 층 표시를 정하는 결정으로 가는 `refines`가 변수다. 처음 출발은 `p0-service-is-a-three-layer-wiki`의 규약이었으나 concrete라 확정 후보가 head 링크를 가질 수 없어 옮겼다(Q-0055 Q112-b).

이미 정해진 것 — 선택 키 `layer: knowledge | methodology | process`는 항목이 서비스의 어느 층에서 역할을 갖는가다. 명시가 없으면 `chunk2kg`가 `knowledge`를 방출하고 방법론·프로세스는 명시한다(`p0-service-is-a-three-layer-wiki` 규약). 층은 지식 종류와 직교한다. 결정 지식 종류에 분야의 결정과 저작 규칙의 결정이 함께 있고 요구 지식 종류에도 같다고 그 근거가 적는다.

현재 상태(2026-10-09 측정) — 개발 요구 36건 중 `layer:` 표시는 0건이다. 측정은 `grep -l "^layer:" kb/dev/requirement/*.md | wc -l`(0)과 `ls kb/dev/requirement/*.md | wc -l`(36)이다.

답이 가르는 것 — 층별 집계(CQ-38)에서 요구가 모두 지식층으로 세어지는지가 갈린다.

선택지 — A는 요구를 표시 없이 기본값 지식층으로 두는 현행 유지안이다(`p0-requirement-layer-default-kept`). B는 방법론 역할을 가진 요구에 방법론층을 표시하는 안이다(`p0-requirement-layer-marked`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/729d224e-9907-4d61-9216-8c0777f4ef5a
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/2d466291-356d-471c-9f03-69292e253f15
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/0719350b-6157-43d1-aa66-87782072217d
    state: open
```
