---
id: https://agentic-knowledge-base.dev/id/chunk/56b4c449-63d5-4f3c-8b25-2983028beab8
type: contract
level: logical
title_ko: 수준 허용표 밖의 조합은 분석 실패로 거부되고 커밋된 청크는 전부 허용표 안이다
title: Out-of-matrix pairs fail at analysis time and every committed chunk sits inside the matrix
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/83c1bb49-81f0-4f0e-a6f9-56b3a2f66924]
---
**합격 기준** — 기준 종류는 **불변식**이다. 모든 청크 타깃에 대해 `level ∈ RESIDENCY[plane]`이 성립하고, 성립하지 않는 입력은 타깃이 되기 전에 거부된다.

**판정식**

- 음성(청크): `bazel test //defs/tests:residency_test`가 PASS다. 이 시험은 `plane = "requirement"`·`level = "concrete"` 타깃의 분석이 `수준 허용표 위반` 문구로 실패할 때만 PASS다.
- 음성(복합체): `bazel test //defs/tests:decision_levels_test`가 PASS다. 결론 수준이 `executable`인 결정 복합체가 같은 문구로 실패한다.
- 양성: `bazel test //kg:gate_test`가 PASS다. head 그래프의 모든 청크가 `residency-shapes.ttl`의 여섯 shape를 통과한다.
- 위반 입력의 거부 형태는 분석 실패이고 메시지에 `수준 허용표 위반`이 있다. `FAIL` 출력이 아니라 빌드 자체가 서지 않는다.

**등급** — A다. 분석 시점 판정은 액션 실행 없이 `bazel build` 한 번으로 즉시 내려진다.

기준의 대상은 `kb/dev`의 모든 청크·복합체 타깃이고 판정의 원본은 `defs/kb.bzl`의 `_check_residency`다.
