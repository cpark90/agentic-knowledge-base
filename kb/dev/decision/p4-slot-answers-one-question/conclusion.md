---
id: https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97
type: decision
level: concrete
title_ko: 슬롯마다 질문 하나를 등록하고 그 답만 적는다
title: Each slot registers one question and holds only its answer
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T20:20:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f7ac1b83-2f07-479d-a1ac-dfa68858e15f
composite: {id: https://agentic-knowledge-base.dev/id/composite/f7ac1b83-2f07-479d-a1ac-dfa68858e15f, title_ko: 슬롯은 질문 하나에 답한다, title: A slot answers one question}
---
**결론** — 본문의 슬롯(`**결론**`·`**근거**`·`**대안**`·`**요구**`·`**검증 목표**`·`**합격 기준**`·`**케이스**` 등 줄 머리 고정 표지)마다 그것이 답하는 질문 하나를 shape에 등록한다. 슬롯에는 그 질문의 답만 적는다.

**첨가**는 셋이다. 다른 슬롯의 질문에 답하는 문장, 내용을 소개하는 **메타 문장**("다음과 같다"·"이 절에서는"), 빈 값을 피하려는 **채움**("특이사항 없음"·"추후 결정")이다. 셋 다 슬롯의 질문에 답하지 않으므로 지운다. 채움 자리에는 세 빈 값을 쓴다(`p4-three-empty-values`).

**목록 규칙**은 다음 다섯이다. 순서 목록의 모든 항목을 `1.`로 적고 `2.` 이상의 손 번호를 쓰지 않는다. 항목은 9개 이하, 중첩은 2단계 이하, 항목당 240자 이하다. 길이를 소스 줄이 아니라 글자로 재는 까닭은 이 저장소가 산문을 110~120자에서 손으로 접어 소스 줄과 렌더 줄이 다르기 때문이다. 빈 목록 대신 `없음`을 적는다.

shape는 **현행 형태를 그대로** 기술한다. 새 슬롯을 요구하지 않고 결정의 세 청크·EARS 패턴·42줄을 바꾸지 않는다. 대상은 실물이 있는 일곱이다 — 요구, 결정 결론·근거·대안, 검증 목표, 합격 기준, 케이스다.

검사는 보고로 시작해 게이트가 됐다. `consistency` ⑧이 첨가를 ⑨가 목록을 세고, 수치가 0이 된 2026-09-22에 `chunk_lint`의 게이트 `addition`·`list-rules`로 올렸다.
