---
id: https://agentic-knowledge-base.dev/id/chunk/67c1293a-e11b-4217-8cec-0d805be04e9d
type: decision
level: logical
title_ko: 시나리오 형식의 다섯 대안 기각
former_title_ko: ["자체 시나리오 형식과 기준 내장의 기각"]
title: Rejecting five alternatives for the scenario format
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea
---
**대안** — 시나리오 형식을 자체 설계하는 안. 기각 — 제약과 커버리지 표기(`keep`·`cover`)를 다시 만드는 것이며 어휘 발명이다 (노트 부록 E.5, 0.0절).

**대안** — OpenSCENARIO 관행대로 합격 기준을 시나리오 파일 안에 두는 안. 기각 — 기준 변경이 테스트 케이스 변경으로 보인다 (노트 8.11절).

**대안** — 동형 YAML을 원본으로 두고 OSC 텍스트 변환기를 두는 안(옛 결론). 기각 — 실물이 없고(변환기 0개), 두 형식의 의미를 대응시키는 비용이 원본 하나를 두는 비용보다 크다 (Q173-a).

**대안** — 세 수준을 한 파일에 두는 안(옛 결론). 기각 — 게이트 `rung-before-descent`가 요구하는 수준별 단위 지식과 `refines` 사슬과 어긋나고, 실행기의 `inherits`는 부모의 `do`를 물려받지 못한다 (Q173-a).

**대안** — `cover`를 표본 추출 규칙 목록으로 계속 쓰는 안. 기각 — DSL 표준의 `cover()`(커버리지 수집점)와 뜻이 부딪히고, 충돌하면 DSL 문법을 지킨다 (Q173-a).
