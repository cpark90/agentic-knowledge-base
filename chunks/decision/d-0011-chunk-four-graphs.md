---
iri: https://agentic-knowledge-base.dev/id/chunk-d0011
plane: decision
level: concrete
label_ko: 청크는 네 개의 이름 붙은 그래프다
label_en: A chunk is four named graphs
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 청크 하나는 나노출판 구조 그대로 네 개의 이름 붙은 그래프다:
head(타입·plane·level·라벨), assertion(본문 — 42줄 제한은 여기만),
provenance(무엇에서 왔는가), pubinfo(누가 언제 만들었는가, 버전).
출처·귀속은 PROV-O로만 쓴다.

**근거** (노트 4.3절)
- 나노출판이 이미 RDF 이름 붙은 그래프로 정의되어 있어 변환이 필요 없다
  — 지어낸 구조가 아니다 (0.0절 표준어 원칙).
- 본문의 내용 해시를 청크 IRI 버전에 넣는다(trusty URI). 본문이 바뀌면
  해시가 바뀌고, 해시 변경이 링크 재판정을 촉발한다 — 변경 감지가
  diff가 아니라 해시 비교가 된다.
- 가정과 링크는 네 그래프 안에 없다. 링크 모델이 청크 IRI를 가리킬
  뿐이고, 청크는 자기가 무엇에 연결되는지 모른다 — 그것이 재사용 가능한
  이유다.

**저장** (4.9절) — head·provenance·pubinfo는 -kg에, assertion 본문은
plane별 위치에(산문 계열은 파일 하나 = 청크 하나, 코드 계열은 심볼).
메타데이터 질의에 본문을 열 필요가 없다.
