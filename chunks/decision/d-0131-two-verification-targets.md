---
id: https://agentic-knowledge-base.dev/id/chunk-d0131
type: decision
level: concrete
title_ko: 검증의 두 대상 — 제품과 에이전트
title: Two verification targets: product and agent
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 검증 대상이 둘이다. **제품**(에이전트가 만든 소프트웨어)과
**에이전트**(소프트웨어를 만드는 주체) 자체. 둘을 섞으면 "무엇이 틀렸는가"가
흐려지므로 시나리오도 판정도 분리한다.

**근거** (노트 10.1절)
- **제품** — 시나리오의 자극은 입력 데이터·외부 서비스 응답·사용자 행동,
  판정은 명세 대비 동작.
- **에이전트** — 자극은 situation(스코프로 거른 scene)과 유저 피드백,
  판정은 산출물 품질과 인지능력(10.3절).
- 두 대상의 시나리오는 **별개의 구성체**이며 `verifies` 링크의 도착점이
  다르다 — 제품 시나리오는 `decision`·`contract` 청크를, 에이전트
  시나리오는 하네스·스코프 개체를 검증한다.
- 실행 기록(`agt:Run`)은 두 대상 모두의 관측을 담는다. 인시던트
  사후분석(10.12절)에서 결함이 제품의 것인지 에이전트의 것인지는 요인
  분류로 갈린다 — 실행 요인은 대체로 제품, 인지 요인은 대체로 에이전트.
