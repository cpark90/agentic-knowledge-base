---
id: https://agentic-knowledge-base.dev/id/chunk/19340826-1e0d-48ab-afa9-16402d5325e1
type: decision
level: concrete
title_ko: 검증은 수직·수평·기준의 질 세 방향에서 확인된다
title: Verification is confirmed vertically, horizontally, and by criterion quality
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
part_of: https://agentic-knowledge-base.dev/id/composite/9ac75416-7fff-4995-be5d-fed7b6ecbb90
composite: {id: https://agentic-knowledge-base.dev/id/composite/9ac75416-7fff-4995-be5d-fed7b6ecbb90, title_ko: 검증의 세 방향, title: The three directions of verification}
---
**결론** — 연쇄의 성립은 세 방향에서 확인된다. **셋 중 하나만으로는 검증이 아니다.**

- **수직** — `refines` 연쇄가 functional까지 닿는가(하강 완주). `refines+` 질의와 level × level 매트릭스(9.12절)로 확인
- **수평** — 검증 역할 executable이 logical 기준에 대해 `verifies`로 실행 통과하는가. 환경 사다리에서 실행해 확인
- **기준의 질** — `verifies`가 실제로 거르는가. 판정식에 **변이**(값 경계 넘김, 조건 반전)를 주입했을 때 실패하는지 표본으로 확인
