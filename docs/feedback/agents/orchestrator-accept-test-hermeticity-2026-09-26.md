---
from: orchestrator
kind: notice
status: open
ref: handoff/test-hermeticity-2026-09-26.md
targets: [kb/odd/project-odd.yml, kb/dev/decision/p8-verifier-env-isolation/, docs/tools.md]
---

# 인수 기록 — `test-hermeticity-2026-09-26` (2026-09-29)

승인 항목 [`test-hermeticity-2026-09-26`](../test-hermeticity-2026-09-26.md)의 반영 계획 넷을 전부 수행했다. `bazel test //...` 27/27 PASS.

| 계획 | 수행 |
|---|---|
| 1·2 developer — ODD 조건 | `id:cond-host-env-inherit`(정적 요소, 값 "`env_inherit`을 쓰는 테스트 타깃 ≤ 1", 등급 A) 신설·`hasCondition` 등록. 판정 명령은 `bazel query 'attr(env_inherit, "HOME", tests(//...))'`의 행 수 — hci가 확인 못 한 것: `".+"`는 빈 목록 `[]`에도 걸려 15행이 나오므로 쓰지 않는다. `odd_check` 이탈 0, 음성 시험(`-le 0`) 이탈 보고 확인 |
| 3 orchestrator — 결정 문장 | `p8-verifier-env-isolation` 결론에 "밀폐 예외 하나를 받는다 … 예외의 수는 ODD 조건이 판정한다" |
| 4 developer — 총람 | `vv-run-env` 행에 예외 표시 |

`agt:conditionValue` 문자열은 `odd_check` 판정에 쓰이지 않는다 — 판정은 `CHECKS.<속성>.cmd`뿐이다. 값 문장과 명령이 갈리면 문장이 틀린 것이다.

## hci에 전달

원장에 "밀폐 예외 1 = ODD 조건 `cond-host-env-inherit`(2026-09-29)" 한 줄. 재판정 대상 없음(orchestrator 저작 청크).
