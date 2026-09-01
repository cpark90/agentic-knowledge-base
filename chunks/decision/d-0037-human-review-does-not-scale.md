---
iri: https://agentic-knowledge-base.dev/id/chunk-d0037
plane: decision
level: concrete
label_ko: 사람의 검토로는 품질을 지킬 수 없다
label_en: Human review cannot hold quality
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — **사람의 검토로 품질을 지키는 방식은 처음부터 성립하지 않는다**고
전제한다. 대신 지식 접근을 **구조로** 통제한다 — 스코프가 무엇을 보는지를
정하고, plane이 무엇과 섞이지 않는지를 정하고, 검사 게이트가 판정한다.

**근거** (노트 1.1절)
- 에이전트가 만든 산출물을 사람이 한 줄씩 따라 읽는 것은 불가능하다.
- **매 시점 산출물이 바뀌고, 상세가 바뀌면 큰 방향도 바뀐다.** 검토가 끝난
  시점에 검토 대상이 이미 다른 것이 되어 있다.
- 에이전트의 자기 검토도 대안이 아니다 — 자기 출력을 검증했다고 믿는 것이
  알려진 편향이며, 그래서 검사 게이트는 에이전트 밖에 두고 규칙과 shape가
  판정하게 한다(1.5절).
- 사람이 남는 자리는 한 줄씩의 검토가 아니라 **판정 방식이 약한 지점의
  승인**이다 — decision plane의 valid 전이가 유저 승인을 조건으로 갖는
  것(5.1절)이 그 자리다.
