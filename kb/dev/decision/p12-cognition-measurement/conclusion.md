---
id: https://agentic-knowledge-base.dev/id/chunk/c480e03a-fbf4-40a8-8e24-8248b934a01d
type: decision
level: concrete
title_ko: 인지능력은 시뮬레이션 프로젝트에서 작업 집합을 재생해 재고 세 누락의 목적지가 다르다
title: Cognition is measured by replaying worksets in the simulation project; the three omissions go to different places
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
composite: {id: https://agentic-knowledge-base.dev/id/composite/d2db1db1-ebc3-4f6d-8f93-3bef450b93f9, title_ko: 인지능력 측정, title: Measuring cognition}
part_of: https://agentic-knowledge-base.dev/id/composite/d2db1db1-ebc3-4f6d-8f93-3bef450b93f9
---
**결론** — 인지능력(입력 정보 누락률) 측정은 에이전트 V&V 3단계(8.9절 시뮬레이션 프로젝트)에서 수행한다 (노트 12.3절).

1. 실행 기록에서 한 결정 시점 T의 작업 집합 W_T(라벨 목록 + 펼친 청크)와 출력 O_T를 뽑는다
2. 기대 출력 O*를 정한다 — 같은 W_T를 받은 기준 절차의 출력, 또는 8.11절 기준
3. 누락 = O*에 있고 O_T에 없는 항목. 각 항목이 어디 있었는지 판정 — W_T 안 → **에이전트 누락** / W_T 밖·지식 베이스 안 → **스코프 누락** / 지식 베이스 밖 → **지식 누락**(일반화 후보)
4. 세 비율을 역할·plane·level별로 집계

세 누락의 목적지가 다르다 — 에이전트 누락은 하네스·프롬프트, 스코프 누락은 카탈로그·스코프(입력), 지식 누락은 일반화. 하나로 합치면 어디를 고칠지 모른다. 지표는 셋으로 제한한다 — 이 지표가 낮으면 무엇을 고치는가가 명확한 것만.
