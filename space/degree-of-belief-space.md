---
id: https://agentic-knowledge-base.dev/id/chunk/49f146e6-b3fa-43b2-aaa7-501d9978a697
type: agt:Space
level: logical
title_ko: 믿음 정도를 어떻게 계산하고 보정하는가
title: How degrees of belief are computed and calibrated
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:09:19+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 링크와 결정 후보는 증거에서 계산한 믿음 정도를 가질 수 있어야 한다(요구 `r-032`). 그 값을 무엇에서 어떻게 계산하고 무엇으로 보정하는가. 요구 `r-032`에서 계산 규칙을 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 믿음 정도는 병기하며 상태 전이와 확정·배제 판정에 들지 않는다(`p9-evidence-ledger-with-belief`, `p9-feasible-set-for-settlement`, Q90-a). 증거 기록 결정의 근거가 말하는 "선호를 돕는다"는 개정된 `p9-preference-partial-order`를 가리키며, 믿음 정도는 부분순서에서 순서가 없는 두 후보의 동률을 언어모델의 제안보다 먼저 깬다(Q109-b). 확률이 표현하는 것은 링크의 믿음 정도와 결정 후보의 선택 확률이다(Q88-a·b). 선행 조건 셋을 지시로 수행한다: 반박 증거 경로, 사람 정답 라벨 표본(구간 하한 20), 동시 편집·공동 커버 증거(Q91).

현재 상태(2026-10-22 측정) — 증거 1,229건 가운데 반박은 6건이고 모두 설계 공간의 배제 근거다. 동시 편집·공동 커버·임베딩·세션 읽음 증거는 0이다. 사람 정답 라벨은 10건이고 20건 표본을 준비하고 있다. V&V 실행 기록의 fail은 옛 테스트 케이스 이름이라 지금 링크로 내려오지 않는다.

답이 가르는 것 — 값이 확률로 해석되는지, 지금 계산할 수 있는지, 어느 선행 조건을 기다리는지가 갈린다.

선택지 — A는 증거 종류 서열 가중 점수다(`p9-belief-by-evidence-kind-rank`). 지금 계산할 수 있으나 보정되지 않는다. B는 극성 계수의 베타-이항 사후다(`p9-belief-by-beta-binomial`). 반박 증거를 기다린다. C는 사람 라벨로 보정한 판정자 확신도다(`p9-belief-by-calibrated-judge`). 사람 라벨 표본을 기다린다. 셋은 배타가 아니어서 한 후보를 확정하고 다른 것을 뒤에 더할 수도 있다. 세 후보 모두 열려 있다.

닫기 기준 — 세 기준을 모두 통과한 계산 규칙만 값을 병기한다(Q137-a, Q158-a). 둘 이상이 통과하면 Brier가 낮은 규칙을 고르고 나머지는 열어 둔다.

1. 계산 규칙은 사람 정답 라벨 표본(하한 20, Q-0047)에서 Brier 점수가 기저율 규칙의 Brier보다 낮아야 닫힌다. 기저율 규칙은 모든 후보에 표본의 참 비율을 내는 규칙이다.
1. 신뢰도 그림의 구간별 관측 빈도가 예측값의 허용폭 안에 들어야 한다. 표본이 50 미만이면 구간은 셋(0~0.33, 0.33~0.67, 0.67~1)이다. 허용폭은 그 구간 표본 수에서 계산한 95% 이항 신뢰구간이다.
1. S2의 일관성 게이트를 통과해야 한다. 그 게이트는 둘을 본다. 상태 전이 규칙은 믿음 정도를 읽지 않는다. 닫힌 계산 규칙이 없는 동안 병기 값은 선호의 동률 깨기에 쓰이지 않는다(Q137-a).

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/a0037ff5-559b-4f3b-894d-2bdef12e206c
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/8b6a4563-17d3-4c5c-a9a1-ea46f0babdbc
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/2dc8dfc7-565d-48c6-9f76-6b81afcd6eea
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/88b97e4d-57de-4ec9-8824-5decb2f9184f
    state: open
```
