---
id: https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb
type: artifact
level: executable
title_ko: 함수 at (tools/judge.py)
title: function at in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add
---
**함수** — `at(root, p)` 다. 상대 경로를 워크스페이스 루트 기준으로 푼다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def at(root: Path, p: str) -> Path:
    """상대 경로를 워크스페이스 루트 기준으로 푼다 — `bazel run` 의 작업 디렉토리는 runfiles 트리다."""
    path = Path(p)
    return path if path.is_absolute() else root / path
```
<!-- 인용 끝 -->
