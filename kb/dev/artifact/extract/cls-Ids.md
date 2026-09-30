---
id: https://agentic-knowledge-base.dev/id/chunk/54593928-2d60-46f2-8052-357ae60657a0
type: artifact
level: executable
title_ko: 클래스 Ids (tools/extract.py)
title: class Ids in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**클래스** — `class Ids` 다. 한정 이름 → uuid.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Ids:
    """한정 이름 → uuid. 등록부가 원본이고 신설만 자동이다."""

    def __init__(self, ids: dict):
        self.ids = dict(ids)
        self.added: list[str] = []

    def get(self, qname: str, prefix: str) -> str:
        if qname not in self.ids:
            self.ids[qname] = prefix + str(uuid.uuid4())
            self.added.append(qname)
        return self.ids[qname]
```
<!-- 인용 끝 -->
