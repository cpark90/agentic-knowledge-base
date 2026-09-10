---
id: https://agentic-knowledge-base.dev/id/chunk/84876fe0-13f8-4691-a6c6-27ff29ac61c1
type: decision
level: concrete
title_ko: 커버리지는 세 지표로 재는 측정치다
title: Coverage is a measurement made with three metrics
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0135]
part_of: https://agentic-knowledge-base.dev/id/composite/205cefbf-aaf5-4b93-9e68-83f242e64e86
composite: {id: https://agentic-knowledge-base.dev/id/composite/205cefbf-aaf5-4b93-9e68-83f242e64e86, title_ko: 커버리지, title: Coverage}
---
**결론** — **커버리지는 측정 지표다.** 완전성을 전제한 무인 운영은 성립하지 않는다. 세 지표로 잰다.

- **하강 완주율** — executable까지 닿은 requirement 청크 비율. 분모는 requirement 청크 수
- **상향 귀속률** — functional까지 거슬러 오르는 executable 청크 비율. 분모는 executable 청크 수
- **logical 공간 커버** — logical 범위 중 concrete 케이스가 표본 추출한 비율. 분모는 ODD 값 범위 × 변수. **경계값 미커버는 별도 집계**
