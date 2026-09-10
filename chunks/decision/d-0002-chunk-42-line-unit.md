---
id: https://agentic-knowledge-base.dev/id/chunk-d0002
type: decision
level: concrete
title_ko: 42줄 청크가 최소 지식 단위
title: 42-line chunk as minimal knowledge unit
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 모든 지식은 본문 42줄 이하의 자립적 청크를 가장 작은 부품으로
한다. 한 청크는 하나의 plane, 하나의 level, 한 주제만 다룬다.

**근거** (노트 4.1절)
- 42줄은 에이전트 컨텍스트 한계 약 200줄의 1/5 — 한 번에 4~5개 청크를
  조망할 수 있는 크기다.
- 같은 개념이 네 분야에서 독립적으로 정립되었다: 인지과학의 chunk(7±2),
  구조적 글쓰기의 information block, 문학적 프로그래밍의 chunk, 모듈형
  문서의 topic.
- 42줄을 넘는 것은 청크가 아니라 구성체이며 분할해야 한다.

**분할·병합 신호** (4.10절)
- 분할: 라벨을 하나로 쓸 수 없음 / 본문 일부만 재사용·가정·suspect 대상.
- 병합: 두 청크가 항상 함께 읽힘 / 한쪽이 다른 쪽 없이 이해 불가 /
  합쳐도 42줄 이하.
- 분할·병합은 새 IRI를 만들고 옛 IRI를 prov:wasDerivedFrom으로 잇는다.
