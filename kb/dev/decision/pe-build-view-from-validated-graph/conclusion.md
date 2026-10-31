---
id: https://agentic-knowledge-base.dev/id/chunk/2f34d682-f7f2-43a2-9489-662da426e01f
type: decision
level: concrete
title_ko: 빌드 뷰는 검증된 그래프에서만 결정론적으로 나온다
title: The build view comes only from a validated graph, deterministically
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0162-deterministic-build-projection.md, id: https://agentic-knowledge-base.dev/id/chunk-d0162, title_ko: "빌드 뷰는 검증된 그래프에서만 결정론적으로 나온다", title: "The build view is gated on validation and deterministic"}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0188, title_ko: "대안 — 재현 가능한 빌드 투영", title: "Alternatives — reproducible build projection"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0162, https://agentic-knowledge-base.dev/id/chunk-d0188]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/00a6593d-57a6-445d-8e50-3dbb23b9df1b
composite: {id: https://agentic-knowledge-base.dev/id/composite/00a6593d-57a6-445d-8e50-3dbb23b9df1b, title_ko: 검증된 그래프에서 나오는 결정론적 빌드 뷰, title: Deterministic build view from a validated graph}
---
**결론** — 그래프에서 산출물을 만드는 빌드는 두 조건을 지킨다.

1. 조립된 union이 **검증을 통과할 때만** 실행한다. 실패하면 한 파일도 쓰지 않고 0이 아닌 코드로 끝난다.
1. 같은 입력이면 **바이트 동일한** 결과를 낸다.
