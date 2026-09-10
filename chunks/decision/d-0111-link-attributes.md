---
id: https://agentic-knowledge-base.dev/id/chunk-d0111
type: decision
level: concrete
title_ko: 링크도 개체다 — 링크가 갖는 속성
title: Links are entities with attributes
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크도 개체이므로 속성을 갖는다. 4.3절 청크의 4분 구조를
링크에도 그대로 적용한다.

**속성** (노트 8.10절)
- **타입** — 8.2절 링크 타입. `agt:` 어휘
- **양 끝** — 청크 또는 구성체 IRI (파일이 아니다)
- **상태** — `candidate` / `confirmed` / `suspect` / `invalid`. `agt:`
- **근거** — 왜 이 링크가 성립하는가. 8.8절 판정 근거 유형.
  `prov:wasDerivedFrom`
- **만든 주체** — 구축이면 에이전트, 복원이면 파이프라인.
  `prov:wasAttributedTo`
- **확인한 주체** — 후보 → 확정을 승인한 사람 또는 위임 에이전트.
  `prov:wasAttributedTo`(별도 활동)
- **시각** — 생성·확정·마지막 재판정. `prov:generatedAtTime`

**근거** — 상태와 시각이 링크에 붙어 있어야 8.6절 재판정 큐와 8.14절
지표를 링크 모델만 보고 계산할 수 있다.
