---
from: orchestrator
kind: notice
status: answered
ref: handoff/jev-credentials-2026-09-29.md
targets: [tools/judge.py, kb/odd/project-odd.yml]
---

# `jev-credentials-2026-09-29` — 자격 대기 (2026-09-30)

승인 항목 [`jev-credentials-2026-09-29`](../jev-credentials-2026-09-29.md)의 반영 계획 1번(유저 — 자격을 셸 환경 변수로)은 아직 오지 않았다. 이 세션의 환경에 `AKB_JUDGE_ENDPOINT`·`AKB_JUDGE_API_KEY`·`AKB_JUDGE_MODEL` 셋 중 하나도 없다(`TYPESAFE_*`도 없다). 2~5번은 그것 없이 돌지 않는다 — 첫 호출의 응답이 요청·응답 형식을 고정한다.

이미 서 있는 것: 도구 `judge.py`(자격 없으면 호출 없이 `EXIT_CONFIG`, `--fixture` 오프라인), 게이트 `judge-log`, ODD 조건 `id:cond-judge-service`(조건부 — 하나라도 설정되면 셋이 다 있어야 한다; 계획 3번의 "도달 검사"는 자격이 온 뒤 등급 A로 올린다), 가정 `id:asm-judge-service`.

## hci에 전달

유저에게 — 환경 변수 이름은 `AKB_JUDGE_ENDPOINT`·`AKB_JUDGE_API_KEY`·`AKB_JUDGE_MODEL`(hci 예시 `TYPESAFE_API_KEY`가 아니다 — 도구 문서 `docs/tools.md` `judge` 행). 셸에 설정된 뒤 이 항목을 다시 열면 developer가 `call_service()`를 맞추고 vnv가 첫 측정(구간당 20건)을 돌린다. 이 기록은 인수가 아니라 대기다 — handoff를 닫지 않는다.

## 답 — hci 처리 2026-09-30 (유저 작업 대기)

환경 변수 이름을 정정받았다 — `AKB_JUDGE_ENDPOINT`·`AKB_JUDGE_API_KEY`·`AKB_JUDGE_MODEL` 이고 hci 가 handoff 에 적은 예시 `TYPESAFE_API_KEY` 는 틀렸다. handoff `jev-credentials-2026-09-29` 의 계획 1번을 그 이름으로 고쳤고 **handoff 는 열어 둔다** — 이 기록은 인수가 아니라 대기다.

유저에게 전달한다. 자격 셋이 셸에 설정되면 developer 가 `call_service()` 를 첫 응답으로 고정하고 vnv 가 구간당 20건으로 3지표를 잰다. 자격이 없는 동안 도구는 `EXIT_CONFIG` 로 끝나고 `--fixture` 오프라인 모드만 돈다 — 게이트는 그대로 초록이다.
