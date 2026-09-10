---
id: https://agentic-knowledge-base.dev/id/chunk/a09428ec-58e9-4538-b698-a9ec667d0762
type: decision
level: logical
title_ko: plane마다 다른 shape을 붙이려면 클래스여야 하고 level은 바뀌지 않는다
title: Planes need per-class shapes; a chunk never changes its level
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/db06bc97-7100-4ad3-bad0-83fb1c876e1c
---
**근거** (노트 4.2절)

- plane을 클래스로 두는 이유는 **plane마다 다른 제약(shape)을 붙이기
  위해서**다. 모듈형 문서의 정보 유형(concept / task / reference)이 topic의
  특수화이듯 plane은 청크의 특수화다.
- level을 속성으로 두는 이유는 **같은 청크가 level을 바꾸는 일이 없기**
  때문이다. 사다리 전이는 기존 청크의 level을 고치는 것이 아니라 새 청크를
  만들고 `refines` 링크를 남기는 일이다. 그래서 속성으로 충분하다.
- `requirement`는 level이 functional로 고정된 유일한 plane이다 (5.5절
  승격의 귀결).
