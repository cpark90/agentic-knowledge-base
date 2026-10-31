---
id: https://agentic-knowledge-base.dev/id/chunk/2337ea47-5c1e-403f-9abe-c5d6f720cd55
type: agt:Space
level: logical
title_ko: 결정 지식 종류가 후보 결정과 확정 결정을 가르는가
former_title_ko: ["결정 plane이 후보 결정과 확정 결정을 가르는가"]
title: Whether the decision plane separates candidate decisions from settled ones
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 설계 공간은 union 밖이고 그 후보 결정은 union 안의 결정 지식 종류에 있다. 결정 지식 종류는 확정 결정과 아직 고르지 않은 후보를 그릇으로 가르지 못한다. 지표는 열린 공간의 후보 결정을 따로 센다(Q60-a). 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). abstract 결정 `p9-candidate-place-variable`(결정 변수 선언)에서 후보 결정의 자리를 정하는 결정으로 가는 `refines`가 변수다. 처음 출발은 `p9-candidate-storage` 결론이었으나 concrete라 확정 후보가 head 링크를 가질 수 없어 옮겼다(Q93-c).

이미 정해진 것 — 후보 링크는 설계 공간(`-space`)에 살고 deps가 되지 않으며 확정은 head로 옮겨진다(`p9-candidate-storage`). 선택지마다 후보 단위 지식을 두고 후보는 draft 결정 기록이며 그 결론은 head에 `refines`를 두지 않는다(Q55-a). 지표는 열린 공간의 open 후보 결정을 결정 완결률의 분모·분자에서 빼고 따로 센다(Q60-a). 두 답의 문장은 후보 결정과 확정 결정을 그릇으로 가르는지를 적지 않는다.

현재 상태(2026-10-15 측정) — 설계 공간은 20개(open 16)이고 열린 공간의 후보 결정은 37개다. 결정 결론은 stable concrete 246 · draft logical 39 · draft concrete 6 · deprecated concrete 7 · stable logical 1이었다. draft logical 39가 정확히 공간의 후보였다(열린 공간 37 · 해소된 공간의 배제 2).

답이 가르는 것 — 결정 지식 종류의 항목이 확정 결정인지 아직 고르지 않은 후보인지를 그릇만으로 판단할 수 있는지가 갈린다.

선택지 — A는 후보 결정을 결정 지식 종류의 draft 결정 기록으로 두고 지표가 따로 세는 현행 유지안이다(`p9-candidates-in-decision-plane`). B는 후보 결정을 확정 결정과 다른 그릇에 두는 안이다(`p9-candidates-outside-decision-plane`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세웠다.

해소 — 유저가 질문지 `Q-0043`의 Q85에서 A를 골랐다(Q85-a). 그릇이 아니라 결론의 수준과 status가 후보와 확정을 가른다. 후보는 logical 결론이고 확정은 concrete로 옮기며 배제는 deprecated로 남긴다. B는 그릇을 정하지 않았고 후보 복합체 117파일의 이동을 요구해 배제됐다. 이 이산 구분은 확정 지식 베이스의 표현이고, 지식 베이스의 확률화(Q87-b)가 정해지면 다시 본다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/0aba0e96-bb4f-47a2-96d5-208a406f3d31
  kind: refines
status: resolved
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/c1354a5b-cf02-4b9f-9376-65d3b6c89a7e
    state: confirmed
    evidence: [{kind: userDecision, ref: Q-0043#Q85}]
  - to: https://agentic-knowledge-base.dev/id/chunk/95b9afa8-18df-42c4-b2ea-8028744b2153
    state: eliminated
    eliminated_by: {kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/ca5b814a-2546-44c3-ae9f-b8ec1feff1b6}
```
