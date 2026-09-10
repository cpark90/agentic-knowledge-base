---
id: https://agentic-knowledge-base.dev/id/chunk-d0152
type: decision
level: concrete
title_ko: 검색의 인덱스는 라벨과 개념이다
title: Retrieval is indexed by labels and concepts
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 검색의 단위는 청크이고 인덱스는 **라벨과 온톨로지 개념**이다.
본문 전문 검색은 마지막 수단이다.

**근거** (노트 10.11절)
- **라벨 검색** — `prefLabel`·`altLabel`·`hiddenLabel`을 인덱스로, 청크
  라벨 목록을 반환한다.
- **개념 검색** — 청크가 참조하는 온톨로지 개념으로 그 개념을 쓰는 청크를
  찾는다.
- **구조 검색** — 링크 패턴("X를 충족하며 Y를 가정하는")을 그래프 질의로
  푼다.
- **유사도 검색**(임베딩) — **후보 추림에만** 쓰고, 결과는 라벨 목록으로
  낸다. 순위가 곧 답이 되지 않게 한다.
- 라벨과 개념으로 못 찾는 것은 **청크가 잘못 나뉘었거나 라벨이 부패한 것**
  이다 (4.13절). 전문 검색으로 덮으면 그 신호가 사라진다.
