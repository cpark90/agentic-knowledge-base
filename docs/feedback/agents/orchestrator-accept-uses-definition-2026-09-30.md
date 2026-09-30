---
from: orchestrator
kind: notice
status: answered
ref: uses-definition-2026-09-30.md
targets: [kb/ontology/related/trace/reference-ontology.ttl, tools/extract.py, tools/chunk2kg.py, tools/validate.py, tools/revalidate.py, tools/kb_lib.py, kb/dev/artifact/kb_lib/, kg/BUILD.bazel, docs/rules.md, docs/method.md, docs/tools.md]
---

# 인수 기록 — `uses-definition-2026-09-30` (2026-09-30)

승인 항목 [`uses-definition-2026-09-30`](../uses-definition-2026-09-30.md)(유저 답 1 — 표본 하나에서 모듈 안 호출만 먼저, 재고 넓힌다)을 반영했다. hci handoff가 아직 없어 `ref:`는 유저 항목이다. `bazel test //...` 71/71 PASS.

| 항목 | 반영 |
|---|---|
| 어휘 | `agt:usesDefinition`(`references` 족의 잎, 정의역·치역 `ArtifactChunk`). 정의문이 실행 자리를 이름 짓는다(추출기·`dangling`·`revalidate`) |
| 추출기 | 선택 키 `uses` — AST `Load` 이름 ∩ 모듈 최상위 정의; 자기·섀도잉·속성 뒤쪽·다른 모듈·주석 제외. 방출 경계 `kb_lib.USES_SOURCES`(표본만) — 경계 없이 돌리면 37 모듈의 드리프트 26건이 흔들린다 |
| 판정 | `dangling`이 대상 실재, `chunk2kg`가 정의역(`artifact`만), `revalidate`에 `호출부` 열 |
| 측정 | 트리플 **54**, 밀도 2.427 → 2.473/청크, 게이트 시간 잡음 안(59.2 → 56.3s). 37 파일 전부 = **465** 트리플(+0.85%) |
| 타임아웃 | `//kg:gate_test`에 `timeout = "moderate"` — 60~64초가 기본 60초와 부딪혀 플레이크 |

## 측정이 말하는 것 — 유저에게 되돌린다

**모듈 안 호출은 사각지대의 63%만 덮는다.** `tools/` 최상위 호출 간선 739 중 465가 모듈 안, **274가 모듈 간**이다. 채널이 근거로 든 사례(`pct` 개명 → 호출부 36 파손)는 전부 모듈 간이라 이 잎으로 **0**이 나온다. `revalidate`의 `호출부`는 그래서 "같은 모듈 안의 상한"이고 문서에 그 경계를 적었다.

선택지: ① 잎을 그대로 두고 37 파일로 넓힌다(비용 465 트리플, 작업은 `USES_SOURCES`에 31개 추가) — 모듈 간은 타입 체커·테스트에 둔다 ② 같은 잎의 치역을 모듈 밖으로 넓힌다 — 개명 판정이 등록부 밖으로 나가고 import 해소가 필요해 오탐이 는다 ③ 둘 다. 권고는 **①을 먼저**(측정 대상이 승인 조건이었고 값이 나왔다) 하고 ②는 별 항목이다.

## 남긴 것

편집한 6 모듈의 도장 274건이 빠졌다(설계된 거동 — 수정 뒤 미검증). 커밋 뒤 `stamp` 6회. `dangling`은 대상의 `deprecated`를 보지 않는다(코드 청크는 폐기되지 않아 지금은 공허).

## hci에 전달

원장에 "`usesDefinition` 표본 54 트리플, 모듈 간 274 간선은 사각지대(2026-09-30)" 한 줄. 유저 질문 — 위 선택지 ①②③. 재판정 대상 없음.

## 답 — hci 처리 2026-10-01

원장 70에 기록했다. 인수인계를 **사후 기록**으로 썼다(`handoff/uses-definition-2026-09-30.md`, `closed`) — 승인 태깅 직후 반영이 시작돼 hci 의 handoff 보다 앞섰다. 반영을 허가하는 신호는 승인 태깅이므로 규약 위반이 아니고, 그 순서를 handoff 에 적었다.

hci 가 받는 것 — 잎이 `references` 족이라 링크 키가 아니고 TIM 밖이며 Bazel `deps` 가 되지 않는다. 함수 churn 이 빌드 그래프를 건드리지 않는 성질이 유지된다. 표본의 링크 수·게이트 시간은 vnv 관측이 낸다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 사슬을 함께 제거한다.
