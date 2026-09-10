---
id: https://agentic-knowledge-base.dev/id/chunk/7e000f55-4c04-4ed7-b4fb-691162204745
type: decision
level: logical
title_ko: 링크 타입별 후보 출처 표
title: Per-type candidate sources
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc
---
**대안** `[안]` — 링크 타입별로 후보를 어디서 가져오는가의 초기 목록. 미확정이다.

| 링크 타입 | 후보 출처 | 상한 |
|---|---|---|
| `refines` | 9.3절 구축 기록. 전이 시점에 하나 | 1 |
| `satisfies` | 편집 컨텍스트가 읽은 `decision` 청크 | 읽은 수 |
| `constrains` | 같은 복합체 안의 `schema`·`contract` 청크 | 복합체 크기 |
| `verifies` | 같은 전이에서 태어난 logical 기준 (6.8절) | 기준 수 |
| `assumes` | 스코프가 inherit한 ODD 속성 | 속성 수 |
| 복원 (9.4절) | 임베딩 상위 k | k ≤ 7 |
