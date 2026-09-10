---
id: https://agentic-knowledge-base.dev/id/chunk/85ac72bf-a4f7-4397-a766-7b9dbb90994a
type: decision
level: concrete
title_ko: 선별·값 할당·폐쇄 선언 세 연산이 ODD를 만든다
title: Selection, valuation, and closure make the ODD
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
part_of: https://agentic-knowledge-base.dev/id/composite/4640aa0e-49a7-4fee-952d-e33ec4d57cbb
composite: {id: https://agentic-knowledge-base.dev/id/composite/4640aa0e-49a7-4fee-952d-e33ec4d57cbb, title_ko: ODD는 온톨로지의 닫힌 뷰이다, title: The ODD is a closed projection of the ontology}
---
**결론** — ODD의 어휘는 전부 온톨로지에서 온다. 그러나 ODD는 온톨로지가 아니라 **세 연산의 결과**다.

- **선별** — `related/condition`의 개념 중 이 프로젝트가 다루는 것만 고른다
- **값 할당** — 선별된 각 속성에 값 또는 범위와 판정 방법을 붙인다
- **폐쇄 선언** — 나열하지 않은 것은 영역 밖임을 선언한다 (`mode restrictive`)

**세 번째 연산이 ODD를 온톨로지와 구분한다.** 온톨로지는 개방 세계 가정을 따라 명시되지 않은 것이 미지이지만, ODD의 restrictive 모드는 닫힌 세계여서 나열하지 않은 것은 밖이다.

두 번째 연산도 구분의 근거다 — 값 할당은 개체를 만드는 일이므로 **A-Box**이고 온톨로지는 T-Box다 (2.4절). 파일 접미사가 이 분리를 강제한다.

온톨로지가 어휘라면 ODD는 그 어휘로 쓴 **첫 번째 문서**다. 스코프·가정·요구·설계 공간은 전부 ODD 안에서 쓴다.
