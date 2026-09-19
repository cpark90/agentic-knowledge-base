---
id: https://agentic-knowledge-base.dev/id/chunk/f8f3858a-879e-4551-8d9f-556452c1a18b
type: decision
level: logical
title_ko: 파일 경로·줄 번호와 언어 심볼 앵커는 기각된다
title: File-path-plus-line and language-symbol anchors are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-18T10:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a0067e4e-afc9-4817-ac08-3aeba8da718f
---
**대안** —

- **파일 경로 + 줄 번호** — 기각. 편집마다 줄이 밀리고 개명·이동에 깨진다. 산문 위치 표기로만 쓴다.
- **언어 심볼(함수 이름·경로)** — 기각. 언어마다 해석기가 다르고 같은 이름이 여러 언어·모듈에 있다.
- **URI 조각(`#fragment`)** — 보류. 웹 문서 앵커에는 맞지만 저장소 코드에는 해석기가 없다. 문서 뷰가 생기면 재검토.
