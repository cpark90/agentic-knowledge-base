---
id: https://agentic-knowledge-base.dev/id/chunk/c0fb71e0-f5bf-44eb-90f4-542b546bf081
type: contract
level: logical
title_ko: 문서 뷰는 bazel-bin에만 생성되고 트리의 생성물은 드리프트 검사가 원본과 일치시킨다
title: Document views are generated only under bazel-bin and every in-tree generated file matches its source under the drift check
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/06bb9a79-21e8-4eb3-8577-38b9a75002c9]
---
**합격 기준** — 기준 종류는 **명세 대조**다. 뷰마다 `render(그래프, 본문) → bazel-bin/<pkg>/<kind>.md`이고 트리에는 그 사본이 없다. 트리에 두는 생성물마다 `render(원본) == 커밋본`이 바이트 단위로 성립한다.

**판정식**

- 양성(뷰): `bazel build //kb/dev:adr //kg:audit`이 성공하고 생성물 머리에 `- 생성 시각:`·`- 질의:` 줄이 있다. `kb/dev/adr.md`·`kg/audit.md`는 소스 트리에 없다.
- 양성(드리프트): `bazel test //:build_drift_test //:skills_drift_test`가 PASS다.
- 음성(BUILD): frontmatter를 고치고 BUILD를 재생성하지 않으면 `FAIL [build-drift]`로 끝난다. 별도 기준 `generated-build-drift`가 그 표본을 갖는다.
- 음성(skill): 도구 docstring을 고치고 skill을 재생성하지 않거나 skill을 손으로 쓰면 `FAIL [skills-drift]`로 끝나고 종료 코드가 1이다.

**등급** — B다. 판정은 기계가 하되 생성기 재실행의 비용이 있다.

기준의 대상은 `kb_weave`의 뷰 전부(adr·requirements·changelog·audit)와 트리의 생성물(BUILD·skill)이고 판정의 원본은 `tools/weave.py`·`tools/gen_build.py`·`tools/gen_skills.py`다.
