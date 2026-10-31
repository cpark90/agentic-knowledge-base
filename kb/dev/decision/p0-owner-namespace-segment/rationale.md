---
id: https://agentic-knowledge-base.dev/id/chunk/3c38797e-70a8-475a-9f1f-3eeb0f3c5aef
type: decision
level: concrete
title_ko: 세그먼트가 소유권 경계여서 이름 충돌을 구조로 막고 개체 IRI와 문서 IRI를 가른다
title: The segment is the ownership boundary, so it blocks name collisions structurally and keeps entity IRIs apart from document IRIs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0158-owner-namespace-segment.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:34:53+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:34:53+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c6b1526b-31e7-41f3-9f13-9cc419803e2d
---
**근거** — 출처는 harness-functional `docs/federation-design.md`의 D3이다.

- 세그먼트가 없으면 두 기여자가 우연히 같은 이름을 쓴 순간 union에서 **같은 IRI로 병합**되어 서로 다른 두 개체가 조용히 뒤섞인다. 세그먼트가 곧 소유권 경계이며, 이름 충돌을 사회적 합의가 아니라 구조로 막는다.
- 본문을 prefix로만 다루면 소유자가 바뀌어도 노드 블록은 그대로다. 다른 소유자의 노드를 참조할 때는 그 소유자용 prefix를 하나 더 선언한다. 두 prefix가 같은 네임스페이스를 가리키므로 union에서 같은 IRI로 해석되고, 그래서 **저장소를 가로지르는 간선이 실제로 성립**한다.
- **개체 IRI와 그 개체를 담는 문서 IRI는 다르다.** import와 카탈로그가 다루는 것은 문서 IRI이므로, 둘을 섞으면 파일을 쪼개는 순간 개체 IRI가 따라 바뀐다. 실제로 공용 부품을 타입별 문서로 분할할 때 문서 IRI만 늘고 개체 IRI는 그대로였으며, 이것이 분할을 값싸게 만든다.

이 규칙은 IRI 설계(`p0-iri-design`)가 정한 지속성 축과 직교하는 축이다. `p0-iri-design`은 한 저장소 안에서 이름이 바뀌어도 정체성이 유지되게 하고, 이 규칙은 여러 저장소가 서로의 이름을 침범하지 않게 한다.
