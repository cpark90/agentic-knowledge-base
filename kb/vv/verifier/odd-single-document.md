---
id: https://agentic-knowledge-base.dev/id/chunk/f8d87a8e-7e20-4fe6-9c0d-66d0f66cc1b9
type: artifact
level: executable
title_ko: //kb/odd:odd 의 srcs 가 project-odd.yml 과 생성 택소노미 둘뿐이고 조건 7 이 전부 판정 방법과 등급을 가져 gate_test 가 PASS 다
title: The srcs of //kb/odd:odd are project-odd.yml and the generated taxonomy only, and all seven conditions carry a method and a grade, so gate_test passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/7cdb48a1-5b6d-491e-ad54-0a0e2975dd41]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — ODD 타깃 하나와 그 게이트를 자극으로 쓴다.

**자극** — `//kb/odd:odd`(`kb_odd_kg`, `src = project-odd.yml`)와 `//kb/odd:gate_test` 다. 2026-09-21 실측의 문서는 조건 7(`build_system`·`python_runtime`·`repository_layout`·`language_policy`·`dependency_lock`·`network_connectivity`·`concurrent_agents`)이고 `CHECKS` 가 조건마다 `grade`·`method`·`cmd` 를 갖는다.

```yaml
srcs:     [//kb/odd:project-odd.yml, //kb/odd:taxonomy]   # 원본 하나 + 생성 택소노미
checks:   {build_system: A, python_runtime: A, repository_layout: A, language_policy: B, dependency_lock: A, network_connectivity: A, concurrent_agents: B}
negative: {condition: zz_no_checks, CHECKS: absent}        # 서술 표본 — odd2kg 거부
```

**기대** — `bazel test //kb/odd:gate_test` 가 PASS 다. `bazel query 'labels(srcs, //kb/odd:odd)'` 의 출력이 위 두 라벨과 같다. `ls kb/odd/*.yml` 은 파일 하나다. 음성 표본은 `odd2kg` 가 비영 종료로 끝나 TTL 이 만들어지지 않는다.

**실행 명령** — `bazel test //kb/odd:gate_test && bazel query 'labels(srcs, //kb/odd:odd)'`

**판정 범위** — ODD 가 하나뿐이라 표본이 전수다. 조건 7 은 등급 A 5 · B 2 로 두 등급을 덮는다. C·D 조건은 문서에 없어 등급 어휘의 나머지는 shape 의 `sh:in` 으로만 검사된다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p3-odd-is-a-document` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
