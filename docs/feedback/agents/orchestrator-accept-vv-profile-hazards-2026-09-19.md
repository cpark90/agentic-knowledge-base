---
from: orchestrator
kind: notice
status: open
ref: handoff/vv-profile-hazards-2026-09-19.md
targets: [kb/ontology/related/defect/, kb/ontology/related/defect-rules/, kb/ontology/shapes/, kg/base-kg.ttl, kb/vv/goal/, kb/vv/criteria/, kb/vv/scenario/, kb/vv/verdict/, tools/chunk2kg.py, tools/weave.py, docs/rules.md, docs/method.md, docs/glossary.md]
---

# 인수 기록 — `vv-profile-hazards-2026-09-19` (2026-09-29)

승인 항목 [`vv-profile-hazards-2026-09-19`](../vv-profile-hazards-2026-09-19.md)의 반영 계획 여섯을 전부 수행했다. hci의 읽기 둘(질문지 전부 채택 · "지식 유실·재생산"은 H1 하위)을 그대로 따랐다. `bazel test //...` 27/27 PASS, 성분 1 · CQ20 100% · 고아 0% 유지.

| 계획 | 수행 |
|---|---|
| 1 developer — `defect` 모듈 | `kb/ontology/related/defect/` 17파일 — 요인 세 갈래·하위 유형 14(재도출 결정 넷의 T-Box 실현, 8.17절 어휘는 온톨로지에 없던 빈 자리)·한정자 3·트리거 5·술어 9·현상 22(`skos:notation` P1~P22, `observationMeans` 13 + `미확정` 9, 출처 넷). shape 둘. 새 상위 개념 0 |
| 2 developer — 피해 | ODC 영향 차원 다섯 + `knowledgeLossImpact`(H1 하위, `skos:broader`) |
| 3 orchestrator — 가정 | `id:asm-links-only-interaction`·`asm-finite-factor-types`·`asm-missing-vocabulary-is-signal`(A3은 `doc-harness-ontology` 파생). 등록 = 파생 항목의 `assumes` 참조(decision plane 넷) |
| 4 vnv — G2~G4 | **G2**: 질문지 24쌍 중 둘 기각(P13→H4, P18→H3 — 경로가 끊긴다)·둘 추가(P2·P3→H1.1) → `defect-rules/impact-causation-rules.ttl` 28 트리플. **G3**: 건수 있는 현상 8 · 0건 7 · 데이터 없음 7(판정 주석 둘). **G4**: S0~S3·E1~E4·D1~D3(D = 게이트 FAIL / 보고서 수치 / 미확정) — **곱하지 않는다**, 정렬 머리 P16·P19·P21. `risk-grade-rules.ttl` 66 + `odc-dimension-rules.ttl` 22, shape `sh:in` |
| 5 vnv — G5·G6 | 부류 셋(P15·P16·P18, abstract 결정 단일 청크)과 목표·기준 셋. 파생의 표지는 새 frontmatter 키 `exposes`(→ `agt:exposesFactor`, deps 아님, shape가 대상이 선언된 현상인지 판정) |
| 6 vnv·developer — 감사 | `//kg:audit` 절 "위험에서 파생된 목표": 3/38 = 7.9%(전부 선언), 어느 목표에도 가리켜지지 않은 현상 16/22 |

## 계획과 다르게 읽은 것

- 현상별 등급의 **정의처는 vnv 판정**(`kb/vv/scenario/risk-grade-scale.md`의 조건을 적용한 표)이고 developer는 옮기기만 한다. 첫 회차에 developer가 자기 도출을 넣었다 — 내가 표를 참조로만 넘긴 탓이고 22행 전부 vnv 값으로 교체했다.
- 시나리오는 규칙(세 청크 복합체 — 자극·요인·배제 자극)대로 저작하지 못했다. `gen_build`의 평평한 `glob`과 `chunk_lint`의 stem 기반 역할 표지가 V&V 패키지에서 그 형태를 표현하지 못한다. 부류는 단일 청크다 — 구조 공백으로 남긴다.

## 남긴 것

미확정 관측 수단 9(P14~P22) · `defect-rules`의 진단 규칙(8.17 분포 판정 — 엔진 선택 선행) · `agt:AlgorithmFactor` 빈 잎(현상 없음 — 분포가 진단이므로 남긴다) · `hasQualifier`는 부류가 주입하는 여섯뿐 · `risk-grade-scale.md`가 시나리오 패키지에 있다 · 새 청크 12 전부 `draft`.

## hci에 전달

원장에 "V&V 프로파일 G1~G6 첫 형태(2026-09-29) — defect 22·피해 6·인과 28·등급 66·부류 3·목표 3" 한 줄. **유저에게 되돌릴 것 둘** — ① 다음 부류 후보 P19(어휘 없는 요소 탈락)·P21(로딩 옵션에 따른 지표 변동)이 정렬 머리(S3∧D3)인데 승인된 우선순위(P15·P16·P18) 밖이다 ② G2에서 질문지의 인과 넷이 vnv 검토로 달라졌다(위 표) — 유저가 준 값의 변경이므로 확인을 구한다. 재판정 대상 없음(새 청크는 미검증 draft).
