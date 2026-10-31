---
id: https://agentic-knowledge-base.dev/id/chunk/18537e8d-b957-4704-add4-639d90f323e5
type: decision
level: concrete
title_ko: 카탈로그는 역할과 지식 종류 권한까지만 규정하고 적용 범위는 ODD와 함께 파생된다
former_title_ko: ["카탈로그는 역할과 plane 권한까지만 규정하고 스코프는 ODD와 함께 파생된다"]
title: The catalog specifies roles and plane permissions only; scope derives from it with the ODD
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0124-agent-catalog-scope.md, id: https://agentic-knowledge-base.dev/id/chunk-d0124, title_ko: "에이전트 카탈로그가 규정하는 범위", title: "What the agent catalog specifies"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0124]
overlapsWith: [https://agentic-knowledge-base.dev/id/chunk/acd3f19b-bb9e-448f-acf3-ac227733c8ab]
restored: [https://agentic-knowledge-base.dev/id/chunk/acd3f19b-bb9e-448f-acf3-ac227733c8ab]
part_of: https://agentic-knowledge-base.dev/id/composite/2e3b40bb-c5f0-4355-8108-ccdf481d998a
composite: {id: https://agentic-knowledge-base.dev/id/composite/2e3b40bb-c5f0-4355-8108-ccdf481d998a, title_ko: 에이전트 카탈로그가 규정하는 범위, title: What the agent catalog specifies}
---
**결론** — 에이전트 카탈로그는 가장 큰 입력이며, **어떤 역할이 존재하고 각자
무엇을 읽고 쓰는가**(지식 종류 권한 요구)까지만 규정한다. 각 역할이 실제로 무엇을
하는지 — 프롬프트, 절차 — 는 하네스의 몫이고 이 체계 밖이다.

적용 범위(3.4절)는 **ODD와 카탈로그 두 입력**에서 파생된다. ODD가 조건의
부분집합을, 카탈로그가 지식 종류 권한을 정한다.
