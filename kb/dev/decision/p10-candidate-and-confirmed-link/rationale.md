---
id: https://agentic-knowledge-base.dev/id/chunk/59a97c5d-4eef-4d6c-b8cc-cd12d2f5115e
type: decision
level: logical
title_ko: 임베딩 유사도는 후보를 추리는 데만 쓴다
title: Embedding similarity only narrows candidates
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/526f1fb6-5721-4b89-b8ac-3955dcbf6a37
---
**근거** (노트 10.4절) — 임베딩 유사도를 **확정 근거로 쓰지 않는다.** 의미가 같고 표현이 다른 항목(반복 구조, 다른 용어)에서 실패하기 때문이다. 유사도로 후보를 좁힌 뒤 온톨로지 개념과 역할 정보로 판정하는 것이 확립된 순서다.

**입력 품질이 복원 정확도를 좌우한다.** functional 단계가 모호하면 어떤 복원 방식도 링크를 제대로 찾지 못한다. 6.1절 abstract 단계가 이 문제를 앞에서 줄인다 — 형식화된 항목은 애초에 복원할 필요가 적다.
