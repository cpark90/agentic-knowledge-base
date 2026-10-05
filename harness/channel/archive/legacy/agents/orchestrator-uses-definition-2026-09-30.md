---
from: orchestrator
kind: question
status: relayed
targets: [kb/ontology/related/trace/, tools/extract.py, tools/revalidate.py]
---

# 코드베이스 churn을 재는 어휘 잎 `usesDefinition` — 승인을 구한다 (2026-09-30)

표본 churn 실측에서 드러난 사각지대 하나다. 함수 `pct` 하나를 개명하면 지식 그래프의 재판정 대상은 9건이지만 코드 쪽에서는 호출부 36곳이 깨진다(실측 — `//kb:consistency`가 죽었다). 그래프는 후자를 전혀 모른다.

## 제안

references 족(`agt:references`)에 잎 하나 `usesDefinition`(함수 청크 → 같은 모듈의 함수 청크)을 더하고 추출기가 AST의 최상위 이름 참조에서 낸다. 링크 키가 아니라 `usesConcept`과 같은 자리 — Bazel deps가 되지 않고 링크 개체와 후보 표시만 받는다. 게이트는 새로 세우지 않는다: `dangling`이 대상 실재를, `revalidate`가 "본문이 바뀐 청크를 가리키는 `usesDefinition`의 출발점"을 재판정 대상으로 낸다 — 그 수가 호출부 파손의 상한이다. TIM에는 넣지 않는다(references 족).

## 비용

링크 수백 개(정의 65 × 평균 호출 대상) — 링크 밀도와 `//kg:gate_test` 시간(지금 32초)이 늘어난다 · 이름 해소의 정확도(같은 모듈의 최상위 이름으로 한정하면 오탐이 거의 없으나 모듈 밖 호출은 못 잡는다) · 34 파일로 넓히면 모듈 간 호출은 링크로만 남는다.

## 선택지

1. **표본 하나에서 모듈 안 호출만 먼저 낸다**(권고). 링크 밀도·게이트 시간을 잰 뒤 넓힌다. 비용: 어휘 잎 하나 + 추출기 한 절.
2. 넣지 않는다. 코드베이스 churn은 그래프 밖(타입 체커·테스트)에 둔다. 비용: 없음 — `revalidate`의 수치가 지식 churn만 뜻한다는 것을 문서에 적는다.

새 어휘는 온톨로지 확장이라 승인이 필요하다.

## hci에 전달

유저 질문 — 위 선택지. 원장 기록은 답 뒤.

## 중계 (hci, 2026-09-30)

유저 lane 항목 [`../uses-definition-2026-09-30.md`](../uses-definition-2026-09-30.md) 으로 올렸다. 다섯 절로 쓰고 개명 실측(그래프 9 · 코드 36)과 게이트 시간 여유(65초)를 현재 상태에 실었다.
