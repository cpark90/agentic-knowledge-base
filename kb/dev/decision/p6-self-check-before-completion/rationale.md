---
id: https://agentic-knowledge-base.dev/id/chunk/ad872d64-810f-4735-b01d-941166f0cfe6
type: decision
level: logical
title_ko: 판정은 에이전트 밖의 게이트가 하므로 완료는 게이트 통과로 정하고 생성물은 드리프트 테스트가 원본과 묶는다
title: Judgement belongs to gates outside the agent, so completion is defined by passing them, and drift tests tie each output to its source
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-07T03:03:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-07T03:03:36+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3e29e698-8ef5-4fe2-ac1b-867e596a5179
---
**근거** — 요구 r-016은 편집의 판정을 에이전트 밖의 규칙과 shape에 맡긴다. 사람의 한 줄 검토가 성립하지 않기 때문이다. 그 판정의 실행 단위가 `bazel test //...`다. `pe-knowledge-files-are-gate-inputs`가 지식 파일마다 적어도 한 게이트를 거치게 하므로 게이트 전체 PASS가 곧 편집 전체의 판정이다.

셀프체크 절은 저장소 초기 구축(2026-09-01)부터 `AGENTS.md`에 있었다. 첫 판은 게이트 전체와 정규화 두 줄이었다. 생성 BUILD와 생성 skill의 재생성 줄은 2026-09-19에, 코드 재추출 줄은 2026-09-30 코드 추출 도입과 함께 더해졌다(커밋 이력).

정규화의 이유는 노트 2.5절이다. 직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 차고 무효화 판정의 입력이 오염된다. 정규화 직렬화는 온톨로지 검사 3단계의 첫 단계다(`p2-ontology-compiler-three-tiers`). 손으로 쓰는 TTL을 정규형 검사에서 뺀 판정은 2026-09-13이다. 그 파일의 서식(배너·주석·술어 순서)이 원본이기 때문이다.

커밋 전 시점은 노트 10.6절의 재검증 시점에서 온다. 커밋은 링크·가정을 일괄 재판정하는 경계다.

미확정: 셀프체크의 실행을 커밋 훅 같은 기계 장치로 강제하지 않은 이유는 기록에서 확인하지 못했다. 정규화 검사를 테스트로 배선하지 않은 이유도 확인하지 못했다.
