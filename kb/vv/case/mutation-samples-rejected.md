---
id: https://agentic-knowledge-base.dev/id/chunk/dd9f88e7-0282-4093-9ac5-70acd9a8e409
type: schema
level: concrete
title_ko: 고정물 다섯이 각각 plane 단방향·수준 허용표·같은 plane·verifies 주어·부분 수준 위반으로 거부되어 failure_test 다섯이 PASS 다
title: The five fixtures are each rejected for plane direction, residency, same-plane supersedes, verifies subject and part levels, so the five failure tests pass
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/193f0438-c6bc-4e78-979d-152cfbf97323]
verifies: [https://agentic-knowledge-base.dev/id/chunk/19340826-1e0d-48ab-afa9-16402d5325e1]
---
**케이스** — 분석 시점 고정물 다섯을 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel` 의 `failure_test` 다섯이다. 각 고정물은 유효한 청크 `fx_req`·`fx_dec`·`fx_ctr` 에 규칙 위반 하나를 더한 것이다.

```yaml
plane_direction_test:  {fixture: bad_plane_dir,       mutation: "decision refines contract",                  expected: "plane 단방향 위반"}
residency_test:        {fixture: bad_residency,       mutation: "requirement at level concrete",              expected: "수준 허용표 위반"}
supersedes_plane_test: {fixture: bad_supersedes,      mutation: "decision supersedes requirement",            expected: "같은 plane 안에서만"}
verifies_subject_test: {fixture: bad_verifies,        mutation: "dev decision verifies dev decision",         expected: "verifies 의 주어는"}
decision_levels_test:  {fixture: bad_decision_levels, mutation: "part levels [executable, logical, logical]", expected: "수준 허용표 위반"}
```

**기대** — 시험 다섯이 전부 PASS 다. 검출률은 5/5 = 100.0% 다. 어느 하나라도 고정물이 통과하면 그 시험이 FAIL 이고 그것이 규칙 약화의 신호다.

**실행 명령** — `bazel test //defs/tests:plane_direction_test //defs/tests:residency_test //defs/tests:supersedes_plane_test //defs/tests:verifies_subject_test //defs/tests:decision_levels_test`

**표본 근거** — 고정물은 `defs/tests` 에 있는 것 전부라 표본이 전수다. 규칙마다 위반 하나씩이고 경계값(허용 구간의 끝)은 고정물에 없다. 판정자 지표는 측정 대상이 없어 표본도 없다.
