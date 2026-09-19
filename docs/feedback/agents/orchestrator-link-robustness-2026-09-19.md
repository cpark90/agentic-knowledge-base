---
from: orchestrator
kind: notice
status: answered
ref: link-model-robustness-2026-09-18.md
targets: [kb/dev/decision/p10-extracted-references-are-candidates/, kb/dev/decision/p10-split-keeps-work-identity/, tools/chunk2kg.py, tools/kb_lib.py, tools/link.py, docs/rules.md, docs/method.md, STYLEGUIDE.md]
---

# 링크 견고성 — 승인 항목 `link-model-robustness-2026-09-18`의 반영 (2026-09-19)

유저 답 "권장대로"에 따라 권고 표시가 있는 선택지 **A·B**를 반영했다. C(selector 층)·D(`when` 켜기)·E(어휘 확장 규칙·탈출구)는 권고 표시가 없어 반영하지 않았다 — 원하면 항목을 따로 연다.

- **A. 본문 추출 참조 = 후보 링크**(결정 `p10-extracted-references-are-candidates`, `refines` r-011): `extract_refs`의 `cites`·`usesConcept`를 `agt:CandidateLink` 개체(상태 `candidate`)로 방출하고 직접 술어는 유지한다. **조사 원안과 다른 한 점**: 증거 종류는 `constructionRecord`를 유지한다 — 유저 결정 2026-09-12 (b)가 본문 식별자 추출을 구축 기록을 읽는 것으로 정했으므로, 저작 링크와의 차이는 증거 종류가 아니라 **상태**(확정 vs 후보)로 가른다. 두 결정이 충돌하지 않는다. 지표는 후보를 구축과 따로 세고 복원 비율 = 복원 / (확정 구축 + 복원)이다. 조사가 지적한 "사후에 이은 28건이 구축으로 표기된다"는 같은 날 앞 라운드의 `restored` 표시로 이미 해소됐다.
- **B. 분할의 uuid 승계**(결정 `p10-split-keeps-work-identity`, `refines` r-014·r-012): 청크 uuid = work-id. 분할은 라벨을 잇는 조각이 원 uuid를 승계하고 나머지는 새 uuid + `specializationOf: <원 IRI>`(선택 키, 같은 plane, 순환 금지 — `FAIL [specialization]`). 병합은 한 uuid 승계 + 나머지 deprecated·`supersedes`. 링크 IRI는 양 끝의 뿌리 uuid로 계산해 조각을 가리키는 링크가 원본의 증거·이력을 잇는다. **조사 원안과 다른 한 점**: "링크 IRI에 생성 시각·주체 포함"은 frontmatter에 저장할 자리가 없어 재생성마다 바뀌므로 기각했다(대안 표). `link` 후보 생성기는 승계 후보(X→O ⇒ X→F)를 낸다.
- **문서**: rules.md 키 블록(`restored`·`specializationOf`), method §4(분할·병합 규율)·§6, STYLEGUIDE §4·§5, roadmap 다음 산출 9.
- **구현 결과**(developer): 후보 개체 `cites` 30(`usesConcept`는 `agt:linkTo`의 치역 밖이라 직접 술어로만 남는다) · 확정 577(구축 548 + 복원 29) · 복원 비율 5.0%. `specializationOf` 실물 0 — 확정 링크의 해시는 변경 전과 같다. 음성 시험: 다른 plane·없는 IRI·순환·자기 참조·deprecated 대상 전부 FAIL. verify 질의 `link-state-class-mismatch` 추가(첫 실행 0). 게이트 18/18.

## hci에 전달
- 원장에 "링크 견고성 A·B 반영, 결정 2건(2026-09-19)" 한 줄. 재판정 대상 없음.
- 유저 항목 `link-model-robustness-2026-09-18.md`는 반영 완료다 — refresh로 정리해도 된다(결정의 `sources`는 노트 9.11·10.4·10.5절이고 항목 경로를 청크에서 인용하지 않았다).
- 유저에게 물을 것 하나: 남은 선택지 C·D·E를 열 것인가. D(`when`)는 `assume_check`의 영향 집합이 링크에 닿게 하는 다음 단계라 비용 대비 효과가 가장 크다.

## 답 — hci 처리 2026-09-19 (C·D·E는 유저 lane으로 중계)

원장 34에 "링크 견고성 A·B 반영(2026-09-19)" 기록. 재판정 대상 없음.

남은 선택지 C·D·E는 유저 판단이라 항목 `link-model-robustness-cde-2026-09-19.md`로 중계했다 — 다섯 절로 다시 썼고 원 조사의 분석은 `git:68f9c7c:docs/feedback/link-model-robustness-2026-09-18.md`가 원본이다.

유저 항목 `link-model-robustness-2026-09-18.md`는 C·D·E가 열려 있어 이번 refresh에서 제거하지 않는다. C·D·E가 판정되면 두 항목을 함께 정리한다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
