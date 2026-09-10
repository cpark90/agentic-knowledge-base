---
id: https://agentic-knowledge-base.dev/id/chunk/6d30bbff-d21e-4c03-9d1c-d5264bc2bed9
type: decision
level: logical
title_ko: ODD 밖 조건을 품은 환경의 통과는 설계 범위 안의 통과가 아니다
title: Passing in an environment beyond the ODD is not passing within design scope
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8475c698-2795-4e94-8c13-85e3aa7d85eb
---
**근거** (노트 8.15절) — 환경이 ODD 밖 조건을 포함하면 그 환경의 통과는 **설계 범위 안에서의 통과를 뜻하지 않는다.** 부분집합 제약이 있어야 "이 테스트베드를 통과했다"가 ODD 안의 주장으로 번역된다.

- 여섯 구성이 전부 이미 있는 자리에 대응한다 — 테스트베드는 새 저장소가 아니라 기존 `-kg`·`run-kg`·`defect-rules`·하네스의 조합이고, 비교기만 질의로 구현된다.
- 영속적이어야 하는 이유는 검증 결과의 가치가 시간에 걸친 비교에서 나오기 때문이다. 리비전마다 환경이 달라지면 결과 변화가 산출물의 변화인지 환경의 변화인지 갈리지 않는다 (7.12절 재현성 기록).
