---
id: https://agentic-knowledge-base.dev/id/chunk/d6fe2e89-0600-4d91-9bf0-3aa8bb1d3528
type: decision
level: logical
title_ko: 나노출판 구조를 그대로 쓰면 변환도 지어낸 출처 어휘도 필요 없다
title: Reusing the nanopublication structure removes both conversion and invented provenance terms
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/428f00f0-6790-41c0-83a8-bf8a564e848e
---
**근거** (노트 4.3절)

- 단일 주장을 출처·메타데이터와 함께 자립적으로 묶는 구조는 나노출판이 이미
  **RDF 이름 붙은 그래프로 정의**해 두었다. 그대로 쓰면 변환이 없다.
- PROV-O가 이 체계가 필요로 하는 관계를 이미 갖고 있다 — 9.3절 구축 기록(읽기
  집합 → 쓰기 집합)은 `prov:used`·`prov:wasGeneratedBy`, 6.3절 일반화은
  `prov:wasDerivedFrom`, 버전은 `prov:wasRevisionOf`. 지어낸 출처 어휘가
  필요 없다.
- 내용 해시 IRI(나노출판의 trusty URI)를 쓰면 **변경 감지가 diff가 아니라 해시
  비교**가 된다. 본문이 바뀌면 해시가 바뀌고, 해시가 바뀌면 9.6절 링크
  재판정이 촉발된다.
- 청크는 자기가 무엇에 연결되는지 모른다 — **그것이 재사용 가능한 이유다.**
