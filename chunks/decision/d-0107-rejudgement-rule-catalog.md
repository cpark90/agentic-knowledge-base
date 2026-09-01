---
iri: https://agentic-knowledge-base.dev/id/chunk-d0107
plane: decision
level: concrete
label_ko: 재판정 규칙 카탈로그
label_en: Re-judgement rule catalog
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 8.6절이 "규칙으로 자동 갱신"이라 한 변경 패턴의 초기 목록.
이 목록에 있는 변경은 링크 상태를 규칙으로 바꾸고, 없는 변경만 판정
(8.4절)으로 보낸다.

**규칙** (노트 8.11절)
- 청크 **라벨만 변경** — 링크 영향 없음. `valid` 유지
- **본문 변경**(해시 변경) — `suspect`. 재판정 큐
- 시그니처 **이름만 변경, 타입 동일** — `satisfies` 유지, `valid`
- 시그니처 **타입 변경** — `constrains` 재검토, `suspect`
- 청크 **분할** — 옛 링크를 두 새 IRI로 복제, 각각 `candidate`
- 청크 **병합** — 두 링크를 합집합, 중복 제거, `candidate`
- 청크 **폐기** — 링크 `invalid`. 대체 청크로 후보 생성
- 상위 결정 `supersedes` — 옛 결정의 `satisfies` 전부 `suspect`

**대안**
- 이 카탈로그는 **미확정**(노트 `[안]`) — 초기 목록이며 확장·수정된다.
  규칙을 먼저 시도한다는 원칙(8.6절)만 확정이다.
