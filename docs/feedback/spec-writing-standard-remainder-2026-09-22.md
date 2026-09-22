---
from: hci
status: approved
targets: [STYLEGUIDE.md, docs/rules.md, kg/base-kg.ttl, docs/feedback/inquiries/spec-writing-standard-proposal.md, docs/feedback/spec-writing-standard-adoption-2026-09-22.md]
---

# 명세 문서 작성 규격 — 반영의 잔여 둘 (2026-09-22)

승인 항목: [`spec-writing-standard-adoption-2026-09-22.md`](spec-writing-standard-adoption-2026-09-22.md) ·
인수 기록: [`agents/orchestrator-spec-writing-standard-2026-09-22.md`](agents/orchestrator-spec-writing-standard-2026-09-22.md)

## 질문

승인 범위의 공백 열 가운데 여덟이 반영됐고 둘(G7 논평 틀 · G8 위험 틀)은 계획대로 그릇만 남겼다. 그와 별개로 **닫히지
않은 것이 둘** 있다. 승인 범위에 있었으나 반영되지 않은 **G10 그림 틀**과, 커밋 뒤에 고치기로 한 **출처 개체의 위치**다.
둘을 지금 닫는가.

어려운 이유는 성격이 다르다는 데 있다. G10은 **승인된 범위의 누락**이라 반영하거나 범위에서 빼는 판단이 필요하고,
출처 개체는 **판단이 아니라 미룬 작업**이지만 그것이 닫히기 전에는 채널에서 제안 원문 922줄을 제거하지 못한다.

## 이미 정해진 것

- 유저 승인 2026-09-22 — "1.을 선택하되 추가적으로 기존 저작에도 적용함". 즉시 규칙 묶음은 **G1·G2·G4·G9·G10**이었다.
- G7·G8은 계획 6번대로 보류다. `annotation` 첫 청크가 생길 때, 그리고 [`vv-profile-hazards-2026-09-19.md`](vv-profile-hazards-2026-09-19.md)의 답이 올 때 연다.
- 채널 파일은 소멸성이므로 지식이 채널을 가리킬 때는 `git:<리비전>:<경로>` 평문 인용을 쓴다(채널 규약, refresh 2026-09-13 선례).
- 제안 원문의 그림 규칙(6.8)은 캡션 한 줄 · 소스 펜스(`mermaid`/`svg`/`plantuml`) 우선 · 읽는 법 명사구 ≤3이다. 이미지는 소스가 없을 때만 쓴다.

## 현재 상태 (실측 2026-09-22, 리비전 `0b7b805`)

- **G10 미반영** — `STYLEGUIDE.md`·`docs/rules.md`에 "그림"·"다이어그램"·"mermaid" 문자열이 없다. 인수 기록에 누락 사유가 적혀 있지 않다.
- 그림을 담은 파일은 저장소 전체에서 **1개**다. 규칙을 넣어도 지금은 잴 표본이 없다.
- **출처 개체가 트리 경로다** — `kg/base-kg.ttl`의 `id:doc-spec-writing-standard`가 `prov:atLocation "docs/feedback/inquiries/spec-writing-standard-proposal.md"`로 적혀 있다. 인수 기록이 스스로 "커밋 뒤 `git:<리비전>:…`로 고쳐야 한다"고 남겼다.
- 그 때문에 채널에 **제안 원문 922줄과 승인 항목**이 남아 있다. 둘 다 반영이 끝난 항목이다.
- 반영된 여덟은 확인했다 — 결정 3건 · 본문 슬롯 shape 4파일 · 게이트 id 셋(`addition`·`empty-value`·`list-rules`) · 뷰 `//kg:open`(미결 10). 게이트 21/21 PASS.

## 답이 가르는 것

- **G10을 반영하면** 다이어그램 저작의 규칙이 선다. 지금 표본이 1개라 효과는 재지 못하지만, 규칙이 없는 상태에서 그림이 늘면 이미지 첨부와 소스가 섞인다. 반영 비용은 `STYLEGUIDE.md` 한 단락이다.
- **G10을 범위에서 빼면** 승인 범위와 반영 결과가 일치하게 된다. 다만 "승인했는데 하지 않은 것"이 남으므로 그 사실을 결정이나 항목에 적어야 다음 세션이 다시 묻지 않는다.
- **출처 개체를 고치면** hci가 다음 refresh에서 제안 원문 922줄과 승인 항목을 제거한다. 인용은 `git:e3b36d2:…`로 살아남는다. 고치지 않으면 채널이 계속 커진다 — 제안 원문 하나가 채널 전체에서 가장 큰 파일이다.

## 선택지

1. **둘 다 닫는다** (권고). `STYLEGUIDE.md` §0 또는 §4에 그림 규칙 한 단락을 더하고(캡션·소스 우선·읽는 법), `kg/base-kg.ttl`의 `prov:atLocation`을 `git:e3b36d2:docs/feedback/inquiries/spec-writing-standard-proposal.md`로 고친다. 비용: 문서 한 단락 + TTL 한 줄 + `canonicalize`. 담당은 orchestrator다. 그 뒤 hci가 채널에서 둘을 제거한다.
2. **출처 개체만 고치고 G10은 범위에서 뺀다.** 근거는 표본 1개다. 결정 `p4-slot-answers-one-question`의 본문이나 이 항목의 답에 "그림 틀은 표본이 생길 때"라고 적어 남긴다. 비용: TTL 한 줄.
3. **둘 다 미룬다.** G7·G8 그릇을 여는 시점에 셋을 함께 닫는다. 비용: 제안 원문 922줄이 그때까지 채널에 남는다.

## 답
1.
