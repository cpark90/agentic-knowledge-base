---
id: https://agentic-knowledge-base.dev/id/chunk/af560333-541b-44ee-b0d0-24f0ab52d8cf
type: decision
level: concrete
title_ko: 생성물은 bazel-out에만 두고 소스 트리의 생성 트리 파일은 드리프트 테스트가 재생성과 비교한다
title: Generated outputs live only in bazel-out, and generated tree files in the source tree are compared against regeneration by drift tests
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:20+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/444519a5-c8d8-416b-88a5-b1bc2fd92ccc
composite: {id: https://agentic-knowledge-base.dev/id/composite/444519a5-c8d8-416b-88a5-b1bc2fd92ccc, title_ko: 생성물은 bazel-out에 둔다, title: Generated outputs stay in bazel-out}
---
**결론** — 생성물은 `bazel-out`에만 존재한다. 소스 트리에 같은 이름의 파일을 두지 않는다(`STYLEGUIDE.md` §6, 2026-09-01).

예외는 소스 트리에 커밋하는 생성 트리 파일이다. 규범 문서는 둘을 적었고(2026-09-19) 규범 문서 자신이 셋째가 됐다(Q19-b, 2026-10-03).

| 생성 트리 파일 | 생성기 | 드리프트 테스트 | 트리에 두는 이유(생성기 docstring) |
|---|---|---|---|
| 생성 BUILD | `tools/gen_build.py` | `//:build_drift_test` | 링크 변화가 PR diff에 보인다 |
| `.claude/skills/*/SKILL.md` | `tools/gen_skills.py` | `//:skills_drift_test` | 도구가 없어도 skill이 읽힌다 |
| 규범 문서(`defs/kb.bzl`의 `NORM_DOCS`) | `tools/gen_norms.py` | `//:norms_drift_test` | 진입 문서는 도구 없이 읽혀야 한다. 원본은 결정의 규약 청크와 `kb/dev/norm/`의 절 청크다(`p12-norm-documents-from-section-chunks`) |

생성 트리 파일은 손으로 고치지 않는다. 드리프트 테스트가 생성기를 다시 돌려 트리의 파일과 비교하고, 어긋나면 `FAIL [build-drift]`·`FAIL [skills-drift]`·`FAIL [norms-drift]`로 거부한다. 손으로 쓴 skill도 이중 원본으로 거부한다. 생성 BUILD의 첫 줄은 손으로 고치지 않는다는 경고와 원본(청크의 frontmatter)이다.

생성 트리 파일에 생성 시각과 지문을 넣지 않는 규칙은 `p12-generated-document-header`가 정한다.
