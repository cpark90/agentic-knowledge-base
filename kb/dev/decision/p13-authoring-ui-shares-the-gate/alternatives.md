---
id: https://agentic-knowledge-base.dev/id/chunk/083fe860-db1e-41b3-afb8-1a2afb19c42d
type: decision
level: concrete
title_ko: 재직렬화 저장과 공유 서버와 네트워크 바인딩과 트리플 스토어 정본은 택하지 않는다
title: Re-serialising saves, a shared server, network binding and a triple-store master copy are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0187-authoring-discipline-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:48:42+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:48:42+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/4f30d4af-1a70-4db1-9bf3-1b2fe3bd8b5b
---
**대안** — 원천(harness-functional `docs/webui-design.md`)이 대비한 안 넷을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 그래프 전체를 rdflib로 재직렬화해 저장한다 | 섹션 배너와 주석, 서식, 술어 순서가 파괴되어 사람의 diff 리뷰가 깨진다. 그래서 노드 블록만 치환한다(webui-design §6) |
| 호스티드 라이브 다중 편집 서버를 둔다 | 원천의 결정 G가 이 안을 범위 밖에 두고, 협업은 git과 PR로 옮긴다(§8) |
| 0.0.0.0에 바인딩한다 | 쓰기와 추론 도구를 네트워크에 노출한다. 그래서 루프백 바인딩과 로컬 신뢰를 전제한다(§7) |
| 정본을 트리플 스토어로 옮긴다 | Oxigraph와 Fuseki는 TTL에서 파생하고 다시 적재하는 색인으로만 둔다(§9의 결정 D와 확장성 절) |
