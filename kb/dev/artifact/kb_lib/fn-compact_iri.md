---
id: https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55
type: artifact
level: executable
title_ko: 함수 compact_iri (tools/kb_lib.py)
title: function compact_iri in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `compact_iri(iri)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def compact_iri(iri: str) -> str:
    for ns, prefix in COMPACT_PREFIXES:
        if iri.startswith(ns):
            return prefix + iri[len(ns):]
    return iri
```
<!-- 인용 끝 -->
