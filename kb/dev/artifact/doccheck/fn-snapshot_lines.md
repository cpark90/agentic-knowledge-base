---
id: https://agentic-knowledge-base.dev/id/chunk/204439f0-e005-4a79-befc-167bfd308ec9
type: artifact
level: executable
title_ko: 함수 snapshot_lines (tools/doccheck.py)
title: function snapshot_lines in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `snapshot_lines(lines)` 다. 시점을 선언한 스냅샷 단락의 줄 번호 — 기준의 대조 밖이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def snapshot_lines(lines: list[str]) -> set[int]:
    """시점을 선언한 스냅샷 단락의 줄 번호 — 기준의 대조 밖이다 (빈 줄로 가른 단락 단위)."""
    out, block = set(), []
    for i, line in enumerate(lines + [""], 1):
        if line.strip():
            block.append(i)
            continue
        text = "\n".join(lines[j - 1] for j in block)
        if block and SNAPSHOT.search(text) and re.search(r"\d{4}-\d{2}-\d{2}", text):
            out |= set(block)
        block = []
    return out
```
<!-- 인용 끝 -->
