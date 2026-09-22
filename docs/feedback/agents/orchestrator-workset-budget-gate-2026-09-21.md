---
from: orchestrator
kind: question
status: open
targets: [tools/workset.py, kg/BUILD.bazel, docs/roadmap.md, kb/dev/decision/p14-stage-pass-conditions/]
---

# 작업 집합의 예산 초과를 게이트로 할 것인가 (2026-09-21)

## 질문

`workset` 뷰가 예산(200줄)을 넘을 때 빌드가 실패해야 하는가. 지금은 성공하고 머리에 "예산 초과" 한 줄만 적는다. 어려운 이유는 도입 2단계 통과 조건("역할·앵커별 작업 집합 ≤ 예산")이 이 판정에 걸려 있는데, 앵커 없는 전체 뷰는 구조적으로 예산을 넘기 때문이다 — 게이트로 만들면 기본 설정의 `//kg:workset` 빌드가 항상 깨진다.

## 이미 정해진 것

- `p14-stage-pass-conditions` — 2단계 구체화 조건은 "역할·작업(앵커)별 작업 집합 ≤ 예산" 이다. 앵커별이다.
- `p0-workset-anchor-neighbourhood` — 작업 집합은 앵커의 이웃을 예산 안에 담는다. 앵커 없는 뷰는 라벨 목록이다.
- `p1-context-budget-breakdown` — 예산 200줄.
- `metrics` 의 2단계 대리는 **앵커별** 비율(`orchestrator` 675/684 = 98.7% 등)이고, `workset` 뷰의 판정은 **앵커 없는 전체**다. 두 문서가 각자 정의를 밝힌다(2026-09-21 gendoc 반영).

## 현재 상태 (실측 2026-09-21)

- `tools/workset.py:145` — `verdict = "예산 안" if used <= a.budget else "예산 초과"`. 종료 코드는 0 이다.
- `bazel-bin/kg/workset-developer.md` — "합계 637줄 / 예산 200줄 → 예산 초과". 앵커 없는 기본 설정이다.
- 앵커를 준 뷰(`--//kb:anchor=<IRI>`)는 예산 안이다 — vnv 가 r-015 케이스 `dispatch-workset-budget` 에서 결정 결론 IRI 를 앵커로 잡아 확인했다.
- `//kg:workset` 의 `data` 에 `//kb/vv:bodies` 가 없어 V&V 청크가 이웃이면 빌드가 실패한다 — developer 가 지금 고치고 있다(별건).

## 답이 가르는 것

- **비영 종료로 하면** 앵커별 뷰는 게이트가 되고 2단계 조건이 `bazel test` 안으로 들어온다. 앵커 없는 뷰는 별도 타깃이거나 예산 검사를 끄는 설정이 필요하다.
- **두면** 2단계 조건은 `metrics` 대리 수치로만 남고 게이트 밖이다. r-015 케이스는 뷰 머리의 문구를 기대로 대조해야 판정이 되는데, `vv_run` 은 종료 코드만 본다(기대 문구 대조는 로드맵 7단계 "남은 것").

## 선택지

1. **앵커가 있을 때만 비영 종료** — `--//kb:anchor` 가 주어지면 예산 초과 시 `FAIL [workset-budget]` 로 실패하고, 앵커 없는 라벨 목록 뷰는 예산 판정을 하지 않는다. 2단계 조건이 게이트가 되고 기본 빌드는 깨지지 않는다. 비용: `tools/workset.py` 한 갈래, `docs/tools.md` 총람 한 행. orchestrator 권장이다.
2. **항상 비영 종료** — 앵커 없는 뷰도 실패. 기본 `//kg:workset` 이 깨지므로 `kg/BUILD.bazel` 의 기본 설정을 앵커 있는 것으로 바꿔야 한다.
3. **두고 `vv_run` 기대 문구 대조로 판정** — 게이트가 아니라 V&V 케이스가 잰다. 비용: `vv_run` 확장(로드맵에 이미 있음).
