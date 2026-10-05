---
id: https://agentic-knowledge-base.dev/id/chunk/d6d0bfc7-7f87-474c-8939-8d7ce8113eaa
type: artifact
level: executable
title_ko: 함수 artifact_pkgs (tools/gen_build.py)
title: function artifact_pkgs in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bd43acdb-4493-4bcb-852c-56bb2a3c929e
---
**함수** — `artifact_pkgs(root)` 다. 추출 대상 패키지 — kb/dev/artifact 아래의 디렉토리.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def artifact_pkgs(root: Path):
    """추출 대상 패키지 — kb/dev/artifact 아래의 디렉토리. 없으면 빈 목록이다."""
    d = root / ARTIFACT_ROOT
    return sorted(p.name for p in d.iterdir() if p.is_dir()) if d.is_dir() else []
```
<!-- 인용 끝 -->
