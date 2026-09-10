---
id: https://agentic-knowledge-base.dev/id/chunk/0f68d642-0020-443f-9876-072e8832b270
type: decision
level: concrete
title_ko: 후보 링크에는 출처와 상한이 있다
title: Candidate links have a source and an upper bound
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0102]
part_of: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc
composite: {id: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc, title_ko: 후보 링크에는 출처와 상한이 있다, title: Candidate links have a source and an upper bound}
---
**결론** — 후보 링크 집합에는 **상한이 있어야 한다.** 상한이 있어야 후보 집합이 청크 라벨 목록 안에 들어가고, 에이전트가 한 화면에서 조망할 수 있다.

복원으로 만드는 후보의 상위 `k`도 **7±2 원칙을 따른다 — `k ≤ 7`.**

상한을 넘는 후보 집합은 후보를 더 만들 문제가 아니라 변수를 잘못 잡았다는 신호로 읽는다.
