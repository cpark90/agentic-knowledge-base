---
id: https://agentic-knowledge-base.dev/id/chunk/07a91c11-d4bb-50b8-bb7a-fed3f2b0ddfd
type: decision
level: logical
title_ko: 논리 시나리오 요인 — 대응 스코프 없는 역할 하나를 가진 하네스의 검증이 노출하는 현상
title: Logical scenario factors — the phenomena exposed by validating a harness holding one role without its matching scope
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4ee07222-bd78-5edf-a40f-de853056fa4d
---
**요인** — 노출하려는 현상은 `agt:roleSpecificationViolation` 하나다. 역할이 명세의 필수 요소를 빠뜨린 것이 이 시나리오의 결함 형태다. 표본 근거는 요인 주입 하나다. 변수 `missing`에 keep 밖 값 `scope`를 주입해 케이스 하나를 낸다. 명령의 `--waivers docs/waivers.md`는 게이트와 같은 입력을 맞춰 면제된 기존 위반이 건수에 섞이지 않게 한다. 기여하는 검증 목표는 `kb/vv/goal/agent-catalog-complete.md`(`https://agentic-knowledge-base.dev/id/chunk/3d83dc02-81cc-4d4f-98bb-fc4ffa44840a`)다.
