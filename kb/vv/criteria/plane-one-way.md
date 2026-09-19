---
id: https://agentic-knowledge-base.dev/id/chunk/68faa51d-47c8-48fb-9cb1-589f793d31a6
type: contract
level: logical
title_ko: 하위 plane을 향한 refines는 분석 실패로 거부되고 커밋된 링크는 전부 순서를 지킨다
title: A refines link toward a lower plane fails at analysis time and every committed link keeps the order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/63c4c14d-87eb-4caf-ad0f-704265706505]
---
**합격 기준** — 기준 종류는 **불변식**이다. 모든 `refines`·`serves` 링크에 대해 `PLANES.index(대상.plane) ≤ PLANES.index(주어.plane)`이고 `LEVELS.index(대상.level) < LEVELS.index(주어.level)`이 성립한다.

**판정식**

- 음성: `bazel test //defs/tests:plane_direction_test`가 PASS다. 이 시험은 `decision`(concrete)이 `contract`(abstract)를 `refines` 하는 타깃의 분석이 `plane 단방향 위반` 문구로 실패할 때만 PASS다.
- 양성: `bazel build //kb/dev/...`가 성공한다. 커밋된 모든 `refines`·`serves`가 두 부등식을 만족한다.
- 위반 입력의 거부 형태는 분석 실패이고 메시지에 `plane 단방향 위반`이 있다. 수준 부등식 위반은 `더 높은 수준이어야 한다` 문구로 먼저 실패한다.

**등급** — A다. 분석 시점 판정은 액션 실행 없이 즉시 내려진다.

기준의 대상은 `kb/dev`의 모든 링크이고 판정의 원본은 `defs/kb.bzl`의 `_check_links`와 상수 `PLANES`·`LEVELS`다.
