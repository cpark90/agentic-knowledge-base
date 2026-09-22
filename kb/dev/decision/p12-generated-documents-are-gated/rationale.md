---
id: https://agentic-knowledge-base.dev/id/chunk/fda5bbdc-cddc-4950-a131-ac6173a5e3cd
type: decision
level: logical
title_ko: 검사받지 않는 생성물은 깨진 채로 통과한다
title: An unchecked artifact passes while broken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/872f4058-1ca6-432e-a0df-ba39a47b867b
---
**근거** — 규약을 문서에만 적으면 지켜지지 않는다. 2026-09-19 실측이 그것을 보인다.

- `p12-documents-are-generated`가 요구한 "생성 시각과 질의"를 여섯 생성물이 어겼다. `metrics`·`cq`·`communities`·`consistency`·`index`·`workset`이다. 결정은 2026-09-10에 stable이었다.
- `docs/rules.md`의 `<생성기>/<버전>` 표기를 지킨 생성물이 0종이었다.
- `bazel-bin/kb/dev/index.md`의 링크 610개가 전부 깨져 있었다. 소스 문서였다면 `doccheck`가 첫 커밋에서 잡았을 결함이다.
- `bazel-bin/kg/cq.md`의 28절 전부에 `행 = 행 = ` 이중 접두가 있었다.

검사 함수를 생성기와 공유하는 근거는 비용이다. 검사와 생성이 따로 있으면 생성기가 규약을 어겨도 게이트가 잡을 때까지 모르고, 고칠 곳이 두 군데가 된다. `docs/tools.md`가 "생성기는 검사기다. 생성 실패가 곧 게이트 실패"라고 정한 것과 같은 구조를 쓴다.

게이트 하나로 묶는 근거는 면제의 관리다. 검사가 흩어지면 면제도 흩어진다. `docs/waivers.md`가 게이트 id 하나로 면제를 선언할 수 있어야 한다.
