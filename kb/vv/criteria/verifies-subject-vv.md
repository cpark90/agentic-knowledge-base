---
id: https://agentic-knowledge-base.dev/id/chunk/2a7d49b7-e29a-4609-acc5-81608e38324a
type: contract
level: logical
title_ko: kb/vv 밖의 verifies는 분석 실패로 거부되고 커밋된 verifies의 주어는 전부 kb/vv다
title: A verifies link outside kb/vv fails at analysis time and every committed subject lives in kb/vv
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/98edd71a-023c-446e-a26f-c24bc834a4b5]
---
**합격 기준** — 기준 종류는 **불변식**이다. 모든 `verifies` 링크에 대해 `주어.package.startswith("kb/vv")`, `대상.package.startswith("kb/dev")`, `주어.level == 대상.level`이 성립한다.

**판정식**

- 음성: `bazel test //defs/tests:verifies_subject_test`가 PASS다. 이 시험은 `defs/tests` 패키지의 `decision` 타깃이 `verifies`를 가질 때 분석이 `verifies 의 주어는` 문구로 실패할 때만 PASS다.
- 양성: `bazel build //kb/vv/...`가 성공한다. `kb/vv`의 케이스가 `kb/dev`의 결정 결론을 같은 수준(concrete)에서 `verifies` 한다.
- 위반 입력의 거부 형태는 분석 실패이고 메시지에 `verifies 의 주어는`이 있다. 대상이 `kb/dev` 밖이면 `verifies 의 대상은 개발 KB 청크다`, 수준이 다르면 `같은 수준끼리`가 있다.

**등급** — A다. 분석 시점 판정은 액션 실행 없이 즉시 내려진다.

기준의 대상은 저장소의 모든 `verifies` 링크이고 판정의 원본은 `defs/kb.bzl`의 `_check_links`다. 판정 근거는 타깃 라벨의 패키지 접두어이므로 파일 내용이 아니라 저장 위치가 주어의 자격을 정한다.
