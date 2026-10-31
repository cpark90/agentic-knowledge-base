---
id: https://agentic-knowledge-base.dev/id/chunk/62ee74cd-d1cf-421f-94fd-69a297308a15
type: norm
level: logical
title_ko: docs/rules.md 절 — 정규화 직렬화
title: docs/rules.md section — Canonical serialization
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:17:27+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
heading: 정규화 직렬화
depth: 3
---
기계가 만든 TTL은 커밋 전에 정규형으로 바꾼다. 직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 오염되고, 그 오염이
무효화 판정의 입력을 더럽히기 때문이다 ([p2-ontology-compiler-three-tiers](../../decision/p2-ontology-compiler-three-tiers/conclusion.md)).
정규형은 `@prefix`를 정렬하고 트리플을 주어와 술어, 목적어 순으로 정렬한 꼴이다. 반면 `kg/*-kg.ttl`과 온톨로지, shape처럼 손으로
쓰는 TTL은 STYLEGUIDE §1·§5의 서식이 원본이므로 정규형 검사 대상이 아니다. 그 서식은 배너와 주석, 술어 순서를 정한다(2026-09-13 판정).

```bash
bazel run //tools:canonicalize -- --write <files>
```
