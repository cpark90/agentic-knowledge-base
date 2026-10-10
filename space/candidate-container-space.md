---
id: https://agentic-knowledge-base.dev/id/chunk/2337ea47-5c1e-403f-9abe-c5d6f720cd55
type: agt:Space
level: logical
title_ko: 결정 plane이 후보 결정과 확정 결정을 가르는가
title: Whether the decision plane separates candidate decisions from settled ones
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 설계 공간은 union 밖이고 그 후보 결정은 union 안의 결정 plane에 있다. 결정 plane은 확정 결정과 아직 고르지 않은 후보를 그릇으로 가르지 못한다. 지표는 열린 공간의 후보 결정을 따로 센다(Q60-a). 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). 결정 `p9-candidate-storage`의 결론에서 후보 결정의 자리를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 후보 링크는 `-space` 청크에 살고 deps가 되지 않으며 확정은 head로 옮겨진다(`p9-candidate-storage`). 선택지마다 후보 청크를 두고 후보는 draft 결정 복합체이며 그 결론은 head에 `refines`를 두지 않는다(Q55-a). 지표는 열린 공간의 open 후보 결정을 결정 완결률의 분모·분자에서 빼고 따로 센다(Q60-a). 두 답의 문장은 후보 결정과 확정 결정을 그릇으로 가르는지를 적지 않는다.

현재 상태(2026-10-09 실측, 이 공간 여섯을 더하기 전) — union 그래프는 `kb_lib.UNION_GRAPH_PATHS`의 일곱 파일과 온톨로지 모듈이고 `space/design-space.ttl`은 거기 없다. 설계 공간은 13개(open 10)이고 열린 공간의 후보 결정은 28개다(`bazel build //kg:open`의 요약, `//kg:metrics`의 구체화 줄). 후보 결정은 status `draft`이고 확정 결정과 같은 `kb/dev/decision/` 아래에 있다.

답이 가르는 것 — 결정 plane의 항목이 확정 결정인지 아직 고르지 않은 후보인지를 그릇만으로 판단할 수 있는지가 갈린다.

선택지 — A는 후보 결정을 결정 plane의 draft 결정 복합체로 두고 지표가 따로 세는 현행 유지안이다(`p9-candidates-in-decision-plane`). B는 후보 결정을 확정 결정과 다른 그릇에 두는 안이다(`p9-candidates-outside-decision-plane`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/7c9d74e6-1a77-4d52-a126-644a65bfab93
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/c1354a5b-cf02-4b9f-9376-65d3b6c89a7e
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/95b9afa8-18df-42c4-b2ea-8028744b2153
    state: open
```
