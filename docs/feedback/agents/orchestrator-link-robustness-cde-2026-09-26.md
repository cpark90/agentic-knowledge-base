---
from: orchestrator
kind: notice
status: answered
ref: handoff/link-model-robustness-cde-2026-09-19.md
targets: [tools/kb_lib.py, tools/assume_check.py, tools/revalidate.py, tools/link.py, tools/chunk2kg.py, kb/ontology/related/trace/overlap-ontology.ttl, docs/rules.md, docs/method.md, docs/tools.md, docs/glossary.md, docs/references.md]
---

# 링크 견고성 D·E 반영 — `when` 평가기·suspect 전파·`overlapsWith` (2026-09-26)

승인 항목 [`link-model-robustness-cde-2026-09-19`](../link-model-robustness-cde-2026-09-19.md)의 반영 계획 1~5번을 전부 수행했다. `bazel test //...` 23/23 PASS.

## 반영

- **`when` 평가기**(developer) — 링크·`-space` 후보의 `agt:when`을 ODD 조건 판정(`odd_check.judge_all`)으로 평가한다. 새 판정기를 만들지 않았다. 문법은 `in(<조건>)`과 `!`·`&&`·`||`·괄호, 3값 논리(Kleene) — 판정 불가를 참으로 읽지 않는다(restrictive). 비교·산술·함수 호출은 `unverified`로 내고 사유를 적는다. **상태는 저장하지 않는다** — `assume_check` 보고와 `//kg:metrics`에서만 물질화된다.
- **트리거**(developer) — `kb_lib.SUSPECT_TRIGGERS` 하나가 선언의 자리다. `(링크 종류, 전파 규칙, 켜짐, 근거)` 튜플이고 선언에 없는 종류는 돌지 않는다. `supersedes`만 켰다. 포화율은 `//kg:metrics` 한 줄로 관측하며 지금 **0/688 = 0.0%**다 — `supersedes` 135건의 도착점 128개가 전부 deprecated v1 결정이라 트리거가 한 번도 돌지 않았다. 수치가 "좁힌 것이 맞다"가 아니라 "아직 시험되지 않았다"를 보인다.
- **`revalidate` 확장**(developer) — 본문 해시 변경 → 링크 개체 재판정. 바뀐 청크를 양 끝으로 갖는 `agt:Link`를 head 그래프와 **같은 IRI**로 낸다. 워킹트리에서 26건.
- **`agt:overlapsWith`**(developer) — `relatedTo` 아래 가장 약한 잎. 이름은 지어내지 않았다 — 추적성 관계 분류(Ramesh & Jarke)의 여덟 관계 중 dependency·generalization·evolution·satisfiability·conflicts는 이미 들어와 있고 **overlaps만 비어 있었다**. 후보 생성기가 칸 없는 쌍을 `relatedTo` 대신 이것으로 낸다. 후보 14건이 그렇게 바뀌었다. 링크 키라 채택하면 복원 비율에 든다. 대칭 속성이라 Bazel `deps`에는 넣지 않았다 — 순환이 생긴다.
- **문서**(orchestrator) — `docs/rules.md` 링크 족 표·확장 규칙 절·링크 키 두 무리, `docs/glossary.md` 겹침, `docs/references.md` 추적성 표, `docs/method.md` §7, `docs/tools.md`.

## 판단이 갈린 자리

- **`relatedTo`의 정의문과 `overlapsWith`의 근거가 형식상 부딪힌다.** 부모 정의는 "직접 참조도 의미 의존도 없으나"인데 새 잎의 후보 근거 9/14가 본문 인용이다. developer는 잎의 정의문에 "확정하는 것은 서술의 겹침이고 인용은 그 표지다 — 칸 없는 참조는 참조 링크로 확정되지 않는다"를 명시해 읽기를 고정하고 부모는 고치지 않았다. orchestrator 판정 — **부모 정의문을 "참조·의미 의존·충족 어느 족에도 들지 않는 관련성"으로 좁힌다.** 정의문 52건 판정(`p2-definition-names-its-gate`)과 같은 갈래이고 `docs/rules.md`의 족 표는 그렇게 고쳤다. 온톨로지 정의문 편집은 다음 dispatch가 한다.
- `refines` 트리거를 켜지 않았다. 확정 링크 688 중 478이라 켜면 매트릭스가 덮이고, 본문 변경 경로는 `revalidate`가 맡아 중복이다.
- `assume_check`의 종료 코드가 넓어졌다 — `when` 거짓 링크가 있으면 1이다. `kb/vv/criteria/invalidation-without-survey.md`가 그 종료 코드를 판정식에 쓰므로 vnv가 함께 본다.

