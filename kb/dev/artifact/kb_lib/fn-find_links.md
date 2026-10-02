---
id: https://agentic-knowledge-base.dev/id/chunk/a0841084-48a1-45f6-842a-57f5b8cbf0c9
type: artifact
level: executable
title_ko: 함수 find_links (tools/kb_lib.py)
title: function find_links in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `find_links(line)` 다. 줄 안의 인라인 링크 목적지 — `](` 뒤에서 괄호 짝을 맞춰 읽는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def find_links(line: str):
    """줄 안의 인라인 링크 목적지 — `](` 뒤에서 괄호 짝을 맞춰 읽는다. 제목("…")은 뗀다."""
    i = 0
    while True:
        j = line.find("](", i)
        if j < 0:
            return
        depth, k = 1, j + 2
        while k < len(line) and depth:
            depth += {"(": 1, ")": -1}.get(line[k], 0)
            k += 1
        if depth:
            return
        dest = line[j + 2:k - 1].strip()
        i = k
        if dest.startswith("<") and ">" in dest:
            dest = dest[1:dest.index(">")]
        else:
            dest = dest.split()[0] if dest.split() else ""
        yield dest
```
<!-- 인용 끝 -->
