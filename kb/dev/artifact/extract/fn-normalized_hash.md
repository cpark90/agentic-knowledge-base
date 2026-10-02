---
id: https://agentic-knowledge-base.dev/id/chunk/8f365d81-2dc9-4f87-8f66-153ed897e871
type: artifact
level: executable
title_ko: 함수 normalized_hash (tools/extract.py)
title: function normalized_hash in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `normalized_hash(text_lines, name)` 다. 이름을 지운 본문의 해시 — 개명 판정의 기준이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def normalized_hash(text_lines: list[str], name: str) -> str:
    """이름을 지운 본문의 해시 — 개명 판정의 기준이다. 이름만 바뀐 정의는 같은 해시를 갖는다."""
    body = "\n".join(l.rstrip() for l in text_lines if l.strip())
    body = re.sub(r"\b" + re.escape(name) + r"\b", "@", body)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
```
<!-- 인용 끝 -->
