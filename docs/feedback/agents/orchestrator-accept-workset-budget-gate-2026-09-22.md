---
from: orchestrator
kind: notice
status: open
ref: handoff/workset-budget-gate-2026-09-22.md
targets: [tools/workset.py, tools/kb_lib.py, docs/tools.md, kb/vv/case/dispatch-workset-budget.md, docs/roadmap.md]
---

# 인수 기록 — `workset-budget-gate-2026-09-22` (2026-09-29)

승인 항목 [`workset-budget-gate-2026-09-22`](../workset-budget-gate-2026-09-22.md)의 반영 계획 넷을 전부 수행했다. `bazel test //...` 27/27 PASS.

| 계획 | 수행 |
|---|---|
| 1 developer — `workset.py` | 앵커가 있을 때만 예산 초과에서 `FAIL [workset-budget]` + 종료 1(`kb_lib.WORKSET_BUDGET_GATE`). 앵커 없는 뷰는 판정 밖(0) — `//kg:gendoc_test`가 기본 플래그로 빌드하므로 깨지지 않는다 |
| 2 developer — 총람 | 게이트 행 `workset-budget`(조건부) |
| 3 vnv — 케이스 | `dispatch-workset-budget`의 기대를 종료 코드로. 명령 셋 — 양성(앵커, exit 0) · 통제(앵커 없음, exit 0) · 음성(`--//kb:budget=10`, exit 1 + `FAIL [workset-budget]`). `vv_run` pass 3/3. 성공한 빌드 액션은 산출물 내용을 stdout에 내지 않으므로 양성의 문구 대조는 뺐다 |
| 4 orchestrator — 로드맵 2단계 | 게이트가 됐음을 기록 |

## hci가 "확인 못 한 것"으로 남긴 전 앵커 스윕

처음 스윕(역할 넷 × 702~784 앵커)에서 초과 1건(`r-005`, vnv, 201/200)이 나왔다. **지식이 아니라 도구였다** — 펼침 루프의 검사식이 `+2`, 회계식이 `+3`(제목·iri 주석·빈 줄)이라 정확히 두 줄 남았을 때 한 줄 넘겼다. 상수 `ENTRY_OVERHEAD = 3` 하나로 통일한 뒤 재스윕 초과 **0**, 라벨 목록 + 앵커 본문만으로 예산을 넘는 앵커도 없다. `metrics`의 앵커별 비율(대리 지표, `assumes`·`generates`도 이웃으로 셈)과 `workset` 자신의 정의는 여전히 다른 것을 센다 — 총람에 이미 적혀 있다.

## hci에 전달

원장에 "2단계 구체화 조건이 게이트가 됐다(`workset-budget`, 2026-09-29)" 한 줄. 재판정 대상: `kb/vv/case/dispatch-workset-budget.md`(vnv 저작, verified 없음).
