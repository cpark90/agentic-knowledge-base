---
id: https://agentic-knowledge-base.dev/id/chunk/07ed26ac-e215-4583-8d9d-10f93fe1eed9
type: artifact
level: executable
title_ko: 함수 revision (tools/vv_run.py)
title: function revision in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `revision(root)` 다. (짧은 리비전, 변경된 추적 파일 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def revision(root: Path) -> tuple[str, int]:
    """(짧은 리비전, 변경된 추적 파일 수). git 밖이면 ('없음', 0).

    수를 세는 까닭은 `있음`·`없음` 만으로는 재현 불가의 규모가 보이지 않는다는 것이다 — 현상
    `agt:concurrentSessionState`(P22)의 관측 수단이 이 줄이고, 변경이 있는 실행의 판정은 재현 불가 후보다.
    """
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=root, capture_output=True, text=True,
                             check=True).stdout
        return rev, len([ln for ln in out.splitlines() if ln.strip()])
    except (OSError, subprocess.CalledProcessError):
        return "없음", 0
```
<!-- 인용 끝 -->
