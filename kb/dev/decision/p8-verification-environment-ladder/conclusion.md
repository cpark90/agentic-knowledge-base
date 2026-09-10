---
id: https://agentic-knowledge-base.dev/id/chunk/daaadd68-8582-441a-8ffe-8648125310c6
type: decision
level: concrete
title_ko: 검증 환경은 여섯 단계 계층이고 피라미드 형태를 유지한다
title: Verification environments form a six-step ladder shaped as a pyramid
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0132]
part_of: https://agentic-knowledge-base.dev/id/composite/ea0859cb-27fc-4f71-a6a9-66d5e96be952
composite: {id: https://agentic-knowledge-base.dev/id/composite/ea0859cb-27fc-4f71-a6a9-66d5e96be952, title_ko: 검증 환경의 계층, title: The ladder of verification environments}
---
**결론** — 검증은 **충실도가 낮고 통제 가능한 환경에서 시작해 실제 환경으로 올라간다.** 위로 갈수록 실제에 가깝고 비용이 크며 재현성이 떨어진다. 각 단계는 그 아래 단계로 걸러지지 않은 것만 다룬다. (앞은 제품 검증, 뒤는 에이전트 검증)

1. **단위** — 청크·함수 단위, plane 판정 도구(5.4절) / 청크 하나 생성·편집의 shape 통과. 통제·재현성 완전
2. **모델** — 복합체 단위, 구현 없이 계약만으로 정합 검사 / 스코프 하나로 작업 집합 조립, 질의 결과 검사
3. **소프트웨어 루프** — 모듈 통합, 외부 서비스 mock·합성 데이터 / **시뮬레이션 프로젝트.** seed 고정으로 재현성 높음
4. **하드웨어 루프** — 실제 인프라(DB·큐) 연결 / 실제 하네스·툴·저장소. 유저는 자동 응답
5. **격리 실환경** — 스테이징, 실제 외부 서비스·합성 사용자 / 실제 프로젝트의 격리 브랜치, 실제 유저 피드백
6. **실환경** — 운영, 실제 사용자. 모니터링(11.5절)과 실행 기록이 검증. 통제·재현성 없음

**단계를 건너뛰지 않는다.** **피라미드 형태를 유지한다** — 낮은 단계에 많은 검증 청크, 높은 단계에 적은 검증 청크.
