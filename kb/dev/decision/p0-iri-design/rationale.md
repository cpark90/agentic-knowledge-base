---
id: https://agentic-knowledge-base.dev/id/chunk/9ae9e0cb-62ef-48a4-a149-d5a3169d55eb
type: decision
level: logical
title_ko: IRI에 의미를 넣으면 이름 변경이 링크를 고아로 만든다
title: Meaningful IRIs orphan links whenever a name changes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/eb847899-2640-4bca-955a-7f511528bc1d
---
**근거** (노트 0.7절)

- 라벨이나 경로가 바뀌어도 IRI가 유지되어야 **시간 정체성**(2.6절)이 성립한다.
  IRI에 의미를 넣으면 이름 변경 시 IRI가 깨지고 그것을 참조하던 링크가 고아가
  된다 — 폐기 정책(0.10절)이 삭제를 금지하는 것과 같은 이유다.
- 버전 IRI는 나노출판의 신뢰 가능 IRI 방식이다. **본문이 같으면 해시가 같으므로**
  동일성 판정이 문자열 비교로 환원되고, 링크의 재판정이 "무엇이 실제로
  바뀌었는가"를 해시 하나로 물을 수 있게 된다.
- 온톨로지 버전만 표준 `owl:versionIRI`를 쓰는 것은 외부 어휘의 정의를
  변경하지 않는다는 원칙(0.3절)의 연장이다.
