---
id: https://agentic-knowledge-base.dev/id/chunk/9dc19dfd-7c12-4029-bac7-090286321af6
type: decision
level: logical
title_ko: 날짜 대리를 유지하는 안과 커밋 경계를 쓰는 안은 기각된다
title: Keeping the date proxy and using commit boundaries are rejected
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1da87f55-7c99-4879-831b-613ea302dc21
---
**대안** — 둘을 기각한다(유저 답 Q39, 2026-10-04).

| 대안 | 기각 이유 |
|---|---|
| 날짜 대리를 유지한다(Q39-a) | 비용은 검증기 하나로 가장 작다. 목표가 요구하는 관측 셋 가운데 예산 소진과 정지 규칙의 구분을 채우지 못한다 |
| 커밋 경계로 라운드를 자른다(Q39-b) | git에 의존하므로 케이스 실행기의 허용 목록 밖이다. 실행이 역사와 무관하게 재현돼야 한다는 요구(`reproducible-runs`)와도 맞지 않는다 |
