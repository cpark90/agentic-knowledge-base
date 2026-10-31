---
id: https://agentic-knowledge-base.dev/id/chunk/f41fc2b0-2cef-49c0-a35f-1848074f7b60
type: decision
level: concrete
title_ko: 규범 문서 규약 — 실행 모드는 입력이고 dispatch에는 적용 범위로 거른 작업 집합만 전달한다
title: Normative-document conventions — Execution mode is an input, and dispatch carries only the scope-filtered workset
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7e1f24c0-e217-46a1-8599-5fd5ac39e486
---
**규약** — `p11-execution-mode-and-workset`의 결론을 규범 문서에 싣는 문장이다.

규약: dispatch 대상에게는 전체 컨텍스트가 아니라 **적용 범위로 거른 작업 집합만** 넘긴다.
규약: developer·vnv는 dispatch 시 역할 표와 적용 범위로 브리핑한다.
규약: dispatch 대상에게는 전체 컨텍스트가 아니라 **작업 집합**만 전달한다. 작업 집합은 적용 범위와 정제 수준 창으로 거른 지식 집합이다([`docs/method.md` §8](../../../../docs/method.md#8-조회)). 그래서 저장소를 통째로 컨텍스트에 싣지 않는다.
