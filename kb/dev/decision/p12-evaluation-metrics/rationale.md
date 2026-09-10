---
id: https://agentic-knowledge-base.dev/id/chunk/d4df01e7-fffe-46ac-9aff-87c1eb8ff0b9
type: decision
level: logical
title_ko: 누락률은 분모가 둘로 갈리고 측정은 기록된 작업 집합의 재생이다
title: The omission rate splits by two denominators, and measurement replays recorded worksets
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a4a5acea-aaed-4439-ac17-164495f5927c
---
**근거** (노트 12.3절)

- **인지능력의 분모가 둘이다.** 지식 베이스 전체 대비 누락은 **스코프 설계
  문제**이고, 작업 집합 대비 누락은 **에이전트 문제**다. 둘을 합치면 누구를
  고쳐야 하는지가 사라진다.
- 측정은 7.9절 에이전트 검증 3단계(시뮬레이션 프로젝트)에 기록된 작업 집합을
  **재생해** 수행한다 — 재현 가능한 단계여야 재생이 성립한다.
- 나머지 둘은 계산식이 이미 있다. 추적 커버리지는 매트릭스의 빈 칸, 가정
  건전성은 상태 집계다. 새 계측기를 붙이면 그 계측기가 또 하나의 진실
  공급원이 된다.
- metric 선택 자체는 아직 설계 대상으로 남아 있다. 이 셋은 **체계가 이미
  산출하는 값**이라는 이유로 고른 초기 집합이며 확정 목록이 아니다.
