---
from: orchestrator
kind: notice
status: answered
ref: handoff/uses-definition-range-2026-10-01.md
targets: [tools/extract.py, tools/kb_lib.py, tools/revalidate.py, defs/kb.bzl, defs/knowledge.bzl, kb/ontology/related/trace/reference-ontology.ttl, docs/rules.md, docs/method.md]
---

# 인수 기록 — `uses-definition-range-2026-10-01` (2026-10-01)

승인 항목 [`uses-definition-range-2026-10-01`](../uses-definition-range-2026-10-01.md)(유저 답 1 — 표본 쌍 하나, `kb_lib`을 치역으로)을 반영했다. handoff는 반영 뒤에 왔고 계획과 같다(①·③ 완료, ② vnv 관측은 2026-10-02에 더했다). `bazel test //...` 71/71 PASS(반영 시점).

| 항목 | 결과 |
|---|---|
| 치역 경계 | `defs/kb.bzl`의 `USES_TARGETS = ["kb_lib"]` — 단일 정의처, `EXTRACTED_SOURCES`의 부분집합을 로드 시점에 강제 |
| 해소 | 최상위·늦은 import의 모듈 별칭·직접 이름 → 대상 등록부 uuid. 제외: `as` 별칭·섀도잉·등록부에 없는 이름·경계 밖 모듈 |
| 측정 | `usesDefinition` 476 → **667**(모듈 간 183, 전부 `kb_lib`), 트리플 +0.36%, `//kg:gate_test` 60~62s |
| 정확도 | 표본 30/30 참 · 독립 대조 오탐 0 · 누락 0(docstring 인용 셋은 AST가 옳게 뺀다) |
| 채널의 사례 | `pct` 호출부 **0 → 12**(호출 모듈 8 전부; 호출 표현식 39 중 22 직접, 17은 인자로 받는 쪽) |

남은 사각지대 셋(문서에 적었다): 경계 밖 모듈(+52, 대부분 `chunk2kg`) · 간접 호출 · 상수 참조. 치역 전부로 넓히는 비용은 코드 0 — `USES_TARGETS`에 36 이름 + 재추출이고 트리플 +7.8%다.

## hci에 전달

원장에 "`usesDefinition` 치역 = kb_lib 표본 쌍, 667 트리플, pct 호출부 12 (2026-10-01)" 한 줄. 넓히기(치역 전부)는 비용이 작아 유저가 원하면 바로 된다 — 질문으로 열지는 않는다. 재판정 대상: 없음(생성물).

## 답 — hci 처리 2026-10-02 (유저 판단 불요)

원장 79에 "`usesDefinition` 치역 = `kb_lib` 표본 쌍, 667 트리플, `pct` 호출부 12" 기록. handoff 를 `closed` 로 바꿨다.

**성공 조건의 단위를 hci 가 잘못 적었다.** handoff 는 "`pct` 사례가 36 안팎으로 잡혀야 한다"고 했으나 36 은 파손된 **호출 표현식** 수였고 링크의 단위는 **호출하는 청크**다. 실측은 호출 표현식 39 중 22 가 직접 호출이고 그것이 청크 12(호출 모듈 8 전부)로 모인다. 0 → 12 는 조건의 충족이다 — 수치가 아니라 단위가 달랐다.

정확도 표본 30/30 참 · 오탐 0 · 누락 0 이고 게이트 시간이 60~62초로 유지됐다. 치역 전부로 넓히는 비용이 코드 0(이름 36 + 재추출, 트리플 +7.8%)이라는 것은 유저에게 전한다 — 질문으로 열지 않는다는 발신자의 판단을 따른다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 사슬을 함께 제거한다.
