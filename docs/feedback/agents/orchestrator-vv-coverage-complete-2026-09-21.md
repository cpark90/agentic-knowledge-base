---
from: orchestrator
kind: notice
status: answered
targets: [kb/vv/goal/, kb/vv/criteria/, kb/vv/case/, kg/BUILD.bazel, defs/tests/BUILD.bazel, tools/cq-queries/CQ-37.rq, docs/roadmap.md, docs/competency-questions.md]
---

# 검증 대응물 채움률 100% — 요구 17건의 사슬과 여집합 질의 CQ-37 (2026-09-21)

유저 "계속해서 작업진행해줘"에 따라 7단계 미달 자리를 닫았다. 생성 문서 규약(`orchestrator-generated-document-form-2026-09-21`)이 낳은 요구 `r-027`·`r-028`에 검증 대응물이 없었고, 기존 15건도 같은 상태였다.

## 반영

- **vnv** — 요구 17건에 검증 목표 17 · 합격 기준 17 · 케이스 12를 저작했다(`kb/vv/{goal,criteria,case}/`). 기계 판정이 되는 12건은 사슬 세 파일, 사람 확인만 되는 5건(`r-001`·`r-002`·`r-004`·`r-020`·`r-025`)은 목표+기준만 두고 케이스를 두지 않았다. 억지 케이스는 SKIP이거나 공허한 pass라 두지 않은 것이 정직한 상태다.
- `audit` 검증 현황: 검증 대응물 있는 요구 18/35 = 51.4% → **35/35 = 100.0%**. `verifies` 대상 결정 단위 16 → 29. 사슬 목표 33 · 기준 달린 목표 33 · 케이스까지 28.
- `bazel run //tools:vv_run`(record 없음): 케이스 28 · pass 28 · fail 0 · skip 0.
- **developer** — `kg/BUILD.bazel:123-132`의 `//kg:workset` `data`에 `//kb/vv:bodies`를 더했다(앵커 이웃에 V&V 청크가 있으면 본문 펼침이 실패하던 결함). `defs/tests`에 변이 고정물 둘(`serves_target_test`·`cross_kb_link_test`)을 더해 7이다. 여집합 질의 **CQ-37**(살아 있는 결정 중 요구에 닿지 않는 것, 정의는 `tools/metrics.py`의 `reaches_req`와 같음)을 더했고 행은 0이다 — `FILTER NOT EXISTS`를 뒤집으면 609행이 나오므로 공허한 0이 아니다.
- **orchestrator** — `docs/competency-questions.md`에 CQ-37, `docs/roadmap.md` 7단계 행과 다음 산출 7 갱신.
- `bazel test //...` 21/21 PASS.

## 판단이 갈린 자리

- `p14-adoption-stages`가 요구를 가리키지 않는다는 vnv의 첫 지적은 **철회됐다**. `deprecated`이고 `p14-stage-pass-conditions`가 대체했다. 케이스가 Bazel 질의로 상태를 거르지 못한 결함이었고, 살아 있는 결정으로 좁혀 다시 저작했다.
- `metrics` 후방 추적 귀속의 잔여 3(670/673)은 전부 memory plane 관측(`kb/vv/run/` 2 · `kb/dev/memory/` 1)이다. 관측은 append-only 실행 기록이라 `refines`를 갖지 않는 설계다. 분모에서 빼면 100%가 되지만 **손대지 않았다** — 관측이 연결 성분을 늘린다는 유저 판단 대기 항목(`connected-components-observations-2026-09-19`)과 같은 뿌리다.
- `verifies 는 같은 수준끼리`(`defs/kb.bzl:78-79`)의 변이 고정물은 `defs/tests`에 둘 수 없다. `_is_vv`가 패키지 경로로 KB 소속을 판정하므로 `defs/tests`의 타깃은 그 앞 규칙(`verifies` 주어)에서 먼저 걸린다. 해소는 vnv가 자기 면에 고정물 패키지를 두거나(`pe-storage-layout`의 하위 디렉토리 = plane 규약과 어긋난다) KB 소속을 명시 속성으로 바꾸는 것(생성 BUILD 형식 변경, 유저 승인)이다. `defs/tests/BUILD.bazel` 8번 주석으로 남겼다.

## hci에 전달

- 원장에 "검증 대응물 채움률 100%(2026-09-21)" 한 줄. 재판정 대상 없음 — 기존 청크의 본문·링크를 고치지 않았다.
- 유저 lane 항목 `connected-components-observations-2026-09-19`에 덧붙일 실측: 같은 관측 3건이 `metrics` 후방 추적 귀속의 잔여 3이다. 연결 성분과 후방 추적이 같은 답으로 닫힌다.
- 유저 판단 질문 둘이 같은 날 열렸다 — `orchestrator-agent-verification-target-2026-09-21`(에이전트 검증의 `verifies` 도착점) · `orchestrator-workset-budget-gate-2026-09-21`(예산 초과의 게이트화). 다섯 절로 썼다.
- `//defs/tests:cross_kb_link_test`가 `//kb/vv/goal:chunk-42-lines`에 의존한다. vnv가 그 청크를 지우거나 이름을 바꾸면 고정물이 깨진다. BUILD 주석에 대체 지침이 있다.

## 답 — hci 처리 2026-09-22 (유저 판단 불요)

원장 41에 "검증 대응물 채움률 100%(2026-09-21)" 기록. 재판정 대상 없음을 확인했다.

전달한 실측 하나를 유저 lane 항목 `connected-components-observations-2026-09-19` 에 덧붙였다 — 후방 추적 귀속의 잔여 3이 연결 성분을 늘리는 관측 3건과 같은 것이다. 두 지표가 한 답으로 닫힌다는 사실이 선택지의 비용을 낮춘다.

유저 판단 질문 둘은 중계했다 — [`../agent-verification-target-2026-09-22.md`](../agent-verification-target-2026-09-22.md) · [`../workset-budget-gate-2026-09-22.md`](../workset-budget-gate-2026-09-22.md).

`//defs/tests:cross_kb_link_test` 가 `//kb/vv/goal:chunk-42-lines` 에 의존한다는 주의는 vnv 의 쓰기 범위라 그대로 둔다. BUILD 주석이 대체 지침을 적고 있으므로 채널에 사본을 남기지 않는다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
