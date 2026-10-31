---
id: https://agentic-knowledge-base.dev/id/chunk/4cb46349-f0c4-499f-b5a7-f5b5a4da5eaa
type: decision
level: concrete
title_ko: 적용 범위는 mode·include·exclude·conditional 네 종류의 문장으로 쓴다
former_title_ko: ["스코프는 mode·include·exclude·conditional 네 종류의 문장으로 쓴다"]
title: A scope is written as four kinds of statement: mode, include, exclude and conditional
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0029-scope-specification-form.md, id: https://agentic-knowledge-base.dev/id/chunk-d0029, title_ko: "스코프 명세는 네 문장으로 쓴다", title: "Scope is written as four statement kinds"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0029]
part_of: https://agentic-knowledge-base.dev/id/composite/780d333f-1d35-4e81-83cf-58355a1d3d41
composite: {id: https://agentic-knowledge-base.dev/id/composite/780d333f-1d35-4e81-83cf-58355a1d3d41, title_ko: 적용 범위 명세는 네 문장으로 쓴다, title: Scope is written as four statement kinds, former_title_ko: ["스코프 명세는 네 문장으로 쓴다"]}
---
**결론** — 적용 범위는 네 종류의 문장으로 쓴다.

- **mode** — 기본 모드. `restrictive`(명시 포함만 허용) 또는
  `permissive`(명시 제외만 금지)
- **include** — 적용 범위 안에 있는 조건·개념
- **exclude** — 적용 범위 밖에 있는 조건·개념
- **conditional** — include/exclude에 붙는 부가 조건. "X이면 Y를 포함"

**write scope의 기본 모드는 `restrictive`다.** read scope는 하네스별로 정한다.

```
scope :developer-scope
  mode restrictive
  include plane source          (write)
  include plane interface       (read)
  conditional: include write plane interface
               if design-decision(target).level = concrete
```

마지막 줄이 conditional의 용도다 — "관련 결정이 확정된 뒤에만 인터페이스
수정을 허용한다"를 적용 범위 문장으로 쓴다.
