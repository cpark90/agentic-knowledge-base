---
id: https://agentic-knowledge-base.dev/id/chunk/60b9e928-9226-4449-b92f-014597e9ff98
type: contract
level: logical
title_ko: 캐시 없이 두 번 실행한 게이트 테스트의 판정이 같고 실행 기록이 리비전과 환경을 적는다
title: Two uncached runs of the gate test agree and the run record carries revision and environment
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/27096663-5ee0-4958-b91f-db0f394c595a]
---
**합격 기준** — 기준 종류는 **불변식**이다. 같은 리비전·환경에서 실행 명령 c를 두 번 돌린 종료 코드 `rc₁ = rc₂`가 성립하고, 실행 기록은 초기 상태(리비전)·환경 버전(bazel·python·OS)·seed를 적는다.

**판정식**

- 양성(재실행): `bazel test //kg:gate_test --runs_per_test=2 --cache_test_results=no`가 PASS다. 두 실행 전부 PASS일 때만 요약이 `1 test passes`다.
- 양성(기록): 실행 기록 본문의 관측 줄에 리비전(짧은 해시)·워킹트리 변경 여부·bazel 버전·python 버전·OS·`seed 없음`이 있다.
- 음성: 두 실행 중 하나라도 FAIL이면 시험 전체가 FAILED로 끝나고 종료 코드가 비영이다. 재현되지 않는 검증은 5~6단계로 강등된다.

**등급** — B다. 판정은 기계가 하되 캐시 없는 재실행의 비용이 있다.

기준의 대상은 케이스의 실행 명령 전부이고 이 기준의 표본은 `//kg:gate_test`다. 판정의 원본은 Bazel의 `--runs_per_test`와 `tools/vv_run.py`의 `observation`이다.
