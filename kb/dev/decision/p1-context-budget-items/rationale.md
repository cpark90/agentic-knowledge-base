---
id: https://agentic-knowledge-base.dev/id/chunk/577c7315-feba-41a7-a3ac-2222730d1221
type: decision
level: logical
title_ko: 분해가 있어야 청크 4~5개 계산이 성립하는지 알 수 있고 단위 교체는 분해를 기각하지 않았다
title: Only a breakdown shows whether the four-to-five-chunk arithmetic holds, and the unit change did not reject the breakdown
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:22:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4b1cecd2-e105-480b-93fd-c5d769657b22
---
**근거** — 노트 1.4절(`[확정]`, 2026-10-01 토큰으로 정정)은 "1.1절의 200줄은 전부 지식에 쓰이지 않는다. 예산을 분해해야 토큰 상한(저작 1,092 · 인용 2,856) 청크 4~5개라는 계산이 실제로 성립하는지 알 수 있다"라고 적고 위 분해표를 둔다. 예산에는 하네스 지시·툴 출력·대화 이력도 실리므로 분해표가 있어야 항목마다 통제 수단이 정해지고 실측이 어느 항목을 재야 하는지가 정해진다. 이것은 `p1-context-budget-breakdown` 근거의 주장과 같다.

그 결정은 `p1-chunk-unit-is-tokens`가 대체했다. 대체 결정의 결론은 단위(토큰)·예산(5,418)·상한(1,092 · 2,856)을 정하고, 근거는 줄이 컨텍스트의 단위가 아니라는 것과 도출(예산 ÷ 5)의 고정을 든다. 기각한 대안은 넷이다 — 참조 저장소의 260, 근사 630, 줄 유지, plane별 배수. 넷 모두 상한의 수와 단위에 관한 것이고, 예산을 분해하지 않는 안은 대안에 없으며 분해를 버린다는 문장도 세 청크에 없다. 분해는 대체에서 기각된 것이 아니라 빠졌다.

노트가 같은 날 정정으로 분해를 토큰 단위로 유지했으므로 분해는 살아 있는 주장이다. 이 결정은 그 주장의 원본 자리를 다시 둔다.
