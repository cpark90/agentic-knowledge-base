---
id: https://agentic-knowledge-base.dev/id/chunk/09164cfd-7490-447c-9360-ac01c2f6d720
type: decision
level: concrete
title_ko: 단위 지식은 draft·stable·suspect·invalidated·deprecated 다섯 상태의 상태 기계를 갖는다
former_title_ko: ["청크는 draft·stable·suspect·invalidated·deprecated 다섯 상태의 상태 기계를 갖는다", "지식 항목은 draft·stable·suspect·invalidated·deprecated 다섯 상태의 상태 기계를 갖는다"]
title: A chunk has a state machine of five states: draft, stable, suspect, invalidated and deprecated
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0078-chunk-state-machine.md, id: https://agentic-knowledge-base.dev/id/chunk-d0078, title_ko: "청크의 다섯 상태와 전이", title: "Five chunk states and their transitions"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0078]
part_of: https://agentic-knowledge-base.dev/id/composite/0662736c-b666-499e-bf57-2097608f4b9b
composite: {id: https://agentic-knowledge-base.dev/id/composite/0662736c-b666-499e-bf57-2097608f4b9b, title_ko: 단위 지식 상태, title: Chunk state, former_title_ko: ["청크 상태", "지식 항목 상태"]}
---
**결론** — 단위 지식도 가정·링크와 같은 상태 기계를 갖는다. 상태 어휘는 OKF의
다섯이다.

| 상태 | 의미 | 전이 |
|---|---|---|
| `draft` | shape 미통과 또는 라벨 미확정 | → `stable` (게이트 통과) |
| `stable` | shape 통과, 가정 전부 참 | → `suspect` (가정 변경, 참조 단위 지식 변경) |
| `suspect` | 재검토 필요 | → `stable` 또는 `invalidated` |
| `invalidated` | 가정 거짓 | → `stable` (수정) 또는 `deprecated` |
| `deprecated` | 폐기. 참조는 남되 신규 참조 금지 | 종료 |

**`draft` 단위 지식은 링크의 끝이 될 수 없다.** 확정되지 않은 것에 의존하는 링크는
만들 수 없다.

노트 4.11절 표는 이 상태를 `valid`로 적고 있으나, 이 체계의 상태 어휘는 OKF의
`draft`/`stable`/`suspect`/`invalidated`/`deprecated`이므로 `valid`는
`stable`로 정정한다.

**게이트** `draft-end`(유저 답 Q108-a, 실행 계층 verify) — 살아 있는(`deprecated` 아닌) 단위 지식의 frontmatter 링크(링크 키 `chunk2kg.LINK_KEYS`)가 `draft` 단위 지식을 끝으로 두면 거부한다. 끝이 복합체이면 상태가 없어 대상이 아니다. 판정은 `validate`의 `check_draft_end`다(2026-10-24). 감사 보고 `//kg:audit`의 "draft 끝 링크" 지표가 0건이 된 뒤에 같은 정의로 켰고(Q108-a 3단계), 판정 함수는 지표와 같은 `kb_lib.draft_end_links`다. 해소는 끝을 쓴 역할이 끝을 검토해 `stable`로 올리거나 링크를 빼는 것이다.
