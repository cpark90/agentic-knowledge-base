---
id: https://agentic-knowledge-base.dev/id/chunk/fx-belief-transition-bad
type: artifact
level: executable
title_ko: 고정물 질의 — 믿음 정도로 후보를 확정하는 상태 전이 규칙
title: fixture query — a transition rule that confirms candidates by degree of belief
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-25T00:00:00Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453]
---
**질의** — 게이트 `belief-consistency` 조건 (i)의 음성 고정물이다. 상태 전이 결정을 refines 로 구현한다고 선언한 질의가 믿음 정도의 값으로 후보를 확정 쪽으로 고른다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 음성 고정물: 믿음 정도 0.9 이상인 후보 링크를 확정 대상으로 고른다 — 상태 전이가 믿음 정도를 읽는다
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT ?link WHERE {
  ?link a agt:Link ; agt:linkState "candidate" ; agt:hasDegreeOfBelief ?b .
  ?b agt:beliefValue ?v .
  FILTER (?v >= 0.9)
}
```
<!-- 인용 끝 -->
