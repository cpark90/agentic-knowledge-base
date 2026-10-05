---
id: https://agentic-knowledge-base.dev/id/chunk/b64cdfc4-ceeb-4bdf-aeee-4d970cccf236
type: decision
level: logical
title_ko: Run에 level을 주는 안과 시나리오와 통합하는 안과 옛 결정을 그대로 두는 안은 기각된다
title: Giving runs a level, merging runs with scenarios, and leaving the old decision as is are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:12:39+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c
---
**대안** — 셋을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| `agt:Run`에 level을 부여해 계층 위에 올린다 | 관측은 정제의 산물이 아니므로 어느 검증 대응물에 놓아도 그 검증 대응물의 판정 방식을 받지 못한다 |
| 시나리오와 실행 기록을 하나의 개념으로 통합한다 | 일반화 단계가 사라지고, 관측된 한 번의 실행이 명세로 오인되어 승격 없이 재사용된다(r-004) |
| 옛 결정을 그대로 두고 차이를 다른 결정의 근거에 적는다 | stable 결정이 실물과 다른 문장을 계속 갖는다. 결정에서 문서를 생성하면 틀린 문장이 나온다. 유저가 Q8에서 대체를 골랐다 |

앞의 둘은 옛 결정 `p0-run-as-observation`의 기각을 승계한다. v1은 이 구분을 scene·scenario 3분리(d-0012) 안에서 다뤘다. 3분리는 폐기되었지만 관측과 명세를 가르는 규칙은 남는다.
