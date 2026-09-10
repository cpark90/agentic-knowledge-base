---
id: https://agentic-knowledge-base.dev/id/chunk/3c8bd124-8f95-4106-83dc-05087cc58c2c
type: decision
level: logical
title_ko: 판정의 독립은 스코프 분리로만 실효를 갖는다
title: Independence of judgement takes effect only through scope separation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8e8697a1-16b9-4c24-a377-340db2b6000b
---
**근거** (노트 6.1절·7.2절) — 두 산출물은 같은 level·같은 plane에 있지만 답하는 질문이 다르다. 하나는 "요구를 이렇게 구현했다"이고 다른 하나는 "그 구현이 기준을 만족한다"이다. 주어를 V&V 청크로 제한하지 않으면 만든 쪽이 자기 산출물에 `verifies`를 걸 수 있고, 그 순간 검증은 형식이 된다 (7.5절).

- 태그만으로 구분하고 스코프를 함께 나누지 않으면 개발 역할의 작업 집합에 검증 청크가 딸려 들어와 편집 가능해진다. 분리의 실효는 스코프에서 난다 (r-015).
- 이 규칙이 6.8절 마지막 게이트(concrete → executable)를 성립시킨다 — 구현 청크와 검증 청크가 같은 전이에서 태어나되 서로 다른 KB에 기록된다.
