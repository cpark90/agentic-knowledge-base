---
id: https://agentic-knowledge-base.dev/id/chunk/c107c57b-16b1-4433-84d6-091ed25bcf08
type: artifact
level: executable
title_ko: metrics 의 후방 추적 잔여 3 이 전부 memory 관측이고 살아 있는 결정 194 는 요구에 닿아 plane_direction_test 가 PASS 다
title: The three residual chunks of the backward trace in metrics are all memory observations, the 194 live decisions reach a requirement, and plane_direction_test passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/e1cc9b56-b318-4f5a-8c98-4af5e9a655e7]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc, https://agentic-knowledge-base.dev/id/chunk/44a05a81-0490-4725-a114-8d42143fdc0e]
restored: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc, https://agentic-knowledge-base.dev/id/chunk/44a05a81-0490-4725-a114-8d42143fdc0e]
---
**검증기** — 생성 뷰 하나와 분석 시점 고정물 하나를 자극으로 쓴다.

**자극** — `//kg:metrics` 의 `후방 추적 귀속 (CQ20)` 절과 `defs/tests/BUILD.bazel` 의 고정물 `bad_plane_dir`(결정이 `contract` 를 `refines`)이다. 2026-09-21 측정은 살아 있는 단위 지식 741 · 비요구 673 · 결정 단위 195(살아 있는 것 194, deprecated 1 = `p14-adoption-stages`, `p14-stage-pass-conditions` 가 `supersedes`)다.

```yaml
metrics:   {line: "요구로 거슬러 오르는 비요구 청크", value: "670/673 = 99.6%", residue: 3}
residue:   # status ≠ deprecated ∧ ¬reaches_req — 전부 memory plane, 결정 0
  - {iri: id:chunk/1f14a8b8-9b54-4f28-bdc4-30374c78f784, at: kb/vv/run/run-20260919T065358Z.md, plane: memory}
  - {iri: id:chunk/3fa64879-9f43-4c16-bf97-3fcfe5e605a9, at: kb/vv/run/run-20260919T062548Z.md, plane: memory}
  - {iri: id:chunk/7726809e-1996-41cb-9da7-71d92f1c30ac, at: kb/dev/memory/obs-20260913T154324Z.md, plane: memory}
excluded:  {p14-adoption-stages: deprecated}     # 이력 — r-010 의 대상이 아니다
fixture:   {bad_plane_dir: "plane 단방향 위반"}
```

**기대** — `plane_direction_test` 가 PASS 다. `bazel build //kg:metrics` 가 성공하고 잔여 `d − n` 의 단위 지식이 전부 `memory` 지식 종류이며 결정이 0 이다. 관측은 `refines` 를 갖지 않는 설계(append-only 실행 기록)라 잔여에 남는 것이 정상이고, 잔여에 살아 있는 결정이 나타나면 r-010 위반이다. 두 명령의 종료 코드는 0 이다.

**실행 명령** — `bazel test //defs/tests:plane_direction_test && bazel build //kg:metrics`

**판정 범위** — 귀속은 전수 계산이라 표본 추출이 없다. deprecated 결정 1 은 "상태를 거르지 않으면 위반으로 보이는" 경계값이고, memory 잔여 3 은 "요구에 닿지 않아도 정상인 지식 종류" 의 경계값이다. 잔여의 지식 종류 대조는 vv_run 밖이라 기대 절에 측정을 남긴다.

**검증 대응물** — 이 검증기는 `defs/kb.bzl`과 `tools/metrics.py`의 항목을 `verifies` 한다. 끝은 파일 복합체의 선언 항목(`module.md`)이고, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p10-link-types`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
