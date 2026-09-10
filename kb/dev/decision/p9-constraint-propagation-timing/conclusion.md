---
id: https://agentic-knowledge-base.dev/id/chunk/21accfe5-3723-46b2-8d44-f700e2099825
type: decision
level: concrete
title_ko: 제약 전파는 게이트와 재검증 시점에서만 실행한다
title: Run constraint propagation only at gates and rejudgement boundaries
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0101]
part_of: https://agentic-knowledge-base.dev/id/composite/560ccdfa-94a3-4a43-bc41-3697c44b69cc
composite: {id: https://agentic-knowledge-base.dev/id/composite/560ccdfa-94a3-4a43-bc41-3697c44b69cc, title_ko: 제약 전파는 게이트와 재검증 시점에서만 실행한다, title: Run constraint propagation only at gates and rejudgement boundaries}
---
**결론** — 제약 전파는 **검사 게이트 통과 시점**과 **재검증 시점**(Part XI 입력의 재검증 시점)에서 실행한다. **편집마다 실행하지 않는다.**

전파의 결과는 후보 집합의 축소이며, 축소로 후보가 하나만 남으면 확정 후보가 되고 하나도 남지 않으면 모순 신호가 된다 (8.8절).
