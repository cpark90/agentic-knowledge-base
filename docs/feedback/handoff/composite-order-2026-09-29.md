---
from: hci
source: composite-order-2026-09-29.md
verdict: apply
status: closed
---

# 복합체 순서를 선언으로 — 결정도 예외 없이 (2026-09-29 승인)

유저 답: *"2."* — **승인하되 결정 복합체도 `ordered` 선언으로 돌린다.** 예외를 두지 않는다.
orchestrator 권장(선택지 1, 결정만 예외)과 다른 쪽이다.

## 파급효과

- 결정 `p4-composite-order-is-declared` 가 `stable` 로 올라가고 도장이 붙는다. **결론 본문에서 결정 예외 조항을 빼야 한다** — 승인된 것은 예외 없는 규칙이다.
- 결정 복합체 **205개**에 `ordered` 선언이 붙는다. 손으로 쓰면 첨가이므로 **생성기(`gen_build`)가 넣는다.**
- 규칙이 단순해진다 — "선언된 것만 순서를 방출한다"에 예외가 없다. 도구는 역할 이름으로 순서를 추측하지 않는다.
- 생성 BUILD 와 head 그래프가 함께 바뀐다. `//:build_drift_test` 가 재생성을 요구한다.
- 닿지 않는 것: ADR 뷰의 출력 순서(결론 → 근거 → 대안). 선언이 그 순서를 그대로 적으므로 결과가 같다.

## 반영 계획

1. **orchestrator — 결정 본문 수정.** 예외 조항("결정 복합체만 선언 없이 고정 순서")을 빼고 "모든 복합체는 순서를 선언한다"로 좁힌다. `status: draft → stable`, 도장은 쓰기 권한 역할이 `endorse` 로 붙인다.
2. **developer — 생성기.** `gen_build` 가 결정 묶음에 `ordered = ["결론", "근거", "대안"]`(또는 파일 순서에 해당하는 선언)을 넣는다. 손으로 205개를 고치지 않는다.
3. **developer — `chunk2kg`.** 역할 표지로 순서를 추측하던 갈래를 지우고 선언만 읽는다. 선언이 없는 복합체는 순서를 방출하지 않는다.
4. **developer — shape.** `composite-order-shapes.ttl` 이 선언과 방출의 일치를 판정한다. 결정 예외 분기가 있으면 지운다.
5. **vnv — 음성 시험.** 선언 없는 복합체가 순서를 방출하면 FAIL, 선언과 부분 목록이 어긋나면 FAIL 인 고정물 둘.

**검색 키워드**: `ordered` · `co:List` · `composite` · `순서` · `결정 복합체` · `gen_build` · `composite-order`.

## 확인 못 한 것

- 선언의 표기 자리. frontmatter 의 `composite:` 안인지 별 키인지 결정 본문이 정한 형식을 따른다 — hci 는 그 형식을 확인하지 않았다.
- 205개 선언이 head 그래프의 트리플 수를 얼마나 늘리는지. 복합체당 한 줄이면 205 트리플 남짓이다.

## 판정

`apply` 다. 유저가 권장과 다른 쪽을 골랐고 그 근거가 규칙의 단순함이다. **예외 조항 삭제가 반영의 핵심**이므로 결정 본문
수정을 1번에 두었다 — 그것을 빼먹으면 승인된 것과 결정이 어긋난다.

## 반영 확인 (hci, 2026-09-30)

인수 기록 [`../agents/orchestrator-accept-composite-order-2026-09-29.md`](../agents/orchestrator-accept-composite-order-2026-09-29.md) 로 돌아왔다 — 예외 조항을 빼고 결정 복합체 205개에 선언을 넣었다. 게이트 33/33 PASS.
제거는 인수 기록이 `closed` 로 바뀐 뒤 유저 lane·handoff·기록을 한 사슬로 함께 한다.
