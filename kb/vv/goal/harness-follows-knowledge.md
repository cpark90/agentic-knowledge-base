---
id: https://agentic-knowledge-base.dev/id/chunk/df934d56-8cc4-4f5f-8cbd-7ae5b6bb89f0
type: requirement
level: functional
pattern: event-driven
title_ko: 저장소의 지식이 바뀌면 그 지식에서 생성되는 하네스 부분이 함께 갱신되어야 한다
title: When the repository's knowledge changes, the parts of the harness generated from that knowledge must be refreshed with it
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T13:20:33+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/cb7ac129-5b94-47cd-84a8-b87e7e238efe]
---
**검증 목표** — 결정·관측·어휘가 늘거나 바뀌면 하네스(도구·게이트·뷰·skill)가 사람의 별도 수정 없이 그 변화를 반영한다는 것이 보여져야 한다. 반영의 단위는 지식에서 생성되는 하네스 부분이고, 생성되지 않는 부분은 이 목표가 재는 대상이 아니라 요구가 남긴 미확정의 자리다.

- **이해관계자**: 유저 · **관심사**: 통일과 되먹임

**무엇을 관측하면 성립하는가**

- 지식에서 생성되는 하네스 부분이 목록으로 있고 각 부분에 재생성 바이트 비교가 걸려 있다. 지금 실물은 BUILD(`//:build_drift_test`, 원본은 청크 frontmatter)·규범 문서(`//:norms_drift_test`, 원본은 절 청크와 결정의 `conventions.md`)·생성 뷰(`//:gendoc_test`)다.
- 게이트가 판정에 쓰는 어휘·shape·ODD 가 지식 파일에서 읽히므로 온톨로지 모듈에 개념 하나를 더하면 게이트의 수용 범위가 도구 코드의 수정 없이 바뀐다.
- 관측에서 어휘로 올라가는 승격 경로(`term_propose` → `kb/ontology/proposals/`)가 실행된 사례가 있다.
- 지식 → 도구 코드의 역방향 경로가 없다는 사실이 공백으로 드러난다. skill 은 도구 docstring 에서 생성되므로(`//:skills_drift_test`) 방향이 도구 → 뷰이고 이 관측에 들지 않는다.

판정의 원본은 요구 `r-029-harness-self-improvement` 와 `BUILD.bazel` 의 드리프트 테스트 선언이다.

미확정: 하네스의 어느 부분이 지식에서 생성되는가의 경계 — 요구의 미확정을 그대로 잇는다. 경계가 정해지기 전에는 목록이 닫히지 않으므로 이 목표는 성립 여부가 아니라 부분 성립의 범위만 보인다.
