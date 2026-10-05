---
from: orchestrator
kind: question
status: relayed
targets: [defs/knowledge.bzl, tools/vv_run_env_test.py, kb/odd/project-odd.yml, kb/dev/decision/p8-verifier-env-isolation/]
---

# 게이트 하나가 `bazel test` 의 밀폐성에서 벗어난다 (2026-09-23)

## 질문

새 게이트 `//tools:vv_run_env_test` 가 `env_inherit = ["HOME"]` 으로 호스트 환경에 의존한다. 이것을 받을 것인가. 어려운 이유는 **밀폐성과 실측 일치가 맞바꿈**이라는 데 있다 — 밀폐를 지키면 실제로 죽었던 검증기가 아닌 것을 검사하게 되고, 실측을 지키면 `bazel test //...` 의 순수 밀폐성에서 한 타깃이 벗어난다.

## 이미 정해진 것

- 결정 `p8-verifier-env-isolation`(2026-09-23) — 검증기는 실행기의 파이썬·runfiles 변수 다섯을 걷어낸 환경에서 돈다. 실행기를 부르는 방식이 판정을 바꾸면 재현이 아니다.
- 요구 `reproducible-runs` — 실행은 같은 리비전과 seed 에서 재현된다.
- ODD 조건 `id:cond-python-runtime`·`id:cond-dependency-lock` 이 파이썬 런타임과 의존성 고정을 판정한다.
- `STYLEGUIDE.md` §6 — 게이트는 `defs/knowledge.bzl` 의 매크로로만 선언한다. 새 매크로 `kb_runner_env_test` 가 그 규약을 지킨다.

## 현재 상태 (실측 2026-09-23)

- `env_inherit` 을 걸지 않으면 샌드박스의 `python3` 이 사용자 site-packages 를 보지 못해 `ModuleNotFoundError: No module named 'rdflib'` 로 죽는다. **격리와 무관한 이유의 FAIL** 이다.
- 실행기 `vv_run` 은 `bazel run` 으로 돌아 클라이언트의 `HOME` 을 그대로 물려받는다. 테스트가 같은 조건에 있어야 자극이 케이스의 자극과 같다.
- 자립 대안은 임시 디렉토리에 `probe.py`+`sidecar.py` 를 두고 `import sidecar` 만 보는 형태다. 밀폐이되 **실제로 죽었던 검증기가 아니다** — `chunk_lint`·`validate`·`doccheck` 가 `PYTHONSAFEPATH=1` 에서 죽는 것은 실측이고, 합성 모듈이 죽는 것은 그 재현이 아니다.
- 나머지 22 타깃은 `env_inherit` 을 쓰지 않는다. 벗어나는 것은 이 하나다.

## 답이 가르는 것

- **받으면** 게이트 하나가 호스트의 `HOME` 에 의존한다. 다른 기계에서 site-packages 가 다르면 이 타깃만 다르게 돌 수 있고, 그것을 ODD 조건으로 판정할지가 따라온다.
- **받지 않으면** 검사가 합성 자극으로 바뀌어 실측과의 일치를 잃는다. 격리가 깨졌을 때 **실제로 죽는 검증기**가 아니라 흉내낸 모듈이 죽는 것을 보게 된다.
- **셋째 길**은 의존성을 샌드박스 안으로 들이는 것이다. `rdflib` 를 테스트의 `deps` 로 넣으면 밀폐이면서 실제 검증기를 쓴다. 비용은 그 의존이 이 타깃에만 필요하다는 것과, 케이스가 쓰는 `python3` 과 샌드박스의 `python3` 이 같은 해석기인지를 다시 확인해야 한다는 것이다.

## 선택지

1. **지금 상태를 받고 ODD 에 조건을 더한다.** `env_inherit` 을 쓰는 타깃이 하나임을 ODD 가 판정하게 한다(예 — 그 수가 1 이하). 비용: ODD 확장 하나. 실측 일치를 지키면서 벗어남을 관측 가능하게 만든다. orchestrator 권장이다.
1. **셋째 길로 옮긴다.** `rdflib` 를 테스트 `deps` 로 들여 밀폐를 회복한다. 비용: 의존 배선과 해석기 동일성 재확인. 밀폐성이 재현성의 전제라고 보면 이쪽이다.
1. **지금 상태를 받고 기록만 남긴다.** ODD 를 넓히지 않는다. 비용: 벗어남이 문서에만 남아 다음 세션이 같은 판단을 다시 한다.

## 함께 확인할 것

developer 가 이름을 `vv_run_test` 가 아니라 **`vv_run_env_test`** 로 좁힌 판단은 유저 판단 사항이 아니라고 보았다. 근거가 이 저장소의 원칙과 같기 때문이다 — 그 타깃은 실행기 전체가 아니라 환경 격리만 판정하므로, 넓은 이름은 **갖지 않은 커버리지를 주장**하고 그 거짓 주장은 `p8-verifier-env-isolation` 이 경계하는 거짓 통과와 같은 종류의 오류다. 다르게 읽으면 답에 적는다.

## 중계 (hci, 2026-09-26)

유저 lane 항목으로 올렸다 — [`../test-hermeticity-2026-09-26.md`](../test-hermeticity-2026-09-26.md). 한 파일에 한 주제 규약대로 질문마다 항목을 따로 세웠고 다섯 절로 썼다. hci 가 실측으로 확인한 줄은 항목에 표시했다. 유저 답이 오면 이 항목에 옮기고 `answered` 로 바꾼다.
