---
id: https://agentic-knowledge-base.dev/id/chunk/07ed26ac-e215-4583-8d9d-10f93fe1eed9
type: artifact
level: executable
title_ko: 함수 revision (tools/vv_run.py)
title: function revision in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `revision(root)` 다. (짧은 리비전, 워킹트리에 추적 파일 변경이 있는가).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def revision(root: Path) -> tuple[str, bool]:
    """(짧은 리비전, 워킹트리에 추적 파일 변경이 있는가). git 밖이면 ('없음', False)."""
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=root, capture_output=True, text=True,
                                    check=True).stdout.strip())
        return rev, dirty
    except (OSError, subprocess.CalledProcessError):
        return "없음", False
```
<!-- 인용 끝 -->
