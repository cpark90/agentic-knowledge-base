---
id: https://agentic-knowledge-base.dev/id/chunk/62ee74cd-d1cf-421f-94fd-69a297308a15
type: norm
level: logical
title_ko: docs/rules.md 절 — 정규화 직렬화
title: docs/rules.md section — Canonical serialization
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
heading: 정규화 직렬화
depth: 3
---
기계가 만든 TTL은 커밋 전 정규형으로 바꾼다. 손으로 쓰는 TTL(`kg/*-kg.ttl`·온톨로지·shape)은 STYLEGUIDE §1·§5의
서식(배너·주석·술어 순서)이 원본이라 정규형 검사 대상이 아니다(2026-09-13 판정). 정규형은 정렬된 `@prefix` + 주어·술어·목적어 정렬이다.
직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 오염되고, 그것이 무효화 판정의
입력을 더럽힌다 ([p2-ontology-compiler-three-tiers](../../decision/p2-ontology-compiler-three-tiers/conclusion.md)).

```bash
bazel run //tools:canonicalize -- --write <files>
```
