---
id: https://agentic-knowledge-base.dev/id/chunk/6c3a5ad2-79e7-4ff9-b8cd-8feb14ef7087
type: contract
level: logical
title_ko: 가정의 참조 조건은 전부 이 저장소의 ODD 안에 있고 청크의 assumes 대상은 전부 실재하는 가정이다
title: Every assumption refers only to conditions of this repository's ODD and every assumes target is an existing assumption
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f8361ae3-aef7-4716-a908-b60084af8079]
---
**합격 기준** — 기준 종류는 **불변식**이다. `∀ 가정 a: refersTo(a) ⊆ conditions(odd-agentic-knowledge-base)` 이고 `∀ 청크 c: assumes(c) ≠ ∅ ∧ assumes(c) ⊆ Assumption` 이며 `∀ 스코프 s: subsetOf(s) = odd-agentic-knowledge-base` 다.

**판정식**

- 양성: `bazel test //kg:gate_test` 가 PASS 다. 그 안의 `odd-ref`·`dangling`·`shacl`(assumption·scope shape) 검사가 위반 0 이다.
- 음성(조건): ODD 에 없는 조건을 `refersTo` 하는 가정은 `FAIL [odd-ref] <파일>: <가정> 가 ODD에 없는 속성을 참조: <조건> (0.4절 — ODD를 먼저 확장하라)` 로 끝난다. 서술 표본이다.
- 음성(가정): 그래프에 없는 가정 IRI 를 `assumes` 하는 청크는 `dangling` 검사가 거부한다. 서술 표본이다.
- 음성(스코프): `agt:subsetOf` 가 없는 스코프는 `scope-shapes.ttl` 의 `sh:minCount 1` 위반으로 `shacl` 검사가 거부한다.

**등급** — A 다. 판정은 그래프 게이트 하나이고 사람 판단이 없다.

판정의 원본은 `tools/validate.py` 의 `check_odd_refs`·`check_dangling`·`check_shacl` 과 `kb/ontology/shapes/assumption-shapes.ttl`·`scope-shapes.ttl` 이다. 프로젝트가 둘일 때의 경계(다른 ODD 의 청크 거부)는 이 저장소에 두 번째 프로젝트가 없어 관측 밖이다.
