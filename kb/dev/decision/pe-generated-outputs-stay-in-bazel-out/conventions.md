---
id: https://agentic-knowledge-base.dev/id/chunk/4b9939fa-9753-4fc9-bd94-312945fc6bc1
type: decision
level: concrete
title_ko: 규범 문서 규약 — 생성물은 bazel-out에만 두고 소스 트리의 생성 트리 파일은 드리프트 테스트가 재생성과 비교한다
title: Normative-document conventions — Generated outputs live only in bazel-out, and generated tree files in the source tree are compared against regeneration by drift tests
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:18:59+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:18:59+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/444519a5-c8d8-416b-88a5-b1bc2fd92ccc
---
**규약** — `pe-generated-outputs-stay-in-bazel-out`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 생성물은 `bazel-out`에만 존재하므로 소스 트리에 같은 이름의 파일을 두지 않는다. 다만 생성 트리 파일 셋은 예외다. 그 셋은 생성 BUILD와 `.claude/skills/`의 SKILL.md, 규범 문서이고, 각각 `//:build_drift_test`와 `//:skills_drift_test`, `//:norms_drift_test`가 재생성 결과와 비교하며, 세 파일은 손으로 고치지 않는다.
규약: skill | 도구 docstring과 `kb_lib.SKILLS`에서 `.claude/skills/*/SKILL.md`를 생성해 트리에 두고 드리프트 검사로 확인한다
