---
id: https://agentic-knowledge-base.dev/id/chunk/d7cfd320-c4eb-4679-a7e6-68ee7610c5f6
type: decision
level: concrete
title_ko: 규범 문서 규약 — 슬롯마다 질문 하나를 등록하고 그 답만 적는다
title: Normative-document conventions — Each slot registers one question and holds only its answer
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f7ac1b83-2f07-479d-a1ac-dfa68858e15f
---
**규약** — `p4-slot-answers-one-question`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다**. 첨가 셋을 쓰지 않는다 — 다른 슬롯의 답, 메타 문장("다음과 같다"·"이 절에서는"), 채움("특이사항 없음"·"추후 결정")이다. 채움 자리에는 세 빈 값을 쓴다. 예산은 상한이지 목표가 아니다.
규약: [지킴] **목록 규칙**은 다섯이다. 순서 목록의 모든 항목을 `1.`로 적는다(`2.` 이상의 손 번호는 항목을 넣고 뺄 때 어긋나고 내용 변경이 아닌데도 `contentHash`를 바꾼다). 항목 9개 이하, 중첩 2단계 이하, 항목당 240자 이하다(소스 줄이 아니라 글자로 잰다 — 산문을 110~120자에서 손으로 접기 때문이다). 빈 목록 대신 `없음`을 적는다.
규약: [지킴] 첨가와 목록 규칙 위반은 `chunk_lint`의 게이트 `addition`·`list-rules`가 거부한다(2026-09-22 승격).
