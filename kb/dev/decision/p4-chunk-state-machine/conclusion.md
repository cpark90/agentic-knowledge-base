---
id: https://agentic-knowledge-base.dev/id/chunk/09164cfd-7490-447c-9360-ac01c2f6d720
type: decision
level: concrete
title_ko: 청크의 다섯 상태와 전이
title: The five chunk states and their transitions
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0078]
part_of: https://agentic-knowledge-base.dev/id/composite/0662736c-b666-499e-bf57-2097608f4b9b
composite: {id: https://agentic-knowledge-base.dev/id/composite/0662736c-b666-499e-bf57-2097608f4b9b, title_ko: 청크 상태, title: Chunk state}
---
**결론** — 청크도 가정·링크와 같은 상태 기계를 갖는다. 상태 어휘는 OKF의
다섯이다.

| 상태 | 의미 | 전이 |
|---|---|---|
| `draft` | shape 미통과 또는 라벨 미확정 | → `stable` (게이트 통과) |
| `stable` | shape 통과, 가정 전부 참 | → `suspect` (가정 변경, 참조 청크 변경) |
| `suspect` | 재검토 필요 | → `stable` 또는 `invalidated` |
| `invalidated` | 가정 거짓 | → `stable` (수정) 또는 `deprecated` |
| `deprecated` | 폐기. 참조는 남되 신규 참조 금지 | 종료 |

**`draft` 청크는 링크의 끝이 될 수 없다.** 확정되지 않은 것에 의존하는 링크는
만들 수 없다.

노트 4.11절 표는 이 상태를 `valid`로 적고 있으나, 이 체계의 상태 어휘는 OKF의
`draft`/`stable`/`suspect`/`invalidated`/`deprecated`이므로 `valid`는
`stable`로 정정한다.
