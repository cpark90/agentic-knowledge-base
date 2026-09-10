---
id: https://agentic-knowledge-base.dev/id/chunk-d0032
type: decision
level: concrete
title_ko: 불투명 지속 IRI와 해시 버전 IRI
title: Opaque persistent IRI and content-hash version IRI
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 청크·구성체·링크·가정은 전부 개체이므로 IRI를 갖는다. 지속성과
버전을 IRI 구조로 표현한다.
- **지속 IRI**: `agt:chunk/<uuid>` — 내용과 무관한 불투명 식별자
- **버전 IRI**: `agt:chunk/<uuid>/<content-hash>`
- **온톨로지 버전**: `owl:versionIRI`
- **사람이 읽는 이름**: IRI가 아니라 `rdfs:label`

**근거** (노트 0.7절)
- 라벨이나 경로가 바뀌어도 IRI가 유지되어야 **시간 정체성**(2.6절)이
  성립한다. IRI에 의미를 넣으면 이름 변경 시 IRI가 깨지고, 그것을 참조하던
  링크가 고아가 된다 — 폐기 정책(0.10절)이 삭제를 금지하는 것과 같은 이유다.
- 버전 IRI는 나노출판의 신뢰 가능 IRI 방식이다. **본문이 같으면 해시가
  같으므로** 동일성 판정이 문자열 비교로 환원되고, 청크의 분할·병합이
  새 IRI를 만들 때(4.10절) 이전 버전과의 관계를 해시로 확인할 수 있다.
- 온톨로지 버전만 표준 `owl:versionIRI`를 쓰는 것은 외부 어휘의 정의를
  변경하지 않는다는 원칙(0.3절)의 연장이다.
