---
id: https://agentic-knowledge-base.dev/id/chunk/810e2101-a0d5-405a-a081-39c0b6d82812
type: artifact
level: executable
title_ko: 함수 refs (tools/weave.py)
title: function refs in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574
---
**함수** — `refs(m, nodes)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def refs(m: Model, nodes) -> str:
    return " · ".join(f"{m.ko(n)} (`{kb_lib.compact_iri(str(n))}`)" for n in nodes) or "없음"
```
<!-- 인용 끝 -->
