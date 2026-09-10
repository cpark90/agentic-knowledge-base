---
id: https://agentic-knowledge-base.dev/id/chunk/9eccc506-292a-43df-a121-15fd00d359ca
type: decision
level: logical
title_ko: 연속 편집 중의 매번 전파는 낭비다
title: Propagating on every edit wastes work
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/560ccdfa-94a3-4a43-bc41-3697c44b69cc
---
**근거** (노트 9.6절) — 편집은 연속으로 일어나고 중간 상태는 대부분 곧 덮인다. 매 편집마다 전파하면 버려질 계산을 반복한다. 링크 붕괴의 재판정을 경계에서 일괄 처리하는 규율(9.6절)과 같은 이유이고, 같은 경계를 공유하면 두 메커니즘이 한 번에 돈다.
