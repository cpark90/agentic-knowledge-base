---
id: https://agentic-knowledge-base.dev/id/chunk/43582b9a-cd83-49b4-94e2-6a056e692492
type: decision
level: logical
title_ko: 실수에 방향이 있으므로 구조로 막을 수 있다
title: Errors have direction, so structure can block them
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d3a0bc2e-b147-4eca-ad4a-3649472ea570
---
**근거** (노트 1.2·1.5절) — 에이전트의 실수는 무작위가 아니라 방향이 있고, 방향을
알면 구조로 막을 수 있다. 학습에 없던 것은 존재하지 않고, 지시하지 않은 곳은
스스로 채우며, 있는 것에서 만들고, 나눌수록 낫다 — 이 성질들은 프롬프트로 못
막는다. "추측하지 마라"는 지시 자체가 추측을 요구하기 때문이다. 그래서 후보가
여럿인 상태를 정상으로 두고 근거 없는 할당을 자료구조 수준에서 불가능하게 한다.

공통 원리의 실증 — 의존 관계를 그래프로 명시하면 모델이 낮은 추론 노력으로도
높은 추론 노력 기준선과 같은 일관성에 도달한다는 것이 문서 편집 도메인에서
실증되었다 (노트 1.5절).