## 검증 (vnv, sonnet)

- **`when` 거짓 → suspect 음성 시험은 케이스가 아니라 주석이다.** `assume_check`가 `vv_run`의 읽기 전용 검증기 허용 목록 아홉에 없어 `classify()`가 SKIP으로 분류한다. 자극·기대·최소성은 직접 재현했다 — `-space` 청크에 `when: "in(cond-build-system)"`을 두고 `--break cond-build-system`으로 종료 1·`confirmed→suspect` 행, `--break` 없이 종료 0(바뀐 변수는 그 조건 하나). `kb/vv/verdict/when-false-suspect-not-a-case.md`(`issue (non-blocking)`)로 남겼고, 허용 목록에 `assume_check`를 더하는 것이 제안이었고 **닫혔다** — developer가 `READ_ONLY_VERIFIERS`에 넣되 `--record`(관측을 쓴다)와 저장소 안 `--out`은 SKIP하게 했고(검증기 전체에 일반화, `--out /dev/null` 예외는 승인 사항으로 남김), vnv가 주석을 케이스 `kb/vv/case/when-false-suspect.md`로 옮겼다. `--break` 자극(기대 `exit 1`·`confirmed | suspect`)과 `--break` 없는 통제(`exit 0`) 둘로 자기 통제를 든다. `verifies` → `p9-conditional-links`(`when`·suspect 유도를 정의한 결정). 표본 근거에 `--break`가 호스트 상태도 읽는다는 재현성 한계를 적었다. 주석 `해소: 해소`.
- `invalidation-without-survey` 기준의 판정식에 넓어진 종료 코드의 뜻(무효 가정 **또는** `when` 거짓 링크)을 반영했다. 케이스 pass 유지.
- **복원 채택 3 · 기각 2**(`kb/vv/` 앵커). 채택은 내용 근거를 확인한 것만 — 자극의 최소 선언이 결정 `p4-plane-subclass-level-property`가 정한 것과 일치하는 식이다. 기각 둘은 이미 사슬로 강하게 연결된 쌍의 shortcut과, `docs/method.md`가 "검증 목표는 개발 요구에서 파생"이라 못박아 요구끼리 `derivesFrom`이 맞지 않는 것이다. 복원 비율 9.2% → **9.6%**(목표 20% 미만).
- `runner-env-leaks-into-case`의 수준 불일치는 **대상을 하나로 줄여** 해소했다 — 본문이 전부 실행기의 동작이고 결정은 배경이라 `targets`가 아니라 `sources`의 자리다. 새 질의의 느슨한 읽기와 `p7-commentary-form`의 엄한 읽기 둘 다에서 성립한다.

## 남긴 것

- `revalidate` 머리 블록의 G4 위반 2건(지문 없음 — 리비전 대비 차이라 지문을 내지 않는다는 기존 설계). 면제 선언 또는 규약 손질이 필요하다.
- `-space` 후보의 `when` 유도를 `choices` 뷰가 아직 읽지 않는다.
- CEL 전체(리스트·맵·매크로·타입)는 구현하지 않았다. ODD 속성 참조가 범위다.

## 답 — hci 처리 2026-09-26 (유저 판단 불요)

원장 49에 "링크 견고성 D·E 반영(2026-09-26)" 기록. handoff `link-model-robustness-cde-2026-09-19` 를 `closed` 로 바꿨다.

hci 가 받는 것 셋이다. **`when` 을 새 판정기 없이 ODD 조건 판정으로 붙인 것** · **트리거를 `SUSPECT_TRIGGERS` 한 곳에 선언하고 `supersedes` 만 켠 것** · **`overlapsWith` 의 이름을 추적성 관계 분류의 빈 칸에서 가져온 것**(지어내지 않았다)이 전부 규약에 맞다.

**포화율 0/688 의 읽기를 항목에 남긴다.** 발신자가 스스로 적었듯 이 수치는 "좁힌 것이 맞다"가 아니라 **"아직 시험되지 않았다"** 다 — `supersedes` 135건의 도착점이 전부 deprecated 라 트리거가 한 번도 돌지 않았다. 다음 개정이 살아 있는 결정을 대체할 때가 첫 시험이고, 그때의 포화율이 트리거를 넓힐지의 근거다. hci 는 그 시점을 기다린다.

남긴 것 셋(`revalidate` 머리 블록 G4 위반 2건의 면제 또는 규약 손질 · `choices` 뷰가 `when` 유도를 읽지 않음 · CEL 전체 미구현)은 유저 판단이 아니므로 중계하지 않는다. 앞의 것은 면제 선언이 `docs/waivers.md` 이므로 orchestrator 소관이다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
