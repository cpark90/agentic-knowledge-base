---
id: https://agentic-knowledge-base.dev/id/chunk-d0124
type: decision
level: concrete
title_ko: 에이전트 카탈로그가 규정하는 범위
title: What the agent catalog specifies
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 에이전트 카탈로그는 **어떤 역할이 존재하고 각자 무엇을 읽고
쓰는가**(plane 권한)까지만 규정한다. 각 역할이 실제로 무엇을 하는지
(프롬프트, 절차)는 하네스의 몫이고 이 체계 밖이다. 스코프(3.4절)는 ODD와
카탈로그 두 입력에서 파생된다 — ODD가 조건의 부분집합을, 카탈로그가 plane
권한을 정한다.

**근거** (노트 9.2절)
- 카탈로그는 가장 큰 입력이다. 바뀌면 스코프 전부가 재파생된다.
- **카탈로그는 ODD의 동적 요소와 연결된다.** ODD가 "동시 에이전트 ≤ 4"라고
  적으면, 동시에 활성화될 수 있는 역할 조합이 그 안에 있어야 한다.
  카탈로그가 ODD를 위반하면 3.5절 이탈이다.
- **설계 / 구현 / 운영은 독립 분리한다.** 세 영역의 역할이 같은 write
  scope를 갖지 않는다.
- 역할 이름은 도메인 프로파일마다 다르되 스코프 파생 방식은 같다 — 그래서
  체계는 역할 이름이 아니라 파생 방식을 고정한다.
