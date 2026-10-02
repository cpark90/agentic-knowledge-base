---
id: https://agentic-knowledge-base.dev/id/chunk/15543daa-568f-4520-a918-066c1904ee6e
type: decision
level: logical
title_ko: 생성기 자체 검사만·사람 검토·렌더 시점 검사 안은 기각된다
title: Self-check only, human review, and render-time checking are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/872f4058-1ca6-432e-a0df-ba39a47b867b
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 생성기가 자기 출력만 검사하고 게이트를 두지 않는다 | `tools/gen_skills.py`가 그 방식이고 SKILL 15개는 균질하다. 그러나 새 생성기가 검사를 빠뜨려도 아무도 모른다. 게이트는 빠뜨림 자체를 잡는다 |
| 게이트 없이 사람이 검토한다 | 610개의 깨진 링크가 사람 검토를 통과해 있었다. 기계적으로 참·거짓이 갈리는 것은 게이트의 몫이다 (`tools/doccheck.py` docstring) |
| 렌더 시점에 검사한다 | 이 문서들은 렌더되지 않고 원문으로 읽힌다. 렌더 단계가 없다 |
| 기존 `doccheck`의 `srcs`에 생성 뷰를 그냥 더한다 | `doccheck`의 세 검사는 소스 문서를 전제한다. 생성물에는 머리 블록·표·수치 표기 검사가 더 필요하고, 면제와 실패 메시지도 갈라야 한다. 게이트 id를 나누면 `docs/waivers.md`가 둘을 구분해 면제할 수 있다 |
