---
id: https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02
type: contract
level: logical
title_ko: 색인 구멍·중복·itemContent 이탈은 shape 하나로 거부되고 정합한 목록은 통과한다
title: An index gap, a duplicate index and an itemContent outside hasDirectPart are each rejected by the shape, and a consistent list passes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T05:10:38+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f0fdfa51-3dd6-4e7f-adee-88b3ad41b93a]
---
**합격 기준** — 기준 종류는 **명세 대조**다. `co:List` 개체와 그 `co:item` 목록에 대해, 색인 집합이 부분 수 `n`의 `{1..n}`이 아니거나(구멍·중복) `co:itemContent`가 `agt:hasDirectPart`의 여집합을 가리키면 `composite-order-shapes.ttl`의 `OrderedCompositeShape`가 `sh:sparql` 위반 정확히 1건을 낸다.

**판정식**

- 음성(구멍): `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data <자극>`이 `FAIL [shacl]` + `FAIL [validate] — 1건`, 종료 코드 1이다.
- 음성(중복): 같은 명령이 같은 위반(첫 `sh:sparql`, 색인 정합)으로 종료 코드 1이다.
- 음성(itemContent 이탈): 같은 명령이 둘째 `sh:sparql`(부분 집합 일치)로 종료 코드 1이다.
- 최소성: 각 자극은 색인 정합·부분 집합 일치 가운데 하나만 어긴다.
- 양성: 색인이 1..n 연속·중복 없음이고 `co:itemContent`가 `agt:hasDirectPart`와 같은 목록은 종료 코드 0이다.

**등급** — B다. shape는 기계 판정이나 `sh:sparql`은 이 저장소의 첫 사용이라 pySHACL 버전에 따른 회귀 위험이 있다.

기준의 대상은 `kb/ontology/shapes/composite-order-shapes.ttl`의 두 `sh:sparql` 제약이고 판정의 원본은 `tools/validate.py`의 `check_shacl`이다.
