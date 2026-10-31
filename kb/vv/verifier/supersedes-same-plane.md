---
id: https://agentic-knowledge-base.dev/id/chunk/407b686d-8589-46e1-8496-18e69c7b99b4
type: artifact
level: executable
title_ko: requirement를 supersedes 하는 decision 고정물 bad_supersedes의 분석이 같은 지식 종류 제한으로 실패한다
former_title_ko: ["requirement를 supersedes 하는 decision 고정물 bad_supersedes의 분석이 같은 plane 제한으로 실패한다"]
title: Analysis of the decision fixture bad_supersedes that supersedes a requirement fails with the same-plane restriction
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/2b1a11cb-160a-45fe-a5cb-4f86f8a42271]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-24T22:39:25+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc]
restored: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc]
---
**검증기** — 지식 종류를 넘는 `supersedes` 하나와 커밋된 결정 전체를 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel`의 고정물 `fx_req`와 `bad_supersedes`다. 둘 다 `manual` 태그다.

```yaml
fx_req:          {src: fx_req.md, plane: requirement, level: functional}
bad_supersedes:  {src: fx_dec.md, plane: decision, level: concrete, supersedes: [fx_req]}
```

**기대** — `bad_supersedes`의 분석이 실패하고 메시지에 `supersedes 는 같은 plane 안에서만 (7.4절): decision → requirement`가 있다. `supersedes_plane_test`는 그 실패를 기대하므로 PASS다. 양성 실행 `bazel build //kb/dev/...`는 성공하고 커밋된 `supersedes` 대상은 전부 `decision`이다.

**실행 명령** — `bazel test //defs/tests:supersedes_plane_test && bazel build //kb/dev/...`

**판정 범위** — 대상으로 `requirement`를 고른 이유는 그것이 `refines`로는 허용되는 방향(상위 지식 종류·상위 수준)이라는 데 있다. 같은 대상이 `refines`에서는 통과하고 `supersedes`에서는 실패하므로 두 링크의 판정이 다름이 드러난다. 커밋된 표본은 `kb/dev/decision`의 살아 있는 결정 사이 `supersedes`다. 2026-10-24 측정으로 결정 11개가 링크 12개를 갖고 대상 12개가 전부 `kb/dev/decision`의 결정이다. 옛 평평한 결정 트리를 가리키던 `supersedes`는 `sources`의 git 영구 링크로 옮겼다.

**검증 대응물** — 이 검증기는 `defs/kb.bzl`의 항목을 `verifies` 한다. 끝은 파일 복합체의 선언 항목(`module.md`)이고, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p7-decision-supersession`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
