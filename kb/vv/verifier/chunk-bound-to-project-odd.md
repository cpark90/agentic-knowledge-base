---
id: https://agentic-knowledge-base.dev/id/chunk/d02a3571-f76f-46ca-99fc-5276321eb3fd
type: artifact
level: executable
title_ko: 가정 전부의 참조 조건이 project-odd.yml 안에 있고 스코프 전부가 그 ODD 의 부분집합이라 //kg:gate_test 가 PASS 다
title: Every assumption refers to conditions inside project-odd.yml and every scope is a subset of that ODD, so //kg:gate_test passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/6c3a5ad2-79e7-4ff9-b8cd-8feb14ef7087]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 그래프 게이트 하나를 자극으로 쓴다. 표본은 커밋된 그래프 전체다.

**자극** — `//kg:gate_test` 다. 입력은 head 그래프(`//kg:chunks_kg`)·A-Box(`//kg:kg`)·참조 그래프·ODD(`//kb/odd:odd`)·온톨로지·shape 다. 2026-09-21 실측의 규모는 가정 2(`asm-bazel-toolchain`·`asm-chunk-conventions`) · 참조 조건 3(`cond-build-system`·`cond-language-policy`·`cond-repo-layout`) · ODD 조건 7 · 스코프 4 · 살아 있는 청크 695 다.

```yaml
assumptions: {asm-bazel-toolchain: [cond-build-system], asm-chunk-conventions: [cond-language-policy, cond-repo-layout]}
odd:         id:odd-agentic-knowledge-base                          # kb/odd/project-odd.yml 하나 — 조건 7
negative:    {assumption: asm-zz, refersTo: id:cond-not-in-odd}     # 서술 표본 — [odd-ref]
```

**기대** — `bazel test //kg:gate_test` 가 PASS 다. 음성 표본은 `FAIL [odd-ref] kg/base-kg.ttl: id:asm-zz 가 ODD에 없는 속성을 참조: https://agentic-knowledge-base.dev/id/cond-not-in-odd (0.4절 — ODD를 먼저 확장하라)` 한 줄로 끝나고 종료 코드가 1 이다.

**실행 명령** — `bazel test //kg:gate_test`

**판정 범위** — 가정이 둘뿐이라 표본이 전수다. 다른 프로젝트의 ODD 는 이 저장소에 없으므로 경계를 넘는 청크는 그래프에 들어올 입력 경로 자체가 없다. 그 부재가 표본이다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p12-cross-project-reuse` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
