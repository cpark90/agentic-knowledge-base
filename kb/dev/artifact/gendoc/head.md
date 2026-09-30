---
id: https://agentic-knowledge-base.dev/id/chunk/c0b686cd-daa8-4f89-8cb1-9e142f072f04
type: artifact
level: executable
title_ko: 모듈 머리 tag (tools/gendoc.py)
title: module head tag in tools/gendoc.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gendoc}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/160ca62a-0dd2-4b06-a5e5-21bb1fc54fbe, https://agentic-knowledge-base.dev/id/chunk/61906023-e4bb-46b1-a6db-4bf4635b631b, https://agentic-knowledge-base.dev/id/chunk/2314093a-f5e3-4fc0-96a0-6c5d35db03ee]
part_of: https://agentic-knowledge-base.dev/id/composite/f2a94f2c-1866-41da-848c-d018a7dfc647
---
**모듈 머리** — `tools/gendoc.py` 의 모듈 머리 `tag` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
TAG = kb_lib.GENDOC_GATE
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
```
<!-- 인용 끝 -->
