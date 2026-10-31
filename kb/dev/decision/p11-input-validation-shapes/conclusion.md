---
id: https://agentic-knowledge-base.dev/id/chunk/9389012a-78f3-4e8b-a051-53c5f6f49a8f
type: decision
level: concrete
title_ko: 입력도 shape로 검사한다
title: Inputs are validated by shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0128-input-validation-shapes.md, id: https://agentic-knowledge-base.dev/id/chunk-d0128, title_ko: "입력도 shape로 검사한다", title: "Inputs are validated by shapes"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0128]
part_of: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792
composite: {id: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792, title_ko: 입력 검증 항목, title: Validation checks on inputs}
---
**결론** — 입력도 단위 지식과 같이 shape로 검사한다. 검사 항목을 넷으로 고정한다.

- **에이전트 카탈로그** — 모든 역할이 최소 하나의 읽기 지식 종류를 가질 것.
  설계/구현/운영 역할이 같은 쓰기 지식 종류를 공유하지 않을 것. 동시 활성 합이
  ODD 동적 요소 안에 있을 것
- **태그 어휘** — 태그가 온톨로지 개념일 것. 중복 없음
- **프로세스 규칙** — 적용 범위 conditional로 표현 가능할 것. 순환 없음
- **재검증 시점** — 최소 하나
