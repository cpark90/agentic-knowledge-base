---
id: https://agentic-knowledge-base.dev/id/chunk/069386af-5167-4f76-a275-aeaa120d139a
type: artifact
level: executable
title_ko: 합격 기준을 양성 쪽에서 판정하는 검증기는 defs/knowledge.bzl 의 매크로가 선언한 테스트 타깃이다
title: The verifiers that judge pass criteria on the positive side are the test targets declared by the macros in defs/knowledge.bzl
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-22T23:42:00+09:00}
---
**검증기** — 합격 기준 하나하나를 양성 쪽에서 판정하는 검증기는 `defs/knowledge.bzl` 의 매크로가 선언한 테스트 타깃이다. 매크로는 `kb_gate_test`·`kb_chunk_lint_test`·`kb_doccheck_test`·`kb_gendoc_test`·`kb_skills_drift_test` 다.

**적용하는 기준** — 타깃마다 판정 도구 하나를 runfiles 로 받아 지식 파일을 인자로 실행하고 도구의 비영 종료를 테스트 실패로 옮긴다. 도구는 `tools/validate.py`·`tools/chunk_lint.py`·`tools/doccheck.py`·`tools/gendoc.py` 다.

**호출 경로** — `bazel test //...` 가 이 타깃 전부를 부른다. 청크 타깃(`kb_chunk`)은 빌드 검증 액션 `KbChunkLint` 로 같은 검사를 한 번 더 돌려 `bazel build` 만으로도 42줄·frontmatter·첨가·목록이 판정된다.

**거부 형식** — 실패 메시지는 `FAIL [<게이트 id>] <위치>: <규칙>` 이라 거부가 곧 수정 방향이다. 면제는 코드가 아니라 `docs/waivers.md` 의 표에 선언되고 게이트 id 로 걸린다.

**검증 대응물** — 없음. 같은 `executable` 수준의 개발 항목이 없어 `verifies` 를 달 수 없다.
