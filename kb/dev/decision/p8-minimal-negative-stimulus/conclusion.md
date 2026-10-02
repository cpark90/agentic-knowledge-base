---
id: https://agentic-knowledge-base.dev/id/chunk/f9540774-0c1e-4234-b396-818d159ec5d4
type: decision
level: concrete
title_ko: 음성 자극은 검사하려는 규칙 하나만 어긴다
title: A negative stimulus violates only the rule under test
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T13:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6eea0a91-2e8d-400c-a830-ea653fa104f0
composite: {id: https://agentic-knowledge-base.dev/id/composite/6eea0a91-2e8d-400c-a830-ea653fa104f0, title_ko: 음성 자극의 최소성, title: Minimality of a negative stimulus}
---
**결론** — 음성 자극은 케이스가 검사하려는 규칙 **하나만** 어기고 나머지는 만족시킨다. 자극이 둘 이상을 어기면 종료 코드가 어느 규칙을 가리키는지 말하지 못한다.

그때 분기를 고정하는 것은 `contains` 문구뿐이고, 게이트 메시지가 바뀌면 케이스가 **조용히 다른 것을 검증한다.** 종료 코드와 문구가 같은 규칙을 가리킬 때만 판정이 둘로 받쳐진다.

`**표본 근거**`에 **이 자극이 어기는 규칙**을 적는다. 그것이 최소성의 주장이고, 다른 규칙도 어긴다면 그 사실과 까닭을 함께 적는다.

최소성이 불가능한 자리가 있다. 검사하려는 규칙이 다른 규칙의 만족을 전제하지 않을 때가 그렇다 — 예를 들어 어휘 밖 술어를 쓴 개체는 그 술어 때문에 어휘 검사에 걸리지만, 개체가 라벨과 수준을 갖추지 않으면 shape 검사에도 함께 걸린다. 그런 자리에서는 **나머지 규칙을 만족시켜** 자극을 최소로 만든다.

그래도 최소가 되지 않으면 케이스를 나눈다. 한 케이스가 두 규칙을 검사하면 표본 근거가 둘을 말해야 하고, 그것은 케이스가 둘이라는 뜻이다.
