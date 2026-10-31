---
id: https://agentic-knowledge-base.dev/id/chunk/f8361ae3-aef7-4716-a908-b60084af8079
type: requirement
level: functional
pattern: ubiquitous
title_ko: 단위 지식의 전제는 이 프로젝트의 ODD 조건에만 묶여야 한다
former_title_ko: ["청크의 전제는 이 프로젝트의 ODD 조건에만 묶여야 한다", "지식 항목의 전제는 이 프로젝트의 ODD 조건에만 묶여야 한다"]
title: The premises of a chunk must be bound only to the ODD conditions of this project
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/20148952-30c4-4f76-8cbf-4d9b32c68b25]
---
**검증 목표** — 지식은 프로젝트 ODD 안에서만 유효하고 프로젝트를 넘어 재사용하지 않는다는 결정이 가정·조건·적용 범위의 참조 무결성으로 강제된다는 것이 보여져야 한다. 단위 지식의 전제는 `assumes` → 가정 → `agt:refersTo` → ODD 조건의 연쇄이고 그 끝은 이 저장소의 ODD 개체 하나다.

- **이해관계자**: 업체 · 감사 역할 · **관심사**: 축적과 재사용

**무엇을 관측하면 성립하는가**

- 살아 있는 단위 지식 전부가 `assumes` 를 갖고 그 대상이 이 그래프의 `agt:Assumption` 개체다. 끊긴 대상은 `dangling` 검사가 거부한다.
- 모든 가정의 `agt:refersTo` 대상이 `kb/odd/project-odd.yml` 의 조건이다. ODD 밖 조건 참조는 `odd-ref` 검사가 거부한다.
- 모든 적용 범위가 `agt:subsetOf` 로 이 ODD 개체를 가리킨다(`scope-shapes.ttl` 의 `sh:minCount 1`).
- 다른 프로젝트의 단위 지식을 들여오는 경로가 없다. 그래프 입력은 이 저장소의 `kb/**` 뿐이다(`//kg:chunks_kg` 의 deps).

판정의 원본은 `tools/validate.py` 의 `check_odd_refs`·`check_dangling` 과 `kb/ontology/shapes/scope-shapes.ttl`·`assumption-shapes.ttl` 이다.
