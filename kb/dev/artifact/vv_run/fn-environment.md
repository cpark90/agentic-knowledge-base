---
id: https://agentic-knowledge-base.dev/id/chunk/de4671f1-1f9f-4715-a852-ab91c7368807
type: artifact
level: executable
title_ko: 함수 environment (tools/vv_run.py)
title: function environment in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `environment(root)` 다. 환경 한 줄 — bazel·python 버전과 OS.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def environment(root: Path) -> str:
    """환경 한 줄 — bazel·python 버전과 OS. p8-reproducibility 의 환경 구성."""
    try:
        bazel = subprocess.run(["bazel", "--version"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        bazel = "bazel 없음"
    return f"{bazel} · python {platform.python_version()} · {platform.system().lower()}"
```
<!-- 인용 끝 -->
