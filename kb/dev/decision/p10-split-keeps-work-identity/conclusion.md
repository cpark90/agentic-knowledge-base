---
id: https://agentic-knowledge-base.dev/id/chunk/57fc48aa-6091-4ee7-9763-13ddab8ac8b1
type: decision
level: concrete
title_ko: 분할은 조각 하나가 uuid를 승계하고 나머지는 specializationOf로 이으며 링크 IRI는 뿌리 uuid로 계산한다
title: A split passes the uuid to one fragment, links the rest by specializationOf, and link IRIs use the root uuid
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T17:20:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
part_of: https://agentic-knowledge-base.dev/id/composite/a76160fc-059f-437e-8f64-6e6c405cd18b
composite: {id: https://agentic-knowledge-base.dev/id/composite/a76160fc-059f-437e-8f64-6e6c405cd18b, title_ko: 분할은 uuid를 승계한다, title: Splits inherit the uuid}
---
**결론** — 청크 uuid는 work-id다. **분할**하면 라벨을 잇는 조각 하나가 원 uuid를 승계하고, 나머지 조각은 새 uuid를 받아
선택 키 **`specializationOf: <원 청크 IRI>`**(단일 값)로 원본을 가리킨다 — `chunk2kg`가 `prov:specializationOf`(같은 것의
다른 입도)를 방출한다. 대상은 살아 있는 같은 plane의 청크여야 하고 사슬은 순환하지 않는다(`FAIL [specialization]`).
**병합**하면 한 uuid를 승계하고 나머지는 deprecated로 두어 승계 청크가 `supersedes`로 가리킨다(`p0-deprecate-not-delete`).
출처 표기 `prov:wasDerivedFrom`은 그대로 쓴다 — 그것은 "어디서 왔는가"이고 `specializationOf`는 "같은 것인가"다.

링크 IRI는 양 끝의 **뿌리 uuid**(`specializationOf` 사슬을 따라 올라간 work-id)로 계산한다. 그래서 조각을 가리키는 링크와
원본을 가리키던 링크가 같은 개체가 되어 증거·이력이 이어진다. 후보 생성기 `link`는 조각 F가 O를 특수화하면 O를 가리키던
링크 X→O마다 X→F 후보(근거 `constructionRecord`, 값 "승계: O")를 낸다.

| 연산 | uuid | 표기 |
|---|---|---|
| 분할 | 조각 하나가 승계 | 나머지 `specializationOf` 원본 |
| 병합 | 하나가 승계 | 나머지 deprecated, 승계 청크가 `supersedes` |
| 개정 | 유지 | `generated.at` 갱신, `verified` 물림 |
