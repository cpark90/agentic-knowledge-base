---
id: https://agentic-knowledge-base.dev/id/chunk/2b1a11cb-160a-45fe-a5cb-4f86f8a42271
type: contract
level: logical
title_ko: plane을 넘는 supersedes는 분석 실패로 거부되고 커밋된 supersedes는 전부 같은 plane 안이다
title: A supersedes link across planes fails at analysis time and every committed one stays inside a plane
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/897a67c4-c07c-4674-a845-dd7841db9c17]
---
**합격 기준** — 기준 종류는 **불변식**이다. 모든 `supersedes` 링크에 대해 `대상.plane == 주어.plane`이 성립한다.

**판정식**

- 음성: `bazel test //defs/tests:supersedes_plane_test`가 PASS다. 이 시험은 `decision`이 `requirement`를 `supersedes` 하는 타깃의 분석이 `같은 plane 안에서만` 문구로 실패할 때만 PASS다.
- 양성: `bazel build //kb/dev/...`가 성공한다. 커밋된 `supersedes`의 대상은 전부 주어와 같은 plane이다.
- 위반 입력의 거부 형태는 분석 실패이고 메시지에 `같은 plane 안에서만`이 있다.

**등급** — A다. 분석 시점 판정은 액션 실행 없이 즉시 내려진다.

기준의 대상은 `kb/dev`와 `chunks/decision`의 모든 `supersedes` 링크이고 판정의 원본은 `defs/kb.bzl`의 `_check_links`다. 옛 항목의 `deprecated` 상태는 이 기준의 대상이 아니라 상태 전이 규칙의 몫이다.
