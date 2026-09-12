---
from: hci
status: open
targets: [kb/dev/decision/p10-traceability-metrics/conclusion.md, kb/dev/decision/p10-standard-trace-queries/conclusion.md, kb/dev/decision/p8-vv-independence-scope/conclusion.md, kb/dev/decision/p6-gate-catalogue/conclusion.md, kb/dev/decision/p8-verification-and-validation/alternatives.md, kb/dev/decision/p8-mismatch-attribution/conclusion.md, kb/dev/decision/p8-vv-roles/rationale.md]
---

# 라벨 재판정 7건 — 재저작 뒤 (2026-09-12, 판정자 = hci 세션)

`agents/orchestrator-consistency-cleanup-2026-09-12.md` 전달 1: 라벨을 재저작하면서 이전 판정(`process:label-judge-20260911`)이
물러났다(trust-shapes: 검증 뒤 수정 금지). 프로토콜은 "재저작 후 같은 판정자로 재판정"이므로 같은 절차로 다시 판정한다 —
라벨만 보고 예측하고, 본문과 대조해 3점으로 판정한다.

| # | 파일 | 라벨(ko) | 예측 | 판정 | 확신도 |
|---|---|---|---|---|---|
| 1 | `p10-traceability-metrics/conclusion` | 추적성은 다섯 지표로 관측하고 지표마다 경고 신호를 정의한다 | 추적성 지표 5개와 각각이 무엇을 경고하는지 | **적합** | 0.95 |
| 2 | `p10-standard-trace-queries/conclusion` | 링크 모델은 영향 분석·커버리지·근거 추적·상태 집계 네 질의에 답해야 한다 | 링크 모델이 답해야 할 네 질의를 이름까지 | **적합** | 0.95 |
| 3 | `p8-vv-independence-scope/conclusion` | 두 KB는 서로 읽기만 허용하고 기준은 요구를 거쳐 고치며 저장도 분리한다 | 두 KB의 스코프 규칙 — 교차 읽기만, 기준은 요구 경유, 저장 분리 | **적합** | 0.95 |
| 4 | `p6-gate-catalogue/conclusion` | 게이트는 다섯 실행 계층에 배치되며 실패는 draft에 머물러 전파되지 않는다 | 게이트를 shape·verify·analysis·test·human 다섯 계층에 배치, 실패는 draft | **적합** | 0.90 |
| 5 | `p8-verification-and-validation/alternatives` | 확인 생략과 자동 귀속의 기각 | 확인(validation)을 생략하는 안과 귀속을 자동화하는 안의 기각 | **적합** | 0.95 |
| 6 | `p8-mismatch-attribution/conclusion` | 검증기 실패의 귀속은 결정이며 V&V decision의 지침으로 남는다 | 검증기 실패의 귀속(산출물/지식/둘 다)은 결정이고 지침 청크로 기록 | **적합** | 0.95 |
| 7 | `p8-vv-roles/rationale` | 기준의 빈틈이 검증기의 빈틈으로 옮겨가지 않게 한다 | 기준 저자와 검증기 저자를 나누는 이유 — 빈틈의 복제 방지 | **적합** | 0.95 |

**적합 7/7.** 재저작이 라벨 대표성을 떨어뜨리지 않았다. #4는 "게이트는 …"으로 시작하나 본문이 "흩어진 게이트를 한 표로
모은다"로 시작해 총람이라는 성격이 라벨에 덜 드러난다 — 적합이되 확신도를 낮게 둔다.

도장은 hci 가 찍지 않는다 — 담당 역할이 `bazel run //tools:endorse -- --by process:label-judge-20260912 --at <시각> <위 7 파일>`.

## 답
(유저가 채움 — 재판정 결과 확인, 또는 판정자 교체 요구)
