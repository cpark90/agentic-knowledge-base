---
id: https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb
type: decision
level: concrete
title_ko: 온톨로지 밖 어휘로 쓴 지식은 존재하지 않는다
title: Knowledge outside the vocabulary does not exist
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7, https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0046]
part_of: https://agentic-knowledge-base.dev/id/composite/0a751e1a-d819-45e5-8425-54945c706108
composite: {id: https://agentic-knowledge-base.dev/id/composite/0a751e1a-d819-45e5-8425-54945c706108, title_ko: 온톨로지는 계층의 어휘다, title: Ontology is the vocabulary of the ladder}
---
**결론** — 온톨로지는 이 체계의 **세계 모델**이다. 개발 작업의 세계에 무엇이 존재하고(개념), 무엇과 어떤 관계를 맺으며(관계), 무엇이 성립해야 하는지(공리)를 정의한다.

**온톨로지는 계층의 한 단계가 아니라 다섯 단계 전부의 어휘다.**

- functional — 어휘의 **서술적** 사용. "인증이 필요하다"는 `agt:AuthenticationRequirement`의 언어적 기술
- abstract — 어휘로 쓴 **형식 문장.** 변수는 선언되었고 도메인은 비어 있다
- logical — 어휘 + **도메인과 제약.** 변수는 온톨로지 개념, 도메인은 그 하위 개념
- concrete — 어휘의 **개체**(A-Box). `OAuth2`는 `agt:AuthenticationMethod`의 인스턴스
- executable — 개체가 가리키는 실제 산출물

스코프·가정·요구·기준·링크도 전부 온톨로지 어휘로 쓴 문장이다. **온톨로지 밖의 어휘로 쓴 지식은 이 체계에 존재하지 않는다.**

사람이나 에이전트가 보는 것 — 라벨 목록, 작업 집합, 코드 파일, 문서 — 은 모두 이 그래프에 대한 질의의 결과이며 저장된 사본이 아니다 (4.6절).
