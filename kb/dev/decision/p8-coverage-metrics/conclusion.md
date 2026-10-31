---
id: https://agentic-knowledge-base.dev/id/chunk/84876fe0-13f8-4691-a6c6-27ff29ac61c1
type: decision
level: concrete
title_ko: 커버리지는 세 지표로 재는 측정치다
title: Coverage is a measurement made with three metrics
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0135-coverage-definition.md, id: https://agentic-knowledge-base.dev/id/chunk-d0135, title_ko: "커버리지의 분모와 단계별 합산", title: "Coverage denominator and cross-rung accumulation"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:03:22+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0135]
part_of: https://agentic-knowledge-base.dev/id/composite/205cefbf-aaf5-4b93-9e68-83f242e64e86
composite: {id: https://agentic-knowledge-base.dev/id/composite/205cefbf-aaf5-4b93-9e68-83f242e64e86, title_ko: 커버리지, title: Coverage}
---
**결론** — **커버리지는 측정 지표다.** 완전성을 전제한 무인 운영은 성립하지 않는다. 세 지표로 잰다.

- **전방 추적 커버리지** — executable까지 닿은 requirement 단위 지식 비율. 분모는 requirement 단위 지식 수
- **후방 추적 커버리지** — functional까지 거슬러 오르는 executable 단위 지식 비율. 분모는 executable 단위 지식 수
- **logical 공간 커버** — logical 범위 중 concrete 테스트 케이스가 표본 추출한 비율. 분모는 ODD 값 범위 × 변수. **경계값 미커버는 별도 집계**

미확정: 커버리지의 분모를 무엇으로 세는가. 상세는 `https://agentic-knowledge-base.dev/id/chunk/5d13b3d5-862c-42b3-9348-cce33f3a5021`다.
