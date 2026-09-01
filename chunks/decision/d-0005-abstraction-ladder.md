---
iri: https://agentic-knowledge-base.dev/id/chunk-d0005
plane: decision
level: concrete
label_ko: 추상화 사다리 다섯 수준
label_en: Five-level abstraction ladder
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 모든 지식 항목은 추상에서 실용으로 내려오는 다섯 단계를 갖는다:
functional(개념·의도) → abstract(형식 문장, 도메인 없음) → logical(선택지
공간: 도메인 + 제약) → concrete(확정된 개체) → executable(동작하는 형태).
단계를 건너뛰지 않는다.

**근거** (노트 6.1절)
- **abstract는 기계가독의 경계다.** functional → abstract 전이가 자연어를
  형식 언어로 옮기는 단계이며, 형식화의 어려움과 선택지 전개의 어려움을
  분리한다.
- **logical은 근거의 보존소다.** functional과 concrete만 있으면 의도와
  결과만 남고 그 사이가 빈다 — 선택되지 않은 대안과 배제 이유가 여기
  보존된다.
- functional에서 곧바로 executable로 가는 것이 현재 에이전트의 기본
  동작이며, 그것이 사다리 단절 문제의 원인이다.

**전이 규칙** (6.2절, 6.8절) — 각 하강 전이는 근거와 refines 링크를
남기고, 전이 게이트(어휘 검사·후보 비어있지 않음·배제 근거 존재·판정
도구 통과)를 통과해야 한다. 게이트 없이 만든 하위 청크는 고아율에 잡힌다.
