---
from: hci
status: approved
targets: [kb/vv/goal/, kb/vv/criteria/, kb/vv/scenario/]
---

# V&V 목표·기준·시나리오 21건의 stable 전이 (2026-10-01 중계)

원본: [`agents/orchestrator-observation-means-2026-10-01.md`](agents/orchestrator-observation-means-2026-10-01.md) ③

## 질문

위험 분석 반영(2026-09-29~30)으로 생긴 V&V 항목 **21건이 전부 `draft`** 다 — 검증 목표 8 · 합격 기준 8 · 시나리오 5(세 청크
복합체). stable 전이는 유저 승인이 조건이다. 올릴 것인가.

어려운 이유는 하나가 **이미 작동하고 있다**는 데 있다. 목표 `verification-round-stop-rule`(정지 규칙 — 연속 두 라운드에서
신규 결함이 줄지 않으면 다음 라운드를 열지 않는다)이 09-29·09-30 두 번 성립했고 orchestrator 가 그 뜻을 받아 **정지했다.**
draft 라 규범이 아니라 관측으로만 작동한 것이다.

## 이미 정해진 것

- 요구·V&V 목표의 stable 전이는 유저 승인 사항이다(AGENTS 역할 표).
- 위험 분석 G1~G6 의 입력과 등급 정렬(P19·P21)은 승인됐다(2026-09-29). 이 21건은 그 승인의 **산출**이다.
- 케이스는 사람이 쓰지 않고 생성기가 만든다(노트 8.22) — 21건에 케이스는 들지 않는다.

## 현재 상태 (실측 2026-10-01)

**검증 목표 8** — `acyclic-relation-axioms`(성질 공리는 verify 질의가 강제) · `agent-catalog-complete`(카탈로그 정합성) ·
`element-without-vocabulary-dropped`(P19) · `document-table-matches-generated`(P18) · `metric-varies-by-loading-option`(P21) ·
`composite-order-shape`(복합체 순서 shape) · `decision-and-artifact-agree`(P16) · `verification-round-stop-rule`(P15).

**합격 기준 8** — 목표마다 하나. 판정식은 게이트(`FAIL [catalog]`·shape·`doccheck --report`·`revalidate`)다.

**시나리오 5(복합체, 자극·요인·배제 자극)** — `decision-and-artifact-agree` · `document-table-matches-generated` ·
`element-without-vocabulary-dropped` · `metric-varies-by-loading-option` · `verification-round-stop-rule`.

관측 수단 `미확정` 은 7 → **2**(P17 과업 이탈 · P20 게이트 밖 소비자)로 줄었고 등급 D3 가 2다. 문서 지연(P18)은 실측 10/16 쌍이
낡아 있었고 전부 생성 명령 인용으로 바꿔 지금 어긋남 0이다.

## 답이 가르는 것

- **전부 올리면** 정지 규칙이 규범이 된다 — 다음부터 orchestrator 는 두 라운드 정체 시 **반드시** 멈추고 채널로 되돌린다. 나머지 일곱도 감사 보고서의 분모에 든다.
- **정지 규칙만 올리면** 이미 작동한 것만 규범이 되고 나머지는 관측 수단이 더 서는 것을 본 뒤 올린다.
- **두면** 21건이 draft 로 남아 감사가 "승인된 목표"로 세지 않는다. 정지 규칙은 관측으로만 작동한다.

## 선택지

1. **21건 전부 stable** (권고). 전부 승인된 입력의 산출이고 케이스까지 선 것(P18 `document-table-matches-generated`, P19 `element-drop`)이 둘이다. 비용: 상태 전이 21 + 도장.
2. **정지 규칙 목표·기준·시나리오 3건만 먼저.** 비용: 상태 전이 3. 나머지 18은 D3 둘·미확정 둘이 정리된 뒤.
3. **둔다.** 비용 없음. 정지 규칙은 규범 아닌 관측으로 계속 작동한다.

## 답
1.
