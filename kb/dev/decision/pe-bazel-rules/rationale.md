---
id: https://agentic-knowledge-base.dev/id/chunk/ceaf0bf1-3306-43b3-85ee-46fed0c6d6b2
type: decision
level: logical
title_ko: 빌드 그래프가 곧 확정 의존 그래프면 영향 분석과 증분 재판정이 공짜다
title: If the build graph is the confirmed dependency graph, impact analysis and incremental re-judgement come free
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/3e725e9e-fd83-432d-b708-ed004a01cedd
---
**근거** (노트 부록 E.6, 9.10절, 12.6절) — 확정 링크를 deps로 두면 `rdeps`가 변경 영향(12.6절)이고 증분 빌드가 재판정 범위다 — 별도 전파 엔진이 필요 없다. 후보를 deps에서 빼는 것은 9.10절의 이유다. Bazel이 못 하는 셋(쓰기 스코프·대칭 관계·suspect 저장)을 명시해 두는 것이 이 바인딩의 한계를 정직하게 적는 일이며, 각각 대체 수단이 있다.
