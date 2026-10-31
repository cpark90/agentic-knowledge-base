---
id: https://agentic-knowledge-base.dev/id/chunk/14188a4f-f9a6-47b8-88d2-4041f32647af
type: decision
level: concrete
title_ko: 해석되지 않은 참조를 빠뜨리는 안과 빌드 실패로 처리하는 안은 택하지 않는다
title: Silently dropping unresolved references and failing the build on them are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:45:53+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:45:53+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/00a6593d-57a6-445d-8e50-3dbb23b9df1b
---
**대안** — 원천(harness-functional `docs/materialize-design.md`)이 대비한 안 둘을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 해석되지 않은 참조를 조용히 빠뜨린다 | 결손이 보이지 않는다. 빌드는 `.ref` 스텁을 내고 참조마다 상태를 `MANIFEST.json`에 남긴다(materialize-design "Validation gate"와 참조 해석 절) |
| 해석되지 않은 참조를 빌드 실패로 처리한다 | 오프라인 환경이 실패한다. 그래서 오프라인 환경은 실패하지 않고 결손을 표시한 채 내려간다(같은 절) |
