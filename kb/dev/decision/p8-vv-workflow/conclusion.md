---
id: https://agentic-knowledge-base.dev/id/chunk/c99ccaef-6c94-4c42-a21b-834c2887372e
type: decision
level: concrete
title_ko: 요구 하나의 V&V 사슬은 열 단계이고 앞 세 단계는 개발 확정 전에 시작한다
title: The V&V chain per requirement has ten steps; the first three start before development is fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2, https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395]
composite: {id: https://agentic-knowledge-base.dev/id/composite/ad7a39e2-6ef7-4ba3-a4df-92cf2c9409ca, title_ko: V&V 워크플로, title: The V&V workflow}
part_of: https://agentic-knowledge-base.dev/id/composite/ad7a39e2-6ef7-4ba3-a4df-92cf2c9409ca
---
**결론** — 요구 하나에 대응하는 V&V 사슬의 작업 순서. 7.3절 개발 저작 흐름과 짝이다 (노트 8.19절).

1. 검증 목표 파생 — `requirement`(vv), 요구마다 최소 하나, `derives-from` · 2. 시나리오 형식화 — `decision`(vv) abstract, 변수가 ODD 속성 · 3. 논리 시나리오 + 기준 — `decision`(vv) logical `keep(범위)` / `contract`(vv) logical 판정식 · 4. 케이스 생성(자동) — concrete `keep(고정값)`, 표본 근거 `cover()` · 5. 검증기 작성 — `artifact`(vv), 기준 바인딩 · 6. 환경 할당 — `env:` 태그, 재현성 · 7. 실행(하네스) — `memory`(vv), seed·리비전 · 8. 판정 — 검증기 + 판정자, `annotation`(vv) 결함 분류, 3지표 · 9. 보고 — 뷰, 저장하지 않음 · 10. 되먹임 — 지침 → 일반화 후보.

**1~3은 개발 KB의 같은 높이가 확정되기 전에 시작할 수 있다.** 요구가 있으면 검증 목표를, 결정 abstract가 있으면 시나리오 abstract를 만든다.
