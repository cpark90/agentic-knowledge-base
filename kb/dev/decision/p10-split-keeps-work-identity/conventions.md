---
id: https://agentic-knowledge-base.dev/id/chunk/d20dbb49-c4af-4d12-8c67-8188a25a0028
type: decision
level: concrete
title_ko: 규범 문서 규약 — 분할은 조각 하나가 uuid를 승계하고 나머지는 specializationOf로 이으며 링크 IRI는 뿌리 uuid로 계산한다
title: Normative-document conventions — A split passes the uuid to one fragment, links the rest by specializationOf, and link IRIs use the root uuid
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a76160fc-059f-437e-8f64-6e6c405cd18b
---
**규약** — `p10-split-keeps-work-identity`의 결론을 규범 문서에 싣는 문장이다.

규약: [권장] ID는 재사용하지 않는다. 폐기는 `state`/`deprecated`로 남기고 새 IRI를 만든다. 분할은 조각 하나가 uuid를 승계하고 나머지는 `specializationOf`로, 병합은 `supersedes`로 잇는다. 출처는 `prov:wasDerivedFrom`이다.
