---
id: https://agentic-knowledge-base.dev/id/chunk/5f5f5f68-edef-4633-bed8-784e67d1dac5
type: decision
level: concrete
title_ko: 규범 문서 규약 — 전제는 가정으로 만들어 assumes로 가리키고 고유 전제를 적기 전에는 기본 가정을 가리킨다
title: Normative-document conventions — A premise becomes an assumption referenced by assumes, and the default assumption holds the place until the item's own premise is written
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c6086cf0-0a2c-47d6-96d4-644307e4529c
---
**규약** — `p0-premise-as-assumption`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **전제가 있으면 가정을 만들고 `assumes`로 가리킨다.** 가정은 ODD 조건 위의 명제다. 고유 전제를 아직 적지 않은 청크는 기본 가정 `id:asm-chunk-conventions`를 `assumes`하고, 실제 전제가 드러나면 고유 가정을 앞에 더한다. 기본 가정만 가진 항목은 전제를 아직 적지 않은 것이다. 리뷰에서 잡는다.
