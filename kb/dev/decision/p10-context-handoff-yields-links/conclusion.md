---
id: https://agentic-knowledge-base.dev/id/chunk/92762c1c-18df-4b8e-9b9d-9d43e4811e0f
type: decision
level: concrete
title_ko: 조회·편집·추론 세 컨텍스트의 경계에서 링크 재료가 넘어간다
title: Link material crosses the boundaries of the retrieval, edit and reasoning contexts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
part_of: https://agentic-knowledge-base.dev/id/composite/65989bd8-c9ca-4659-8069-5b9913ce7b7e
composite: {id: https://agentic-knowledge-base.dev/id/composite/65989bd8-c9ca-4659-8069-5b9913ce7b7e, title_ko: 조회·편집·추론 세 컨텍스트의 경계에서 링크 재료가 넘어간다, title: Link material crosses the boundaries of the retrieval, edit and reasoning contexts}
---
**결론** — 검사·계획·실행을 한 컨텍스트에 뒤섞지 않고 셋으로 분해한다 — **조회 컨텍스트**(질의를 받아 관련 청크만 반환), **편집 컨텍스트**(대상과 지시를 받아 수정만 실행), **추론 컨텍스트**(무엇을 바꿀지 결정). 관계는 **컨텍스트 경계에서 명시적으로 넘겨진다.**

| 경계 | 넘어가는 것 | 링크의 재료 |
|---|---|---|
| 추론 → 조회 | 질의 (자연어 + 온톨로지 개념) | — |
| 조회 → 추론 | 읽기 집합 (청크 라벨 + 펼친 본문) | `satisfies`·`derives-from` 후보 |
| 추론 → 편집 | 대상 청크 IRI + **편집 지시** | `refines` 근거 |
| 편집 → 추론 | 쓰기 집합 (변경된 청크) | 후보와 대조해 확정 |

**편집 지시가 의도의 명시적 표현이다.** 형식 문법(찾아-바꾸기)이 아니라 의도를 담은 지시로 넘기고, 실행은 편집 컨텍스트가 담당한다.
