---
id: https://agentic-knowledge-base.dev/id/chunk/42465bf4-c107-4403-8921-695bc1fbc3bf
type: decision
level: logical
title_ko: 반응형 전용 V&V의 기각과 적응형 실행기의 보류
title: Rejecting reactive-only V&V; deferring the adaptive executor
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/579b14ac-e4d4-4718-9516-4211838cb9d0
---
**대안** — V&V를 개발 KB 변화에만 반응하게 두는 안. 기각 — 환경·지식의 변화가 이탈·회귀로 드러난 뒤에야 잡힌다 (노트 8.27절).

**대안(미확정)** — 규칙 기반 생성기 위에 **적응형 실행기**(실행 이력·커버리지 공백·요인 분포를 읽어 다음 케이스를 고르는 에이전트)를 두는 안(`[안]`). 보류 — 고르는 것은 에이전트, 케이스는 여전히 생성기가 만들어 표본 근거 규칙은 유지된다는 조건으로만 가능하다 (노트 8.27절).
