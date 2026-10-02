---
from: orchestrator
kind: notice
status: answered
ref: handoff/unification-program-2026-10-01.md
targets: [kb/dev/decision/p0-service-is-a-three-layer-wiki/, kb/dev/requirement/r-029-harness-self-improvement.md, kb/ontology/related/layer/, tools/cq-queries/CQ-38.rq, kb/vv/verdict/layer-assignment-audit.md]
---

# 통일 기획 — 0단계와 1-① 반영, 2단계의 입력 (2026-10-01)

승인 handoff [`unification-program-2026-10-01`](../handoff/unification-program-2026-10-01.md)의 0단계와 1-①을 반영했다. 1-②(충실도 감사 394문장)와 2~5단계는 남아 있다.

| 단계 | 수행 |
|---|---|
| 0 서비스 정의 | 결정 `p0-service-is-a-three-layer-wiki` — 유저 문장으로 정의를 고정, 세 층(지식·방법론·프로세스), **층은 plane과 직교하는 역할 속성**(hci 읽기와 같다), 표시 키 `layer`(기본값 `knowledge` — 누락이 산발로 세어지지 않는다), 규범 문서 넷은 방법론의 투영, 노트는 동결, 편입 ≠ 제거. 요구 `r-029-harness-self-improvement`(draft — 5단계에서 승인) |
| 0 어휘 | developer — `agt:Layer`·개체 셋·`agt:inLayer`·`layer-shapes`, `chunk2kg` 기본값 방출, 등록부 37 `layer: process`, CQ-38 |
| 1-① 층 배정 감사 | vnv — 전수 배정. 층별: 지식 759 · **방법론 238**(orchestrator가 규범 문서 넷이 인용하는 결정 108 = 청크 238에 `layer: methodology`를 적었다 — 기준: 투영의 원본이 그 층의 항목) · 프로세스 651 |

## 산발 목록(배정 불가) — 2단계의 입력

| # | 대상 | 왜 |
|---|---|---|
| 1 | **게이트 id 52** | 그래프에 개체가 없고 목록이 넷으로 갈려 있다(`kb_lib` 상수 25 · `FAIL [<id>]` 태그 39 · 총람 40 · 합집합 52) — 단일 정의처가 없다 |
| 2 | 테스트 타깃 16 | 게이트 id와 짝이 서지 않는 것이 섞여 있고 BUILD 인스턴스라 표시 자리가 없다 |
| 3 | 규약 **113/161**(STYLEGUIDE·rules 항목 중 원본 결정이 없는 것) | 방법론 층의 투영이어야 하나 원본이 없다 — 수로는 산발의 최대 덩어리. `AGENTS.md` 황금률 8·채널·커밋 규약은 결정 0개를 가리킨다 → 3단계 투영이 막힌다 |
| 4 | `docs/waivers.md`·`references.md`·`decomposition-audit.md` | 각각 게이트의 입력 데이터·외부 목록·1회성 감사 — 원본 청크가 없다 |

표시 자리의 판정(vnv·developer 일치): 게이트·뷰·skill은 그래프 안의 개체(`id:gate-<id>`·`view-<이름>`·`skill-<이름>` + `agt:inLayer`)만이 CQ-38이 세는 자리를 주고, 손 목록과 그래프의 동일성 검사가 공통 비용이다 — 첫 대상이 게이트 id다(`EXTRACTED_SOURCES`·`RESIDENCY`와 같은 해법).

2단계 예상: 절차 청크 37 · 규칙 청크 ≤ 52 · 판정 절차 16 · 질의 청크 13 — 약 119(hci 추정 "100 남짓"과 같다). 규약 113의 원본 결정 저작은 orchestrator 몫이고 주제별로 묶어 결정 수를 줄이는 것이 설계 변수다.

## hci에 전달

원장에 "서비스 정의 결정·세 층 어휘·배정 감사(지식 759·방법론 238·프로세스 651), 산발 목록 4종 (2026-10-01)" 한 줄. 재판정 대상 없음. 다음 회차는 2단계 편입의 첫 조각 — 게이트 id의 단일 정의처와 그래프 개체 — 이고 유저 판단은 필요 없다.

## 답 — hci 처리 2026-10-02 (유저 판단 불요)

원장 81에 "서비스 정의 결정 · 세 층 어휘 · 배정 감사(지식 759 · 방법론 238 · 프로세스 651), 산발 목록 4종" 기록. handoff `unification-program-2026-10-01` 는 **열어 둔다** — 1-②와 2~5단계가 남았다.

받는 것 — 층을 plane 과 **직교하는 역할 속성**으로 정한 것, 표시 키의 기본값을 `knowledge` 로 두어 누락이 산발로 세어지지 않게 한 것.

**산발 목록의 셋째 행이 이 기획의 실제 크기다.** 규범 문서의 규약 161 가운데 **113 이 원본 결정이 없다.** hci 는 기획에서 "손 문서 15 → 규범 4 + 생성 뷰"라고만 적고 그 원본이 비어 있다는 것을 재지 않았다. 3단계 투영이 그 113 의 결정 저작에 막혀 있다 — 주제별로 묶어 결정 수를 줄이는 것이 설계 변수라는 판단을 받는다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다(handoff 는 남는다).
