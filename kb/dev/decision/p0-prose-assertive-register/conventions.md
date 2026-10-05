---
id: https://agentic-knowledge-base.dev/id/chunk/f622b88d-d39a-466d-80bd-f0084c89da03
type: decision
level: concrete
title_ko: 규범 문서 규약 — 산문은 학술 산문체의 단정 서술형으로 쓰고 한 문장에 한 주장을 담는다
title: Normative-document conventions — Prose is written in the assertive declarative register of academic writing, one claim per sentence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7
---
**규약** — `p0-prose-assertive-register`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **산문은 학술 산문체의 단정 서술형이다**(유저 결정 2026-09-13). 대상은 문서·청크 본문·채널 메시지·질문지·세션 보고·dispatch 브리핑 전부다. 문장은 평서형 종결 "…다"로 끝난다. 경어체("습니다·세요·해요"), 감탄, 구어("근데·그냥·좀"), 추측 표현("것 같다·듯하다·수도 있다")을 쓰지 않는다. 의문문은 질문을 다루는 절에만 둔다. 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다. 경어·감탄은 게이트 `prose`(`chunk_lint`·`doccheck`)가 거부한다. 추측·구어·대시 밀도는 `consistency` ⑦이 보고한다.
규약: [권장] 한 문장에 한 주장을 담는다. 대시("—")로 절을 이어 붙이지 않고 문장으로 나눈다. 강조(굵게)는 결론·규칙에만 쓴다. 괄호는 인용 위치(절 번호·파일)에만 쓰고 부연은 문장으로 푼다. 불릿은 완결된 문장이거나 명사구 하나다.
