---
id: https://agentic-knowledge-base.dev/id/chunk/190168d1-87d1-4283-b933-8ad804f767cb
type: decision
level: concrete
title_ko: 개발 KB는 다섯 산출을 내놓고 여섯 지표로 진행을 잰다
title: The development KB emits five outputs and measures progress with six metrics
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f44b4776-de6f-44bf-893b-72ce88179fdb, title_ko: 개발 KB의 산출과 지표, title: Outputs and metrics of the development KB}
part_of: https://agentic-knowledge-base.dev/id/composite/f44b4776-de6f-44bf-893b-72ce88179fdb
---
**결론** — 개발 KB가 밖으로 내놓는 것 (노트 7.8절):

| 산출 | 소비자 | 형태 |
|---|---|---|
| 요구·결정·계약·스키마·구현 청크 | V&V KB | `verifies`의 도착점 |
| ODD | V&V KB, 운영 | 시나리오 변수의 분모 |
| 코드 파일, 문서 | 빌드, 사람 | tangle·weave 뷰 (4.6절) |
| 결정 기록 (ADR) | 사람 | `decision` 복합체의 뷰 |
| 변경 영향 보고 | 유저 | 12.6절 |

지표 — 전방 추적 커버리지(100%) · 후방 추적 커버리지(100%) · 결정 완결률(concrete 청크가 있는 결정 비율 = 진행도) · `-space` 체류 시간(유저 피드백 병목) · 계약 선행률(100%) · 대안 기록률(100%).
