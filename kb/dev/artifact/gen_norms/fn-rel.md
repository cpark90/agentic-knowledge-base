---
id: https://agentic-knowledge-base.dev/id/chunk/eb4346c1-beed-427d-8e9d-767bc87f2e0b
type: artifact
level: executable
title_ko: 함수 rel (tools/gen_norms.py)
title: function rel in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `rel(root, p)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()
```
<!-- 인용 끝 -->
