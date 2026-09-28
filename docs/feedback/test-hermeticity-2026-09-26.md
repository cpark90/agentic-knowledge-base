---
from: hci
status: approved
targets: [defs/knowledge.bzl, tools/BUILD.bazel, kb/odd/project-odd.yml, kb/dev/decision/p8-verifier-env-isolation/]
---

# 게이트 하나가 `bazel test` 의 밀폐성에서 벗어난다 (2026-09-26 중계)

원본: [`agents/orchestrator-test-hermeticity-2026-09-23.md`](agents/orchestrator-test-hermeticity-2026-09-23.md) — 다섯 절이 그대로 있다.

## 질문

새 게이트 `//tools:vv_run_env_test` 가 `env_inherit = ["HOME"]` 으로 호스트 환경에 의존한다. 받을 것인가.
어려운 이유는 **밀폐성과 실측 일치가 맞바꿈**이라는 데 있다 — 밀폐를 지키면 실제로 죽었던 검증기가 아닌 것을 검사하고,
실측을 지키면 게이트 23 중 하나가 순수 밀폐에서 벗어난다.

## 이미 정해진 것

- 결정 `p8-verifier-env-isolation`(2026-09-23) — 검증기는 실행기의 파이썬·runfiles 변수 다섯을 걷어낸 환경에서 돈다.
- 요구 `reproducible-runs` — 실행은 같은 리비전과 seed 에서 재현된다.
- ODD 조건 `id:cond-python-runtime`·`id:cond-dependency-lock` 이 런타임과 의존성 고정을 판정한다.
- 게이트는 `defs/knowledge.bzl` 의 매크로로만 선언한다. 새 매크로 `kb_runner_env_test` 가 그 규약을 지킨다.

## 현재 상태 (실측, hci 확인)

- `env_inherit` 없이 돌리면 샌드박스의 `python3` 이 사용자 site-packages 를 못 보고 `ModuleNotFoundError: No module named 'rdflib'` 로 죽는다. **격리와 무관한 이유의 FAIL** 이다.
- 실행기 `vv_run` 은 `bazel run` 으로 돌아 클라이언트의 `HOME` 을 물려받는다. 테스트가 같은 조건이어야 자극이 케이스의 자극과 같다.
- 나머지 **22 타깃은 `env_inherit` 을 쓰지 않는다.** 벗어나는 것은 하나다.
- 합성 대안(임시 디렉토리의 `probe.py`+`sidecar.py`)은 밀폐이되 **실제로 죽었던 검증기가 아니다.**

## 답이 가르는 것

- **받으면** 게이트 하나가 호스트의 `HOME` 에 의존한다. 다른 기계에서 site-packages 가 다르면 이 타깃만 다르게 돌 수 있고, 그 벗어남을 ODD 가 판정할지가 따라온다.
- **받지 않으면** 검사가 합성 자극이 되어 실측과의 일치를 잃는다. `PYTHONSAFEPATH=1` 에서 실제 검증기 셋이 죽는 것이 실측이고 흉내낸 모듈이 죽는 것은 그 재현이 아니다.
- **셋째 길**(`rdflib` 를 테스트 `deps` 로 들이기)을 고르면 밀폐이면서 실제 검증기를 쓴다. 대신 해석기 동일성을 다시 확인해야 한다.

## 선택지

1. **받고 ODD 에 조건을 더한다** (orchestrator 권장). `env_inherit` 을 쓰는 타깃 수가 1 이하임을 ODD 가 판정한다. 비용: ODD 확장 하나. 벗어남이 관측 가능해진다.
2. **셋째 길로 옮긴다.** `rdflib` 를 테스트 `deps` 로 들여 밀폐를 회복한다. 비용: 의존 배선 + 해석기 동일성 재확인.
3. **받고 기록만 남긴다.** ODD 를 넓히지 않는다. 비용: 벗어남이 문서에만 남아 다음 세션이 같은 판단을 다시 한다.

## 함께 확인할 것

발신자는 타깃 이름을 `vv_run_test` 가 아니라 `vv_run_env_test` 로 좁힌 것이 유저 판단 사항이 아니라고 보았다 — 넓은 이름은
갖지 않은 커버리지를 주장하기 때문이다. hci 도 같게 읽는다. 다르게 읽으면 답에 적는다.

## 답
1.
