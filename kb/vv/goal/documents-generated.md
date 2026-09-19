---
id: https://agentic-knowledge-base.dev/id/chunk/06bb9a79-21e8-4eb3-8577-38b9a75002c9
type: requirement
level: functional
pattern: ubiquitous
title_ko: 문서·코드 뷰는 청크에서 생성되고 별도 원본으로 저장되지 않아야 한다
title: Document and code views must be generated from chunks and never stored as separate sources
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
---
**검증 목표** — 문서를 저장하지 않고 질의로 생성하며 생성 시각과 질의를 적는다는 결정이 생성기와 드리프트 검사로 강제된다는 것이 보여져야 한다. 문서 뷰는 `bazel-bin`에만 있고, 트리에 두는 생성물(BUILD·skill)은 드리프트 검사가 원본과 대조한다.

- **이해관계자**: 업체 · 사람 독자 · **관심사**: 갱신 단절 방지

**무엇을 관측하면 성립하는가**

- ADR·요구 색인·감사 보고서가 `bazel build`로 `bazel-bin/`에 생성되고 머리에 생성 시각(UTC)과 질의가 있다. 소스 트리에 같은 이름의 파일이 없다.
- 트리에 두는 생성물(BUILD·`.claude/skills/*/SKILL.md`)은 원본(frontmatter·도구 docstring)과 어긋나면 `FAIL [build-drift]`·`FAIL [skills-drift]`로 거부된다.
- `//:build_drift_test`·`//:skills_drift_test`가 PASS다.

판정의 원본은 `tools/weave.py`의 `head`, `tools/gen_build.py --check`, `tools/gen_skills.py --check`다.
