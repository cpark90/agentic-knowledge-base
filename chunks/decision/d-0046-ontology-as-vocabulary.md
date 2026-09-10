---
id: https://agentic-knowledge-base.dev/id/chunk-d0046
type: decision
level: concrete
title_ko: 온톨로지는 사다리의 단계가 아니라 전체의 어휘다
title: The ontology is the whole system's vocabulary, not a ladder rung
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 온톨로지는 이 체계의 세계 모델이다. 개발 작업의 세계에 무엇이
존재하고(개념), 그것들이 어떤 관계를 맺으며(관계), 무엇이 성립해야 하는지
(공리)를 정의한다. 온톨로지는 사다리의 한 단계가 아니라 **사다리 전체가 쓰는
어휘**이며, 이 어휘 밖에서 쓴 지식은 이 체계에 존재하지 않는다.

**근거** (노트 2.1절)
- 다섯 level은 같은 어휘를 다르게 쓸 뿐이다 — functional은 어휘의 서술적
  사용("인증이 필요하다"는 `agt:AuthenticationRequirement`의 언어적 기술),
  abstract는 도메인이 비어 있는 형식 문장, logical은 어휘에 도메인과 제약을
  더한 것, concrete는 어휘의 개체(ABox), executable은 그 개체가 가리키는
  실제 산출물이다.
- 스코프·가정·시나리오·링크도 전부 온톨로지 어휘로 쓴 문장이다. 어휘가 하나로
  묶여야 이것들이 서로를 참조하고 하나의 그래프로 질의된다.

**뷰** — 라벨 목록·situation·코드 파일·문서 등 사람이나 에이전트가 보는 모든
것은 그래프에 대한 질의의 결과이며 저장된 사본이 아니다. 저장된 뷰는 원본과
어긋나는 순간부터 거짓이 된다 (4.6절).
