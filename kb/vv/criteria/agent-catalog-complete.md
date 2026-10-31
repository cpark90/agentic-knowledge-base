---
id: https://agentic-knowledge-base.dev/id/chunk/081e9e28-c736-49bc-84ea-6d41f0a1c44a
type: contract
level: logical
title_ko: 카탈로그 정합성은 gate_test 의 catalog 검사 다섯 갈래로 판정하고 어긴 카탈로그는 FAIL [catalog] 로 끝난다
title: Catalog consistency is judged by the five branches of the catalog check in gate_test, and a violating catalog ends in FAIL [catalog]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T00:43:01+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-24T03:41:41+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-24T22:39:25+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-25T00:43:01+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/3d83dc02-81cc-4d4f-98bb-fc4ffa44840a]
---
**합격 기준** — 기준 종류는 **불변식**이다. 데이터 그래프의 모든 `agt:Harness` 에 대해 다섯 갈래가 동시에 성립한다 — 역할마다 적용 범위 실재와 `agt:grants`, `agt:reads` ≥ 1, KB 별 쓰기 지식 종류의 역할 중복 0, `agt:maxConcurrent` 합 ≤ ODD `id:cond-concurrent-agents` 상한, 하위 역할의 `agt:subRoleOf` 대상이 같은 하네스가 hasRole 하는 다른 역할이고 그 하위 역할의 `agt:maxConcurrent` 가 0 이라는 것이다. 기준을 새로 만들지 않고 이미 도는 게이트를 그대로 판정 술어로 쓴다.

**판정 술어**

- 양성: `bazel test //kg:gate_test` 가 PASS 다. 커밋된 카탈로그는 역할 4 · 적용 범위 4 · KB 별 쓰기 지식 종류 중복 0 · 합 4 ≤ 5 였다(2026-09-13 첫 실행). 2026-10-24 측정은 역할 5 · 적용 범위 5 · 중복 0 · 합 4 ≤ 5 이고, 하위 역할 hci 의 maxConcurrent 는 0 이다.
- 음성(적용 범위 부재): 대응 적용 범위 없는 역할을 가진 하네스를 `--data` 에 더하면 `FAIL [catalog] … 역할 <역할> 에 대응 스코프 <스코프> 가 없다` 로 끝나고 종료 코드가 1 이다.
- 음성(쓰기 중복): 같은 KB 의 같은 `agt:writes` 지식 종류를 두 역할이 가지면 `KB <kb> 의 write plane <plane> 을 역할 … 이 공유한다` 가 나온다.
- 음성(한도 초과): 합이 상한을 넘으면 `역할별 agt:maxConcurrent 합 <합> > … 상한 <상한>` 이 나온다.
- 음성(상위 역할): `agt:subRoleOf` 의 대상이 하네스의 다른 역할이 아니면 `하위 역할 <역할> 의 상위 역할 <역할> 가 하네스 <하네스> 의 다른 역할이 아니다` 가 나온다.
- 음성(하위 역할 동시 실행): 하위 역할의 `agt:maxConcurrent` 가 0 이 아니면 `하위 역할 <역할> 의 agt:maxConcurrent 가 <값> 이다` 가 나온다. 커밋된 카탈로그에서 hci 의 값을 1 로 바꾸면 합은 5 ≤ 5 로 한도 안이므로 오류는 이 한 건이다.
- 판정 불가: ODD 그래프나 조건값이 없으면 통과가 아니라 `EXIT_CONFIG` 다.

**등급** — A 다. 다섯 갈래 전부 `bazel test //...` 안에서 기계가 판정하고 사람의 해석이 들어가지 않는다.

기준의 대상은 `//kg:gate_test` 의 `--data` 에 오르는 모든 `agt:Harness` 이고 판정의 원본은 `tools/validate.py` 의 `check_catalog` 다. 역할별 `generated.by` 의 쓰기 권한은 같은 도구의 `check_writer` 가 보고 별도 기준 `read-write-sets-recorded` 의 몫이다.
