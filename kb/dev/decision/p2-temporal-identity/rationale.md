---
id: https://agentic-knowledge-base.dev/id/chunk/18465672-aa51-43e4-9d02-53fbb6da158e
type: decision
level: logical
title_ko: 정체성이 없으면 개정마다 링크가 끊어진다
title: Without identity, every revision severs the links
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/215abd9c-4b8f-458e-aec7-6d09034dd8bd
---
**근거** (노트 2.6절) — 같은 결정, 같은 시그니처, 같은 모듈이 시간이 지나며 변한다. 변한 뒤에도 "같은 것"으로 추적되어야 5.4절 무효화 전파와 Part X 링크가 성립한다. 시간 정체성을 명시하지 않으면 매 개정마다 새 개체가 생겨 그것을 가리키던 링크가 전부 끊어진다.

정체성 관계를 새로 만들지 않는 것은 0.0절 표준어 원칙이다. PROV-O에 이미 있는 `wasRevisionOf`가 개정 연쇄를 표현하고, IRI 불투명성(0.7절)이 정체성을 이름에서 분리한다.
