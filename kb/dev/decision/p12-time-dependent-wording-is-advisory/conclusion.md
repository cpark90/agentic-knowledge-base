---
id: https://agentic-knowledge-base.dev/id/chunk/2b217004-dffd-4c45-bc52-4081a5cd0a84
type: decision
level: concrete
title_ko: 생성 문서는 시점 의존 표현을 값 대신 쓰지 않고 이 규약은 후보만 보고하는 권장이다
title: Generated documents do not use time-dependent words in place of values, and the rule is advisory with candidates reported only
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/9807be26-ff48-4cca-89c1-129f52e69df4]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5f72b379-57f1-49df-b178-9b9de7afac11
composite: {id: https://agentic-knowledge-base.dev/id/composite/5f72b379-57f1-49df-b178-9b9de7afac11, title_ko: 시점 의존 표현은 권장 규약이다, title: Time-dependent wording is an advisory rule}
---
**결론** — 생성 문서는 시점 의존 표현("현재·최신·지금")을 값 대신 쓰지 않는다. 값은 버전·날짜·수치로 고정한다. 인용 자리는 예외다.

이 규약은 **권장**이고 게이트가 아니다(규약 G17).

- `kb_lib.check_gendoc`은 G17 후보를 둘째 반환값으로 낸다. 게이트 `gendoc`은 그 목록을 판정에 쓰지 않는다.
- 후보 추출은 제목 줄·표 헤더 행·인용 구역·링크 텍스트를 뺀다. 그 자리의 낱말은 이름과 원문이지 측정이 아니다.
- 값 대신 쓰였는가는 사람이 판단한다.

게이트로 올리는 조건은 `p6-mass-fail-suspects-the-rule`의 기준이다. 판정이 기계적으로 갈리고 오탐이 없어야 한다.
