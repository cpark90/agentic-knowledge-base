---
id: https://agentic-knowledge-base.dev/id/chunk/407b686d-8589-46e1-8496-18e69c7b99b4
type: artifact
level: executable
title_ko: requirement를 supersedes 하는 decision 고정물 bad_supersedes의 분석이 같은 plane 제한으로 실패한다
title: Analysis of the decision fixture bad_supersedes that supersedes a requirement fails with the same-plane restriction
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/2b1a11cb-160a-45fe-a5cb-4f86f8a42271]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — plane을 넘는 `supersedes` 하나와 커밋된 결정 전체를 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel`의 고정물 `fx_req`와 `bad_supersedes`다. 둘 다 `manual` 태그다.

```yaml
fx_req:          {src: fx_req.md, plane: requirement, level: functional}
bad_supersedes:  {src: fx_dec.md, plane: decision, level: concrete, supersedes: [fx_req]}
```

**기대** — `bad_supersedes`의 분석이 실패하고 메시지에 `supersedes 는 같은 plane 안에서만 (7.4절): decision → requirement`가 있다. `supersedes_plane_test`는 그 실패를 기대하므로 PASS다. 양성 실행 `bazel build //kb/dev/... //chunks/...`는 성공하고 커밋된 `supersedes` 대상은 전부 `decision`이다.

**실행 명령** — `bazel test //defs/tests:supersedes_plane_test && bazel build //kb/dev/... //chunks/...`

**판정 범위** — 대상으로 `requirement`를 고른 이유는 그것이 `refines`로는 허용되는 방향(상위 plane·상위 수준)이라는 데 있다. 같은 대상이 `refines`에서는 통과하고 `supersedes`에서는 실패하므로 두 링크의 판정이 다름이 드러난다. 커밋된 표본은 `kb/dev/decision`의 `supersedes`가 `chunks/decision`의 옛 결정을 가리키는 실제 대체 사례들이다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p7-decision-supersession` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
