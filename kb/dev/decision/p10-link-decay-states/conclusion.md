---
id: https://agentic-knowledge-base.dev/id/chunk/fd6617a6-5387-4059-9014-faf6ad5effcf
type: decision
level: concrete
title_ko: 링크의 붕괴는 세 상태로 관리하고 경계에서 일괄 재판정한다
title: Link decay is tracked in three states and rejudged in batches at boundaries
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0106, https://agentic-knowledge-base.dev/id/chunk-d0107]
part_of: https://agentic-knowledge-base.dev/id/composite/c88e9891-e992-4e33-a891-0dcba05746b3
composite: {id: https://agentic-knowledge-base.dev/id/composite/c88e9891-e992-4e33-a891-0dcba05746b3, title_ko: 링크의 붕괴는 세 상태로 관리하고 경계에서 일괄 재판정한다, title: Link decay is tracked in three states and rejudged in batches at boundaries}
---
**결론** — 링크는 가정(6.5절)과 같은 상태를 갖는다 — `valid`(양 끝이 마지막 확정 이후 바뀌지 않음), `suspect`(양 끝 중 하나가 바뀜, 트리거는 편집 통지), `invalid`(재검토 결과 관계가 성립하지 않음).

**변경 통지가 트리거다.** 링크 모델은 양 끝 산출물의 변경을 구독하고, 변경이 오면 링크를 `suspect`로 바꾼다. **재판정은 즉시 하지 않는다** — 커밋이나 세션 종료 같은 경계에서 일괄 재판정한다.

**재판정은 규칙부터 시도한다.** 알려진 변경 패턴은 규칙으로 자동 갱신하고, 규칙에 없는 변경만 9.4절 판정으로 보낸다.

편집 직후의 재판정 대상은 셋으로 고정한다 — **참조 무결성**(양 끝이 살아 있는가), **용어 일관성**(prefLabel만 쓰였는가), **의미 정합**(구성체 안에서 모순이 없는가).
