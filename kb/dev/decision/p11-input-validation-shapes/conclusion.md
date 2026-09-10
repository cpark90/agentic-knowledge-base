---
id: https://agentic-knowledge-base.dev/id/chunk/9389012a-78f3-4e8b-a051-53c5f6f49a8f
type: decision
level: concrete
title_ko: 입력도 shape로 검사한다
title: Inputs are validated by shapes
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0128]
part_of: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792
composite: {id: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792, title_ko: 입력 검증 항목, title: Validation checks on inputs}
---
**결론** — 입력도 청크와 같이 shape로 검사한다. 검사 항목을 넷으로 고정한다.

- **에이전트 카탈로그** — 모든 역할이 최소 하나의 read plane을 가질 것.
  설계/구현/운영 역할이 같은 write plane을 공유하지 않을 것. 동시 활성 합이
  ODD 동적 요소 안에 있을 것
- **태그 어휘** — 태그가 온톨로지 개념일 것. 중복 없음
- **프로세스 규칙** — 스코프 conditional로 표현 가능할 것. 순환 없음
- **재판정 경계** — 최소 하나
