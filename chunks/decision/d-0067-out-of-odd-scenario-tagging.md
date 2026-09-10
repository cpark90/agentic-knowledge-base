---
id: https://agentic-knowledge-base.dev/id/chunk-d0067
type: decision
level: concrete
title_ko: ODD 밖 시나리오는 별도 태그로 분리해 보관한다
title: Out-of-ODD scenarios are kept but tagged separately
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — ODD 밖 시나리오는 존재할 수 있되 별도 태그로 표시한다. 파생물이
ODD에 없는 속성을 참조하면 게이트가 거부하지만, 시나리오만은 기각 대신
태그로 처리한다.

**근거** (노트 3.3절)
- 설계 범위 밖 상황에서 무엇이 일어나는지 아는 것도 가치가 있다. 기각하면
  그 지식이 사라진다.
- 그렇다고 범위 안 시나리오와 섞으면 커버리지가 왜곡된다. 커버리지의 분모는
  ODD이므로(10.1절), 분모에 없는 시나리오가 같은 집합에 섞이면 커버리지
  수치가 뜻을 잃는다. 태그가 두 집합을 가른다.
