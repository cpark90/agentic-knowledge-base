---
id: https://agentic-knowledge-base.dev/id/chunk/c3d2d14a-33fd-4aa3-b95f-644da452cb45
type: decision
level: concrete
title_ko: 이름이 구현을 따라 바뀌면 교체가 아니라 다른 산출물의 등장이 된다
title: If the name follows the implementation, a swap becomes the appearance of a different output
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0180-output-address-from-spec-slot.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:02:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:02:35+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/e69281eb-93ed-4314-8a54-0c18ff5cf4f1
---
**근거** — 출처는 harness-concrete `docs/odr-bind-lock.md`의 "Stable emitted filenames" 절이다.

- 이것이 기술이 바뀌어도 같은 것이라는 주장의 조작적 정의다. 같은 슬롯을 다른 구현이 실현하는 것이 교체이고, 이름이 따라 바뀌면 그것은 교체가 아니라 다른 산출물의 등장이다.
- 구현 파일의 이름을 그대로 물려받으면 후보 교체가 곧 이름 변경이 된다. 명세는 그대로인데 사용자가 깨지므로, 같은 명세와 다른 바인딩에서 같은 판정 결과가 나온다는 교체의 무해성이 이름 층에서 무너진다.
- 이 규칙은 앵커를 내용이 아니라 지속 식별자에 두는 규칙(`p4-chunk-iri-is-the-anchor`)의 산출물 쪽 대응이다. 그래서 명세의 슬롯 식별자가 산출물의 앵커 노릇을 한다.
- 후보 개념 자체가 없는 퇴화 경우, 곧 구현이 하나뿐이고 슬롯을 세우지 않은 경우에만 참조의 원래 이름을 그대로 쓴다.
