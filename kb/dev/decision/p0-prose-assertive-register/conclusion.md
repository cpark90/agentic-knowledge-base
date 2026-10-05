---
id: https://agentic-knowledge-base.dev/id/chunk/477da7b5-a2d1-4ea9-9adc-5b06a152e544
type: decision
level: concrete
title_ko: 산문은 학술 산문체의 단정 서술형으로 쓰고 한 문장에 한 주장을 담는다
title: Prose is written in the assertive declarative register of academic writing, one claim per sentence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:34:38+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7
composite: {id: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7, title_ko: 산문 문체 — 단정 서술형, title: Prose register — assertive declarative}
---
**결론** — 산문은 학술 산문체의 단정 서술형이다(유저 지시 2026-09-13). 대상은 문서·청크 본문·채널 메시지·질문지·세션 보고·dispatch 브리핑 전부다.

- 문장은 평서형 종결 "…다"로 끝난다. 경어체("습니다·세요·해요"), 감탄, 구어("근데·그냥·좀"), 추측 표현("것 같다·듯하다·수도 있다")을 쓰지 않는다.
- 의문문은 질문을 다루는 절에만 둔다.
- 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다.
- 한 문장에 한 주장을 담는다. 대시로 절을 이어 붙이지 않고 문장으로 나눈다. 이 항목과 아래 항목은 권장이다.
- 굵게는 결론·규칙에만 쓴다. 괄호는 인용 위치(절 번호·파일)에만 쓰고 부연은 문장으로 푼다. 불릿은 완결된 문장이거나 명사구 하나다.

강제는 둘로 나뉜다. 경어·감탄은 게이트 `prose`가 거부한다. `chunk_lint`와 `doccheck`가 같은 판정처 `kb_lib.check_prose`를 쓴다. 추측·구어·대시 밀도는 `consistency` ⑦이 보고한다. 생성 문서에도 같은 산문 판정이 걸린다(`p12-generated-document-form`).
