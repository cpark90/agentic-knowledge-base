---
id: https://agentic-knowledge-base.dev/id/chunk/622a0314-a454-4b41-aef7-c8644cff448c
type: decision
level: logical
title_ko: 삭제는 참조 링크를 고아로 만들어 추적성을 끊는다
title: Deletion orphans referring links and severs traceability
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8453e658-a276-4f75-83a4-9926df17826b
---
**근거** (노트 0.10절)

- 삭제하면 그것을 참조하던 링크가 **고아가 되어 추적성이 끊긴다.** 추적성은
  이 체계가 세 단절(1.3절)을 잇는 수단이므로 손실이 국소에 그치지 않는다.
- 대체 개념을 `agt:replacedBy`로 남기면 폐기가 단순한 표시가 아니라 **이관
  경로**가 된다 — 참조하던 청크가 어디로 옮겨야 하는지가 그래프에 적힌다.
- 경고를 거부로 하지 않는 것은 이관이 한 커밋에 끝나지 않기 때문이다. 거부로
  하면 폐기가 곧 전면 수정을 강제해 폐기를 미루게 만든다.
- 불투명 IRI(0.7절)로 이름 변경이 IRI를 깨뜨리지 않게 한 것과 같은 원칙이다.
  식별자는 살아남고 상태만 바뀐다.
