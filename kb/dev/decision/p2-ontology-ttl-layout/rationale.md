---
id: https://agentic-knowledge-base.dev/id/chunk/b0230fef-7e54-4b16-8af3-8d64962babc4
type: decision
level: logical
title_ko: 규약은 결정론적 표기 요구에 기여하고 실측에서 이미 지켜지나 순서의 이유는 기록되지 않았다
title: The convention contributes to the deterministic-notation requirement and already holds in measurement, but the reason for the order is unrecorded
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/aa03212b-6699-4c65-bbc8-0f9836401c6d
---
**근거** — 출처는 저장소 구축(2026-09-01) 때 `STYLEGUIDE.md` §1에 적힌 규약이다. 그 원문은 배너에 주제와 노트 절 번호를 적게 했고 순서의 이유는 적지 않았다.

이 규약이 기여하는 요구는 "명명과 표기는 결정론적이다"다. 그 요구는 같은 내용이 같은 바이트로 직렬화되기를 요구하고 그 이유로 diff의 오염을 든다.

2026-10-03 실측에서 규약은 이미 지켜진다.

- `-ontology.ttl` 59개 전부가 첫 줄에 배너 주석을 둔다.
- 58개의 `@prefix` 선언이 규약의 순서와 맞는다. 최상위 `project-ontology.ttl`은 owl → dcterms 순으로 선언해 규약의 다섯 접두어 밖이다.
- 개념 블록 250개를 줄 머리의 술어 이름으로 대조한 근사 검사에서 순서 어긋남은 0이다.

미확정: 술어 순서와 `@prefix` 순서를 이 꼴로 정한 이유의 기록이 없다. 이 꼴을 게이트로 올릴지도 정하지 않았다.
