---
id: https://agentic-knowledge-base.dev/id/chunk-d0137
type: decision
level: concrete
title_ko: 재현성은 환경 배정의 조건이다
title: Reproducibility is a condition of rung assignment
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 1~4단계 시나리오는 재현 가능해야 한다. 재현성은 시나리오의
속성이 아니라 **환경 배정의 조건**이며, 재현되지 않는 시나리오는 5~6단계로
강등된다.

**근거** (노트 10.1절)
- concrete 시나리오가 재현 가능하려면 청크에 다섯 가지가 기록된다 —
  **초기 scene**(실행 시작 시점의 전체 상태), **자극 열**(순서 있는 입력,
  시각 포함), **난수 seed**(합성 데이터·자동 응답의 seed), **환경 버전**
  (실행 단계, mock 버전, 인프라 버전), 에이전트 검증이면 **에이전트 버전**
  (모델, 하네스, 스코프 버전).
- 재현되지 않는 것을 낮은 단계에 두면 그 단계가 보장하는 통제·재현성이
  무너지고, 사다리의 필터 역할이 사라진다.
- 실행 기록에서 시나리오를 일반화할 때(6.3절 상승) 재현 가능한 형태로
  만들 수 없는 관측은 `origin:observed` 태그를 유지한 채 **6단계 관측으로
  남긴다.** 억지로 concrete 시나리오로 만들지 않는다 — 재현되지 않는
  concrete 시나리오는 커버리지를 부풀린다.
