---
id: https://agentic-knowledge-base.dev/id/chunk/145ba81b-fdd4-4cf8-aa11-b8ceb3165a08
type: artifact
level: executable
title_ko: 클래스 Repo (tools/doccheck.py)
title: class Repo in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/41567349-5994-4e9e-aec7-ac6603e2e6f5
---
**클래스** — `class Repo` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Repo:
    def __init__(self, root: Path, empty_dirs: set[str] = frozenset()):
        self.root = root
        self.empty_dirs = {d.strip("/") for d in empty_dirs}  # 파일이 없어 runfiles 에 안 나타나는 빈 패키지 — BUILD 가 선언
        self._anchors: dict[str, set[str]] = {}

    def exists(self, rel: str) -> bool:
        if not rel:
            return True
        return (self.root / rel).exists() or rel.strip("/") in self.empty_dirs

    def anchors_of(self, rel: str) -> set[str]:
        if rel not in self._anchors:
            self._anchors[rel] = anchors(self.read(rel))
        return self._anchors[rel]

    def read(self, rel: str) -> list[str]:
        return (self.root / rel).read_text(encoding="utf-8").splitlines()
```
<!-- 인용 끝 -->
