---
id: https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67
type: artifact
level: executable
title_ko: 함수 head (tools/weave.py)
title: function head in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/63c8b052-77ba-4c50-bc59-9b1fea9e598d]
part_of: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574
---
**함수** — `head(kind, title, query, g, inputs, extra)` 다. 모든 생성물의 머리 블록 — 규약 G1~G7 (kb_lib.gendoc_header 가 단일 정의처, p12-documents-are-generated).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def head(kind: str, title: str, query: str, g: Graph, inputs: list[str], extra: list[str]) -> list[str]:
    """모든 생성물의 머리 블록 — 규약 G1~G7 (kb_lib.gendoc_header 가 단일 정의처, p12-documents-are-generated)."""
    return kb_lib.gendoc_header(kind, title, "tools/weave.py", query, REPRODUCE[kind], inputs,
                                f"트리플 {len(g)} ({kb_lib.gendoc_union(inputs)})", kb_lib.gendoc_view_notice("청크"), extra=extra)
```
<!-- 인용 끝 -->
