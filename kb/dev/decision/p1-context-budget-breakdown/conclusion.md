---
id: https://agentic-knowledge-base.dev/id/chunk/de38da18-3de5-4b30-86d6-af112ca9659c
type: decision
level: concrete
title_ko: 컨텍스트 예산은 항목별로 분해하고 지식 본문은 잔여로 둔다
title: Decompose the context budget; knowledge body gets the remainder
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0036, https://agentic-knowledge-base.dev/id/chunk-d0041]
part_of: https://agentic-knowledge-base.dev/id/composite/ee6bf20f-7b60-4ee8-8681-af13f995682d
composite: {id: https://agentic-knowledge-base.dev/id/composite/ee6bf20f-7b60-4ee8-8681-af13f995682d, title_ko: 컨텍스트 예산의 분해, title: Context budget breakdown}
---
**결론** — 에이전트가 한 번에 파악하는 맥락은 200줄 안팎이고, 이 수치가 모든
결정의 출발점이다. 200줄은 전부 지식에 쓰이지 않으므로 예산을 항목별로 분해해
각각 다른 수단으로 통제하고, **지식 청크 본문은 잔여**로 둔다.

| 항목 | 예상 소비 | 통제 수단 |
|---|---|---|
| 하네스 지시 (역할·규칙) | 고정 | 짧게 — 온톨로지 어휘로 압축 |
| 작업 집합 (0.5절) | 라벨 목록 + 펼친 청크 | 스코프가 상한 |
| 툴 출력 | 가변, 위험 | 5.3절 읽기 응답 형태로 제한 |
| 대화 이력 | 누적 | 실행 모드(10.3절)로 주기적 비우기 |
| 지식 청크 본문 | **남는 것** | — |
