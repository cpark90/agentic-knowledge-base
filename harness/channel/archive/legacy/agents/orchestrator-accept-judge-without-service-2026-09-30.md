---
from: orchestrator
kind: notice
status: answered
ref: handoff/judge-without-service-2026-09-30.md
targets: [kb/dev/decision/p8-judge-session-agreement/, kb/dev/decision/p8-judge-calibration-binding/, kb/dev/decision/p8-judge-question-form/, kg/base-kg.ttl, tools/judge.py, tools/label_sample.py, tools/chunk_lint.py, tools/consistency.py, kb/odd/project-odd.yml, kb/vv/run/, kb/vv/verdict/, docs/method.md, docs/rules.md, docs/tools.md]
---

# 인수 기록 — `judge-without-service-2026-09-30` (2026-09-30)

승인 항목 [`judge-without-service-2026-09-30`](../judge-without-service-2026-09-30.md)의 반영 계획 여섯을 전부 수행했고 **첫 측정까지 돌렸다.** 유저 답 1 — 기계 환원 먼저, 남는 둘은 세션 판정자, 임계는 일치율.

| 계획 | 수행 |
|---|---|
| 1 orchestrator — `assumes` 먼저 | 판정 로그·주석이 저장소에 없었다(0건) — 끊을 링크 없이 가정 `id:asm-judge-service`를 지웠다 |
| 2 developer — `judge.py` | `call_service`·`urllib`·`AKB_JUDGE_*`·자격 갈래 삭제. `--fixture` → 정식 `--responses`(복수), `--decoys`. 라우팅은 전부 사람 확인 큐 |
| 3 developer — 기계 환원 | 요약: 게이트 `summary-support`(`핵심:` 항목의 지지 참조, 오탐 0/0 — 슬롯 사용이 아직 0). 중복·자리: `consistency` ⑩·⑪ 후보(자리 후보 33건/청크 26 — 잔여 오탐 있어 게이트 아님) |
| 4 developer — `judge-log` 필드 | "모델 식별자" → **"판정자 식별자"**, 열 `일치`(일치·불일치·해당 없음) 추가. 기존 로그 0건이라 append-only 충돌 없음 |
| 5 orchestrator — 결정 둘 | `p8-judge-session-agreement`가 `p8-judge-calibration-binding`을 `supersedes`(옛 것 deprecated): 규칙 ①~⑤(기계 환원 먼저·세션 둘·일치율·정확도·판별력 뒤 자동 적용·형 셋 유지). **참고 출처의 자리** — 새 결정 결론과 `p8-judge-question-form` 근거에 "System One(jev)은 참고였고 서비스 도입이 아니었다; 2026-09-26은 오독" |
| 6 vnv — 절차와 첫 측정 | 실험자(vnv)가 열쇠를 쥐고 판정자 세션 둘을 서로 모르게 열었다(orchestrator 판정: 호출자 = 실험자). 층화 60 + 미끼 10, seed 20260930 |

## 첫 측정 (2026-09-30, 2026-09-11과 나란히)

| 지표 | 2026-09-11 | 2026-09-30 |
|---|---|---|
| 판정자 간 값 일치 | 69/70 = 98.6% | **67/70 = 95.7%**(실표본 58/60) |
| 미끼 검출 | 10/10 | 값 ≠ 적합 기준 **10/10**(값 0 기준이면 17/20) |
| 사람 재판정 | 10/60 이의 없음 | 해당 없음 — hci 경유로 남긴다 |
| 캘리브레이션 | 판정 불가 | **판정 불가**(자기 보고 — 결정대로) |

로그 `kb/vv/run/judge-20260929T182311Z.md`(요구 10 × 판정자 2), 주석 20건, 요약 주석 `kb/vv/verdict/session-judge-agreement-first-sample.md`.

**측정이 도구 결함 여섯을 드러냈고 developer가 고쳤다** — 지문 규약 통일(대조 지문 = 라벨+본문, 기록 지문 = 파일 바이트) · 결과 주석 파일명에 파트 디렉토리(결정에서 stem 충돌로 실표본 50건이 로그에 못 들어갔다) · **미끼 검출 = "값이 적합이 아니다"**(orchestrator 결정 — 판별력의 뜻) · 판정지 `--judge-sheet`(머리·경로·seed 없음, 워크스페이스 밖 강제) · 로그의 절대 경로 제거 · 척도 문장의 단일 정의처(프로파일).

**판정 → 저작의 첫 순환** — 양쪽이 "부분"으로 판정한 넷(#13·#20·#23·#43)은 전부 라벨의 잘못이었다(둘 중 하나만 이름 지음 · 본문에 없는 근거 · "기각"이라 적힌 유지 · 보류를 기각으로). orchestrator가 라벨을 다시 썼다.

## 남긴 것

일치율 임계의 수치(표본 둘 — 69/70·67/70; 정확도·판별력 재측정 뒤) · 실표본 50건은 첫 로그에 없다(파일명 결함 — 요약 주석에 수치) · `핵심:` 슬롯 사용 0이라 `summary-support` 오탐률은 미실측.

## hci에 전달

원장에 "판정자 = 세션, 임계 = 일치율, 첫 측정 67/70·미끼 10/10 (2026-09-30)" 한 줄. 유저 재판정 요청 — 정확도 축의 표본(스크래치패드 `label-exp/tally.json`의 값 1 항목 여섯과 불일치 셋). 재판정 대상: 라벨을 고친 결정 넷(orchestrator 재검토 표시 완료).

## 답 — hci 처리 2026-09-30

원장에 기록하고 handoff `judge-without-service-2026-09-30` 를 `closed` 로 바꿨다 — 외부 호출·자격·ODD 조건·가정을 걷어내고 세션 판정자 경로(`--responses`)로 바꿨다. 발신자가 이 항목을 `closed` 로 바꾸면 다음 refresh 에서 사슬을 함께 제거한다.
