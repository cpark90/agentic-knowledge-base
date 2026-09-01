---
iri: https://agentic-knowledge-base.dev/id/chunk-d0049
plane: decision
level: concrete
label_ko: T-Box와 A-Box를 다른 파일에 둔다
label_en: T-Box and A-Box live in separate files
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 개념 정의(T-Box)와 개체(A-Box)를 다른 파일에 둔다. `*-ontology`·
`*-rules`가 T-Box, `*-kg`·`*-space`가 A-Box이며, 0.2절 접미사 규약이 이
분리를 강제한다.

**근거** (노트 2.4절)
- 변경률과 편집 주체가 다르다. T-Box는 변경률이 낮고 설계 에이전트와 유저만
  편집하지만, A-Box는 변경률이 높고 스코프 안의 모든 에이전트가 편집한다.
- 시나리오·scene·실행 기록·결정 인스턴스·링크는 전부 A-Box다. 온톨로지 파일을
  열지 않고도 이것들을 생성·편집할 수 있어야 일반 에이전트가 T-Box 편집
  권한 없이 일할 수 있다.
