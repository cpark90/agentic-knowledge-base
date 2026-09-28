---
from: hci
source: workset-budget-gate-2026-09-22.md
verdict: apply
status: open
---

# 작업 집합 예산 초과의 게이트화 (2026-09-29 승인)

유저 답: *"1."* — **앵커가 있을 때만 비영 종료**한다. 앵커 없는 라벨 목록 뷰는 예산 판정을 하지 않는다.

## 파급효과

- 도입 2단계의 구체화 조건("역할·**앵커별** 작업 집합 ≤ 예산")이 `bazel test` 안으로 들어온다. 조건의 문언과 검사 범위가 일치한다.
- 기본 `//kg:workset` 은 깨지지 않는다 — 앵커 없는 뷰는 판정 밖이다. 현재 그 뷰는 684줄로 구조적 초과다.
- `r-015` 케이스 `dispatch-workset-budget` 의 판정이 뷰 머리 문구 대조에서 **종료 코드**로 바뀐다. `vv_run` 이 종료 코드를 보므로 케이스가 단단해진다.
- 닿지 않는 것: `metrics` 의 앵커별 비율(다른 정의이고 머리에 그 차이를 이미 적는다).

## 반영 계획

1. **developer — `tools/workset.py`.** 앵커가 주어졌을 때만 예산 초과에서 `FAIL [workset-budget]` 과 비영 종료를 낸다. 앵커가 없으면 지금처럼 판정만 적는다.
2. **developer — `docs/tools.md` 게이트 총람**에 한 행(게이트 id `workset-budget`, 조건부 — 앵커가 있을 때만).
3. **vnv — 케이스 갱신.** `dispatch-workset-budget` 의 기대를 종료 코드로 바꾸고, 앵커 없는 실행을 통제로 둔다(종료 0).
4. **orchestrator — `docs/roadmap.md` 2단계 칸**에 이 조건이 게이트가 됐음을 적는다.

**검색 키워드**: `workset` · `예산` · `anchor` · `budget` · `dispatch-workset-budget` · `2단계`.

## 확인 못 한 것

- 앵커별 초과가 실제로 0 인지. `metrics` 의 역할별 비율은 98.7~100% 이므로 초과 앵커가 있을 수 있다. 게이트를 켜기 전에 전 앵커 스윕으로 세는 것을 권한다 — 있으면 그 앵커가 첫 수정 대상이다.
- 예산 200줄이 앵커별로도 맞는 값인지. 결정 `p1-context-budget-breakdown` 이 정한 값을 바꾸지 않는다.

## 판정

`apply` 다. 답이 명확하고 기본 빌드가 깨지지 않는 쪽이다.
