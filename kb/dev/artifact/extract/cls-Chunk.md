---
id: https://agentic-knowledge-base.dev/id/chunk/cea6fcfc-b3e0-4dab-b8f5-e0727ee9c70d
type: artifact
level: executable
title_ko: 클래스 Chunk (tools/extract.py)
title: class Chunk in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**클래스** — `class Chunk` 다. 생성할 청크 하나 — 파일 이름·frontmatter·본문.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Chunk:
    """생성할 청크 하나 — 파일 이름·frontmatter·본문."""

    def __init__(self, fname: str, qname: str, iri: str, title_ko: str, title: str, body: list[str]):
        self.fname, self.qname, self.iri = fname, qname, iri
        self.title_ko, self.title, self.body = title_ko, title, body
        self.part_of = ""
        self.composite: dict = {}
        self.links: dict = {}
        self.uses: list = []  # 같은 모듈의 최상위 정의 IRI (agt:usesDefinition) — 정의 청크만 갖는다
```
<!-- 인용 끝 -->
