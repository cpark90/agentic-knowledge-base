---
id: https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc
type: artifact
level: executable
title_ko: 파일 defs/kb.bzl
title: file defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/c5bb1922-eb82-4b96-a49c-a46e41c239e4, https://agentic-knowledge-base.dev/id/chunk/ee51de32-a48b-4ade-a147-4953bce27364, https://agentic-knowledge-base.dev/id/chunk/af618b63-841a-4c19-a935-62ec246c2218, https://agentic-knowledge-base.dev/id/chunk/525c2b08-d69e-41f1-bbcd-fbffa082a5eb]
composite: {id: https://agentic-knowledge-base.dev/id/composite/9a583117-c61c-48f7-b30a-f60bddda9bfe, title_ko: 파일 복합체 defs/kb.bzl, title: file composite defs/kb.bzl, ordered: [https://agentic-knowledge-base.dev/id/chunk/a0bfff7b-bee9-4e2a-91c8-0640117414d1, https://agentic-knowledge-base.dev/id/chunk/c8ca6ad0-31b7-43b9-bca5-a31871f4ee1b, https://agentic-knowledge-base.dev/id/chunk/e8380930-b5fb-496b-bd8a-5c1baa7c9ea3, https://agentic-knowledge-base.dev/id/composite/b5154bf0-e67d-4227-8b66-c63012041201, https://agentic-knowledge-base.dev/id/composite/84e893d0-8cc4-4710-b3b9-3885ce121377]}
---
**파일** — `defs/kb.bzl` 다. 689줄 · 최상위 정의 10개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**배선** — 입력 집합과 인자를 잇기만 하는 최상위 이름 12개를 청크로 내지 않았다 (등록부 `wiring`): `norm_doc_labels` · `_lint_action` · `_head_action` · `_composite_outputs` · `_kb_ontology_module_impl` · `kb_ontology_module` · `_kb_bundle_impl` · `kb_bundle` · `_kb_kg_merge_impl` · `kb_kg_merge` · `_kb_workset_view_impl` · `kb_workset_view`.

**모듈 머리** — 모듈 docstring 과 `load` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
load("@bazel_skylib//rules:common_settings.bzl", "BuildSettingInfo")

"""지식 항목을 Bazel 타깃으로 — provider·규칙·가시성 (bazel-dependency-review B + 연결성, 2026-09-11).

원칙: 의존의 원본은 그래프(frontmatter·owl:imports)이고 BUILD는 생성물(tools/gen_build.py)이다.
Bazel이 맡는 것은 링크의 **구조** — 끝점의 존재(로드 시점), 방향(가시성·분석 시점 fail), 파급(rdeps).
링크의 **의미**(SHACL·통제 어휘·상태 전이)는 그래프 게이트(d-0157 union)가 그대로 맡는다.
"""
```
<!-- 인용 끝 -->
