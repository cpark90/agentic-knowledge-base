---
id: https://agentic-knowledge-base.dev/id/chunk/56e06c99-9d2f-4dbb-b207-aa6dbbe39761
type: decision
level: concrete
title_ko: 중앙이 도메인을 모르고 부품을 IRI로 참조해야 중립성과 재사용이 유지된다
title: Neutrality and reuse hold only if the centre knows no domain and parts are referenced by IRI
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0018-recipe-assembly-spec.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:21:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:21:21+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/34c7f15b-534a-47b4-813a-16c2edda3703
---
**근거** — 출처는 harness-concrete `README`다.

- 중앙 라이브러리는 의도적으로 중립을 유지한다. 특정 하네스 하나를 기술하는 순간 중립성이 깨지고 재사용이 막히기 때문이다.
- 중앙은 도메인을 결코 알지 못하고, 모든 도메인 노드는 레시피 쪽에 산다. 도메인 지식이 한쪽으로만 흘러 들어오므로 중앙의 어휘가 오염되지 않는다.
- 부품 결합은 복사가 아니라 IRI 참조다. 그래서 중앙 부품이 개선되면 모든 레시피가 그 개선을 받는다.

이 결정은 온톨로지 코어와 확장의 원칙(노트 2.3절)의 A-Box판이다. 그 원칙은 최상위가 import만 하고 확장은 새 모듈의 추가로만 한다는 것이다. 도메인 프로파일(2.11절)이 코어와 분리되는 것과 같은 구도다.
