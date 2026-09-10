---
id: https://agentic-knowledge-base.dev/id/chunk-d0024
type: decision
level: concrete
title_ko: 지어낸 용어를 쓰지 않는다
title: No invented terminology
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 확립된 표준어가 있으면 그것을 쓰고, 없을 때만 새로 만든다.
개념의 **최상위 분류는 상위 온톨로지에서 가져온다** — "결정이 무엇인가"를
이 프로젝트가 처음부터 정의하지 않는다.

**근거** (노트 0.0절, 2.2절)
- 학습자료 종속(1.2절)과 직결된다. 지어낸 용어는 모델이 사전 지식으로
  해석할 수 없어 **매번 정의를 컨텍스트에 실어야** 하고, 이는 1.1절
  컨텍스트 예산을 잠식한다.
- 표준어를 쓰면 모델이 이미 가진 분포가 그대로 해석기 역할을 하므로,
  같은 뜻을 전달하는 데 드는 토큰이 줄고 오해도 줄어든다.
- 최상위 분류를 직접 정의하면 그 정의가 상위 온톨로지 커뮤니티의 검증을
  받지 않은 채 체계 전체의 분류 기준이 된다.
