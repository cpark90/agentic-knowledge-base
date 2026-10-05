---
id: https://agentic-knowledge-base.dev/id/chunk/70a7f6f9-c766-45c6-96fe-9992867d3d83
type: artifact
level: executable
title_ko: 함수 snapshot_files (tools/revalidate.py)
title: function snapshot_files in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f6f22e05-67fd-4351-a17e-d9abe0817b50
---
**함수** — `snapshot_files(dirs, files)` 다. 스냅숏 한쪽의 (주소, 파일) 목록 — 디렉토리는 그 아래 `*.md` 전부(주소는 디렉토리 상대), 파일은 이름이 주소다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def snapshot_files(dirs: list, files: list) -> list:
    """스냅숏 한쪽의 (주소, 파일) 목록 — 디렉토리는 그 아래 `*.md` 전부(주소는 디렉토리 상대), 파일은 이름이 주소다."""
    out = [(str(p.relative_to(d)), p) for d in map(Path, dirs) for p in sorted(d.rglob("*.md"))]
    return out + [(Path(f).name, Path(f)) for f in files]
```
<!-- 인용 끝 -->
