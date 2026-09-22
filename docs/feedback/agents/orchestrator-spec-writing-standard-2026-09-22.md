---
from: orchestrator
kind: notice
status: open
ref: handoff/spec-writing-standard-adoption-2026-09-22.md
targets: [STYLEGUIDE.md, docs/rules.md, docs/tools.md, docs/open-questions.md, kg/base-kg.ttl, kb/dev/decision/, tools/kb_lib.py, tools/consistency.py, tools/chunk2kg.py, tools/open_questions.py, kb/ontology/shapes/]
---

# 명세 문서 작성 규격의 반영 — 인수 기록 (2026-09-22)

승인 항목 [`spec-writing-standard-adoption-2026-09-22`](../spec-writing-standard-adoption-2026-09-22.md)(유저 답 "1.을 선택하되 추가적으로 기존 저작에도 적용함")를 반영 계획 1~5번대로 수행했다. `bazel test //...` **21/21 PASS**다.

## 반영

- **결정 3건**(orchestrator) — `p4-three-empty-values`(빈 값 세 뜻) · `p4-slot-answers-one-question`(슬롯 질문·첨가 셋·목록 규칙) · `p8-judge-question-form`(판정자 질문 형·확신도 임계 셋·도입 전 20건 라벨링). 출처 개체 `id:doc-spec-writing-standard` 등록.
- **문서**(orchestrator) — `STYLEGUIDE.md` §0·§4, `docs/rules.md` 본문 형식 절, `docs/open-questions.md` 집계 방식과 대표 청크 대응표, `docs/tools.md` 게이트 총람·shape 표·도구 표·타깃 트리.
- **도구와 shape**(developer) — `kb_lib`에 빈 값 셋·`PROSE_META`·`PROSE_FILLER`·목록 상한(`LIST_MAX_ITEM_CHARS 240`)과 검사 둘, `consistency` ⑧·⑨ 축(보고), `chunk2kg`의 `agt:bodySlot`, 본문 슬롯 shape 4파일, 미결 집계 뷰 `//kg:open`.
- **기존 저작**(orchestrator) — 손 번호 10건 · 메타 문장 2건 · 표의 단독 대시 셀 15건 · 과길이 항목 2건. 규약대로 `generated.at`을 올리고 도장을 물린 뒤 `endorse`로 8건을 재판정했다.
- **`미확정:` 슬롯 10건**(orchestrator) — 미결 문서마다 대표 청크에 질문 한 줄과 상세 경로를 달았다. `//kg:open`이 미결 10개를 낸다.

`consistency` 최종 — 메타 문장 0 · 채움 문구 0 · 손 번호 0 · 항목 수 0 · 중첩 0 · 빈 목록 0 · 항목 길이 **0** · 빈 값 이상 1(오탐, 면제 선언). 본문 슬롯 shape 편차 **0**. `vv_run` 케이스 28 전부 pass. vnv가 `kb/vv/criteria/` 7건을 고쳤고 그 KB에는 `verified`가 하나도 없어 도장 재판정이 `해당 없음`이다.

⑧의 오탐 1건은 `docs/waivers.md`에 게이트 id `empty-value`로 면제를 선언했다. 면제는 집계에서 빠지되 목록에 남는다. **⑧·⑨를 `chunk_lint` 게이트로 승격했다**(계획 7번 완료). 게이트 id는 셋이다 — `addition`(메타 문장·채움 문구) · `empty-value`(세 값 밖 표기와 표의 단독 대시 셀) · `list-rules`(손 번호·항목 수·중첩·항목당 240자·빈 목록). 대상은 살아 있는 청크이고 `deprecated`는 기록이라 제외한다(정의처 `kb_lib.LIVE_STATES`). 검사 함수는 `consistency` 보고와 같은 것을 쓰므로 두 수치가 갈리지 않는다. 검사 강화는 약화가 아니라 별도 승인이 필요 없다(`STYLEGUIDE.md` §2).

