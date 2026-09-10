---
id: https://agentic-knowledge-base.dev/id/chunk-d0048
type: decision
level: concrete
title_ko: 온톨로지는 entity/related와 어휘/형식화로 나눈 모듈이다
title: Ontology modules split by entity/related and vocabulary/formalization
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 온톨로지를 단일 파일이 아니라 모듈로 나누고, import만 하는 얇은
최상위 `project-ontology`가 합친다. 분할 축은 둘이다 — plane으로 분류되는
개념(`entity/`)과 그렇지 않은 횡단 개념(`related/`), 그리고 어휘(`defect`)와
형식화(`defect-rules`).

**근거** (노트 2.3절)
- **(a) entity / related** — 스코프·가정·채널·정책·하네스는 어느 plane에도
  속하지 않고 모든 plane과 상호작용한다. 이것들을 plane 안에 억지로 넣으면
  plane 분류 자체가 무너진다.
- **(b) 어휘 / 형식화** — 어휘는 안정적이고 규칙은 자주 바뀐다. 결함이
  무엇인지(개념과 포섭 관계)와 실행 기록에서 결함을 추론하는 규칙을 나눠야
  어휘 사용자가 규칙 변경에 영향받지 않는다.

**구성** — `upper`(외부), `entity/`(knowledge-item·decision·contract·schema·
artifact·annotation·memory), `related/`(condition·scope·assumption·scene·
trace·channel·policy·harness), `profile/`(2.11절), `defect`, `defect-rules`.

**경계 규칙** — 모듈은 서로를 import할 수 있어도 다른 모듈의 개념을 정의해
넣어서는 안 되고, `upper`는 수정 금지다. 확장은 새 모듈을 추가하는 것으로만
하며 기존 모듈을 수정하지 않는다.
