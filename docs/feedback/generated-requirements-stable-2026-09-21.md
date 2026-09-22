---
from: hci
status: open
targets: [kb/dev/requirement/r-027-generated-documents-carry-provenance.md, kb/dev/requirement/r-028-generated-documents-share-one-form.md]
---

# 요구 `r-027`·`r-028`을 stable로 올릴 것인가 (2026-09-21)

원본: [`agents/orchestrator-generated-document-form-2026-09-21.md`](agents/orchestrator-generated-document-form-2026-09-21.md)

## 질문

생성 문서 규약을 반영하면서 요구 둘이 새로 생겼다. **요구의 stable 전이는 유저 승인 사항**이라 orchestrator가 `draft`로
두었다. 둘을 stable로 올릴 것인가.

어려운 이유는 이 둘이 **이미 강제되고 있다**는 데 있다. 게이트 `//:gendoc_test`가 켜져 있고 생성기 전부가 규약을 따른다.
즉 요구의 상태와 실제 강제력이 어긋나 있고, 그 어긋남을 상태를 올려 없앨지 게이트를 되돌려 없앨지가 질문이다.

## 이미 정해진 것

- 요구 저작은 orchestrator의 몫이고 **stable 전이는 유저 승인**이다(`AGENTS.md` 역할 표).
- 요구 `documents-are-generated`와 결정 `p12-documents-are-generated` — 생성물마다 생성 시각과 질의를 적는다.
- 규약 G1~G18의 근거는 전부 외부 출처다(markdownlint·Microsoft Writing Style Guide·ISO/IEC/IEEE 26514:2022·WCAG 2.2·PROV-O·Sandve et al. 2013·IEC/IEEE 82079-1:2019). 받지 않은 것 셋도 `docs/references.md`에 적혀 있다.
- 결정 3건(`p12-generated-document-header`·`p12-generated-document-form`·`p12-generated-documents-are-gated`, 9청크)이 이 둘을 `refines` 한다.

## 현재 상태 (실측 2026-09-21)

- `kb/dev/requirement/`의 요구 35건 가운데 **33건이 stable, 2건이 draft**다. draft는 이 둘뿐이다.
- 게이트 19/19 PASS. `//:gendoc_test`의 입력은 생성 뷰 11종과 SKILL.md 16개다.
- 생성물 머리 블록이 실제로 바뀌었다 — `bazel-bin/kg/metrics.md`는 생성기 `tools/metrics.py · gendoc/1`, 시각 `2026-09-21T12:40:27Z`, 입력 지문 `sha256:aac70976f420`, 재현 명령 `bazel build //kg:metrics`를 담는다.
- 조사가 잡은 실측 결함 7건(트리플 수 세 갈래·`index.md` 링크 610개 파손·`cq.md` 이중 접두 등)은 해소됐다.

## 답이 가르는 것

- **stable이면** 검증 대응물 분모가 33에서 35로 늘고, 두 요구는 검증 대응물이 없는 요구 목록에 새로 들어간다(현재 15/33 → 17/35). 추적 지표가 즉시 나빠 보이지만 그것이 실상이다.
- **draft로 두면** 게이트는 계속 돌지만 요구 층은 미확정으로 남는다. `//kg:audit`의 요구 집계가 강제되는 규칙을 세지 않아, 감사 보고서가 체계의 실제 구속력을 과소 보고한다.
- **되돌리면** 게이트를 끄는 것이고, 이것은 검사 약화라 별도 승인 사항이다.

## 선택지

1. **둘 다 stable로 올린다** (권고). 근거: 규약이 이미 게이트로 강제되고 근거가 전부 외부 표준이다. 비용: orchestrator가 두 파일의 `status`를 고치고 `bazel test //...` 확인. 검증 대응물 비율이 17/35로 표시된다.
2. **`r-027`만 올린다.** 출처·재현 수단은 확정하고 서식(`r-028`)은 규약 버전이 한 번 더 도는 것을 본 뒤 올린다. 비용: 같은 편집 하나. 서식 규약이 바뀌면 요구를 고치지 않아도 된다.
3. **둘 다 draft로 두고 재검토 시점을 정한다.** 예를 들어 생성 뷰가 15종이 되는 시점이다. 비용: 그때까지 감사 보고서의 과소 보고를 감수한다.

## 답
(유저가 채움)
