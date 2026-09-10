---
id: https://agentic-knowledge-base.dev/id/chunk/f64bb63b-9741-4f24-8831-1fcd0f0eaded
type: decision
level: concrete
title_ko: 검증기 실패의 귀속은 결정이며 V&V decision의 지침로 남는다
title: Attributing a 검증기 failure is a decision, recorded as a guidance chunk in V&V decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4d7432c4-7474-4d30-bfcb-dcb756408d72, title_ko: 불일치의 귀속, title: Attribution of a mismatch}
part_of: https://agentic-knowledge-base.dev/id/composite/4d7432c4-7474-4d30-bfcb-dcb756408d72
---
**결론** — verifier가 실패하면 세 가지 중 무엇이 틀렸는지 판단해야 한다 — **산출물**(구현이 요구를 못 지킴), **지식**(요구·기준·가정이 현실을 못 담음), **둘 다**. 이 판단은 자동이 아니며 하나의 **결정**이다. V&V KB `decision` plane에 **지침(guidance)**로 기록한다 — 결론(귀속과 조치), 근거(진단), 대안(배제된 귀속) (노트 8.4절).

| 귀속 | 조치 | 되먹임 목적지 |
|---|---|---|
| 산출물 | 구현 수정 요청 | 개발 KB `artifact` — 결정은 그대로 |
| 지식 — 요구 과도 | 요구 완화 | 개발 KB `requirement` 일반화 |
| 지식 — 제약 부족 | 계약·범위 강화 | 개발 KB `contract`·`decision` logical 일반화 |
| 지식 — 가정 누락 | 새 가정 또는 ODD 속성 | ODD 확장 (3.6절) |
| 둘 다 | 위 조합 | 각각 |

진단은 기호 도구가 먼저 한다 (12.12절). 언어모델은 도구 결과 위에서 귀속을 제안하고, 유저가 승인한다.
