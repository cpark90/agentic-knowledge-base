---
from: hci
status: open
targets: [tools/workset.py, kg/BUILD.bazel, kb/dev/decision/p14-stage-pass-conditions/, docs/roadmap.md]
---

# 작업 집합의 예산 초과를 게이트로 할 것인가 (2026-09-22 중계)

원본: [`agents/orchestrator-workset-budget-gate-2026-09-21.md`](agents/orchestrator-workset-budget-gate-2026-09-21.md)

## 질문

`workset` 뷰가 예산 200줄을 넘을 때 빌드가 실패해야 하는가. 지금은 성공하고 머리에 "예산 초과" 한 줄만 적는다.

어려운 이유는 도입 2단계 통과 조건이 이 판정에 걸려 있는데 **앵커 없는 전체 뷰는 구조적으로 예산을 넘는다**는 데 있다.
게이트로 만들면 기본 설정의 `//kg:workset` 빌드가 항상 깨진다.

## 이미 정해진 것

- `p14-stage-pass-conditions` — 2단계 구체화 조건은 "역할·작업(**앵커**)별 작업 집합 ≤ 예산"이다.
- `p0-workset-anchor-neighbourhood` — 작업 집합은 앵커의 이웃을 예산 안에 담는다. 앵커 없는 뷰는 라벨 목록이다.
- `p1-context-budget-breakdown` — 예산은 200줄이다.
- `metrics`의 2단계 대리는 **앵커별** 비율(역할마다 98.7~100%)이고 `workset` 뷰의 판정은 **문서 전체**다. 두 생성물이 각자 정의를 머리에 밝힌다.

## 현재 상태 (실측 2026-09-22)

- `tools/workset.py:145` — `verdict = "예산 안" if used <= a.budget else "예산 초과"`. **종료 코드는 0**이다. hci가 코드를 확인했다.
- `bazel-bin/kg/workset-developer.md` — "합계 **684줄 / 예산 200줄 → 예산 초과**". 앵커 없는 기본 설정이다. 같은 문서가 두 수치의 정의 차이를 적는다.
- 앵커를 준 뷰(`--//kb:anchor=<IRI>`)는 예산 안이다. vnv가 `r-015` 케이스 `dispatch-workset-budget`에서 확인했다.
- `vv_run`은 **종료 코드만** 본다. 기대 문구 대조는 로드맵 7단계의 "남은 것"이다.

## 답이 가르는 것

- **앵커가 있을 때만 실패하게 하면** 2단계 조건이 `bazel test` 안으로 들어오고 기본 빌드는 깨지지 않는다. 조건의 문언("앵커별")과 검사 범위가 정확히 일치한다.
- **항상 실패하게 하면** 기본 `//kg:workset`이 깨지므로 `kg/BUILD.bazel`의 기본 설정을 앵커 있는 것으로 바꿔야 한다. 앵커 없는 라벨 목록 뷰는 별도 타깃이 된다.
- **두면** 2단계 조건은 `metrics` 대리 수치로만 남고 게이트 밖이다. `r-015` 케이스는 뷰 머리의 문구를 대조해야 판정이 되는데 그 수단이 아직 없다.

## 선택지

1. **앵커가 있을 때만 비영 종료** (orchestrator 권장). 앵커가 주어지면 초과 시 `FAIL [workset-budget]`으로 실패하고, 앵커 없는 뷰는 예산 판정을 하지 않는다. 비용: `tools/workset.py` 한 갈래 + `docs/tools.md` 총람 한 행.
2. **항상 비영 종료.** 비용: 위에 더해 `kg/BUILD.bazel` 기본 설정 변경과 라벨 목록 뷰의 분리.
3. **두고 `vv_run` 기대 문구 대조로 판정한다.** 게이트가 아니라 V&V 케이스가 잰다. 비용: `vv_run` 확장(로드맵 7단계에 이미 있다).

## 답
(유저가 채움)
