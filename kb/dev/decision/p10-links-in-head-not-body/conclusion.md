---
id: https://agentic-knowledge-base.dev/id/chunk/879d0716-8560-4f32-90f4-e926e38f334d
type: decision
level: concrete
title_ko: 링크는 본문에 쓰지 않고 확정은 head에, 후보는 설계 공간 청크에 두며 본문 링크는 비공식 참조다
title: Links are not written in the body; confirmed links live in the head, candidates in design-space chunks, and body links are informal references
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2280fd28-d481-4b52-94d4-aab439be78b1
composite: {id: https://agentic-knowledge-base.dev/id/composite/2280fd28-d481-4b52-94d4-aab439be78b1, title_ko: 링크의 자리 — head와 설계 공간, title: Where links live — head and design space}
---
**결론** — 링크는 산출물의 본문(assertion) 안에 쓰지 않는다(노트 10.5절 `[확정]`).

| 링크 | 자리 | 링크 모델로 올리는 생성기 |
|---|---|---|
| 확정 링크 | 청크 head — frontmatter의 링크 타입 키 | `chunk2kg` |
| 후보 링크 | `-space` 청크 | `space2kg` (`chunk2kg`의 파서) |

- 양 끝은 각 plane의 네이티브 앵커로 해석되는 청크 IRI다.
- head는 본문이 아니다. "청크는 자기 링크를 모른다"(노트 4.3절)는 본문에 대해 유지된다.
- 본문의 마크다운 링크는 비공식 참조다. lint가 그 대상이 head 또는 `-space`에 있는지 검사한다.

`p10-link-storage-and-anchors`는 링크를 산출물 밖에 둔다고 정한다. 이 결정은 frontmatter와 본문이 한 파일에 있는 이 저장소에서 "밖"이 본문 밖이라는 것을 정한다. 후보의 저장 형식은 `p9-candidate-storage`, head를 손으로 쓴 그래프에 옮기지 않는 규칙은 `pe-kg-hand-and-generated-files`가 정한다.
