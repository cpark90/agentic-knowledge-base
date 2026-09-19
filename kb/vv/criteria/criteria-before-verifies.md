---
id: https://agentic-knowledge-base.dev/id/chunk/23979ee5-fd7a-4e14-9f91-6d3ec2794725
type: contract
level: logical
title_ko: 모든 verifies의 주어는 contract 청크를 refines 하고 verify 질의의 결과 행은 0이다
title: Every verifies subject refines a contract chunk and the verify query returns zero rows
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/73d83879-75e4-43f9-a07a-4335711e2ac1]
---
**합격 기준** — 기준 종류는 **불변식**이다. 병합 그래프의 모든 `?s agt:verifies ?o`에 대해 `?s agt:refines ?c . ?c a agt:ContractChunk`가 성립한다.

**판정식**

- 음성: 기준을 `refines` 하지 않는 케이스 하나를 head 그래프에 더하면 `//kg:gate_test`가 `FAIL [verify] tools/verify-queries/verifies-without-criteria.rq: <주어> <대상>  (안티패턴: 기준 없는 verifies …)`로 끝나고 종료 코드가 1이다.
- 양성: `bazel test //kg:gate_test`가 PASS다. 질의의 결과 행이 0이다.
- 대조: `bazel build //kg:audit`의 검증 현황 절에 기준 없는 `verifies` **0**이 있다. 감사는 같은 정의로 센다.

**등급** — B다. 판정은 기계가 하되 그래프 병합과 질의 실행의 비용이 있다.

기준의 대상은 `//kg:gate_test`의 `data`에 오르는 모든 `verifies` 링크이고 판정의 원본은 `tools/validate.py`의 `check_verify`와 질의 파일이다. 주어의 자격(`kb/vv` 패키지)은 별도 기준 `verifies-subject-vv`의 몫이다.
