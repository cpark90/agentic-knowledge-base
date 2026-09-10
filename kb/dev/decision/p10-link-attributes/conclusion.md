---
id: https://agentic-knowledge-base.dev/id/chunk/80ce7bef-d9df-40ac-84da-c534c1c726c2
type: decision
level: concrete
title_ko: 링크도 개체이므로 속성을 갖는다
title: Links are individuals and carry attributes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0111]
part_of: https://agentic-knowledge-base.dev/id/composite/eec0c89d-bba0-404c-a19e-b43043e2e1a2
composite: {id: https://agentic-knowledge-base.dev/id/composite/eec0c89d-bba0-404c-a19e-b43043e2e1a2, title_ko: 링크도 개체이므로 속성을 갖는다, title: Links are individuals and carry attributes}
---
**결론** — 링크도 개체이므로 속성을 갖는다. 4.3절 청크의 4분 구조를 링크에도 적용한다.

| 속성 | 내용 | 어휘 |
|---|---|---|
| 타입 | 9.2절 링크 타입 | `agt:` |
| 양 끝 | 청크 또는 복합체 IRI | — |
| 상태 | `candidate` / `confirmed` / `suspect` / `invalid` | `agt:` |
| 근거 | 왜 이 링크가 성립하는가 (9.8절 근거 유형) | `prov:wasDerivedFrom` |
| 만든 주체 | 구축이면 에이전트, 복원이면 파이프라인 | `prov:wasAttributedTo` |
| 확인한 주체 | 후보 → 확정을 승인한 사람 또는 위임 에이전트 | `prov:wasAttributedTo` (별도 활동) |
| 시각 | 생성·확정·마지막 재판정 | `prov:generatedAtTime` |
