---
id: https://agentic-knowledge-base.dev/id/chunk/09ec638e-da51-455f-af35-fc6fb1c7793e
type: decision
level: concrete
title_ko: 저장소를 가로지르는 간선은 양쪽이 union에 있어야 판정되고 좁은 게이트의 통과는 파급이 없다는 증거가 아니다
title: Cross-repository edges are judged only with both ends in the union, and a narrow green gate is no evidence of no ripple
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0157-validate-the-union.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:32:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:32:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/6e580ff9-3d4a-423c-987d-4724894725a5
---
**근거** — 출처는 harness-functional `docs/federation-design.md`의 D4다.

- 저장소를 가로지르는 간선, 곧 A의 개체가 B의 개체를 참조하는 간선은 양쪽이 union에 들어와야 도달성 검사와 타입 검사가 성립한다. 그래서 조립(`p2-catalog-resolved-union`)과 검증은 한 설계의 양면이고, 조립 방식은 검증할 union이 하나 있다는 사실을 보존해야 한다.
- **좁은 게이트가 초록인 것은 파급이 없다는 증거가 아니다.** 어휘만 있는 저장소의 단독 게이트는 개체가 0이어서 연결성 축이 공허하게 통과한다. 개체가 있어야 걸리는 불변식은 개체가 사는 쪽의 union 게이트가 강제한다.
- 따라서 어휘가 바뀌면 데이터가 한 줄도 바뀌지 않아도 데이터 쪽의 **전량 재검증**이 필요하다. 이 파급을 ODD의 조건부 규정으로 명문화해 잊히지 않게 한다.
- 어휘는 fork하지 않는다. 데이터 저장소가 중앙 어휘에 **conform**하는 것이 저장소를 가로지르는 drift 방지의 실체다. 어휘를 복사하는 순간 사본마다 뜻이 갈라지고, union은 같은 이름의 다른 개념을 담게 된다.

이 결정은 세 방어선(`p6-three-failure-mode-defences`)의 적용 대상을 정한다. 방어선은 파일이 아니라 union에 건다.
