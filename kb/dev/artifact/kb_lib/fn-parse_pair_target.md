---
id: https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2
type: artifact
level: executable
title_ko: 함수 parse_pair_target (tools/kb_lib.py)
title: function parse_pair_target in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6309baee-3513-4835-affe-e76a4382e7d5
---
**함수** — `parse_pair_target(cell)` 다. 판정 로그 `대상` 열 → (앵커 IRI, 대상 IRI, 링크 종류).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_pair_target(cell: str) -> tuple[str, str, str] | None:
    """판정 로그 `대상` 열 → (앵커 IRI, 대상 IRI, 링크 종류). 쌍 꼴이 아니면(단일 항목 판정) None 이다."""
    m = JUDGE_PAIR_TARGET.match(cell.strip().strip("`").strip())
    return (m.group(1), m.group(2), m.group(3)) if m else None
```
<!-- 인용 끝 -->
