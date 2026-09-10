---
id: https://agentic-knowledge-base.dev/id/chunk/6bb5eb59-ceed-4397-bfa9-4c2e47cc29f4
type: decision
level: logical
title_ko: 상태 어휘가 하나여야 가정·링크·청크·복합체를 한 규칙 집합으로 다룬다
title: One state vocabulary lets one rule set cover assumptions, links, chunks, composites
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0662736c-b666-499e-bf57-2097608f4b9b
---
**근거** (노트 4.11절)

- 청크·가정·링크가 **같은 상태 기계**를 쓰면 전이 규칙을 `defect-rules` 한
  집합으로 쓸 수 있고, 복합체 상태를 부분에서 추론하는 규칙(4.5절)도 같은
  어휘 위에서 성립한다.
- `draft`를 링크의 끝에서 배제하는 이유는 **미확정 위에 판정을 쌓지 않기**
  위해서다. draft 청크를 가리키는 링크는 그 청크가 확정될 때 통째로 재판정
  대상이 되므로, 처음부터 만들지 않는다.
- `invalidated`에서 `deprecated`로 가는 길이 있고 삭제가 없다 — 참조는 남되
  신규 참조만 금지된다.
