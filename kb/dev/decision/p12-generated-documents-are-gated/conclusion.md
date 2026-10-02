---
id: https://agentic-knowledge-base.dev/id/chunk/2314093a-f5e3-4fc0-96a0-6c5d35db03ee
type: decision
level: concrete
title_ko: 생성 문서는 gendoc 게이트의 대상이고 생성기가 그 검사를 공유한다
title: Generated documents are inputs to the gendoc gate, and generators share its checks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/9807be26-ff48-4cca-89c1-129f52e69df4]
serves: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
restored: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/872f4058-1ca6-432e-a0df-ba39a47b867b
composite: {id: https://agentic-knowledge-base.dev/id/composite/872f4058-1ca6-432e-a0df-ba39a47b867b, title_ko: 생성 문서의 게이트, title: The gate over generated documents}
---
**결론** — 생성 문서는 게이트 `gendoc`의 입력이다. `bazel test //...`가 생성 뷰를 빌드해 검사한다.

`STYLEGUIDE.md` §6은 "어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 orphan이다"라고 정한다. 생성 문서에도 같은 규칙을 적용한다. 2026-09-19 실측에서 생성물은 어떤 문서 게이트도 통과하지 않았고, 그 결과 `bazel-bin/kb/dev/index.md`의 링크 610개가 전부 깨진 채로 있었다.

검사 함수는 `tools/kb_lib.py`에 둔다. 생성기와 게이트가 같은 함수를 쓰므로 검사 항목이 늘 때 두 곳을 고칠 필요가 없다. 이것은 `docs/tools.md`의 "생성기 = 검사기"를 문서 층에 적용한 것이다.

게이트 id는 `gendoc`이다. 실패는 `FAIL [gendoc] <파일>:<줄>: <근거>`로 내고, 메시지의 인용이 수정 방향이다. 종료 코드는 `kb_lib` 상수를 따른다. SKIP은 PASS가 아니다.

면제는 코드가 아니라 `docs/waivers.md`에 게이트 id로 선언한다. `prose` 게이트와 같은 방식이다.
