---
iri: https://agentic-knowledge-base.dev/id/chunk-d0127
plane: decision
level: concrete
label_ko: 단기·장기 구분과 메모리 승격 규칙
label_en: Short-term vs long-term memory and the promotion rule
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 지식 **생산 시점에** 단기·장기를 구분한다. 단기기억은 `memory`
plane에 두고 첫 실행 시 한 번에 읽으며, 장기기억은 주제 plane으로 승격해
필요한 순간에 읽는다. 승격 규칙(언제, 무엇을)은 체계가 고정하지 않는
**입력**이다.

**근거** (노트 9.4절)
- 승격은 6.3절 상승의 최소 단위다. 설계 판단이면 `decision`, 코드 논평이면
  `annotation`으로 올라간다.
- 무엇이 오래 남을 지식인지는 프로젝트마다 다르므로 규칙을 유저가 준다.
  규칙이 바뀌면 `memory` plane 비우기 정책이 바뀐다 (9.1절 파급).
- 세션 유지 모드의 컨텍스트 누적을 비우는 것이 이 규칙이다 (9.3절) —
  승격 규칙이 없으면 `memory`가 무한히 커져 컨텍스트 예산을 잠식한다.
- 읽는 시점이 다른 것이 두 저장 위치를 가르는 기준이다. 첫 실행 시 한 번에
  들어가야 하는 것만 단기기억이다.
