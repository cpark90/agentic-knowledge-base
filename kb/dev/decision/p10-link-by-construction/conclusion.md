---
id: https://agentic-knowledge-base.dev/id/chunk/8d09b0e4-44b4-47b2-9ff6-5da9f3b22e12
type: decision
level: concrete
title_ko: 링크는 구축이 기본이고 복원은 예외다
title: Links are built by construction; recovery is the exception
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T12:20:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0009]
part_of: https://agentic-knowledge-base.dev/id/composite/6651b045-a578-4114-a942-eae19ab99b0c
composite: {id: https://agentic-knowledge-base.dev/id/composite/6651b045-a578-4114-a942-eae19ab99b0c, title_ko: 링크는 구축이 기본이고 복원은 예외다, title: Links are built by construction; recovery is the exception}
---
**결론** — 링크를 만드는 방식은 둘이고, **구축(by construction)이 기본이며 복원(recovery)은 예외다.** 구축은 산출물이 만들어지는 순간에 일어나 정확도가 높고 작업의 부산물이므로 비용이 낮다. 복원은 사후 추정이라 정확도가 낮고 후보 생성·확인 비용이 든다.

**구축의 실체 — 링크는 편집 연산의 부산물이다.** 에이전트가 산출물을 만들 때 하네스가 다음을 기록한다.

| 기록 | 링크 |
|---|---|
| 계층 전이 (6.2절) | `refines` |
| 결정을 읽고 코드를 씀 | `satisfies` 후보 |
| 결정을 읽고 결정을 씀 | `derives-from` 후보 |
| 스코프의 조건을 참조함 | `assumes` |
| 같은 IRI의 본문을 다시 씀 | `prov:wasRevisionOf` |
| 본문에 식별자를 적음 (`d-NNNN` · `agt:Term`) | `cites` · `usesConcept` — 추출(`extract_refs`)은 이 기록을 읽는 것이지 사후 추정이 아니다 (유저 결정 2026-09-12) |

**복원은 셋에만 쓴다** — 이 체계 도입 전 산출물, 외부에서 가져온 산출물, 구축이 누락된 것의 감사.
