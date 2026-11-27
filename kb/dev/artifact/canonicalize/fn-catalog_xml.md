---
id: https://agentic-knowledge-base.dev/id/chunk/72c905c8-58fa-4d17-8305-7a26c700de4e
type: artifact
level: executable
title_ko: 함수 catalog_xml (tools/canonicalize.py)
title: function catalog_xml in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/48c79ecc-7011-4d44-bc3e-be0cc65036b7
---
**함수** — `catalog_xml(entries)` 다. IRI → 같은 디렉토리 안 상대 경로의 대응표.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def catalog_xml(entries: dict[str, str]) -> str:
    """IRI → 같은 디렉토리 안 상대 경로의 대응표. 항목은 IRI 순이어서 같은 입력이면 같은 바이트다."""
    lines = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
             f'<catalog prefer="public" xmlns="{CATALOG_NS}">']
    lines += [f"    <uri name={quoteattr(iri)} uri={quoteattr(entries[iri])}/>" for iri in sorted(entries)]
    lines.append("</catalog>")
    return "\n".join(lines) + "\n"
```
<!-- 인용 끝 -->
