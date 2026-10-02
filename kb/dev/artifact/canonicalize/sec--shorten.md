---
id: https://agentic-knowledge-base.dev/id/chunk/6f3a5510-5370-4caa-80a7-903dfc4b95ff
type: artifact
level: executable
title_ko: 절 -shorten (tools/canonicalize.py)
title: section -shorten in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/a9cc1a02-29b3-4f53-8711-8d60a4bea3cf]
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
composite: {id: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389, title_ko: 절 복합체 -shorten (tools/canonicalize.py), title: section composite -shorten in tools/canonicalize.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/6f3a5510-5370-4caa-80a7-903dfc4b95ff, https://agentic-knowledge-base.dev/id/chunk/0dbea10c-f751-4ac3-b58a-ee9b7bb1ba4b, https://agentic-knowledge-base.dev/id/chunk/a2ba3352-fcbb-4d76-9b20-a5d8b6eb5402, https://agentic-knowledge-base.dev/id/chunk/221ff1dd-1b9e-4518-831b-2c8e960001ac, https://agentic-knowledge-base.dev/id/chunk/04b68be9-58b9-4c04-8eab-6c48e91ef5cb], part_of: https://agentic-knowledge-base.dev/id/composite/cf91a784-b983-40fa-afff-ff9105164656}
---
**절** — `tools/canonicalize.py` 의 절 `-shorten` 다. 정규 직렬화 — 출력 순서를 고정한다

**정의** — `_shorten` · `_term` · `canonical_text` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 정규 직렬화 — 출력 순서를 고정한다 ────────────────────









if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
