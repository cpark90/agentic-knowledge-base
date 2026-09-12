---
from: hci
source: label-representativeness-protocol.md
verdict: apply
status: closed
---

# 라벨 대표성 실험 — 재판정 1건 (`p6-gate-catalogue/conclusion`, 2026-09-12)

orchestrator 의 인수 기록(`agents/orchestrator-agrtls-practices-2026-09-12.md` 전달 2): 결론 청크에 게이트 id 단락을 더하면서
오늘의 판정자 표시(`process:label-judge-20260912`)가 물러났다(trust-shapes). 프로토콜은 "재저작 후 같은 판정자로 재판정".
같은 절차 — 라벨만 보고 예측한 뒤 본문과 대조.

| 라벨(ko) | 예측 | 판정 | 확신도 |
|---|---|---|---|
| 게이트는 다섯 실행 계층에 배치되며 실패는 draft에 머물러 전파되지 않는다 | 게이트를 shape·verify·analysis·test·human 다섯 계층에 배치하고, 실패한 청크는 draft 에 머물러 하류로 전파되지 않는다 | **적합** | 0.90 |

본문은 "흩어진 게이트를 한 표로 모은다"로 시작해 다섯 계층의 정의와 배치, 새로 더한 id 단락, 실패의 draft 잔류를 담는다.
id 단락이 늘었어도 라벨이 가리키는 것(계층 배치 + 실패 잔류)은 그대로다 — 총람 성격은 여전히 라벨에 덜 드러나 확신도는 낮게 둔다.

## 파급효과
head 만 바뀐다(`verified` 항목 추가). 본문·라벨·링크·복합체는 닿지 않는다 — `impact` 를 돌릴 대상이 없다.

## 반영 계획
1. `bazel run //tools:endorse -- --by process:label-judge-20260912 --at <시각> kb/dev/decision/p6-gate-catalogue/conclusion.md`
2. `label-experiment-agent-2026-09-11.md` 의 집계는 바뀌지 않는다(같은 판정).
검색 키워드: `p6-gate-catalogue` · `label-judge-20260912` (도장 목록·실험 결과 파일).

## 확인 못 한 것
없음.

## 판정
`apply` — 판정 절차는 승인된 프로토콜의 일부이고 유저 판단이 새로 필요하지 않다. 도장은 담당 역할이 찍는다.
