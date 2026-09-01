---
iri: https://agentic-knowledge-base.dev/id/chunk-d0042
plane: decision
level: concrete
label_ko: 부분관측 모델에 개념을 대응시킨다
label_en: Map concepts onto the partial-observability model
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — "에이전트는 **부분관측 분산 시스템의 행위자**"라는 전제를
형식화하고, 그 모델의 요소마다 이 체계의 개념을 하나씩 대응시켜 각 개념의
자리를 정한다.

| 부분관측 모델의 요소 | 이 체계 |
|---|---|
| 상태 | scene — 전체 시스템 상태 |
| 관측 함수 | 스코프 — scene에서 situation을 만드는 사상 |
| 관측 | situation |
| 행동 | 편집 연산. 링크의 부산물을 남김 (8.3절) |
| 신념 상태 | 에이전트의 `memory` plane |

**근거** (노트 1.6절)
- 이 대응이 있어야 **"이 에이전트가 왜 그 판단을 했는가"를 관측(situation)과
  신념(memory)으로 재구성할 수 있다.** 10.3절 인지능력 측정의 근거다.
- 스코프를 관측 함수로 두면 누락의 책임이 갈라진다 — scene 대비 누락은
  스코프 설계 문제, situation 대비 누락은 에이전트의 문제다(0.5절).
- 행동을 편집 연산으로 두면 행동의 흔적이 링크로 남아, 관측·신념·행동의
  세 요소가 모두 그래프 위에 기록된다.
