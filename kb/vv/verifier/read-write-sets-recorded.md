---
id: https://agentic-knowledge-base.dev/id/chunk/4c926521-890e-41e0-9ea8-8e4e8b8c754d
type: artifact
level: executable
title_ko: 카탈로그 역할 4 의 권한 행 29 가 CQ-24 에 나오고 writer·catalog 검사가 위반 0 이라 gate_test 가 PASS 다
title: The 29 permission rows of the four catalog roles appear in CQ-24, and the writer and catalog checks report zero violations, so gate_test passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/01c6af30-b0a6-47c9-b574-578ca00c50c3]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 그래프 게이트 하나와 질의 뷰 하나를 자극으로 쓴다.

**자극** — `//kg:gate_test`(`catalog`·`writer` 검사 포함)와 `//kg:cq`(CQ-24)다. 2026-09-21 실측의 카탈로그는 역할 4(orchestrator·developer·vnv·hci) · `agt:writesIn "kb/vv"` 는 vnv 하나 · 권한 행 29 다.

```yaml
roles:    {orchestrator: {writes: [requirement, decision, memory]}, developer: {writes: [artifact]}, vnv: {writesIn: kb/vv, writes: 7 planes}, hci: {writes: []}}
cq24:     {rows: 29}
negative: {chunk: kb/vv/goal/zz.md, generated.by: developer/x}    # 서술 표본 — [writer] 거부
handoff:  {workset: bazel-bin/kg/workset-vnv.md, expanded_to_sources: true}   # bazel run — vv_run 밖
```

**기대** — `bazel test //kg:gate_test` 가 PASS 다. `bazel build //kg:cq` 가 성공하고 CQ-24 절의 행 수가 29 다. 음성 표본은 `FAIL [writer] kb/vv/goal/zz.md: 생성자 developer/x 의 역할 developer 는 KB kb/vv 의 RequirementChunk 쓰기 권한이 없다 (agt:writesIn · agt:writes) — 담당 역할의 verified(인수) 또는 되돌림 (AGENTS 표 · 11.2절)` 로 끝나고 종료 코드가 1 이다.

**실행 명령** — `bazel test //kg:gate_test && bazel build //kg:cq`

**판정 범위** — 쓰기 집합 검사는 살아 있는 청크 전수를 대상으로 하므로 표본 추출이 없다. 읽기 집합 쪽은 도구 실행이라 케이스의 실행 명령 밖에 두고 기대 절에 절차만 적는다. hci 는 쓰기 plane 이 없는 경계값이다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p10-link-by-construction` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
