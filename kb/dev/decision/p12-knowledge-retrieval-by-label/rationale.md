---
id: https://agentic-knowledge-base.dev/id/chunk/455bac43-8a38-426b-98a8-6d02b966a8f7
type: decision
level: logical
title_ko: 앵커 수 × k로 상한되어 지식 베이스 크기와 무관하다
title: Bounded by anchors times k, the loop is independent of knowledge base size
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5133b9c7-e45d-462d-ad99-20e3b49ef15c
---
**근거** (노트 12.11절)

- 어휘 검색만 쓰면 구조적 관계(의존·참조·검증)를 놓치고, 구조 탐색만 쓰면
  진입점이 없다. 순서가 둘을 각자의 자리에 둔다.
- 이 순서는 **별도 검색 시스템 없이 라벨 목록 루프 안에서** 동작하며, 반복별
  추가 토큰이 **앵커 수 × k**로 상한되어 **지식 베이스 크기와 무관**하다.
  KB가 커져도 컨텍스트 예산이 흔들리지 않는다는 뜻이다.
- 라벨과 개념으로 못 찾는 것은 **청크가 잘못 나뉘었거나 라벨이 부패한
  것**이다(4.13절). 전문 검색으로 덮으면 그 신호가 사라진다.
