---
id: https://agentic-knowledge-base.dev/id/chunk-d0077
type: decision
level: concrete
title_ko: 청크 IRI가 앵커다 — 앵커 드리프트를 청크 안에 가둔다
title: The chunk IRI is the anchor - drift is confined inside the chunk
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 별도의 앵커 장치를 두지 않는다. **청크 IRI가 앵커다.** plane별
식별자(파일 경로, 심볼 ID, 세션 ID)는 IRI를 실제 저장 위치로 해석하는
수단일 뿐이다.

**근거** (노트 4.8절)
- **앵커 드리프트가 청크 안으로 갇힌다.** 링크는 IRI를 가리키므로 본문
  편집은 링크에 아무 영향을 주지 않는다. 링크가 `suspect`가 되는 것은
  청크가 분할·병합될 때 — 즉 IRI가 새로 생기거나 사라질 때뿐이다.
  "경로 + 줄 번호" 앵커가 편집마다 깨지던 문제가 사라진다.
- 분할·병합은 `prov:wasDerivedFrom`으로 옛 IRI와 이어져 추적된다.
- 같은 IRI가 다른 메커니즘의 기준점도 겸한다: 링크의 양 끝(`agt:KnowledgeItem`
  IRI), `assumes`의 출발점, 상승의 `prov:wasDerivedFrom` 사슬.
- **시간 정체성에 별도 링크가 필요 없다.** 청크 IRI가 지속하고 본문 버전이
  `prov:wasRevisionOf`로 이어진다.

**본문 해시가 재판정의 트리거다** — 본문이 바뀌면 해시가 바뀌고, 그 IRI를
끝으로 하는 링크가 `suspect`가 된다.
