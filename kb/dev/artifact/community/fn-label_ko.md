---
id: https://agentic-knowledge-base.dev/id/chunk/4dce45c5-55b4-4c63-9ef4-5f4d522ea26d
type: artifact
level: executable
title_ko: 함수 label_ko (tools/community.py)
title: function label_ko in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5
---
**함수** — `label_ko(g, s)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_ko(g: Graph, s) -> str:
    return next((str(o) for o in g.objects(s, RDFS.label) if o.language == "ko"), str(s).split("/")[-1])
```
<!-- 인용 끝 -->
