---
id: https://agentic-knowledge-base.dev/id/chunk/d93c308e-575c-442f-b99e-a56e1c76148c
type: decision
level: concrete
title_ko: 복합체는 부분 하나의 frontmatter에 한 번 선언하고 부분 2~9개를 같은 패키지에 둔다
title: A composite is declared once in one part's frontmatter, with two to nine parts in the same package
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7130e6d8-2b81-49eb-b1a3-96d3c7f93ff3
composite: {id: https://agentic-knowledge-base.dev/id/composite/7130e6d8-2b81-49eb-b1a3-96d3c7f93ff3, title_ko: 복합체의 선언과 부분 배치, title: Composite declaration and part placement}
---
**결론** — 복합체는 저작 파일에서 선언하고 생성기가 세운다. 부분-전체 어휘는 `p4-composite-as-part-of`가, 동질성·부분 상한은 `p4-composition-rules`가 정한다. 이 결정은 선언과 배치를 정한다.

- 부분 중 하나의 frontmatter에 `composite: {id, title_ko, title}`를 한 번 선언한다. 같은 복합체 IRI를 두 청크가 선언하면 `chunk2kg`·`gen_build`가 거부한다.
- 부분 전부에 `part_of: <복합체 IRI>`를 적는다. 선언 없는 `part_of` 대상은 거부된다.
- 부분은 같은 디렉토리(패키지)에 둔다. 중첩 복합체(`composite.part_of`)도 뿌리부터 잎까지 한 패키지다.
- 부분은 2개 이상이다. 부분이 하나면 청크다.
- 선언 청크의 파일 이름이 Bazel 타깃 이름이 된다. 중첩이면 뿌리 복합체를 선언한 청크의 파일 이름이다.
- 결정은 예외다. `<파트>-<슬러그>/` 디렉토리에 결론·근거·대안 세 청크와 선택 규약 청크 `conventions.md`를 두고 `kb_decision`이 세운다(`p4-convention-slot`).
- 생성 경로가 표현하지 못하는 복합체만 `kg/composite-kg.ttl`에 손으로 쓴다.
