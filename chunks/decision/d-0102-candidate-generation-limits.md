---
iri: https://agentic-knowledge-base.dev/id/chunk-d0102
plane: decision
level: concrete
label_ko: 후보 링크의 출처와 상한
label_en: Candidate link sources and their upper bounds
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 후보 링크는 링크 타입별로 정해진 출처에서 가져오고, 각 출처는
**상한**을 갖는다.

- `refines` — 8.3절 구축 기록. 전이 시점에 하나. 상한 1
- `satisfies` — 편집 컨텍스트가 읽은 `decision` 청크(8.3절 인수인계).
  상한은 읽은 수
- `constrains` — 같은 구성체 안의 `schema`·`contract` 청크. 상한은 구성체 크기
- `verifies` — 시나리오의 scene이 참조하는 청크. 상한은 scene 수
- `assumes` — 스코프가 inherit한 ODD 속성. 상한은 속성 수
- 복원(8.4절) — 임베딩 상위 k. 상한 k ≤ 7

**근거** (노트 7.7절)
- **상한이 있어야 후보 집합이 청크 라벨 목록에 들어간다** — 후보가
  무제한이면 유저에게도 에이전트에게도 제시할 수 없다.
- 복원의 k도 7±2 원칙을 따른다.

**대안**
- 타입별 출처 목록 자체는 **미확정**(노트 `[안]`) — 상한을 둔다는 원칙만
  확정이다.
