---
id: https://agentic-knowledge-base.dev/id/chunk/5efca330-1381-4309-b742-17d4a347e425
type: decision
level: concrete
title_ko: V&V KB는 개발이 바뀌지 않아도 네 트리거로 선제적으로 움직이고 산출은 전부 후보다
title: The V&V KB moves proactively on four triggers even without development changes; all outputs are candidates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
composite: {id: https://agentic-knowledge-base.dev/id/composite/579b14ac-e4d4-4718-9516-4211838cb9d0, title_ko: 선제적 V&V, title: Proactive V&V}
part_of: https://agentic-knowledge-base.dev/id/composite/579b14ac-e4d4-4718-9516-4211838cb9d0
---
**결론** — 8.19절 워크플로는 개발 KB의 변화에 반응한다. V&V KB는 그와 별도로 **선제적으로** 움직인다 — 개발이 바뀌지 않아도 환경과 지식이 바뀌기 때문이다 (노트 8.27절).

| 트리거 | 동작 | 산출 |
|---|---|---|
| ODD 모니터링 주기 (`odd_check`) | 실제 조건이 경계 근처면 그 속성을 자극하는 시나리오를 우선 실행 | 이탈 전 경고, 관측 |
| 실행 이력의 공백 | `cover()` 미달 구간, 오래 실행되지 않은 verifier를 골라 실행 | 커버리지 갱신 |
| 외부 지식 변화 | 표준·규제·의존성 릴리스 노트에서 새 조건 후보 추출 | ODD 확장 제안, 새 검증 목표 후보 |
| 확정 링크의 증거 노화 | 마지막 지지 증거가 오래된 `satisfies`·`verifies`를 재실행 | 증거 기록 갱신 (9.11절) |

선제적 V&V의 산출은 전부 **후보**다. 새 검증 목표는 개발 KB 요구에서 파생되지 않았으므로 `origin:observed` 태그를 달고, 8.4절 귀속 판단을 거쳐 요구 일반화 후보가 된다.
