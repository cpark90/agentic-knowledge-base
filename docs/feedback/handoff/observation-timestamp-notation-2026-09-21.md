---
from: hci
source: observation-timestamp-notation-2026-09-21.md
verdict: apply
status: closed
---

# 관측 청크의 시각 표기 (2026-09-21 항목, 2026-09-23 승인)

유저 답: *"1."* — **새 기록부터 G3 표기(`%Y-%m-%dT%H:%M:%SZ`)로 바꾸고 소급하지 않는다.** 규약에 소급 금지를 한 줄 적는다.

## 파급효과

- 고칠 자리는 넷이다 — `tools/assume_check.py:171`·`:179`, `tools/vv_run.py:143`·`:149`. frontmatter 는 `isoformat` 오프셋형, 본문 요약은 분 해상도를 쓴다.
- 기존 기록 셋(`obs-20260913T154324Z` · `run-20260919T062548Z` · `run-20260919T065358Z`)은 **커밋된 append-only 기록이라 고치지 않는다.** 두 표기가 한동안 공존하며 그것이 의도된 상태다.
- 정의처는 `kb_lib.GENDOC_TIME_FORMAT` 하나다. 주석이 이미 "오프셋 표기·분 해상도를 쓰지 않는다"고 적는다 — 관측 생성기가 그것을 쓰지 않고 있었을 뿐이다.
- 파일명 규약(UTC 압축형)은 그대로다. 닿지 않는다.
- 쓰기 범위가 갈린다 — 도구는 developer, `kb/vv/run/` 의 결과 확인은 vnv, `kb/dev/memory/` 는 orchestrator 다.

## 반영 계획

1. **developer — 네 자리를 `kb_lib.now_utc()` 로 통일**한다. frontmatter 의 `generated.at` 과 본문 요약 시각 둘 다 초 해상도 `Z` 표기가 된다.
2. **orchestrator — 소급 금지 한 줄.** `docs/rules.md` 의 관측 절 또는 `STYLEGUIDE.md` §4 `memory` 항에 "커밋된 관측 기록은 표기가 바뀌어도 소급하지 않는다"를 적는다. 적지 않으면 다음 세션이 소급을 시도한다.
3. **vnv — 다음 `vv_run --record` 결과가 새 표기인지 확인**한다. `kb/vv/` 는 vnv 의 쓰기 범위다.
4. **developer — `gendoc` 의 G3 검사를 관측 청크로 넓히지 않는다.** 관측은 생성 문서가 아니라 청크이고, 넓히면 기존 기록 셋이 FAIL 이 된다(선택지 3을 고르지 않았다).

**검색 키워드**: `GENDOC_TIME_FORMAT` · `now_utc` · `isoformat` · `strftime` · `관측` · `append-only` · `소급`.

## 확인 못 한 것

- 본문 요약의 분 해상도를 초로 올릴 때 요약 문장의 길이가 42줄 예산에 닿는지. 한 줄이라 영향은 없을 것이나 실측하지 않았다.
- 다른 생성기가 관측 형식을 참조하는지. `weave` 의 감사 보고서가 실행 기록을 읽으므로 표기 변경 뒤 그 절을 확인한다.

## 판정

`apply` 다. 답이 명확하고 편집이 네 줄이며 append-only 규율을 깨지 않는다.

## 반영 확인 (hci, 2026-09-29)

인수 기록 [`../agents/orchestrator-accept-observation-timestamp-notation-2026-09-21.md`](../agents/orchestrator-accept-observation-timestamp-notation-2026-09-21.md) 로 돌아왔다 — 관측 시각 표기를 새 기록부터 G3 으로 바꿨다. 게이트 32/32 PASS.
**제거는 인수 기록이 `closed` 로 바뀐 뒤다** — 기록의 `ref` 와 handoff 의 `source` 가 실재를 요구하므로 유저 lane 항목·handoff·기록이 한 사슬로 함께 나간다(2026-09-29 refresh 에서 순서를 잘못 잡아 게이트가 잡았다).
