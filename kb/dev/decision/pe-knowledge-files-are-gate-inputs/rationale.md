---
id: https://agentic-knowledge-base.dev/id/chunk/a62bcab9-b521-436a-94fd-b2dbdf3a40cd
type: decision
level: logical
title_ko: 게이트 밖의 지식 파일은 재검증 시점에 아무 검사도 받지 않고 매크로가 도구 배선을 한 자리에 모은다
title: A knowledge file outside every gate is never checked at revalidation, and the macros keep the tool wiring in one place
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5adbc91e-1e33-46f6-bf34-c2d5f037c068
---
**근거** — 이유는 2026-09-01의 `STYLEGUIDE.md` 원문과 노트 부록 E가 적었다.

- **게이트 입력**: 노트 부록 E는 게이트를 test에, 재검증 시점을 `bazel test //...`에 대응시킨다. 게이트의 입력이 아닌 파일은 그 시점에 검사를 받지 않는다. 그래서 orphan을 링크가 아니라 검사로 정의한다. 생성 문서에 같은 정의를 넓힌 것이 `p12-generated-documents-are-gated`다.
- **게이트 선언**: 매크로가 도구의 `srcs`·`data`를 한 자리에서 맞춘다. `defs/knowledge.bzl`의 `_with_gates`는 `kb_lib.py`를 싣는 타깃의 runfiles에 게이트 등록부 `//defs:kb.bzl`을 넣는다. 그것이 빠지면 도구가 적재 시점에 죽는다.
- **패키지 이름**: 원문의 이유는 짧은 참조다. filegroup 이름이 디렉토리 이름과 같으면 `//kb/ontology/shapes`처럼 타깃 이름 없이 가리킨다.
- **glob 한 디렉토리 깊이**: 원문은 깊은 glob 대신 패키지를 나누라고 적었다. `glob`은 하위 패키지의 경계를 넘지 못한다.

실측(2026-10-03)에서 규약과 갈리는 자리가 셋이었다.

- 최상위 `BUILD.bazel`의 `//:build_drift_test`는 `py_test`를 직접 썼다.
- `tools/gen_build.py`가 생성하는 청크 패키지(`kb/dev/*`·`kb/vv/*`·`chunks/*`·`space`)의 filegroup 이름은 디렉토리 이름이 아니라 `bodies`였다.
- 결정 패키지는 결정마다 하위 디렉토리를 두고 `glob(["**/*.md"])`를 썼다.

세 자리는 규약의 예외가 아니었다. 유저 답 Q5-a(2026-10-03)가 코드를 규약에 맞추기로 정했고 같은 날 시행됐다. 지금 `//:build_drift_test`는 매크로 `kb_build_drift_test`로 서고, 결정 패키지의 filegroup 이름은 디렉토리 이름 `decision`이며 그 `srcs`는 파일을 나열한다.
