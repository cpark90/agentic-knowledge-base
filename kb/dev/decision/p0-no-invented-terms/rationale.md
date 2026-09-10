---
id: https://agentic-knowledge-base.dev/id/chunk/2ef6272e-5c8f-4f52-b0e8-968c367709d0
type: decision
level: logical
title_ko: 지어낸 용어는 정의를 매번 컨텍스트에 실어야 한다
title: Invented terms force the definition into every context window
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/049f46d7-97d5-42ae-b0d7-dddf6f35d5fa
---
**근거** (노트 0.0절)

- 1.2절 학습자료 종속과 직결된다. 지어낸 용어는 모델이 사전 지식으로 해석할
  수 없어 **매번 정의를 컨텍스트에 실어야** 하고, 이는 1.1절 컨텍스트 예산을
  잠식한다.
- 표준어를 쓰면 모델이 이미 가진 분포가 해석기 역할을 하므로 같은 뜻을
  전달하는 토큰이 줄고 오해도 줄어든다.
- 최상위 분류를 직접 정의하면 그 정의가 상위 온톨로지 커뮤니티의 검증을 받지
  않은 채 체계 전체의 분류 기준이 된다 (2.2절).
