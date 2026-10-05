---
id: https://agentic-knowledge-base.dev/id/chunk/a8b39926-8382-4084-a8e4-2a6b5814b56c
type: decision
level: logical
title_ko: 문체는 유저가 정했고 경어·감탄은 문장 끝 형태로 판정되나 추측·구어는 판정이 필요해 보고로 둔다
title: The user set the register; honorifics and exclamations are decided by sentence-end form, while hedges and colloquialisms need judgement and stay a report
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7
---
**근거** — 유저 지시(2026-09-13)는 문서와 에이전트가 만드는 문장을 논문체의 단정한 서술형으로 고치고 하네스에 반영하라는 것이다. 같은 날 `STYLEGUIDE.md`·`CLAUDE.md`·`INTENT.md`·`README.md`와 `docs/`가 이 문체로 다시 쓰였다. 이 규약과 한 문장 한 주장의 권장이 그때 `STYLEGUIDE.md` §0에 함께 들어갔다.

강제를 게이트와 보고로 나눈 까닭은 판정 가능성이다. 경어·비격식 종결과 느낌표는 문장 끝의 형태로 참·거짓이 갈린다. 추측·구어 후보는 판정이 필요하다. `doccheck`와 `consistency`의 설명이 이 구분을 그대로 적는다. 그래서 ⑦은 파일·줄·표현의 목록을 내고, 대시 밀도는 문장당 대시 수가 1.0을 넘는 청크로 보고한다. 코드·따옴표 안은 산문이 아니므로 두 검사 모두 세지 않는다.

명세 문서 작성 규격(유저 제안)은 표현 규칙 9.5절에 "한 문장 한 사실"을 적는다. 그 제안은 2026-09-22에 왔으므로 이 권장의 출처가 아니라 뒤에 같은 규칙을 적은 문서다.

미확정: 한 문장 한 주장과 대시·강조·괄호의 권장이 2026-09-13에 들어간 이유는 그날의 기록에 따로 적히지 않았다.
