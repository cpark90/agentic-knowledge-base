---
id: https://agentic-knowledge-base.dev/id/chunk/d577873b-6b6f-426b-8be3-190a69370562
type: decision
level: logical
title_ko: 실행 기록은 하나이고 요인 분류가 두 대상을 가른다
title: One run record; the factor taxonomy is what separates the two targets
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/e11ea926-9802-41f2-92a9-62dccfa80b4d
---
**근거** (노트 8.8절) — 실행 기록(`agt:Run`)은 두 대상 모두의 관측을 담으므로 기록 단계에서는 나뉘지 않는다. 사후분석(11.12절)에서 결함이 제품의 것인지 에이전트의 것인지가 **요인 분류**로 갈린다 — 실행 요인은 대체로 제품, 인지 요인은 대체로 에이전트다 (7.16절).

- 도착점을 다르게 두는 것이 분리의 실체다. 같은 `verifies`를 쓰되 끝점이 logical 기준이면 제품 검증이고 하네스·스코프면 에이전트 검증이므로, 두 집합이 질의로 갈린다.
- 섞으면 개선 대상이 지목되지 않는다. 산출물이 틀렸을 때 코드를 고쳐야 하는지 스코프를 고쳐야 하는지가 요인 분포로만 드러난다 (7.17절).
