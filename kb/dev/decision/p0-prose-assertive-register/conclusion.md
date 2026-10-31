---
id: https://agentic-knowledge-base.dev/id/chunk/477da7b5-a2d1-4ea9-9adc-5b06a152e544
type: decision
level: concrete
title_ko: 산문은 학술 산문체의 단정 서술형으로 쓴다
title: Prose is written in the assertive declarative register of academic writing
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7
composite: {id: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7, title_ko: 산문 문체 — 단정 서술형, title: Prose register — assertive declarative}
---
**결론** — 산문은 학술 산문체의 단정 서술형이다(유저 지시 2026-09-13). 대상은 문서와 단위 지식의 본문, 채널 메시지, 질문지, 세션 보고, dispatch 브리핑 전부다.

- 문장은 평서형 종결 "…다"로 끝난다. 경어체("습니다·세요·해요"), 감탄, 구어("근데·그냥·좀"), 추측 표현("것 같다·듯하다·수도 있다")을 쓰지 않는다.
- 의문문은 질문을 다루는 절에만 둔다.
- 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다.
- 문장을 어떻게 짜고 잇는가는 이 결정이 아니라 결정 `p0-sentence-composition`이 정한다(유저 답 Q104-a, 2026-10-23).

강제는 둘로 나뉜다. 경어와 감탄은 게이트 `prose`가 거부한다. `chunk_lint`와 `doccheck`가 같은 판정처 `kb_lib.check_prose`를 쓴다. 추측과 구어, 대시 밀도는 `consistency` ⑦이 보고한다. 생성 문서에도 같은 산문 판정이 걸린다(`p12-generated-document-form`).

**게이트** `prose`(`STYLEGUIDE.md` §0, 2026-09-13) — 해소는 저작자가 문장을 고치는 것이다. 고유명사에 든 느낌표는 `docs/waivers.md`에 면제로 선언한다.
