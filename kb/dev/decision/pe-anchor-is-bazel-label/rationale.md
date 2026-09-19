---
id: https://agentic-knowledge-base.dev/id/chunk/9add2be1-9465-45a1-beda-670c3213bb9e
type: decision
level: logical
title_ko: 라벨은 유일하고 이동에 강하며 파급을 질의로 준다
title: Labels are unique, survive moves, and give impact by query
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-18T10:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a0067e4e-afc9-4817-ac08-3aeba8da718f
---
**근거** (노트 4.8절·0.5절; `pe-bazel-rules`·`p10-link-storage-and-anchors`) — 앵커는 링크가 가리키는 기준점이라
바뀌지 않아야 하고 기계가 해석할 수 있어야 한다. 파일 경로와 줄 번호는 개명·이동·편집에 깨지고, 언어 심볼은
언어마다 해석기가 다르다. Bazel 라벨은 저장소 안에서 유일하고, 파일이 옮겨져도 타깃 이름이 남으며, 의존 그래프에
이미 올라 있어 `rdeps`로 파급을 준다. 이 저장소는 청크를 타깃으로 두었으므로(`pe-bazel-rules`) 청크 앵커와 코드
앵커가 같은 해석기를 쓴다 — 프로파일이 채워야 할 "실제 해석기"가 새 장치 없이 정해진다.
