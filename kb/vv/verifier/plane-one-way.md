---
id: https://agentic-knowledge-base.dev/id/chunk/bfba0f21-9dfd-4f49-8aa6-08cfcfdc4735
type: artifact
level: executable
title_ko: contract를 refines 하는 decision 고정물 bad_plane_dir의 분석이 plane 단방향 위반으로 실패한다
title: Analysis of the decision fixture bad_plane_dir that refines a contract fails with a one-way plane violation
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/68faa51d-47c8-48fb-9cb1-589f793d31a6]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 하위 plane을 향한 `refines` 하나와 커밋된 개발 KB 전체를 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel`의 고정물 `fx_ctr`와 `bad_plane_dir`다. 둘 다 `manual` 태그다.

```yaml
fx_ctr:         {src: fx_dec.md, plane: contract, level: abstract}                 # 대상 — 상위 수준, 하위 plane
bad_plane_dir:  {src: fx_dec.md, plane: decision, level: concrete, refines: [fx_ctr]}
```

대상의 수준 `abstract`는 주어의 `concrete`보다 높아 수준 부등식은 통과한다. 그래서 실패 원인이 plane 순서 하나로 좁혀진다.

**기대** — `bad_plane_dir`의 분석이 실패하고 메시지에 `plane 단방향 위반 (5.2절) — decision 가 하위 plane contract 를 refines 한다`가 있다. `plane_direction_test`는 그 실패를 기대하므로 PASS다. 양성 실행 `bazel build //kb/dev/...`는 성공한다.

**실행 명령** — `bazel test //defs/tests:plane_direction_test && bazel build //kb/dev/...`

**판정 범위** — `decision`(순서 2)과 `contract`(순서 3)는 인접한 plane이라 순서 비교의 경계값이다. 수준을 일부러 통과시켜 두 검사의 독립성을 보인다. 인접하지 않은 쌍(`requirement` → `memory`)은 같은 분기라 표본을 늘리지 않는다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p5-plane-order-one-way-influence` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
