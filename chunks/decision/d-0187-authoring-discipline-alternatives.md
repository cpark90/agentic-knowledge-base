---
id: https://agentic-knowledge-base.dev/id/chunk-d0187
type: decision
level: concrete
title_ko: 대안 — 저작 규율
title: Alternatives — authoring discipline
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:56+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-authoring-discipline
---
**대안** — 묶음의 세 결정마다 원천(harness-functional `ONTOLOGYSTYLE.md`·`docs/webui-design.md`)이 대비한 안을 적는다.

- d-0160(검색 선행·단일 책임): 같은 뜻의 노드를 하나 더 만드는 안은 기각이다. 근사 동의어 클래스는 저장소가 막는 drift이고, 동의어는 새 노드가 아니라 한 노드의 `skos:altLabel`로 붙인다(ONTOLOGYSTYLE §1b).
- d-0160(검색 선행·단일 책임): 서술 상한을 넘는 노드는 분해하거나 대안 서술을 별도 노드로 분리하며, 한 노드에 두 가지를 담아 두는 안은 단일 책임 위반 신호로 다룬다(§1c).
- d-0161(그래프가 못 보여주는 것만): 정의·주석에 라벨 재진술·수정 이력·주석 처리된 죽은 선언을 적는 안은 기각이다. 원천은 그것들을 쓰지 않을 항목으로 열거하고 발견 시 삭제 대상으로 정한다(ONTOLOGYSTYLE §1d).
- d-0163(저작 UI): 그래프 전체를 rdflib로 재직렬화해 저장하는 안은 기각이다. 섹션 배너·주석·서식·프레디킷 순서가 파괴되어 사람의 diff 리뷰가 깨지므로 노드 블록만 치환한다(webui-design §6).
- d-0163(저작 UI): 호스티드 라이브 다중 편집 서버는 결정 G의 대안으로 범위 밖에 두고 협업은 git/PR로 옮긴다(§8).
- d-0163(저작 UI): 0.0.0.0 바인딩은 쓰기·추론 도구를 네트워크에 노출하므로 기각하고 루프백 바인딩과 로컬 신뢰를 전제한다(§7).
- d-0163(저작 UI): 정본을 트리플 스토어로 옮기는 안은 기각이고, Oxigraph·Fuseki는 TTL에서 파생·재적재하는 색인으로만 둔다(§9 결정 D·확장성).
