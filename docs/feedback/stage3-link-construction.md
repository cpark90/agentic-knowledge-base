---
from: hci
status: approved
targets: [tools/chunk2kg.py, tools/handoff.py, tools/workset.py, tools/metrics.py, docs/roadmap.md]
---

# 도입 3단계 착수 — 링크 개체·구축 증거·읽기 집합 인수인계 (hci 가 반영함 — 담당 역할 인수 대기)

## 질문

유저의 "계속해서 작업진행해줘"(2026-09-11)를 근거로 hci 가 3단계의 기계화 가능한 부분을 채널 밖에 반영했다.
hci 는 소통만 해야 하는데 수행했다. 이 항목은 그 반영을 담당 역할이 검토할 단위로 만든 것이다 — orchestrator 가
검토 뒤 `인수: orchestrator <날짜>` 줄을 남기면 유지, 아니면 되돌리고 closed. 게이트가 그 전까지 FAIL 로 붙잡는다.

## 이미 정해진 것

- 14.1 정정본 3단계 조건: 링크마다 근거(증거 기록 ≥ 1) · 구축 비율 · `refines` 한 단계씩 · 매트릭스 채움률 · 복원 비율 < 20% (`stage-pass-conditions.md`, 원장 18)
- 링크는 개체이며 증거 기록을 갖는다 (`p9-evidence-ledger`); 구축 = 편집 부산물 (`p10-link-by-construction`)
- OKF `sources` 는 읽기 집합 인수인계의 산출 (부록 E.2)

## 현재 상태 (반영된 것)

| 무엇 | 내용 |
|---|---|
| `chunk2kg` | frontmatter 링크마다 `agt:Link`(+`ConfirmedLink`) + 구축 기록 증거(`constructionRecord`, 극성 +, 참조 = 청크 생성 기록). 469 링크, 증거 100%. verify 질의가 실제 데이터를 검사 |
| `handoff` | workset 뷰의 펼친 청크(`<!-- iri -->`)를 새 청크의 `sources` 에 병합 — 하네스 자동 기록 전의 첫 형태 |
| `workset` | 복합체 노드를 통과해 형제(근거·대안)까지 한 홉 |
| `metrics` | 3단계 절: 근거 있는 링크 비율, 복원 비율(6.0%), plane×plane 매트릭스(TIM 8칸 중 2) |
| 문서 | roadmap 3단계 행, tools.md, method §6, 원장 23 |

## 답이 가르는 것

- 승인하면 3단계의 "링크마다 근거"·"복원 비율" 두 조건이 측정 가능한 상태로 남는다.
- 되돌리면 `chunk2kg`·`metrics`·`workset`·`handoff` 변경과 문서 5곳을 커밋 전 상태로 돌린다 (한 커밋 분량).

## 선택지

1. 인수 — orchestrator 가 검토하고 `인수: orchestrator 2026-09-11` 줄을 남긴다. 청크는 `bazel run //tools:endorse -- --by orchestrator/<모델> <파일>` 로 verified 를 붙인다. (권고)
2. 되돌림 — orchestrator 가 이 항목에 적힌 파일을 되돌리고 항목을 `closed` 로.

## 답
1.

인수: orchestrator 2026-09-11 — 청크·도구·문서 변경을 검토했다(요구 7건 전문, 결정 표본, 온톨로지 폐기 표기, 게이트 구조 검사). endorse 로 verified 부여.
