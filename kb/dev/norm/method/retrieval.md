---
id: https://agentic-knowledge-base.dev/id/chunk/8b14396c-6b2d-4082-ab9a-6cecb682ae06
type: norm
level: logical
title_ko: docs/method.md 절 — 조회는 라벨 목록에서 작업 집합으로 간다
title: docs/method.md section — retrieval goes from label lists to the workset
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:22:52+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/8fb872fb-34de-4823-8019-358e4f069652
composite: {id: https://agentic-knowledge-base.dev/id/composite/8fb872fb-34de-4823-8019-358e4f069652, title_ko: docs/method.md의 조회·뷰·일반화 절 묶음, title: docs/method.md retrieval, view and generalization section group, part_of: https://agentic-knowledge-base.dev/id/composite/c040ba95-dc6c-4c10-af69-8d0d4c0cf6ec, ordered: [https://agentic-knowledge-base.dev/id/chunk/8b14396c-6b2d-4082-ab9a-6cecb682ae06, https://agentic-knowledge-base.dev/id/chunk/4137bc99-bfe1-4503-8ddb-83b9c7564180, https://agentic-knowledge-base.dev/id/chunk/b5a1192b-b5d0-4ea9-9ff8-719588388644, https://agentic-knowledge-base.dev/id/chunk/dce0da5b-5dfc-4e15-9fa2-a43dc2bd7981, https://agentic-knowledge-base.dev/id/chunk/af0fbe72-b6d1-4f0f-8007-2ac39fed6be9, https://agentic-knowledge-base.dev/id/chunk/a057e7da-4ff1-4d29-b7fb-8048e006ca12]}
heading: 조회
depth: 2
form: bullets
items: [p0-workset-anchor-neighbourhood#3, p11-execution-mode-and-workset#1, p5-plane-assignment-tool-surface#1, p1-context-budget-items#1]
---
**읽기 응답의 기본은 라벨 목록이지 본문이 아니다** (d-0082). 순서는 스코프 → 라벨 목록 →
필요한 것만 펼치기 → 작업 집합이다. 도구는 `bazel build //kg:workset_<role>`이다. 수준 창·앵커는
`defs/kb.bzl`의 규칙 `kb_workset_view` 인자로, 예산은 빌드 설정 `--//kb:budget`으로 준다.
