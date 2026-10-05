---
id: https://agentic-knowledge-base.dev/id/chunk/a2ee370f-ac4d-49e8-a688-4c9b4ff541dd
type: decision
level: concrete
title_ko: 규범 문서 규약 — 조회·편집·추론 세 컨텍스트의 경계에서 링크 재료가 넘어간다
title: Normative-document conventions — Link material crosses the boundaries of the retrieval, edit and reasoning contexts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/65989bd8-c9ca-4659-8069-5b9913ce7b7e
---
**규약** — `p10-context-handoff-yields-links`의 결론을 규범 문서에 싣는 문장이다.

규약: 탐색의 **읽기 집합**을 편집 컨텍스트에 후보 목록으로 넘기고, 편집 후 **쓰기 집합**과 대조해 확정한다. 하네스의 도구가 읽기·쓰기를 기록하지 않으면 이 절차가 성립하지 않는다. 첫 형태는 `bazel build //kg:workset --//kb:anchor=…`로 펼친 청크를 `bazel run //tools:handoff`가 새 청크의 `sources`에 옮기는 것이다.
