---
id: https://agentic-knowledge-base.dev/id/chunk/5af1bbb5-3d25-4501-af0a-4470e70d1b4f
type: decision
level: concrete
title_ko: 규범 문서 규약 — 복합체는 부분 하나의 frontmatter에 한 번 선언하고 부분 2~9개를 같은 패키지에 둔다
title: Normative-document conventions — A composite is declared once in one part's frontmatter, with two to nine parts in the same package
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:08+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7130e6d8-2b81-49eb-b1a3-96d3c7f93ff3
---
**규약** — `p4-composite-declared-in-frontmatter`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 복합체를 저작할 때는 부분 중 하나의 frontmatter에 `composite: {id, title_ko, title}`를 한 번 선언하고 부분 전부에 `part_of`를 적는다. 부분은 **같은 디렉토리, 곧 같은 패키지**에 두고 지식 종류와 정제 수준을 같게 하는데, 묶음은 액션의 입력 집합이고 입력 집합은 패키지를 넘지 못하기 때문이다. 부분은 2~9개이고 선언하는 단위 지식의 파일 이름이 타깃 이름이 된다. 다만 결정은 예외여서 `<파트>-<슬러그>/` 디렉토리에 단위 지식 셋과 선택 `conventions.md`를 두고 `kb_decision`이 세운다(2026-09-29, `p4-convention-slot`).
