---
id: https://agentic-knowledge-base.dev/id/chunk/2674f907-6204-42f7-a25e-6789137904d6
type: artifact
level: executable
title_ko: 함수 to_rel (tools/doccheck.py)
title: function to_rel in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `to_rel(path, root, workdir)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def to_rel(path: str, root: Path, workdir: str | None) -> Path:
    p = Path(path)
    if not p.is_absolute() and workdir:
        p = Path(workdir) / p
    p = Path(os.path.abspath(p))  # 심볼릭 링크는 따라가지 않는다 — runfiles 의 링크가 루트 밖을 가리킨다
    try:
        return p.relative_to(root)
    except ValueError:
        raise ValueError(f"{path}: 루트 {root} 밖의 파일이다")
```
<!-- 인용 끝 -->
