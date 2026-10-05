---
id: https://agentic-knowledge-base.dev/id/chunk/931fd393-9a95-498e-b775-a0f4e2276fb6
type: norm
level: logical
title_ko: docs/method.md 절 청크 저작의 이어짐 — 분할 신호와 병합 신호
title: docs/method.md chunk authoring section continued — split signals and merge signals
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/005b8875-a251-4864-a47e-7f261fffe156
continues: true
---
**분할 신호**는 라벨을 하나로 쓸 수 없는 것, 본문 일부만 재사용·가정·`suspect`의 대상이 되는
것이다. **병합 신호**는 두 청크가 항상 함께 읽히는 것, 한쪽이 다른 쪽 없이 이해되지 않는 것,
합쳐도 상한 이하인 것이다. 분할은 라벨을 잇는 조각 하나가 원 uuid를 승계하고 나머지 조각은 새 uuid에
`specializationOf: <원 IRI>`를 적는다. 병합은 한 uuid를 승계하고 나머지를 deprecated로 두어 `supersedes`로
가리킨다. 링크 IRI는 뿌리 uuid로 계산되므로 조각을 가리키는 링크가 원본의 증거·이력을 잇는다
([`p10-split-keeps-work-identity`](../../decision/p10-split-keeps-work-identity/conclusion.md)). 출처는 `prov:wasDerivedFrom`이다.
