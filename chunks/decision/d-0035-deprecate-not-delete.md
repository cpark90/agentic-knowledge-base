---
id: https://agentic-knowledge-base.dev/id/chunk-d0035
type: decision
level: concrete
title_ko: 삭제하지 않고 폐기한다
title: Deprecate, never delete
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 개념·청크·링크 타입은 삭제하지 않고 **폐기(deprecate)** 한다.
- `owl:deprecated true` + 대체 개념을 `agt:replacedBy`로 지정
- 폐기된 개념을 참조하는 청크는 검사 게이트가 **경고**한다 (거부는 아님)

**근거** (노트 0.10절)
- 삭제하면 그것을 참조하던 링크가 **고아가 되어 추적성이 끊긴다.** 추적성은
  이 체계가 세 단절(1.3절)을 잇는 수단이므로, 고아 링크는 손실이 국소에
  그치지 않는다.
- 대체 개념을 `agt:replacedBy`로 남기면 폐기가 단순한 표시가 아니라 이관
  경로가 된다 — 참조하던 청크가 어디로 옮겨야 하는지가 그래프에 적힌다.
- 불투명 IRI(0.7절)로 이름 변경이 IRI를 깨뜨리지 않게 한 것과 같은
  원칙이다. 식별자는 살아남고 상태만 바뀐다.