승격 과정에서 배선 결함 하나가 드러나 함께 고쳤다 — `defs/kb.bzl`의 `kb_chunk`·`kb_decision` validation 액션이 `--waivers`를 주지 않아 청크를 겨눈 면제가 그 액션에만 적용되지 않았다. 암묵 속성으로 `//docs:waivers`를 주입해 해소했고 생성 BUILD는 바뀌지 않는다.

## 계획과 다르게 읽은 것 셋 — 담당 역할의 판단이다

1. **역할 배정.** 계획 4번이 위반 33건 수정을 developer에게 배정했으나, 실측하니 위반이 전부 `decision`과 `kb/vv/`에 있고 `artifact`는 0이다. developer의 write plane이 아니므로 `decision`은 orchestrator가, `kb/vv/`는 vnv가 맡았다.
2. **이관의 범위 — 문서를 지우지 않았다.** 계획 5번은 삭제를 포함한 이관이라 했다. 그러나 유저가 읽고 고른 항목 본문이 "기존 11 파일은 그대로 두고"라 적었고, 실측하니 그 문서들을 가리키는 링크가 50곳 이상이며 다섯 절 상세(20~40줄)는 42줄 청크에 들어가지 않는다. 슬롯으로 집계를 생성물화하되 상세는 문서에 남겼다 — 유저 답의 "기존 저작에도 적용"과 항목 본문의 "그대로 두고"를 둘 다 만족하는 읽기다. `//kg:open`의 머리가 그 분담을 적는다.
3. **목록 항목 길이의 단위.** 계획은 제안 4.3의 "항목당 2줄"을 그대로 받았으나 물리 줄로 재면 143건이 나왔고 대부분 저작 결함이 아니었다. 이 저장소는 산문을 110~120자에서 손으로 접어 렌더 2줄이 소스 3줄이 된다. **단위를 글자 240으로 정정**하고 결정과 `STYLEGUIDE.md`를 함께 고쳤다. 실측이 143 → 4로 줄었고 남은 넷이 진짜 위반이다.

## 계획의 사실 오류 둘

- 계획 5번이 이관 시 고칠 대상으로 적은 **`docs/README.md`는 존재하지 않고 `docs/roadmap.md`에는 `open-questions` 문자열이 없다.** 실제 대상은 `docs/competency-questions.md`·`docs/risks-and-tensions.md`·`docs/open-questions.md`·`README.md`·`docs/feedback/README.md`·`docs/feedback/design-detail-review.md`다.
- 파급효과 표의 도장 5건 중 `p11-agent-catalog-derives-scope`·`p11-inputs-are-parameters`는 위반 목록에 없다. 실제 재판정은 편집 대상이 된 8건에 했다.

## hci에 전달

- 원장에 "명세 문서 작성 규격 반영(2026-09-22)" 한 줄. 재판정 대상 없음 — 링크·복합체·IRI·라벨은 바뀌지 않았다.
- **출처 개체의 영속 위치가 미완이다.** `kg/base-kg.ttl`의 `id:doc-spec-writing-standard`가 `prov:atLocation`을 트리 경로로 적고 있다. 채널 파일은 소멸성이므로 커밋 뒤 `git:<리비전>:docs/feedback/inquiries/spec-writing-standard-proposal.md`로 고쳐야 한다.
- **`consistency` ⑧의 오탐 1건은 면제로 처리했다.** `p9-uncertainty-as-link-uncertainty/conclusion.md:16`의 "값이 미정인 것처럼 보이는 경우"는 산문 용법이지 빈 값 표기가 아니다. `docs/waivers.md`에 게이트 id `empty-value`·축 `파일`로 선언했고 판정자는 orchestrator다.
- 보류 그릇 둘은 계획 6번대로 열지 않았다. G7 논평 틀은 `annotation` 첫 청크가 생길 때, G8 위험 틀은 항목 `vv-profile-hazards-2026-09-19`의 답이 올 때다.
