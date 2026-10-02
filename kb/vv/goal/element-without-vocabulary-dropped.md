---
id: https://agentic-knowledge-base.dev/id/chunk/b055c55f-c77b-421f-8cc0-d1e832f7b207
type: requirement
level: functional
pattern: unwanted-behaviour
title_ko: 어휘가 없는 소스 요소가 산출물에서 빠지면 그 탈락이 수로 드러나야 한다
title: When a source element without vocabulary is dropped from the output, the drop must surface as a count
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/elementWithoutVocabularyDropped]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
---
**검증 목표** — 소스에 있으나 어휘에 슬롯이 없는 요소가 방출에서 빠질 때 그 탈락이 0이 아닌 수로 드러난다는 것이 보여져야 한다. 이 목표가 다루는 위험은 현상 `agt:elementWithoutVocabularyDropped`(P19)이고 규범은 가정 `id:asm-missing-vocabulary-is-signal`이다.

- **이해관계자**: 온톨로지 편집 역할 · 검증자 · **관심사**: 어휘 확장 신호가 묻히지 않는 것

**무엇을 관측하면 성립하는가**

- 소스 요소의 전수와 방출 요소의 전수가 대조되고 그 차가 수로 나온다. 차가 0이 아니면 그 요소의 이름이 어휘 확장 후보로 올라간다.
- 어휘를 베낀 표(`tools/chunk2kg.py`의 `PROFILE_SUBSTANCE`)의 치역이 온톨로지 `kb/ontology/profile/development/plane-substance-ontology.ttl`의 정의 집합과 같다. 표가 뒤처지면 그 plane의 실체가 조용히 빠진다.
- 알려진 키 집합 밖의 frontmatter 키가 무시되지 않고 세어진다. 지금 `chunk2kg`는 알 수 없는 키를 거부하지도 세지도 않는다.
- 이 목표의 표본 근거는 참조 저장소 `../harness-functional`의 실측 실패 R3이다. 반영이 알려진 요소 집합에서 조립되는 방식이라 어휘 없는 소스 요소가 슬롯을 얻지 못해 빠졌다.
- 기존 검증 목표 35건은 게이트·음성 시험을 사슬로 묶은 것이고 이 목표는 위험 분석 G1의 현상에서 나왔다. 파생의 표지는 본문의 현상 IRI 인용이며 `agt:usesConcept`로 질의된다.
