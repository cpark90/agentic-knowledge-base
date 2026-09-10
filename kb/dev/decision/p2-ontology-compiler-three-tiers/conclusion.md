---
id: https://agentic-knowledge-base.dev/id/chunk/a9cc1a02-29b3-4f53-8711-8d60a4bea3cf
type: decision
level: concrete
title_ko: 3계층을 통과한 온톨로지만 릴리스된다
title: Only an ontology that passes three tiers is released
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0050]
part_of: https://agentic-knowledge-base.dev/id/composite/33d988f2-27b2-44d7-98f2-110215bfe237
composite: {id: https://agentic-knowledge-base.dev/id/composite/33d988f2-27b2-44d7-98f2-110215bfe237, title_ko: 온톨로지 검사기 — 검사 3계층, title: The ontology compiler and its three check tiers}
---
**결론** — 온톨로지는 **컴파일된다.** 손으로 쓴 Turtle이 그대로 기반이 되지 않고, **검사 3계층**을 통과한 것만 릴리스된다. OBO Foundry가 ROBOT·ODK로 정착시킨 구조를 그대로 쓰고 새로 만들지 않는다.

| 계층 | 도구 | 검사 |
|---|---|---|
| 구문·스타일 | `robot report` | 라벨·정의 누락, 잘못된 참조, 폐기 규약 (0.6·0.9·0.10절) |
| 안티패턴 | SPARQL + `robot verify` | "바람직하지 않은 상황"을 질의로 명세. 결과가 나오면 실패 |
| 논리 정합성 | OWL 추론기 | 불만족 클래스, 의도치 않은 동치, 순환 계층 (2.9절 RL 안에서) |

**안티패턴 계층이 이 체계의 게이트 대부분을 흡수한다.** "근거 없는 할당"(Part IX), "ODD에 없는 조건을 참조하는 가정"(3.3절), "`sources`가 빈 청크"(4.3절), "`verifies`에 기준이 없음"(7.11절), "수준 허용표 밖의 plane·level 조합"(6.4절)은 전부 "이런 트리플이 존재하면 실패"라는 SPARQL 한 줄이다. shape로 쓰기 어색한 제약은 verify 질의로 쓴다.

**빌드 시스템이 컴파일러다.** Bazel의 `ontology()` 규칙이 세 계층을 테스트로 묶는다 — 통과 전에는 병합되지 않는다. **정규화 직렬화**가 첫 계층에 포함된다.
