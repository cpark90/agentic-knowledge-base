---
id: https://agentic-knowledge-base.dev/id/chunk/79d5bf07-3d05-4696-acab-2b6fe7b02ed1
type: decision
level: logical
title_ko: 양 끝 해시로 만든 링크 IRI는 분할 순간 증거와 이력을 끊는다
title: Link IRIs hashed from both ends cut evidence and history at the moment of a split
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T17:20:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a76160fc-059f-437e-8f64-6e6c405cd18b
---
**근거** (노트 10.5절·10.11절; hci 조사 2026-09-18 선택지 B, 유저 승인 2026-09-19) — 링크 IRI가 `sha256(출발|종류|도착)`이라
분할·병합으로 uuid가 바뀌면 링크 개체가 다른 것이 되어 증거·확인 주체·시각을 실어 나르지 못한다. 42줄 상한이 분할을
강제하므로 이 손실은 예외가 아니라 정상 경로다. `prov:wasDerivedFrom`만으로는 "같은 것의 다른 입도"와 "새로 만든 것"이
갈리지 않는다.

정착된 해법은 2단 식별자다 — Akoma Ntoso(OASIS)의 `wId`(불변)·`eId`(재번호매김 시 변경), 나노출판의 "발행분은 고치지 않고
`supersedes`로 대체", 참조 저장소의 "조항 번호 보존 + 원 자리에 포인터 한 줄". uuid를 `wId` 자리에 두고 링크 IRI를
뿌리 uuid로 계산하면 frontmatter 형식을 바꾸지 않고 같은 효과를 얻는다. 승계 규칙(라벨을 잇는 조각)은 자의성을 줄인다 —
라벨 하나로 요약되는 쪽이 원본의 정체를 잇는다(STYLEGUIDE 분할 신호).
