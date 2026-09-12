---
id: https://agentic-knowledge-base.dev/id/chunk/bb0eca8e-bf60-453d-b558-0f20e20a8744
type: decision
level: logical
title_ko: 만든 주체와 확인한 주체는 다른 활동이다
title: Creating and confirming a link are different activities
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/eec0c89d-bba0-404c-a19e-b43043e2e1a2
---
**근거** (노트 10.10절) — 링크를 개체로 만들지 않으면 상태·근거·주체를 붙일 자리가 없고, 붕괴 관리(9.6절)와 판정 근거 서열(9.8절)이 저장될 곳을 잃는다.

**만든 주체와 확인한 주체를 별도 PROV 활동으로 나눈다.** 후보 생성은 에이전트나 복원 파이프라인이 하지만 확정은 유저 또는 위임된 에이전트가 하며, 둘을 합치면 "누가 이 링크를 책임지는가"를 답할 수 없다. 시각도 생성·확정·마지막 재판정 셋을 따로 남겨야 평균 재판정 지연(9.14절)을 계산할 수 있다.
