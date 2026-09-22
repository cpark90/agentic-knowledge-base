---
id: https://agentic-knowledge-base.dev/id/chunk/4d68f7c4-f8b5-4715-8cdd-8bfa82903b0e
type: decision
level: logical
title_ko: 외부 린터 도입·렌더러 의존·사후 포매터 안은 기각된다
title: Adopting an external linter, relying on the renderer, and a post-hoc formatter are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/6364f6e3-f553-4178-946c-36246fed08a9
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| markdownlint를 그대로 의존성으로 들인다 | Node 런타임이 ODD 조건에 없다. `id:cond-dependency-lock`과 `id:cond-python-runtime`을 넓혀야 하고, 규칙 200여 개 중 쓰는 것은 여덟이다. 규칙 번호는 출처로 인용하고 판정은 `kb_lib`에 구현한다 |
| 서식을 렌더러에 맡기고 원문은 느슨하게 둔다 | 이 문서들의 첫 독자는 다음 세션의 에이전트이고 그 에이전트는 원문을 읽는다. 렌더 결과가 아니라 원문이 산출물이다 |
| 사후 포매터를 붙여 생성물을 다듬는다 | 생성기가 단계 하나 늘고, 포매터가 고친 것과 생성기가 낸 것이 갈라진다. 형태는 생성 전에 고정하는 것이 이 결정의 사상이다 |
| ASD-STE100의 문장 20단어·문단 6문장 상한을 함께 받는다 | 영어 기술 문서를 위한 수치이고 한글 산문에 옮길 근거가 없다. 단정 서술형(`STYLEGUIDE.md` §0)이 같은 자리를 이미 맡는다 |
