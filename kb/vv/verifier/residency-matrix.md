---
id: https://agentic-knowledge-base.dev/id/chunk/7576a24f-6aea-4001-8172-ce6f9803a38a
type: artifact
level: executable
title_ko: requirement×concrete 고정물 bad_residency의 분석이 수준 허용표 위반으로 실패한다
title: Analysis of the requirement-by-concrete fixture bad_residency fails with an allowed-level-matrix violation
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/56b4c449-63d5-4f3c-8b25-2983028beab8]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 수준 허용표 밖 조합 둘(청크 하나·복합체 하나)과 커밋된 저장소 전체를 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel`의 고정물 `bad_residency`와 `bad_decision_levels`다. 둘 다 `manual` 태그라 `//...`에 잡히지 않는다.

```yaml
bad_residency:        {src: fx_req.md, plane: requirement, level: concrete}   # 허용 구간 [functional]
bad_decision_levels:  {conclusion: fx_dec.md, part_levels: [executable, logical, logical]}   # decision 허용 구간 밖
```

`fx_req.md`의 frontmatter는 `type: requirement`·`level: functional`이고 파일 내용은 판정에 쓰이지 않는다. 판정은 BUILD 속성 `plane`·`level`로만 한다.

**기대** — 두 타깃의 분석이 실패하고 메시지에 `수준 허용표 위반 — plane requirement 는 level concrete 에 살 수 없다 (6.4절)`와 `plane decision 는 level executable 에 살 수 없다`가 있다. 두 음성 시험은 그 실패를 기대하므로 PASS다. 양성 실행 `//kg:gate_test`·`//kb/ontology:gate_test`는 PASS다 — 후자가 게이트 `residency`(shape 대 `defs/kb.bzl` 동일성)를 돈다.

**실행 명령** — `bazel test //defs/tests:residency_test //defs/tests:decision_levels_test //kg:gate_test //kb/ontology:gate_test`

**판정 범위** — `requirement`는 허용 구간이 `functional` 하나뿐인 plane이라 구간 밖 값의 선택이 가장 단순하다. 복합체 표본은 결론 수준을 `executable`로 두어 `kb_decision`이 `kb_chunk`와 같은 `_check_residency`를 부분마다 적용함을 보인다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p6-plane-level-occupancy` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
