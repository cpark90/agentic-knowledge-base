---
from: orchestrator
kind: question
status: relayed
targets: [kb/vv/verdict/, kb/vv/verifier/, tools/chunk2kg.py, defs/kb.bzl, kb/dev/decision/p4-all-knowledge-is-composite/]
---

# 판정 주석·검증기가 섰고 두 구조적 공백이 드러났다 (2026-09-22)

`annotation` plane 0 → **4**, `artifact` plane 0 → **3**이다. `bazel test //...` 22/22 PASS. 일곱 plane 중 여섯이 실물을 가졌다.

## 반영

- **결정**(orchestrator) — `p7-commentary-form`. 라벨 일곱·장식 셋·슬롯 다섯이고 `issue (blocking)` + `해소: 열림`만 게이트를 막는다. 어휘는 Conventional Comments에서 가져왔다.
- **배선·게이트**(developer) — `VV_PKGS`에 `verdict: annotation`, `agt:targets` 방출(`deps`는 만들지 않는다), 논평 슬롯 등록, shape `review-comment-body-shapes.ttl`, 게이트 `blocking-comment`. 음성 확인 셋을 실제로 돌렸다.
- **`vv_run` 판정 정정**(developer) — 명령 하나라도 건너뛰면 케이스가 `pass`가 아니라 `skip`이다. 판정 어휘를 넷으로 늘리지 않고 `pass`의 조건을 좁혔다. 지금 실측은 케이스 28(pass 26 · skip 2) · 명령 46(실행 44 · 건너뜀 2)이다.
- **청크**(vnv) — 판정 주석 4(라벨 넷이 서로 다르고 해소는 열림 2 · 해소 1 · 기각 1) · 검증기 3. `issue (blocking)`은 쓰지 않았다 — 실행이 fail 0이라 게이트를 막을 근거가 없다. 대신 임시 사본으로 게이트가 실제로 막는 것을 확인했다.
- **문서**(orchestrator) — `docs/tools.md`에 게이트 `blocking-comment`·shape·감사 절·`vv_run` 판정 규칙 정정.

## 유저 판단이 필요한 것 둘

### 1. 결정이 요구하는 복합체를 도구가 만들지 못한다

`p4-all-knowledge-is-composite`는 검증기를 **"케이스 열의 `co:List`"** 복합체로 정한다. vnv가 검증기 셋을 복합체로 묶으려다 `FAIL [chunk2kg] … part_of 대상 복합체가 이 묶음 안에 선언되지 않았다`를 받았다. 원인은 `chunk2kg --fragment`가 **파일 하나를 묶음으로 보는 것**이다. 복합체는 `kb_decision`처럼 여러 파일을 한 액션으로 묶는 규칙에서만 성립하므로, `kb_chunk` 단위 청크끼리는 복합체를 만들 수 없다.

같은 제약이 결정 표의 다른 줄에도 걸린다 — 요구의 "관심사별 복합체", 합격 기준의 "기준 집합", 시나리오의 "세 청크의 복합체"가 전부 같은 자리다. **지금 복합체를 가진 것은 결정뿐이다.**

가르는 것은 셋이다. 도구를 고쳐 `kb_chunk` 묶음 규칙을 만드는 것, 결정을 좁혀 복합체를 결정 전용으로 하는 것, 지금처럼 두고 결정과 실물이 어긋난 채 남기는 것이다. 셋째는 `r-009`(모든 산출물은 요구로 거슬러 오른다)와 감사에 불리하다.

### 2. 개발 KB의 `artifact` plane이 비어 있어 검증기가 대상을 갖지 못한다

vnv가 검증기 셋에 `verifies`를 **하나도 달지 못했다.** `verifies`는 같은 수준의 개발 KB 항목을 대상으로 해야 하는데(`defs/kb.bzl`) 개발 KB에 `executable` 수준 항목이 0이고 `artifact` plane도 0이다. 사다리 대응이 개발 쪽에서 비어 있다. 세 검증기 본문에 `**검증 대응물** — 없음`과 근거를 적었다.

이것은 로드맵 6단계의 tangle("복합체의 `artifact` 부분을 `co:index` 순으로 이어 붙인다")이 없는 것과 같은 자리다. 이 저장소의 코드는 `tools/*.py`이고 청크로 올라와 있지 않다. 올리면 `artifact` plane이 서고 검증기가 대상을 갖지만, 코드를 청크로 저장하는 것은 **저장소의 작업 방식을 바꾼다.** 유저 판단 사항이다.

## 부수 실측

- **연결 성분 4 → 6.** 새 청크 7건 중 검증기 2개(`gate-test-targets`·`negative-failure-test`)가 링크 없이 고립됐다. vnv는 `refines`로 케이스 하나를 임의로 고르는 것이 사다리를 오염시킨다고 보아 하지 않았다 — 옳은 판단이다. 위 공백 2가 풀리면 `verifies`로 붙는다.
- **논평이 관측을 묶는 수단이 됐다.** `agt:targets`가 `metrics`의 간선 15종에 들어 있어, 실행 기록 2건을 함께 가리킨 논평 하나가 그 둘을 한 성분으로 묶었다. 관측의 고립을 푸는 길이 하나 생겼다 — 유저 항목 `connected-components-observations`에 더할 실측이다.
- 고아율은 0/760 = 0.0%로 그대로다. 고아율과 연결 성분은 다른 지표다.

## 중계 (hci, 2026-09-26)

유저 lane 항목으로 올렸다 — [`../composite-beyond-decisions-2026-09-26.md`](../composite-beyond-decisions-2026-09-26.md) · [`../code-as-chunks-2026-09-26.md`](../code-as-chunks-2026-09-26.md). 한 파일에 한 주제 규약대로 질문마다 항목을 따로 세웠고 다섯 절로 썼다. hci 가 실측으로 확인한 줄은 항목에 표시했다. 유저 답이 오면 이 항목에 옮기고 `answered` 로 바꾼다.
