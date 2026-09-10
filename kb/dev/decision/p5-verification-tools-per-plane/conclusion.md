---
id: https://agentic-knowledge-base.dev/id/chunk/0feae549-1641-4f26-95d1-067e531e8945
type: decision
level: concrete
title_ko: 판정 도구 없는 plane은 검사 게이트를 통과할 수 없다
title: A plane without a verification tool cannot pass the gate
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0083]
part_of: https://agentic-knowledge-base.dev/id/composite/e41d8f22-3084-4182-870e-8abbf9f95076
composite: {id: https://agentic-knowledge-base.dev/id/composite/e41d8f22-3084-4182-870e-8abbf9f95076, title_ko: plane별 판정 도구, title: Verification tools per plane}
---
**결론** — 5.1절 "판정 방식"을 실제 도구에 대응시킨다. **판정 도구가 없는 plane은
검사 게이트를 통과할 수 없다.**

| plane | 판정 도구 | 자동화 |
|---|---|---|
| `requirement` | EARS 형식 검사, 관심사·이해관계자 필드 존재 | 형식만 |
| `decision` | 논증 구조 검사(결론·근거·대안 존재), 상위 결정과의 모순 검사(`supersedes` 순환) | 부분 |
| `schema` | 스키마 검사기, 호환성 검사기 | 전체 |
| `contract` | 타입 체커, 컴파일러 | 전체 |
| `artifact` | 컴파일, 테스트, 린터 | 전체 |
| `annotation` | 해소 상태 존재 여부만 | 전체 (내용은 검사 안 함) |
| `memory` | 없음 | — |

**`requirement`와 `decision`의 판정이 가장 약하다.** 합의와 논증의 타당성은
기계가 판정하지 못한다. 그래서 두 plane의 청크는 **유저 승인이 `stable` 전이의
조건**이다.
