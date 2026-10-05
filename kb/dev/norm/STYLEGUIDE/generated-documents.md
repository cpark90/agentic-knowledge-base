---
id: https://agentic-knowledge-base.dev/id/chunk/e8358b4b-f328-470d-951c-72cc930678d1
type: norm
level: logical
title_ko: STYLEGUIDE.md 절 — 생성 문서 (`bazel-bin/**/*.md` · 생성 트리 파일)
title: STYLEGUIDE.md section — Generated documents
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/390d6694-f163-4cd2-911e-bd351e11eaf4
heading: 생성 문서 (`bazel-bin/**/*.md` · 생성 트리 파일)
depth: 2
items: [p12-generated-document-header#1, p12-generated-document-header#2, p12-generated-document-header#3, p12-generated-document-form#1, p12-generated-document-form#2, p12-generated-document-form#3, p12-generated-document-form#4, p12-generated-document-form#5, p12-generated-document-form#6, p12-generated-document-form#7, p12-generated-document-form#8, p12-generated-document-input-section#1, p12-generated-document-form#9, p12-time-dependent-wording-is-advisory#1]
---
도구가 내는 마크다운이다. 사람이 쓰지 않는다. 쓰는 것은 **생성기**이므로 이 절의 대상은
`tools/*.py`의 출력 문자열이다. 규약의 원본은 결정 셋
([`p12-generated-document-header`](../../decision/p12-generated-document-header/conclusion.md) ·
[`p12-generated-document-form`](../../decision/p12-generated-document-form/conclusion.md) ·
[`p12-generated-documents-are-gated`](../../decision/p12-generated-documents-are-gated/conclusion.md))이고,
구현의 단일 정의처는 `tools/kb_lib.py`이며, 게이트 `gendoc`이 강제한다. 외부 출처는
[`docs/references.md`](../../../../docs/references.md) §생성 문서 작성에 있다.
