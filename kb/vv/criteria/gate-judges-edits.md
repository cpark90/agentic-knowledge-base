---
id: https://agentic-knowledge-base.dev/id/chunk/47ee0dfa-f035-4220-a756-a447df307de9
type: contract
level: logical
title_ko: 다섯 위반 고정물이 분석 시점에 각자의 규칙 문구로 실패하고 커밋된 트리는 shape·verify·test 게이트를 통과한다
title: Five violating fixtures fail at analysis time each with its own rule text and the committed tree passes the shape, verify and test gates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-06T11:23:25+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-06T11:23:25+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/e815eab2-4c4b-41dc-8b57-6617bb76e566]
---
**합격 기준** — 기준 종류는 **불변식**이다. 편집 e마다 `gate(e) ∈ {PASS, FAIL[id]: 근거}`이고 FAIL은 규칙 문구를 동반한다. 커밋된 트리 전체는 PASS다.

**판정식**

- 음성(analysis): `bazel test //defs/tests:residency_test //defs/tests:plane_direction_test //defs/tests:supersedes_plane_test //defs/tests:verifies_subject_test //defs/tests:decision_levels_test` 가 PASS 다.
- 시험마다 짝지은 고정물과 실패 문구가 있고, 고정물의 분석이 그 문구로 실패할 때만 그 시험이 PASS 다.
- 양성(shape·verify): `bazel test //kg:gate_test`가 PASS다. `[shacl]`·`[vocab]`·`[verify]`·`[dangling]`·`[odd-ref]` 출력이 없다.
- 양성(test): `bazel test //kb/dev:lint_test`가 PASS다.
- human 실행 계층(`stable` 전이 승인)은 이 기준 밖이고 `writer` 검사가 `generated.by`의 역할로 대신 판정한다.

| 시험 (`//defs/tests:`) | 고정물의 실패 문구 |
|---|---|
| `residency_test` | `수준 허용표 위반` |
| `plane_direction_test` | `plane 단방향 위반` |
| `supersedes_plane_test` | `같은 plane 안에서만` |
| `verifies_subject_test` | `verifies 의 주어는` |
| `decision_levels_test` | `수준 허용표 위반` |

**등급** — A와 B가 섞인다. analysis 실행 계층은 액션 실행 없이 즉시 판정되고(A) shape·verify·test 실행 계층은 실행 비용이 있다(B).

기준의 대상은 `defs/tests`의 고정물 다섯과 커밋된 청크 전부이고 판정의 원본은 `defs/kb.bzl`·`tools/validate.py`·`tools/chunk_lint.py`다.
