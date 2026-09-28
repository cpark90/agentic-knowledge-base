---
from: hci
source: test-hermeticity-2026-09-26.md
verdict: apply
status: closed
---

# 게이트 하나의 밀폐성 벗어남 (2026-09-29 승인)

유저 답: *"1."* — **현재 상태를 받고 ODD 에 조건을 더한다.** 벗어남을 관측 가능하게 만든다.
셋째 길(`rdflib` 를 테스트 `deps` 로 들이기)은 고르지 않았다 — 실측 일치를 밀폐성보다 앞에 둔 판단이다.

## 파급효과

- 게이트 23 중 하나가 호스트의 `HOME` 에 의존하는 상태가 **선언된 예외**가 된다. 선언이 없으면 다음 세션이 같은 판단을 다시 한다.
- ODD 조건이 하나 늘어 조건 수와 판정 방법 등급의 분포가 바뀐다. 조건마다 `conditionValue`·`checkMethod`·`verificationGrade` 가 필수다.
- 닿지 않는 것: 나머지 22 타깃 · `p8-verifier-env-isolation` 의 결론 · 케이스의 자극.

## 반영 계획

1. **developer — ODD 조건 신설.** `kb/odd/project-odd.yml` 에 `id:cond-host-env-inherit` 를 더한다. 갈래는 정적 요소, 값은 "`env_inherit` 을 쓰는 테스트 타깃 수 ≤ 1", 판정 방법은 **객관적 관측 수단**으로 적는다 — 예를 들어 `bazel query 'attr(env_inherit, ".+", tests(//...))'` 의 행 수다. 등급은 A 를 목표로 한다.
2. **developer — 조건 등록.** ODD 개체의 `agt:hasCondition` 목록에 넣는다. 등록 없는 조건을 만들지 않는다.
3. **orchestrator — 결정에 근거 한 문장.** `p8-verifier-env-isolation` 또는 새 결정에 "실측 일치를 위해 한 타깃의 밀폐 예외를 받고 그 수를 ODD 가 판정한다"를 적는다. 그것이 다음 세션의 재판단을 막는다.
4. **developer — `docs/tools.md`** 게이트 총람의 해당 행에 예외를 표시한다.

**검색 키워드**: `env_inherit` · `밀폐` · `hermetic` · `vv_run_env_test` · `cond-` · `PYTHONSAFEPATH`.

## 확인 못 한 것

- 판정 명령의 정확한 형태. `bazel query` 로 `env_inherit` 속성을 거를 수 있는지 hci 는 확인하지 않았다. 되지 않으면 `grep` 기반 판정이 되고 등급이 내려간다.
- 다른 기계에서 이 타깃이 실제로 다르게 도는지. ODD 조건은 그 차이를 **드러내는** 장치이고 없애지는 않는다.
- 타깃 이름을 `vv_run_env_test` 로 좁힌 판단에 유저가 이견을 적지 않았다 — 발신자·hci 의 읽기대로 둔다.

## 판정

`apply` 다. 예외를 문서가 아니라 **판정 가능한 조건**으로 두는 쪽이라 규약에 맞다.

## 반영 확인 (hci, 2026-09-29)

인수 기록 [`../agents/orchestrator-accept-test-hermeticity-2026-09-26.md`](../agents/orchestrator-accept-test-hermeticity-2026-09-26.md) 로 돌아왔다 — 밀폐 예외를 ODD 조건으로 판정하게 했다. 게이트 32/32 PASS.
**제거는 인수 기록이 `closed` 로 바뀐 뒤다** — 기록의 `ref` 와 handoff 의 `source` 가 실재를 요구하므로 유저 lane 항목·handoff·기록이 한 사슬로 함께 나간다(2026-09-29 refresh 에서 순서를 잘못 잡아 게이트가 잡았다).
