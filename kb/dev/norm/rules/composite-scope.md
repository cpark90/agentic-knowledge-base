---
id: https://agentic-knowledge-base.dev/id/chunk/56c61b87-dfb8-4f29-b1c5-2d9faeddc958
type: norm
level: logical
title_ko: docs/rules.md 절 복합체의 이어짐 — 묶는 기준·결정 복합체·kb_composite
title: docs/rules.md composite section continued — grouping criteria, decision composites and kb_composite
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:36:31+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e2326375-ac83-490d-ab30-09a01c5f73f0
continues: true
---
**모든 chunk가 복합체에 속할 필요는 없다** (유저 결정 2026-09-02). 통합이 필요한 것만
묶고 나머지는 개별로 둔다. 통합의 기준은 둘이다. 첫째는 **함께 읽혀야 이해되는가**(병합 신호,
[p4-chunk-split-and-merge](../../decision/p4-chunk-split-and-merge/conclusion.md))이고, 둘째는 **순서가 뜻을 갖는가**([p4-composite-as-part-of](../../decision/p4-composite-as-part-of/conclusion.md))다. 셋째 기준인 "무효화가 함께 번져야 하는가"는
복합체가 아니라 링크(`relatedTo`)로 표현한다 (§4 링크 타입 표). 복합체 **후보**는 커뮤니티 탐지가
제안하고 채택은 사람이 한다 ([`p4-community-detection-proposes-composites`](../../decision/p4-community-detection-proposes-composites/conclusion.md)).

**결정은 세 청크의 복합체다** (노트 4.7절·7.4절, 유저 결정 C2). 결론은 concrete, 근거는 logical,
대안은 logical이다. 대안은 **필수**이며 "대안 없었음"도 기록한다. 세 청크는
`kb/dev/decision/<파트>-<슬러그>/` 디렉토리 하나에 살고, 복합체 개체는 conclusion의 frontmatter
선언에서 `chunk2kg`가 생성한다. 이 복합체는 level이 섞이므로 동질성 규칙과 긴장했다. 그 긴장은
[`p4-composition-rules`](../../decision/p4-composition-rules/conventions.md)의 규약이 결정 복합체를 동질성의 level 예외로 정해 닫혔다(2026-09-13).

**결정 밖의 복합체는 `kb_composite`로 선다** (유저 답 2026-09-26, 도구를 고친다). 묶음의 단위는 파일이 아니라
**액션의 입력 집합**이다 — 같은 패키지에서 `composite.id`를 공유하는 청크 2~9개가 타깃 하나가 되고 부분 청크의
개별 `kb_chunk` 타깃은 사라진다. 타깃 이름은 `composite:`를 선언한 청크의 파일 이름이다. 부분과 선언은 같은
패키지에 있어야 하고 부분의 plane·level은 서로 같아야 한다. 판정은 세 시점이다 — 생성 시점 `tools/gen_build.py`의
`_check_bundle`, 분석 시점 `kb_composite`(`plane`·`level`을 한 쌍만 받으므로 이질 복합체를 표현할 수 없다), 그래프
verify 질의 `composite-heterogeneous`. 수준 혼합은 결정 복합체의 예외뿐이다. 손으로 쓴 `kg/composite-kg.ttl`의
복합체는 이 경로로 옮기고, 부분이 하나인 것은 복합체가 아니므로 남기지 않는다. 복합체 IRI는 지속 IRI 원칙대로
기존 `id:comp-*`를 유지한다.
