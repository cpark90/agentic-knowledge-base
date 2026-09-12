---
id: https://agentic-knowledge-base.dev/id/chunk/6321bf38-7026-4c60-b4fb-7cf3a956b35b
type: decision
level: concrete
title_ko: 판정 근거는 검사 가능한 것부터 쓴다
title: Prefer link evidence that can be checked
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0110]
part_of: https://agentic-knowledge-base.dev/id/composite/4f68217b-9725-4607-9748-151d55d543a8
composite: {id: https://agentic-knowledge-base.dev/id/composite/4f68217b-9725-4607-9748-151d55d543a8, title_ko: 판정 근거는 검사 가능한 것부터 쓴다, title: Prefer link evidence that can be checked}
---
**결론** — 링크 판정의 근거는 **검사 가능성이 높은 것부터** 쓴다.

| 후보 | 검사 가능성 | 비고 |
|---|---|---|
| **구축 기록** (9.3절) | **가장 높음** | 만든 주체가 남긴 것 |
| 동시 편집 이력 (같은 커밋) | 높음 | |
| 테스트가 두 항목을 함께 커버 | 높음 | `verifies`의 근거 |
| 임베딩 유사도 | 중간 | **후보 추림에만** |
| 한 세션에서 둘 다 읽음 | 낮음 | 구축 기록의 약한 형태 |

낮은 근거로 확정하지 않는다 — 그 근거는 후보를 만드는 데까지만 쓰인다.
