---
id: https://agentic-knowledge-base.dev/id/chunk/a0037ff5-559b-4f3b-894d-2bdef12e206c
type: requirement
level: functional
pattern: ubiquitous
title_ko: 링크와 결정 후보는 증거에서 계산한 믿음 정도를 가질 수 있어야 한다
title: Links and decision candidates shall be able to carry a degree of belief computed from evidence
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:09:19+09:00}
part_of: https://agentic-knowledge-base.dev/id/comp-req-accumulation
---
**요구** — 링크와 설계 공간의 결정 후보는 증거 기록에서 계산한 믿음 정도를 가질 수 있어야 한다.

- **이해관계자**: 업체 · 프로젝트 · **관심사**: 지식 베이스 자체의 확률화
- **출처**: 유저 지시 2026-10-22, 유저 답 Q87-b · Q88(a·b) · Q89-a · Q90-a · Q109-b · Q137-a

링크는 후보와 확정, 결정 후보는 열림과 배제, 확정의 이산 상태를 갖는다. 믿음 정도는 그 상태를 대신하지 않고 곁에 병기되며, 선호의 부분순서에서 순서가 없는 두 후보의 동률을 깬다. 병기의 경계는 r-011의 개정과 결정 `p9-evidence-ledger-with-belief`가 정했고(Q90-a), 동률 깨기는 결정 `p9-preference-partial-order`가 정했다(Q109-b). 그래서 이 요구는 계산 규칙만 남기고, 그 규칙은 설계 공간 '믿음 정도를 어떻게 계산하고 보정하는가'가 고른다.
