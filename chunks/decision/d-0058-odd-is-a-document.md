---
iri: https://agentic-knowledge-base.dev/id/chunk-d0058
plane: decision
level: concrete
label_ko: ODD는 영역 개념이 아니라 프로젝트당 하나의 문서다
label_en: The ODD is a document, one per project - not a permission region
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — ODD는 이 프로젝트의 지식과 작업이 설계된 운영 조건의 명세이며,
스코프처럼 권한을 나누는 영역 개념이 아니라 **실제로 작성되고 버전 관리되고
참조되는 문서**다. 프로젝트당 하나이며, 하위 시스템이 별도 ODD를 가지면
상위 ODD의 부분집합이어야 한다.

**근거** (노트 3.1절)
- ODD가 답하는 질문은 하나다 — "이 프로젝트의 산출물은 어떤 조건에서
  동작하도록 설계되었는가." 스코프가 "누가 무엇을 볼 수 있는가", 가정이
  "이 항목이 무엇을 전제하는가"라면 ODD는 "전체가 무엇을 전제하는가"다.
- 온톨로지가 어휘라면 ODD는 그 어휘로 쓴 **첫 번째 문서**다. 스코프·가정·
  시나리오·설계 공간 등 다른 모든 문장은 ODD 안에서 쓴다.
- 온톨로지와 단위·변경률이 다르다. 온톨로지는 "어떤 개념이 존재할 수 있는가"
  를 분야 전체 단위로 답하고, ODD는 "이 프로젝트에서 그 개념이 어떤 값을
  갖는가"를 프로젝트 하나 단위로 답한다. `agt:NetworkConnectivity`가 환경
  조건이라는 것은 온톨로지, 이 프로젝트가 오프라인 동작을 지원하지 않는다는
  것은 ODD다.
