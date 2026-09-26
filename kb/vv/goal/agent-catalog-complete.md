---
id: https://agentic-knowledge-base.dev/id/chunk/3d83dc02-81cc-4d4f-98bb-fc4ffa44840a
type: requirement
level: functional
pattern: ubiquitous
title_ko: 카탈로그의 역할은 저마다 스코프와 읽기 plane 을 갖고 쓰기 plane 을 나누며 동시 실행 한도 안이어야 한다
title: Each role in the catalog must have a scope and read planes, must not share a write plane, and must stay within the concurrency bound
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-24T11:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
---
**검증 목표** — 에이전트 쪽 검증 사슬이다. 만드는 쪽을 규정하는 입력은 카탈로그이므로, 카탈로그가 스스로 정한 역할의 책임을 지키는지가 에이전트가 검증되었다는 말의 내용이다. 역할마다 스코프와 읽기 plane 이 있고, 한 KB 의 한 쓰기 plane 을 두 역할이 나눠 갖지 않으며, 역할별 동시 실행 한도의 합이 ODD 상한 안이라는 것이 보여져야 한다.

- **이해관계자**: 검증자 · **관심사**: 역할과 권한

**무엇을 관측하면 성립하는가**

- 하네스가 `agt:hasRole` 하는 역할마다 대응 스코프(`id:scope-<슬러그>`)가 실재하고 하네스가 그것을 `agt:grants` 한다.
- 역할마다 `agt:reads` 가 하나 이상이다. 읽지 못하는 역할은 작업 집합을 받을 수 없다.
- 한 KB(`agt:writesIn`, 없으면 `kb/dev`) 안에서 한 `agt:writes` plane 을 두 역할이 공유하지 않는다. 설계·구현·운영의 분리다.
- 역할별 `agt:maxConcurrent` 의 합이 ODD 동적 요소 `id:cond-concurrent-agents` 의 상한 이하다.
- 넷 중 하나라도 어긋난 카탈로그는 거부되고 거부 문구가 어느 역할의 무엇인지 가리킨다.

판정의 원본은 `tools/validate.py` 의 `check_catalog` 와 `kb/dev/decision/p8-agent-vv/conclusion.md` 의 기준 행이다.
