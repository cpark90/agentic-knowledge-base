---
id: https://agentic-knowledge-base.dev/id/chunk/688dd654-9493-4ff5-a3bc-1fe4906776ce
type: decision
level: concrete
title_ko: V&V 프로파일은 도메인당 한 번의 위험 분석 G1~G6으로 만든다
title: The V&V profile is built once per domain by risk analysis G1–G6
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
composite: {id: https://agentic-knowledge-base.dev/id/composite/a9889acc-3e51-4428-8dff-b9bce3e26ce5, title_ko: 위험 분석에 의한 V&V 프로파일, title: V&V profile by risk analysis}
part_of: https://agentic-knowledge-base.dev/id/composite/a9889acc-3e51-4428-8dff-b9bce3e26ce5
---
**결론** — V&V KB의 프로파일(2.11절)은 **위험 분석**으로 만든다. 도메인의 열린 세계를 유한한 산출물로 구조화하는 절차이며, 프로젝트에 앞서 도메인당 한 번 수행하고 프로젝트마다 재사용한다 (노트 8.21절).

G1 현상 추출 → ODD 조건 어휘 + `defect` 요인 · G2 인과 모델 → `defect-rules` · G3 데이터로 타당성 검토 → 실행 기록·사후분석 · G4 위험 지표 → 학습 판정자 입력, 평가 · G5 추상화·정련 → 시나리오 abstract 라이브러리 (V&V `decision` abstract, 프로젝트를 넘어 재사용) · G6 목표 거동 → Runbook, 안전 정지.

위험의 정의는 도메인에 맞게 바꾼다 — 소프트웨어면 행위자는 에이전트·유저·외부 서비스, 피해는 실패·회귀·데이터 손상·추적성 상실. **규칙성 가정을 먼저 적는다** (ODD 정적 갈래 또는 프로파일 전제). G1~G3은 전문가 기반으로 시작하고 실행 기록이 쌓이면 데이터 기반으로 보정한다.
