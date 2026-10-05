---
id: https://agentic-knowledge-base.dev/id/chunk/7e58cd2b-ecf9-4a21-a66b-9e28aa4474e9
type: artifact
level: executable
title_ko: 함수 norm_pkgs (tools/gen_build.py)
title: function norm_pkgs in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6400a2c9-ed32-428b-bd76-5952553e5e04
---
**함수** — `norm_pkgs(root)` 다. 규범 문서 패키지 — kb/dev/norm 아래의 디렉토리(문서 stem).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def norm_pkgs(root: Path):
    """규범 문서 패키지 — kb/dev/norm 아래의 디렉토리(문서 stem). 없으면 빈 목록이다."""
    d = root / NORM_ROOT
    return sorted(p.name for p in d.iterdir() if p.is_dir()) if d.is_dir() else []
```
<!-- 인용 끝 -->
