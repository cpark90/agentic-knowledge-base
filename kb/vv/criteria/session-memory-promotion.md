---
id: https://agentic-knowledge-base.dev/id/chunk/8f99e13b-7e9a-43f0-8dad-46f0ac143a87
type: contract
level: logical
title_ko: 승격은 관측을 출처로 가리키는 주제 plane 청크가 있는지와 승격 규칙이 프로젝트 입력으로 적혔는지를 사람이 확인한다
title: Promotion is confirmed by a person checking that a topic-plane chunk cites an observation as its source and that the promotion rule is written down as a project input
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-06T10:55:32+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-06T10:55:34+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/c7aaa3bd-826c-425b-9d0d-76d009002ae6]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. `∃ c ∈ 주제 plane: sources(c) ∋ o ∨ (c prov:wasDerivedFrom o)` 인 관측 `o ∈ memory` 가 있고, 승격 규칙(언제·무엇을)이 문서로 적혀 있는지를 사람이 본다.

**확인 절차**

1. `bazel build //kg:cq` 의 CQ-01 로 memory plane 의 살아 있는 관측 목록을 얻는다(2026-09-21 실측 3건).
1. 주제 plane(요구·결정·기준) 청크 중 `sources`·`prov:wasDerivedFrom` 이 관측 IRI 를 가리키는 것이 있는지 `grep -r` 로 본다.
1. 승격 규칙이 `docs/method.md` 의 갱신·일반화 절 또는 결정으로 적혀 있는지 본다. 없으면 규칙 없는 상태이고 성립이 아니다.
1. 판단을 관측으로 남긴다.

**등급** — C 다. 단기기억·장기기억 두 자리의 존재는 기계가 보장하고 승격 사례와 규칙의 유무는 사람이 본다.

케이스를 두지 않는다. memory plane 의 존재와 append-only 는 케이스 `observations-append-only` 가 이미 관측하고, 승격 자체는 실행 명령으로 판정되지 않는다. 판정의 원본은 `kb/dev/decision/p11-memory-promotion-rule/conclusion.md` 와 이 절차다.
