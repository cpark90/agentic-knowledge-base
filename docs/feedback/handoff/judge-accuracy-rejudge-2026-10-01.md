---
from: hci
source: judge-accuracy-rejudge-2026-10-01.md
verdict: apply
status: open
---

# 판정자 정확도 축 — 유저 재판정 10건 (2026-10-01 승인)

유저 답: *"1."* — **10건 재판정.** 불일치 셋 + 무작위 일곱을 hci 가 판정지로 만들고, 유저가 채우면 vnv 가 정확도를 계산한다.

## 파급효과

- 3지표 가운데 **정확도 축이 처음 채워진다.** 판별력(10/10)·판정자 간 일치(67/70)와 함께 자동 적용 조건 둘 중 하나가 완성된다.
- **판정자 응답이 휘발성 자리에 있었다** — 다른 세션의 스크래치패드. hci 가 `a.json`·`b.json`·`key-fp.json` 셋을 `docs/feedback/inquiries/label-exp-2026-09-30/` 로 **복사**해 두었다. 채널은 임시 자리이고 정식 자리는 `kb/vv/run/`(관측)이다 — vnv 가 옮긴다.
- 판정지는 [`../judge-rejudge-sheet-2026-10-01.md`](../judge-rejudge-sheet-2026-10-01.md) 다. 판정자의 값은 판정지에 없다. 유저의 편향을 막기 위해 **아래 표에만** 둔다.
- 닿지 않는 것: 결정 `p8-judge-question-form` 의 임계·형. 수치가 나온 뒤 임계를 정하는 것은 별도 항목이다.

## 판정 키 (유저에게 보이지 않게 — 정확도 계산용)

| 판정지 번호 | 표본 n | 청크 | 층 | 판정자 a | 판정자 b |
|---|---|---|---|---|---|
| 1 | 12 | `kb/dev/decision/p1-partial-observability-harness-projections/conclusion.md` | conc | 1 | 2 |
| 2 | 20 | `kb/dev/decision/p6-gate-catalogue/rationale.md` | rat | 1 | 1 |
| 3 | 25 | `kb/dev/decision/p0-artifact-filename-suffix/rationale.md` | rat | 2 | 2 |
| 4 | 28 | `kb/dev/decision/pe-scenario-is-openscenario/rationale.md` | rat | 2 | 2 |
| 5 | 42 | `kb/dev/decision/p7-dev-kb-outputs-and-metrics/conclusion.md` | conc | 2 | 2 |
| 6 | 46 | `kb/dev/requirement/r-019-record-read-write-sets.md` | req | 2 | 2 |
| 7 | 56 | `kb/dev/decision/p11-inputs-as-versioned-vocabulary/conclusion.md` | conc | 2 | 2 |
| 8 | 58 | `kb/dev/decision/p9-constraint-sources-and-kinds/alternatives.md` | 미끼 | 0 | 1 |
| 9 | 62 | `kb/dev/decision/p9-contradiction-handling/alternatives.md` | alt | 1 | 2 |
| 10 | 66 | `kb/dev/decision/p12-symbolic-diagnosis/rationale.md` | rat | 2 | 2 |

척도는 적합 2 / 부분 1 / 부적합 0 이다. #58 은 미끼(라벨을 다른 청크의 본문에 바꿔 붙인 것)라 정답이 0 이다.

## 반영 계획

1. **유저 — 판정지 10건.** 1단계(라벨만 보고 예측) → 2단계(본문 보고 3점). 끝나면 판정지의 `status: open → done`.
2. **vnv — 정확도 계산.** 유저 값을 사람 기준으로 삼아 판정자 a·b 각각의 일치 수를 낸다(10 중 몇). 불일치 셋은 **누가 맞았는지**가 결과다. 미끼 #58 의 유저 값이 0 이 아니면 그 자체가 관측이다.
3. **vnv — 관측으로 남긴다.** `kb/vv/run/` 에 판정 관측 하나(seed·표본·값·정확도). 복사해 둔 응답 셋도 그 옆으로 옮기고 채널의 복사본은 다음 refresh 에서 hci 가 지운다.
4. **orchestrator — 결정 보강.** 정확도 수치가 나오면 `p8-judge-question-form` 의 일치율 임계 항에 첫 실측(판정자 일치 69/70·67/70, 사람 일치 N/10)을 적는다. 임계 수치 자체는 표본이 더 쌓인 뒤의 항목이다.

**검색 키워드**: `labelRepresentsBody` · `정확도` · `재판정` · `미끼` · `judge-a` · `judge-b` · `label-exp` · `일치율`.

## 확인 못 한 것

- 유저 10건으로 정확도의 신뢰 구간이 얼마나 넓은지. 2026-09-11 과 같은 수(10)라 비교는 되나 통계적 근거는 없다.
- 표본의 층 비율. 무작위 일곱은 실표본 60 에서 균등 추출이라 층(요구·결론·근거·대안)이 고르지 않을 수 있다.
- 응답 JSON 의 정식 자리. `kb/vv/run/` 의 관측은 42줄 청크라 JSON 을 그대로 담지 못한다 — 지문과 요약만 청크에 두고 원본은 생성 트리 파일로 둘지 vnv 가 정한다.

## 판정

`apply` 다. 유저 작업 하나(10건)가 전부이고 판정지가 준비됐다. **휘발성 데이터를 먼저 채널로 옮긴 것**이 이 handoff 가 한 일의 절반이다.
