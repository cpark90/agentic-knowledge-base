---
id: https://agentic-knowledge-base.dev/id/chunk/45d16364-c786-43ff-93f9-0c31ce02decb
type: decision
level: logical
title_ko: 정지 조건이 없으면 전파가 순환하고 KB 전체가 물든다
title: Without the stopping condition propagation cycles and stains the whole KB
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/01ce160f-72c9-4898-b0b1-fe6842b799e8
---
**근거** (노트 6.10절) — 6단계의 정지 조건이 절차의 핵심이다. 단방향 규칙이 없으면 전파가 순환한다 — 결정이 계약을 무효화하고 계약이 다시 결정을 건드리는 경로가 생기면 종료가 보장되지 않고, 가정 하나의 실패가 KB 전체를 `invalidated`로 물들인다.

- 4·5단계에서 복합체와 링크를 `invalidated`가 아니라 `suspect`로 두는 이유 — 부분의 무효가 전체의 무효를 함의하지 않는다. 판정은 재검증 시점에서 규칙 또는 사람이 한다 (r-012).
- 7단계 통지가 필요한 이유는 무효화가 조용히 일어나면 아무도 재검토하지 않기 때문이다. 범위를 수로 알려야 우선순위가 정해진다.
- 8단계가 이 절차를 일반화와 잇는다 — 자주 깨지는 가정이 일반화 대상이다 (r-004).
