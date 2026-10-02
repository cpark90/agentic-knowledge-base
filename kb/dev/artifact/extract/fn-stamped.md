---
id: https://agentic-knowledge-base.dev/id/chunk/719f0696-c0dc-4eff-aa6d-bb4dcdf148ce
type: artifact
level: executable
title_ko: 함수 stamped (tools/extract.py)
title: function stamped in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bdbaec34-7407-4d5e-83f8-0706026f0b98
---
**함수** — `stamped(reg)` 다. 도장이 지금 소스를 가리키는가 — `tested.source_hash` 가 등록부의 `source_hash` 와 같을 때만 참이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def stamped(reg: dict) -> str:
    """도장이 지금 소스를 가리키는가 — `tested.source_hash` 가 등록부의 `source_hash` 와 같을 때만 참이다.

    소스가 도장 뒤에 바뀌면 거짓이 되고 `verified` 가 빠진다 (p7-code-extraction-direction "도장"). 사람이 등록부에서
    도장을 지우는 행위도 같은 결과를 낸다 — 도장은 저작물이고 청크는 뷰다.
    """
    t = reg.get(kb_lib.STAMP_KEY) or {}
    return t.get("at", "") if t.get("source_hash") and t["source_hash"] == reg["source_hash"] else ""
```
<!-- 인용 끝 -->
