---
id: https://agentic-knowledge-base.dev/id/chunk/cfdb2129-54b2-477e-912a-4b69cf1199d8
type: decision
level: logical
title_ko: 무효화는 assumes를 따라 전파되는데 그래프의 가정 링크가 하나뿐이어서 기본 가정을 전부에 잇고 좁혀 간다
title: Invalidation travels along assumes links, and with a single such link in the graph the default assumption was attached to every chunk to be narrowed later
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c6086cf0-0a2c-47d6-96d4-644307e4529c
---
**근거** — 요구 "조건이 깨지면 전수조사 없이 무효화한다"는 가정이 깨질 때 그 가정에 의존하는 항목이 무효화 표시되기를 요구한다(`p6-invalidation-propagation`). 전파는 `assumes` 링크를 따르므로 링크가 없는 항목에는 닿지 않는다.

의존성 그래프 설계 항목의 실측에서 `agt:assumes`는 노드 153 가운데 1건이었다. 그 항목은 152의 공백을 채우는 경로로 기본 가정 후 좁힘을 냈고, 유저가 2026-09-12에 수용했다. 기본 가정이 살아 있는 청크 614에 연결되었고, 그때 `metrics`는 기본 가정만 가진 청크를 614/615로 보고했다.

기본 가정의 명제가 저장소 구조와 언어 정책인 까닭은 `kg/base-kg.ttl`의 명제가 적는다. 둘 중 하나가 깨지면 청크의 IRI↔파일 해석과 라벨 인터페이스가 무효다. 모든 청크가 이 둘에 기댄다.

고유 전제의 유무를 판정하는 기계 검사는 없다. `assume_check`는 가정을 ODD 조건으로 판정할 뿐 빠진 가정을 찾지 않는다. 그래서 리뷰가 잡는다.
