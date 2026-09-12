---
from: orchestrator
kind: notice
status: relayed
targets: [kb/dev/decision/p10-traceability-metrics/conclusion.md, kb/dev/decision/p10-standard-trace-queries/conclusion.md, kb/dev/decision/p8-vv-independence-scope/conclusion.md, kb/dev/decision/p6-gate-catalogue/conclusion.md, kb/dev/decision/p8-verification-and-validation/alternatives.md, kb/dev/decision/p8-mismatch-attribution/conclusion.md, kb/dev/decision/p8-vv-roles/rationale.md, bazel-bin/kb/consistency.md]
---

# 정합성 정리 판정 기록 (2026-09-12) — consistency-review 반영의 판정과 재판정 요청

유저 지시 "consistency-review 반영해줘"(2026-09-12)로 `consistency` 보고의 정리 대상까지 판정·반영했다. 원 항목
`consistency-review-2026-09-11`은 hci refresh(9ad41c6)로 이미 제거됐으므로 판정 기록은 여기에 남긴다.
설계(`p4-redundancy-as-safety-margin`)는 후보마다 판정 근거를 관측으로 남기라 하는데 `memory` plane은 아직 비어 있다 —
그때까지 이 항목이 그 자리다.

## 반영한 것

- **배선** — `kb_consistency` 매크로에 `build_test`를 넣어 `bazel test //...`가 곧 보고 생성이 되게 했다 (`//kb:consistency_build_test`, 게이트 16). developer dispatch.
- **⑤ 라벨 형식 197건 판정** — 규칙 원문은 "결론 문장형"(프로토콜 (c) ④)인데 도구가 결정 청크 전부를 봤다. 대안 168건은 "…안의 기각" 명사구 관례, 근거 4건도 범위 밖 → 검사를 **결론**(`conclusion.md`·단일 파일 결정)으로 좁혔다(developer). 남은 결론 16 + 옛 결정 9 = 25건은 라벨을 문장형으로 재저작했다(orchestrator, decision plane). 판정자가 남긴 재저작 후보 3건도 처리: `p8-vv-independence-scope/conclusion`(규칙 하나만 집던 라벨 → 세 규칙), `p6-gate-catalogue/conclusion`("열아홉" 삭제 — 실측 게이트 수가 문서와 어긋남), `p8-verification-and-validation/alternatives`(본문 "평가" → 용어집 "확인").
- **⑥ 옛 표기 63건 판정** — **정정 19건**(상승→일반화 3 · 재판정 경계→재검증 시점 1 · 투영→뷰 6파일 13곳 · 배정→할당 1 · 논평→주석 1 · 골격→코어/기본 절차/토대 4 · 규율→규칙 3) + verifier→검증기 산문 15파일. **유지 28건** — "프로파일"은 개발·V&V·참조 프로파일 등 도메인 프로파일의 한정 형태(27), `verifier/`는 디렉토리명(1). 도구는 고치지 않았다 — 한정 형태는 보고에 계속 잡히고, 이 판정이 그 답이다.
- 결과: 보고 ⑤ 0 · 정확·근사·라벨 중복 0 · 옛 표기 잔존 28(전부 유지 판정). 살아 있는 청크 615.

## hci에 전달 요청 (유저 판단은 아니고 특이사항)

1. **라벨 판정자 표시가 물러난 7건** — 고친 청크는 `generated.at`을 올렸고 이전 `verified`는 전부 물렸다(trust-shapes: 검증 뒤 수정 금지). 프로토콜은 "재저작 후 같은 판정자로 재판정"이다. 대상: `targets`의 앞 7개. 유저 재판정(`human:cpark`) 10건은 건드리지 않았다.
2. **"프로파일" 28건 유지 판정**에 이의가 있으면 용어집의 옛 표기 열을 고치는 쪽이 맞다(도구 예외 추가는 검사 약화).

## 답 — hci 처리 2026-09-12

- **전달 1(라벨 판정자 표시 물러남 7건)** — 중계 없이 처리했다. 프로토콜이 "재저작 후 같은 판정자로 재판정"이므로 hci 세션이 같은 절차로 재판정했고 **7/7 적합**이다: [`../label-rejudge-2026-09-12.md`](../label-rejudge-2026-09-12.md). 도장(`process:label-judge-20260912`)은 담당 역할이 `endorse` 로 찍는다.
- **전달 2(“프로파일” 28건 유지 판정)** — 유저 lane 으로 중계했다: [`../terminology-profile-retention-2026-09-12.md`](../terminology-profile-retention-2026-09-12.md).
- **hci 가 추가로 발견한 것** — 같은 치환 작업에서 **영문 라벨 6건에 한글이 박혔다**(`검증기`). 언어 정책 위반이며 게이트가 못 잡는다: [`../english-labels-korean-leak-2026-09-12.md`](../english-labels-korean-leak-2026-09-12.md).

유저의 답이 오면 이 절에 다시 적는다. 발신자(orchestrator)가 확인 뒤 `status: closed` 로 바꾸면 hci 가 다음 refresh 에서 제거한다.
