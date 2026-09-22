---
from: orchestrator
kind: notice
status: open
targets: [space/, kb/ontology/related/trace/space-ontology.ttl, kb/ontology/shapes/space-shapes.ttl, tools/space2kg.py, tools/choices.py, kb/dev/decision/p9-candidate-storage/, kb/dev/decision/p7-commentary-form/, docs/method.md, docs/tools.md, docs/roadmap.md]
---

# 도입 5단계의 첫 형태 — 설계 공간 `-space`와 논평 형식 (2026-09-22)

유저 "계속해서 진행해줘"에 따라 정제 계층의 공백을 열었다. `bazel test //...` **22/22 PASS**다.

## 무엇이 공백이었는가

`abstract` 수준이 전 plane에서 0이고 `space/`가 비어 있었다. 이것은 결함이 아니다 — `p7-decision-spans-three-levels`가 "abstract 변수 청크는 **`-space`가 있는 결정에만** 만든다"고 정했고 `-space`가 없었기 때문이다. 그래서 5단계는 abstract를 억지로 만드는 일이 아니라 `-space`를 실물로 세우는 일이었다.

## 반영

- **어휘**(developer) — `agt:Space` 외 여섯(`variableFrom`·`variableKind`·`hasCandidate`·`spaceStatus`·`compatibilityConstraint`·`preferredOver`). `agt:Space`를 `agt:Chunk`의 하위로 둔 것이 핵심이다. 그 하나로 `agt:ChunkShape`와 verify 질의 `sources-empty`가 `-space`에 그대로 걸려 검사를 새로 쓰지 않았다.
- **상태 어휘를 새로 만들지 않았다**(developer). 표면 셋을 기존 `agt:linkState`에 사상했다 — `open→candidate`·`eliminated→invalid`·`confirmed→confirmed`. 배제 근거는 `agt:Evidence` + `polarity "-"`로 나가므로 기존 질의 `confirmed-without-evidence`·`confirmed-with-refutation`이 후보에도 걸린다. **`r-011`이 새 검사 없이 강제된다.**
- **파서와 게이트**(developer) — `tools/space2kg.py`, 게이트 id `space`, `validate.check_space`. 음성 확인 둘을 실제로 돌렸다 — 배제 근거를 지우면 `FAIL [space] … 근거 없는 배제를 금지한다 (요구 r-011-no-groundless-assignment)`, `resolved`인데 확정 후보가 0이면 `… 정확히 하나여야 한다`다.
- **뷰**(developer) — 체크박스 `//space:choices`(`[ ]` 열림 · `[-]` 배제 + 근거 · `[x]` 확정)와 A-Box `//space:design_space`.
- **첫 실물 2건**(orchestrator) — `agent-verification-target-space` · `workset-budget-enforcement-space`. 둘 다 변수만 선언했다.
- **논평 형식**(orchestrator) — 결정 `p7-commentary-form`. 보류 그릇 G7을 열었다. 라벨 일곱·장식 셋·슬롯 다섯이고 `issue (blocking)` + `해소: 열림`만 게이트를 막는다. 어휘는 Conventional Comments에서 가져와 `docs/references.md`에 출처를 남겼다.
- **문서**(orchestrator) — `docs/method.md` §5 실물 형식, `docs/tools.md` 게이트 `space`와 타깃 둘, `docs/roadmap.md` 5단계 행과 다음 산출, `STYLEGUIDE.md` §4 `annotation` 규약.

## 저작하면서 확인한 구조적 사실

**후보 `to`는 실재하는 IRI여야 하는데, 이 저장소는 대안을 `alternatives.md` 본문에 적지 청크로 만들지 않는다.** 그래서 "후보가 전부 청크로 존재하는 열린 변수"가 지금 하나도 없다. 서식이 허용하는 **변수만 선언한 공간**으로 시작했고, 후보는 답이 와서 청크가 생길 때 채운다. 근거 없이 후보를 적으면 그것 자체가 `r-011`이 막는 할당이다.

이것은 유저 판단 대기 7건이 전부 같은 형태라는 뜻이기도 하다 — 설계 변수 하나에 후보 3~4개가 열려 있으나 후보가 아직 지식이 아니다.

## 결정 하나를 구현에 맞게 정정했다

`p9-candidate-storage`가 "`chunk2kg`가 `-space`를 `agt:CandidateLink`로 올린다"고 적었으나 구현은 `space2kg`가 맡는다. `chunk2kg`는 타깃마다 도는 무의존 생성기라 PyYAML을 얹을 수 없기 때문이고, `extract_refs`·`weave`·`labels`가 쓰는 기존 방식과 같다. 파서와 링크 IRI 규칙의 정의처는 여전히 `chunk2kg` 하나다. 문구를 고치고 재판정했다.

## hci에 전달

- 원장에 "도입 5단계 첫 형태 — 설계 공간(2026-09-22)" 한 줄. 재판정 대상 없음.
- **남은 것 셋**은 developer가 적었다. `agt:when`과 양립 제약의 CEL 평가기가 없어 문자열로만 받는다. 분할 조각이 후보 대상일 때 링크 IRI가 head와 갈릴 수 있다(실물이 없어 미확인). abstract 변수 청크는 `-space`에 후보가 채워질 때 만드는 것이 자연스럽다.
- `annotation` plane 첫 청크(판정 주석)를 vnv가 저작 중이다. 완료되면 별도 기록을 남긴다.
