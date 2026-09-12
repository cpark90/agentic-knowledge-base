---
id: https://agentic-knowledge-base.dev/id/chunk/9d3f4240-66d0-4dfd-9124-9499e65cb57a
type: decision
level: concrete
title_ko: 본문 중복은 안전율로 용인하되 coUpdatesWith로 묶고 재검증 시점에서 정리한다
title: Body redundancy is tolerated as a safety margin, linked by coUpdatesWith, consolidated at revalidation points
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-label-representativeness-protocol}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
part_of: https://agentic-knowledge-base.dev/id/composite/6053b67e-afec-4a59-b710-31b6ab85b108
composite: {id: https://agentic-knowledge-base.dev/id/composite/6053b67e-afec-4a59-b710-31b6ab85b108, title_ko: 중복의 용인과 주기적 정리, title: Redundancy tolerance and periodic consolidation}
---
**결론** — 같은 내용이 여러 청크에 반복되는 것을 **안전율**로 용인한다. 단 용인의
범위와 조건이 있다 (유저 결정 2026-09-11).

| 층 | 같은 내용의 반복 | 판정 |
|---|---|---|
| T-Box 개념·용어 | 같은 뜻의 개념 둘 | 용인 불가 — 한 단어 한 개념, 만들기 전에 검색 |
| `requirement` | 같은 관심사의 요구 둘 | 용인 불가 — refines 연쇄가 갈라져 추적 커버리지가 왜곡 |
| 라벨 | 다른 청크에 같은 라벨 | 용인 불가 — 라벨이 인터페이스다 |
| 청크 **본문** (결정 부분·주석·관측) | 같은 서술이 여러 청크에 | **용인** |

조건 셋:

1. **알고 둔 중복은 `coUpdatesWith`로 묶는다.** 한쪽이 바뀌면 다른 쪽이 `suspect`가
   되어 정리 큐에 오른다. **링크 없는 중복은 안전율이 아니라 드리프트**다.
2. **다른 스코프 사이의 중복은 안전율, 같은 작업 집합 안의 중복은 정리 대상**이다 —
   후자는 같이 펼쳐져 컨텍스트 예산만 먹는다.
3. **정리는 재검증 시점에서 일괄로 한다** — 편집마다 하지 않는다. `consistency` 보고는
   커밋마다 자동, 병합·묶기·유지 판정은 도입 단계 끝마다. 판정 근거는 관측으로 남긴다.
