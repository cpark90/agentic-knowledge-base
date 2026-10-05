---
id: https://agentic-knowledge-base.dev/id/chunk/525c2b08-d69e-41f1-bbcd-fbffa082a5eb
type: decision
level: concrete
title_ko: 시나리오 계층의 세 높이에 검증 대응물이 필수다
title: Three heights of the scenario ladder require a mandatory rung
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T20:16:58+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T20:17:35+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
part_of: https://agentic-knowledge-base.dev/id/composite/0ef3233e-c6aa-434b-a0ef-350c857e690e
composite: {id: https://agentic-knowledge-base.dev/id/composite/0ef3233e-c6aa-434b-a0ef-350c857e690e, title_ko: 시나리오 계층과 검증 대응물, title: The scenario ladder and its rungs}
---
**결론** — 시나리오는 V&V KB 안에서 다섯 수준을 가지며, 개발 계층과 **같은 높이가 같은 것을 뜻한다.**

- **functional** 검증 목표 ↔ 요구 — `derives-from` **필수**
- **abstract** 시나리오 형식화(변수 선언) ↔ 형식화된 설계 — 검증 대응물 선택
- **logical** 논리 시나리오(변수 범위 + **합격 기준 판정식**) ↔ 범위·제약 — 기준 → 검증 목표 `refines` **필수**
- **concrete** 구체 시나리오 = 케이스(표본 추출 근거 동반) ↔ 확정 값 — `verifies` 선택
- **executable** 검증기 ↔ 구현 — `verifies` **필수**

**검증 대응물 필수 규칙** — 개발 게이트(6.8절)가 V&V 대응물을 요구한다. functional → abstract는 파생된 검증 목표의 존재를, logical → concrete는 그 범위를 검사하는 합격 기준의 존재를, concrete → executable은 검증기의 존재와 기준 바인딩을 요구한다 (abstract → logical은 요구하지 않는다).

**logical의 검증 대응** (유저 결정 2026-10-04, Q30-b) — logical 높이에서는 합격 기준이 검증 목표를 `refines`하는 것으로 검증 대응이 성립한다. 기준은 개발 결정을 `verifies`하지 않고 `verifies` 링크의 속성으로 바인딩된다(`p8-pass-criteria`). 그래서 추적 매트릭스에 `verifies`:contract→decision 칸은 없고, V&V KB 안의 기준(logical) → 목표(functional) `refines`는 수준 건너뜀으로 세지 않는다.

시나리오의 변수는 **ODD 속성에서** 온다. 시나리오 계층도 `refines` 연쇄를 남긴다.
