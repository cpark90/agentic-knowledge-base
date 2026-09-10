---
id: https://agentic-knowledge-base.dev/id/chunk/023c6da3-a7d3-4d02-84ed-0b2a6016159e
type: decision
level: logical
title_ko: 링크 생성을 게이트에 묶는 것이 강제의 실체이고 마지막 게이트가 V-모델의 가로대다
title: Binding link creation to the gate is the enforcement; the last gate is the V-model rung
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/7daf868e-e331-4e89-bbcc-447c0ce05f29
---
**근거** (노트 6.8절) — 링크 생성을 게이트에 묶는 것이 강제의 실체다. 링크 없는 하위 청크는 4.13절 고아율에 잡히므로 게이트를 우회해 만든 청크는 만들자마자 지표에 드러난다. 규약이 아니라 구조로 막는다 (r-011).

- **마지막 게이트가 V-모델의 가로대다.** 구현 청크와 검증 청크가 같은 전이에서 태어나고 검증 청크는 logical 기준에 묶인다 — 검증이 구현 뒤의 단계가 아니라 같은 시점의 산출물이 된다 (7.3절).
- 실패 시 처리를 게이트마다 다르게 두는 이유는 실패의 성격이 다르기 때문이다. 판정식 없음은 강등(되돌릴 수 있음), 봉사 없음은 기각(만들지 말았어야 함), 후보 미확정은 대기(유저 입력이 필요)다.
