---
id: https://agentic-knowledge-base.dev/id/chunk/7bf6ac61-b7c4-45bf-a7b1-438cf6d24079
type: decision
level: logical
title_ko: 청크가 아닌 개체는 verifies의 대상이 될 수 없어 사슬이 서지 못한다
title: A non-chunk entity cannot be a verifies target, so the chain never forms
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-24T10:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/70615ceb-7f52-4c6f-ae72-3d83ab59dbe0
---
**근거** — 옛 결론과 `defs/kb.bzl`의 링크 규칙이 2026-09-21에 정면으로 어긋난 것이 드러났다. 규칙은 `verifies`의 대상을 개발 KB **청크**로 한정하고 같은 수준을 요구하는데, 하네스·스코프는 `kg/catalog-kg.ttl`의 A-Box 개체라 `ChunkInfo`도 수준도 없다. 그래서 요구 `r-025`의 에이전트 쪽 사슬이 0이었다.

둘 중 하나를 고쳐야 했고 규칙을 넓히는 쪽은 비용이 크다. 분석 시점 검사가 A-Box 개체를 알아야 하고, 수준 일치 검사는 개체에 수준이 없어 예외가 되며, 그것은 검사 약화라 유저 승인 사항이다.

결정을 좁히는 쪽은 잃는 것이 적다. **분리의 실체는 도착점의 종류가 아니라 겨누는 결정의 종류에 있다.** 산출물이 틀렸을 때 코드를 고칠지 스코프를 고칠지는 도착점이 청크냐 개체냐로 갈리는 것이 아니라 그 청크가 무엇을 정한 것이냐로 갈린다. 역할·스코프를 정한 결정을 겨누면 에이전트 검증이고 산출물의 기준을 겨누면 제품 검증이다. 질의로 갈리는 성질은 그대로 남는다.

실측이 그것을 받친다. 에이전트 쪽 합격 기준으로 쓸 게이트가 이미 돈다 — shape 통과·`refines` 완주·게이트 통과율이고 전부 `bazel test //...` 안에 있다. 없던 것은 기준이 아니라 도착점이었다.
