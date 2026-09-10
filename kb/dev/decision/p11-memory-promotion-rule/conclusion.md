---
id: https://agentic-knowledge-base.dev/id/chunk/7279105c-038a-4f28-ae4c-9c6d04237001
type: decision
level: concrete
title_ko: 단기·장기는 생산 시점에 갈리고 승격 규칙은 입력이다
title: Short-term and long-term split at production time, and the promotion rule is an input
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0127]
part_of: https://agentic-knowledge-base.dev/id/composite/46d1f19a-5541-4328-903d-caa729dcb9b4
composite: {id: https://agentic-knowledge-base.dev/id/composite/46d1f19a-5541-4328-903d-caa729dcb9b4, title_ko: 단기·장기 구분과 메모리 승격 규칙, title: Short-term versus long-term memory and the promotion rule}
---
**결론** — 지식 **생산 시점에** 단기·장기를 구분한다.

- **단기기억** — `memory` plane에 두고 첫 실행 시 한 번에 읽는다
- **장기기억** — 주제 plane으로 승격해 필요한 순간에 읽는다

승격은 6.3절 상승의 최소 단위다. 설계 판단이면 `decision`, 코드 논평이면
`annotation`으로 올라간다. **승격 규칙(언제·무엇을)은 체계가 고정하지 않는
입력이다** — 프로젝트마다 다르다.
