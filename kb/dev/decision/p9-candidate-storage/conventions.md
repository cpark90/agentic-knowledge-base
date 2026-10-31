---
id: https://agentic-knowledge-base.dev/id/chunk/170edca8-616b-4e2f-9242-e122224f3120
type: decision
level: concrete
title_ko: 규범 문서 규약 — 후보는 -space 단위 지식에 살고 절대 deps가 되지 않으며 확정은 head로 옮겨진다
title: Normative-document conventions — Candidates live in -space chunks, never become deps, and are moved to the head on confirmation
former_title_ko: ["규범 문서 규약 — 후보는 -space 지식 항목에 살고 절대 deps가 되지 않으며 확정은 head로 옮겨진다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b4561dfb-19ea-4f34-b57e-c241cae4b9da
---
**규약** — `p9-candidate-storage`의 결론을 규범 문서에 싣는 문장이다.

규약: 후보 링크 | `type: agt:Space`이고 변수 하나에 파일 하나인 `kb/dev/**/*.space.md` | 미구현
규약: **실물 형식**은 2026-09-22의 첫 형태를 따른다. 파일은 `space/<슬러그>-space.md`이고 **변수 하나가 파일 하나**다. frontmatter는 `type: agt:Space`·`level: logical`이며 지식 종류 이름을 쓰지 않는다. 본문은 산문 한두 줄과 `yaml` 펜스 하나이고, 펜스는 `variable`과 `status`, `candidates`, `constraints`, `preferences`를 담는다. `variable`은 `from`과 `kind`를, `status`는 `open` 또는 `resolved`를, `candidates`는 `to`, `state`, `when`, `evidence`, `eliminated_by`를 갖는다. 후보를 아직 열거하지 않은 공간은 `candidates`를 쓰지 않는다.
규약: **후보는 `deps`가 되지 않는다.** `space/`에는 `kb_chunk` 타깃이 없고, 나가는 것은 A-Box 그래프 `//space:design_space`와 체크박스 뷰 `//space:choices` 둘이다. 게이트 `space`가 근거 없는 배제와 확정 후보 수를 판정하며, 이 게이트가 `r-011`의 실물이고, `r-011`은 "근거 없는 할당은 자료구조 수준에서 불가능하여야 한다"이다.
규약: 결정 확정 | `-space`에서 유저가 체크박스로 후보 하나를 고르면 구체 수준 결정이 생기고, 배제된(eliminated) 항목은 대안으로 승격한다 | `space_check`·`feedback`(미구현)
