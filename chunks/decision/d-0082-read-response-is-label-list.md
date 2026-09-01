---
iri: https://agentic-knowledge-base.dev/id/chunk-d0082
plane: decision
level: concrete
label_ko: 라벨이 인터페이스 — 읽기 응답은 라벨 목록이 기본
label_en: The label is the interface - reads return a label list by default
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — **라벨이 청크의 인터페이스다.** 읽기 응답의 기본은 본문이 아니라
**청크 라벨 목록**이고, 에이전트는 라벨 목록을 먼저 받아 필요한 청크만
assertion 그래프를 연다.

**근거** (노트 4.4절, 5.3절, 5.6절)
- 본문을 기본으로 반환하면 42줄 제한이 무의미해진다 — 청크를 작게 나눈
  이유가 조망이었는데 전부 열면 조망이 되지 않는다.
- **라벨이 본문을 대표하지 못하면 청크가 잘못 나뉜 것이다.** 라벨 목록이
  기본 응답이므로 잘못된 라벨은 곧바로 잘못된 읽기가 된다.
- plane마다 라벨이 담는 것이 다르다: `decision`은 ID + 결론 + 상태,
  `annotation`은 미해소 스레드만, `schema`는 변경된 필드 diff, `contract`는
  시그니처 목록, `artifact`는 심볼 목록.

**응답의 실제 형태** (5.6절) — scope별로 묶고 청크마다 한 줄:
`[ID] 라벨` + 상태 + 핵심 링크. `suspect`인 이유는 한 줄로 붙인다
(예: `← 가정 a2 unverified`). 넘치는 청크는 접고 개수만 알린다. 본문은
요청 시에만.
