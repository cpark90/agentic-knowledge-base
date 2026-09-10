---
id: https://agentic-knowledge-base.dev/id/chunk-d0009
type: decision
level: concrete
title_ko: 링크는 구축이 기본, 복원은 예외
title: Links by construction, recovery as exception
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 링크는 산출물이 만들어지는 순간 편집 연산의 부산물로 만든다
(구축). 이미 존재하는 산출물에서 관계를 되짚는 복원은 체계 도입 전
산출물, 외부 유입물, 구축 누락 감사에만 쓴다.

**근거** (노트 8.3절)
- 구축은 만든 주체가 관계를 알기에 정확도가 높고 비용이 낮다. 복원은
  본질적으로 사후 추정이라 정확도가 낮고 비용이 높다.
- 사다리 전이는 refines를, 결정을 읽고 쓴 산출물은 satisfies 후보를,
  조건 참조는 assumes를, 같은 IRI 재작성은 prov:wasRevisionOf를 남긴다.
- **읽기 집합과 쓰기 집합의 인수인계** — 탐색과 편집이 분리된 구조에서는
  탐색의 읽기 집합을 편집 컨텍스트에 후보 링크 목록으로 넘기고, 편집 후
  실제로 쓴 것과 대조해 확정해야 링크가 생긴다.
- 중간 단계(abstract·logical)를 거친 링크는 변화를 흡수한다 — 사다리가
  추적성의 완충 구조다.

**대안** — 임베딩 유사도를 확정 근거로 쓰는 것은 기각 (8.4절). 후보를
추리는 데만 쓰고, 판정은 온톨로지 개념과 역할 정보로 한다.
