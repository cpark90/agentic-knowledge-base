---
id: https://agentic-knowledge-base.dev/id/chunk/f21050ba-f71f-4e47-8e4f-e0ddbd6c2095
type: decision
level: logical
title_ko: 복합체는 선언이고 커뮤니티는 계산이라 탐지는 후보 생성기로만 맞는다
title: Composites are declared and communities are computed, so detection fits only as a candidate generator
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/165ef75a-d4f3-4de2-aba2-ea3a8efb787a
---
**근거** (노트 4.5절·9.8절; LARGER §5 절제 실험) — 복합체는 "함께 읽힘·순서"라는 **의도**의
선언이고, 커뮤니티는 링크 밀도라는 **구조**의 계산이다. 구조가 촘촘하다고 함께 읽혀야 하는
것은 아니므로 계산 결과를 곧 복합체로 삼으면 근거 없는 할당이 된다(r-011). 판정은 사람 또는
승인된 판정자의 몫이고(9.8절), 도구는 후보를 추리는 데서 멈춘다 — 임베딩 유사도를 후보 추림에만
쓰는 규칙과 같은 자리다.

LARGER의 절제 실험에서 커뮤니티 제거의 손실(−4.1)은 그래프 확장 제거(−13.5)보다 훨씬 작다 —
커뮤니티는 보조 신호이지 검색의 주된 요소가 아니다. 이 체계의 복합체 동질성 규칙(같은
plane·level) 때문에 plane을 넘는 군집은 복합체가 될 수 없고, 그런 군집이 말하는 "함께 갱신됨"은
`relatedTo` 링크의 영역이다. 그래서 탐지의 출력은 복합체 후보와 링크 후보 두 갈래로 나뉜다.
