---
id: https://agentic-knowledge-base.dev/id/chunk/ffa0cd12-143b-45ac-b932-3972b4eaf2aa
type: decision
level: logical
title_ko: 묶음은 액션의 입력 집합이라 패키지를 넘지 못하고 선언이 한 번이라 composite.id가 묶음의 판별 기준이 된다
title: A bundle is an action's input set and cannot cross a package, and a single declaration makes composite.id the bundle key
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7130e6d8-2b81-49eb-b1a3-96d3c7f93ff3
---
**근거** — 묶음은 Bazel 액션의 입력 집합이고 타깃의 `srcs`는 자기 패키지 밖에 있을 수 없다(`gen_build.group_composites` docstring). 그래서 부분은 한 패키지에 있어야 한다. `chunk2kg`는 `part_of` 대상을 같은 실행의 입력 집합에서 찾으므로 중첩 복합체도 뿌리부터 잎까지 한 액션이 받아야 한다.

선언이 한 번이므로 `composite.id`가 패키지 안 묶음의 판별 기준이 된다. 평평한 패키지 하나에 복합체 여럿이 설 수 있어 디렉토리로는 가를 수 없다(같은 docstring). 결정은 디렉토리가 묶음의 기준이다(같은 docstring). 결정의 세 청크 필수는 대안 기록의 구조 형태다(`p7-alternatives-mandatory`).

선언을 frontmatter로 옮긴 것은 2026-09-29 유저 답 "도구를 고친다"다. 손으로 쓴 복합체 41건이 생성 경로로 옮겨졌다(`composite-kg.ttl` 배너). 결정 밖 plane의 복합체는 `kb_composite`(부분 2~9 가변, `srcs` 목록)가, 결정은 `kb_decision`(세 청크 + 선택 `conventions.md`)이 세운다(`defs/kb.bzl`).

부분 하한 2는 같은 날의 orchestrator 판정이다. 부분 하나뿐이던 손 복합체 `comp-project-harness`를 "부분이 하나면 청크이지 복합체가 아니다"로 지웠다. 상한 9는 노트 4.5절의 7±2다.
