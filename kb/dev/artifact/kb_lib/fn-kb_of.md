---
id: https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99
type: artifact
level: executable
title_ko: 함수 kb_of (tools/kb_lib.py)
title: function kb_of in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
---
**함수** — `kb_of(location)` 다. 청크 위치(assertionLocation)가 속한 KB — kb/vv/ 아래면 V&V KB, 그 밖(kb/dev·chunks/…)은 개발 KB.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def kb_of(location: str) -> str:
    """청크 위치(assertionLocation)가 속한 KB — kb/vv/ 아래면 V&V KB, 그 밖(kb/dev·chunks/…)은 개발 KB."""
    return KB_VV if location.startswith(KB_VV + "/") else KB_DEV
```
<!-- 인용 끝 -->
