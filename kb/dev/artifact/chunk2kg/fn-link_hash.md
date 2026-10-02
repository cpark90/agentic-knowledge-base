---
id: https://agentic-knowledge-base.dev/id/chunk/4dcdeb22-0819-48a5-96a4-72da225a3003
type: artifact
level: executable
title_ko: 함수 link_hash (tools/chunk2kg.py)
title: function link_hash in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `link_hash(frm, kind, to)` 다. 링크 개체 IRI 의 해시 부분 — sha256(출발|종류|도착)[:12].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_hash(frm: str, kind: str, to: str) -> str:
    """링크 개체 IRI 의 해시 부분 — sha256(출발|종류|도착)[:12]. 호출자가 양 끝에 뿌리 uuid(work_id)를 넣는다. extract_refs 도 같은 함수를 쓴다."""
    return hashlib.sha256(f"{frm}|{kind}|{to}".encode("utf-8")).hexdigest()[:12]
```
<!-- 인용 끝 -->
