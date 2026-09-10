---
id: https://agentic-knowledge-base.dev/id/chunk-d0083
type: decision
level: concrete
title_ko: 판정 도구 없는 plane은 검사 게이트를 통과할 수 없다
title: A plane without a verification tool cannot pass the gate
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 각 plane의 "판정 방식"을 실제 도구에 대응시키고, **판정 도구가
없는 plane은 검사 게이트를 통과할 수 없다**고 둔다.

| plane | 판정 도구 | 자동화 |
|---|---|---|
| `decision` | 논증 구조 검사(결론·근거·대안 존재), 상위 결정과의 모순 검사(`supersedes` 순환) | 부분 |
| `schema` | 스키마 검사기, 호환성 검사기 | 전체 |
| `contract` | 타입 체커, 컴파일러 | 전체 |
| `artifact` | 컴파일, 테스트, 린터 | 전체 |
| `annotation` | 해소 상태 존재 여부만 | 전체 |
| `memory` | 없음 | — |

**근거** (노트 5.4절)
- 판정 방식은 plane의 정의이지만 그 자체로는 게이트가 되지 못한다. 실행
  가능한 도구로 내려와야 `concrete → executable` 전이 게이트(6.8절)가
  성립한다.
- `annotation`은 **해소 상태만** 검사하고 내용은 검사하지 않는다. 논평의
  타당성은 사회적 합의이지 기계 판정 대상이 아니다.
- `memory`는 판정 도구가 없으므로 게이트 대상이 아니다 — 휘발성 관측을
  검사하려는 시도 자체가 plane 정의에 어긋난다.
